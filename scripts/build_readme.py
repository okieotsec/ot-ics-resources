# SPDX-License-Identifier: MIT
"""Generate README from the canonical catalog and the editorial template."""
from pathlib import Path
from urllib.parse import quote
import argparse
import re
import sys
from catalog import ROOT, load, validate

ACCESS_LABELS = {
    "public_free": ("🟢", "Free"),
    "free_with_conditions": ("🟡", "Free, with conditions"),
    "paid": ("🔵", "Paid"),
}


def md(value):
    """Escape text for Markdown: resource text is data, never trusted markup."""
    text = str(value).replace("\n", " ")
    for ch in ("\\", "[", "]", "*", "_", "`", "<", ">", "|"):
        text = text.replace(ch, "\\" + ch)
    return text


def link(title, url):
    return "[" + md(title) + "](" + quote(url, safe=":/?&=#%+~;,!@$") + ")"


def slug(text):
    """The anchor GitHub gives a heading: lower case, punctuation dropped, spaces to hyphens."""
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def access_badge(r):
    icon, label = ACCESS_LABELS[r["access_class"]]
    return f"{icon} {label}"


def card(r, heading="####"):
    parts = [f"{heading} {r['id']} · {link(r['title'], r['url'])}" + (" — ⭐ Recommended starting point" if r.get("recommended") else ""), "",
             f"**Best fit:** {md(r['level'])}  ", f"**Access:** {access_badge(r)}. {md(r['access'])}  ", f"**Cost:** {md(r['cost'])}", "", md(r['summary']), "", "**Use it for:** " + md(r['practical_use']), ""]
    if r.get("publication_status"):
        parts += ["**Publication status:** " + md(r["publication_status"]), ""]
    for key, label in (("related_url", "Related official source/project"), ("evidence_url", "Supporting publisher source")):
        if r.get(key) and r[key] != r["url"]:
            parts += [f"**{label}:** {link('Open link', r[key])}", ""]
    if r.get("manual_pdf_pages"):
        parts += ["**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) " + ", ".join(map(str, r["manual_pdf_pages"])) + " (printed page(s) " + ", ".join(map(str, r["manual_printed_pages"])) + ").", ""]
    parts += ["**Review date:** " + md(r["last_reviewed"]), "", "**Verification:** " + md(r["verification"]), ""]
    return "\n".join(parts) + "\n"


def folded(rows, heading):
    """Full cards for a group of resources, folded so the page stays easy to scan."""
    noun = "resource" if len(rows) == 1 else "resources"
    body = "".join(card(r, heading) for r in rows)
    return f"<details>\n<summary>Details for the {len(rows)} {noun} above</summary>\n\n{body}</details>\n"


def free_table(rows):
    lines = ["| ID | Resource | Best fit | Access |", "| --- | --- | --- | --- |"]
    for r in rows:
        star = " ⭐" if r.get("recommended") else ""
        lines.append(f"| {r['id']} | {link(r['title'], r['url'])}{star} | {md(r['level'])} | {access_badge(r)} |")
    return "\n".join(lines) + "\n"


def categories(free):
    return list(dict.fromkeys(r["category"] for r in free))


def contents(free):
    items = [f"- [{md(c)}](#{slug(c)}) ({sum(r['category'] == c for r in free)})" for c in categories(free)]
    items += ["- [Affordable paid resources](#affordable-paid-resources)", "- [Publishing and maintenance](#publishing-and-maintenance)"]
    return "\n".join(items)


def glance(free, paid):
    lines = ["| Topic | Resources |", "| --- | ---: |"]
    lines += [f"| [{md(c)}](#{slug(c)}) | {sum(r['category'] == c for r in free)} |" for c in categories(free)]
    lines.append(f"| [Affordable paid resources](#affordable-paid-resources) | {len(paid)} |")
    return "\n".join(lines)


def render(data):
    rows = data["resources"]
    free = [r for r in rows if r["cost_group"] == "free"]
    paid = [r for r in rows if r["cost_group"] == "paid"]
    chunks = ["## Free resources\n\nEntries with forms, registration, eligibility or limited tiers keep those conditions in their cards. Hardware and setup requirements stay visible in each access note.\n"]
    for category in categories(free):
        group = [r for r in free if r["category"] == category]
        chunks += ["### " + md(category) + "\n", free_table(group), folded(group, "####")]
    chunks += ["## Affordable paid resources\n\nPrices are observed publisher listings. Check billing periods, promotions, regional pricing and checkout before buying.\n",
               "| ID | Resource | Best fit | Observed cost | Buying priority |\n| --- | --- | --- | --- | --- |\n"
               + "\n".join(f"| {r['id']} | {link(r['title'], r['url'])} | {md(r['level'])} | {md(r['cost'])} | {md(r.get('priority', 'Optional'))} |" for r in paid) + "\n",
               folded(paid, "####")]
    template = (ROOT / "README.template.md").read_text(encoding="utf-8")
    values = {"research_date": data["research_date"], "free_count": data["counts"]["free"], "paid_count": data["counts"]["paid"],
              "total_count": data["counts"]["total"], "category_count": len(categories(free)), "contents": contents(free),
              "glance": glance(free, paid), "catalog": "\n".join(chunks)}
    for key, value in values.items():
        template = template.replace("{" + key + "}", str(value))
    return template.rstrip() + "\n"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true", help="Fail when committed README differs from generated content.")
    args = p.parse_args()
    data = load()
    errors, _ = validate(data)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    content = render(data)
    target = ROOT / "README.md"
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            print("README is stale. Run python3 scripts/build_readme.py", file=sys.stderr)
            return 1
        print("README matches resources.json and README.template.md")
    else:
        target.write_text(content, encoding="utf-8")
        print("Generated", target.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
