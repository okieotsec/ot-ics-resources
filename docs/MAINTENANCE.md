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

## Refreshing the website

The Resources page on okieotsec.com shows a generated snapshot of `resources.json`; it does not update itself. After a catalog change is merged here:

1. In the website repository (`okieotsec/okieotsec.github.io`), run `python3 scripts/refresh_resources.py` (add `--ref <sha>` to pin a commit). It downloads `resources.json` at the exact commit over https, checks the schema version and counts, and records the commit and the file's SHA-256 in `_data/resources_source.json`.
2. Run `python3 scripts/refresh_resources.py --verify` (offline) and build the site locally.
3. Open a pull request in the website repository with the two changed files in `_data/`, and merge it once the build succeeds.

The first snapshot was taken from commit `a93684f07b28d7a144a36020aa4fd39792933a9a` (104 entries, SHA-256 `fcdb2439237aa4593c179b968638a07824ec5e6ffe188d39d3ade06d9d4015d7`).

Check subscriptions and promotions before presenting prices as current. Preserve historical references and draft status where appropriate. Do not redistribute the SANS manual, paid books, licensed standards, restricted reports or packet captures merely because their URLs are public.
