# SPDX-License-Identifier: MIT
"""Create an advisory link-review report. Never remove or reclassify entries."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import argparse
import json
from catalog import ROOT, load, validate

def inspect(url, timeout):
    headers = {"User-Agent": "OkieOTSec-catalog-review/1.0", "Range": "bytes=0-4095"}
    # GET avoids false failures from servers that do not implement HEAD.
    try:
        with urlopen(Request(url, headers=headers), timeout=timeout) as response:
            status, destination = response.status, response.url
        return {"url": url, "http_status": status, "final_url": destination, "result": "reachable" if 200 <= status < 400 else "manual_review"}
    except HTTPError as e:
        return {"url": url, "http_status": e.code, "result": "unavailable_candidate" if e.code in (404, 410) else "manual_review", "detail": str(e.reason)}
    except (URLError, TimeoutError, OSError, ValueError) as e:
        return {"url": url, "result": "manual_review", "detail": str(e)}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dry-run", action="store_true", help="Count targets without sending network requests.")
    p.add_argument("--limit", type=int, help="Review only the first N unique primary links.")
    p.add_argument("--timeout", type=float, default=12)
    p.add_argument("--workers", type=int, default=6)
    p.add_argument("--output", default=str(ROOT / "reports" / "link-review.json"))
    args = p.parse_args()
    if args.workers < 1 or args.workers > 12 or args.timeout <= 0 or (args.limit is not None and args.limit < 1):
        p.error("Use 1–12 workers, a positive timeout, and a positive limit.")
    data = load()
    errors, _ = validate(data)
    if errors:
        p.error("Catalog is invalid: " + "; ".join(errors))
    urls = list(dict.fromkeys(r["url"] for r in data["resources"]))
    if args.limit:
        urls = urls[:args.limit]
    if args.dry_run:
        print(f"Would review {len(urls)} unique primary URLs. No network requests sent.")
        return
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        findings = list(pool.map(lambda u: inspect(u, args.timeout), urls))
    report = {"attempted_at": datetime.now(timezone.utc).isoformat(), "note": "Reachability is not content quality, enrollment, checkout or safety verification. 403/429/timeouts require manual review.", "results": findings}
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    for f in findings:
        if f["result"] != "reachable":
            print(f["result"], f.get("http_status", "network"), f["url"])
    print("Review report:", output)

if __name__ == "__main__":
    main()
