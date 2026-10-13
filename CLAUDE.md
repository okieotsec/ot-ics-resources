# OkieOTSec resource repository

This repository is a curated directory, not a mirror of third-party documents. Keep the content accessible and the maintenance process simple.

## Source of truth

- Edit `resources.json` for resource changes.
- Edit `README.template.md` for shared introduction and editorial policy.
- Generate `README.md`; do not edit its resource cards by hand.
- Preserve resource IDs and important access/cost limitations.
- Do not change review dates merely because a link responds.
- Shared portal URLs are valid for different courses/plans. IDs, not URLs, identify resources.

## Checks

```bash
python3 scripts/update_counts.py
python3 scripts/validate_catalog.py
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
python3 -m unittest discover -s tests
python3 -m compileall -q scripts tests
```

The implementation uses Python's standard library. Live link review is advisory and separate from required content checks:

```bash
python3 scripts/check_links.py --dry-run
python3 scripts/check_links.py
```

Treat 403, 429 and timeouts as manual-review cases. Never automatically delete entries or assert enrollment, purchase or tool functionality from an HTTP response.

## Integration

Use `docs/WEBSITE_INTEGRATION.md` for the existing OkieOTSec.com site. Preserve its existing build system, routes and CNAME. Do not modify OT Triage as part of this work.

Use normal pull requests and passing checks. Do not disable repository protections or use admin bypass to merge. Follow applicable repository instructions and the user's task authorization.

## Editorial scope

Free entries come first. Keep affordable paid options visibly separate. Distinguish draft guidance from final publications, educational overviews from licensed normative standards, public content from account-gated material, and permanent free tiers from trials.

Use official publisher/project links wherever possible. Retain research limitations and original summaries. Do not add copyrighted PDFs, licensed standards, API credentials or private facility information.
