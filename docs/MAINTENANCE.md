# Maintain an accessible catalog

## Updating a resource

Change the canonical JSON record, preserve its ID, and describe the official evidence supporting changes to cost, access or availability. Update `last_reviewed` only when the content/access information was actually reviewed. Record meaningful changes in CHANGELOG.md.

```bash
python3 scripts/update_counts.py
python3 scripts/validate_catalog.py
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
```

The generator preserves the split between free and paid resources and includes verification/provenance notes. Commit both the data and regenerated README.

## Link review

```bash
python3 scripts/check_links.py --dry-run
python3 scripts/check_links.py --limit 10
python3 scripts/check_links.py
```

The manual GitHub Actions workflow publishes review candidates in its job summary. Local runs retain the full JSON under ignored `reports/`.

- 2xx/3xx indicates HTTP reachability only.
- 403/429, timeout, DNS and TLS failures need manual review.
- 404/410 is an unavailable candidate, not an automatic deletion decision.
- A signup page, paywall or redirected homepage may respond successfully while the resource is inaccessible.

This script does not change resource data or review dates. The live network review is not a required PR gate because automated-access blocking would produce misleading failures.

## Publishing

Use PRs. Required data/generated-file checks should pass on the reviewed commit. Refresh the website from the canonical data and record the source SHA according to WEBSITE_INTEGRATION.md.

Check subscriptions and promotions before presenting prices as current. Preserve historical references and draft status where appropriate. Do not redistribute the SANS manual, paid books, licensed standards, restricted reports or packet captures merely because their URLs are public.
