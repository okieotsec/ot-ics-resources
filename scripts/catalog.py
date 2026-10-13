# SPDX-License-Identifier: MIT
"""Publishing rules for the catalog. Python 3.10+, standard library only."""
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("id", "category", "title", "url", "level", "summary", "practical_use", "cost_group", "cost", "access", "last_reviewed", "verification", "access_class", "audience_tags")

def valid_url(value):
    if not isinstance(value, str) or re.search(r"\s", value):
        return False
    try:
        u = urlsplit(value)
        return u.scheme == "https" and bool(u.hostname) and not u.username and not u.password
    except ValueError:
        return False

def validate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["Catalog must be a JSON object."], []
    if data.get("schema_version") != 2:
        errors.append("schema_version must be 2.")
    for key in ("title", "research_date"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"{key} must be a nonempty string.")
    try:
        date.fromisoformat(data.get("research_date", ""))
    except (ValueError, TypeError):
        errors.append("research_date must be an ISO date.")
    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        return ["resources must be a nonempty array."], []
    ids, urls = [], []
    for index, r in enumerate(resources):
        label = f"entry {index + 1}"
        if not isinstance(r, dict):
            errors.append(f"{label}: must be an object.")
            continue
        label = r.get("id", label)
        for key in REQUIRED:
            if key not in r:
                errors.append(f"{label}: missing {key}.")
        for key in REQUIRED:
            if key == "audience_tags":
                continue
            if key in r and (not isinstance(r[key], str) or not r[key].strip()):
                errors.append(f"{label}: {key} must be a nonempty string.")
        if not re.fullmatch(r"R\d{3,}", str(r.get("id", ""))):
            errors.append(f"{label}: ID must use R plus at least three digits.")
        ids.append(str(r.get("id", "")))
        for key in ("url", "related_url", "evidence_url"):
            if key in r and not valid_url(r[key]):
                errors.append(f"{label}: invalid HTTPS URL in {key}.")
        if isinstance(r.get("url"), str):
            urls.append(r["url"])
        group = r.get("cost_group")
        if group not in ("free", "paid"):
            errors.append(f"{label}: cost_group must be free or paid.")
        if group == "free" and r.get("cost") != "$0":
            errors.append(f"{label}: free entries must have cost $0; explain extra costs in access.")
        if group == "paid" and r.get("cost") == "$0":
            errors.append(f"{label}: paid entry cannot have cost $0.")
        access = r.get("access_class")
        if access not in ("public_free", "free_with_conditions", "paid"):
            errors.append(f"{label}: invalid access_class.")
        if group == "paid" and access != "paid":
            errors.append(f"{label}: paid entry must use paid access_class.")
        if group == "free" and access == "paid":
            errors.append(f"{label}: free entry cannot use paid access_class.")
        tags = r.get("audience_tags")
        if not isinstance(tags, list) or not tags or any(not isinstance(t, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", t) for t in tags):
            errors.append(f"{label}: audience_tags must be a nonempty list of lowercase slugs.")
        if "recommended" in r and not isinstance(r["recommended"], bool):
            errors.append(f"{label}: recommended must be a boolean.")
        try:
            date.fromisoformat(r.get("last_reviewed", ""))
        except (ValueError, TypeError):
            errors.append(f"{label}: last_reviewed must be an ISO date.")
        for key in ("manual_pdf_pages", "manual_printed_pages"):
            if key in r and (not isinstance(r[key], list) or any(type(p) is not int or p < 1 for p in r[key])):
                errors.append(f"{label}: {key} must contain positive integer page numbers.")
    duplicate_ids = [i for i, n in Counter(ids).items() if n > 1]
    if duplicate_ids:
        errors.append("Duplicate IDs: " + ", ".join(duplicate_ids))
    for u, n in Counter(urls).items():
        if n > 1:
            warnings.append(f"Shared URL used by {n} distinct entries: {u}")
    counts = {"free": sum(isinstance(r, dict) and r.get("cost_group") == "free" for r in resources), "paid": sum(isinstance(r, dict) and r.get("cost_group") == "paid" for r in resources), "total": len(resources)}
    if data.get("counts") != counts:
        errors.append(f"counts must match actual entries: {counts}")
    return errors, warnings

def load(path=None):
    return json.loads(Path(path or ROOT / "resources.json").read_text(encoding="utf-8"))
