# Feature the catalog on the existing OkieOTSec.com website

## Discovery before implementation

Identify the actual GitHub Pages repository from the user's account, remotes, Pages configuration and CNAME. Do not assume its name or framework. Inspect its README, repository instructions, package/build configuration and current deployment workflow.

Keep the current framework and theme. The new resources repository is the content source; the existing website remains the published domain. Do not add a new CNAME to the resources repository or change the existing site's DNS/domain settings.

## Minimum page behavior

- A Resources link in the existing site's navigation.
- A `/resources/` page or the equivalent route in the site's current router.
- The heading “OT/ICS Resources” and a short accessibility-first introduction.
- Free resources first, with affordable paid options in a visibly separate section.
- Search across title, summary, category and practical use.
- Filters for topic, audience and access class.
- Resource title, summary, practical use, audience, access conditions, review date, and link.
- Observed prices and billing periods on paid entries.
- Draft/publication status, verification limits, and related source links where relevant.
- Clear loading, empty-result and data-unavailable states.
- A link to the canonical GitHub repository and its contribution instructions.

Keep the page practical and readable. Avoid hiding important limits behind hover-only controls or making all details dependent on JavaScript. Favor the site's current static rendering approach.

## Content synchronization

Preferred: fetch/import the catalog at build time, render searchable data through the current site's tooling, and retain provenance identifying the resources-repo commit used.

If the existing Pages setup cannot safely import another repository during its build, generate a local snapshot from the canonical JSON for the initial site PR. Record its source repo, full commit SHA and SHA-256 in a sidecar file. Document how to refresh it. A snapshot is a generated derivative, not a second manually edited catalog.

Do not require a secret or paid service just to display a public catalog. Do not introduce cross-repository dispatch tokens for the initial implementation unless genuinely required and explicitly authorized. A manual refresh path is acceptable for the first version.

Keep JSON content as text. Use the framework's normal escaping or DOM `textContent`; do not inject resource titles/summaries as trusted HTML.

## Brand assets

The resource repo carries the OkieOTSec brand kit v1.1 files it needs under `assets/brand/` (vector originals in `svg/`). The website uses the brand kit's own tokens, so use the website's existing colors and fonts rather than a separate palette, and keep alt text meaningful. Do not redraw the logo.

## Validation and merge

Run the site's real build/lint/test commands. Inspect at desktop and mobile widths. Exercise search, combined filters, resetting filters, empty results, keyboard controls and external links. Check paid/free separation and that all 88 initial records are represented.

Use a separate PR in the website repository. After its required checks pass, merge within the user's authorization. Preserve CNAME, existing routes and deployment settings. Verify the deployed resources route when the deployment completes; report a pending deployment as pending, not as a verified published page.

OT Triage is outside this integration scope.
