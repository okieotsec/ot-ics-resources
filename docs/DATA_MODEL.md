# Catalog data model

`resources.json` is the canonical publication source. The catalog began with 88 stable resource IDs and now has more (see the counts); new records are appended. Validation should allow the count to grow rather than hardcoding 88 forever.

## Top-level fields

| Field | Purpose |
| --- | --- |
| `schema_version` | Data-contract version; version 2 adds website filter fields. |
| `title` | Catalog title. |
| `research_date` | Original research batch date. Per-resource review dates are authoritative for later updates. |
| `counts` | Derived free, paid and total counts. Refresh using `scripts/update_counts.py`. |
| `resources` | Resource records. |

## Required record fields

| Field | Purpose |
| --- | --- |
| `id` | Stable ID such as R074; never renumber existing records. |
| `category` | Human-readable topic. |
| `title`, `url` | Resource title and official primary link. |
| `level` | Human-readable audience guidance retained from the research. |
| `audience_tags` | Normalized audience filters; a record may have multiple values. |
| `summary` | Original description of what the resource provides. |
| `practical_use` | Editorial suggestion for using it. |
| `cost_group` | `free` or `paid`, for the principal split. |
| `access_class` | `public_free`, `free_with_conditions` or `paid`, for the more detailed website filter. |
| `cost` | Observed price text, including billing context; $0 for free entries. |
| `access` | Account, eligibility, limited-tier, license, hardware and other conditions. |
| `last_reviewed` | YYYY-MM-DD research/review date. |
| `verification` | Exact limits of the research, including blocked retrieval. |

`access_class` is a curator-assigned display category, not proof of universal availability. Read the detailed `access` note. Forms or accounts that may apply are represented conservatively as free with conditions; ordinary local computing requirements remain in the notes.

## Optional fields

`recommended`, `priority`, `publication_status`, `related_url`, `evidence_url`, `discovery_source`, `manual_pdf_pages`, `manual_printed_pages`, and `manual_original_url` preserve useful recommendation/provenance information. Avoid discarding them when creating a website view.

`audience_tags` currently includes `foundation`, `practitioner`, `specialist`, `program-lead`, `architect`, and `electric-sector`. Display reader-friendly labels and keep tags combinable.

## Maintenance

Append new stable IDs. Never create a new ID merely because a publisher changes a URL. If a resource is archived later, preserve its identity and record the reason rather than silently dropping it. Do not assume shared URLs are duplicates: CISA courses share a portal, and Labshock plans share a pricing page.

The supplied Python validator enforces this publishing contract directly. It is a standard-library validator, not a general JSON Schema engine.
