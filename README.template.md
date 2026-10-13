<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/brand/png/okieotsec-lockup-dark-1200.png">
    <img src="assets/brand/png/okieotsec-lockup-1200.png" alt="OkieOTSec" width="420">
  </picture>
</p>

<h1 align="center">OT/ICS and Industrial Cybersecurity Resources</h1>

<p align="center"><em>An accessibility-first collection for people learning industrial automation, moving from IT security into OT, or defending operational environments.</em></p>

<p align="center">
  <a href="https://github.com/okieotsec/ot-ics-resources/actions/workflows/catalog.yml"><img alt="Catalog checks" src="https://github.com/okieotsec/ot-ics-resources/actions/workflows/catalog.yml/badge.svg"></a>
  <img alt="{total_count} resources" src="https://img.shields.io/badge/resources-{total_count}-2E6CB5">
  <img alt="License: CC BY 4.0 and MIT" src="https://img.shields.io/badge/license-CC%20BY%204.0%20%C2%B7%20MIT-lightgrey">
</p>

<p align="center">
  <a href="https://okieotsec.com/resources/">Browse and filter on OkieOTSec.com</a> ·
  <a href="CONTRIBUTING.md">Contribute</a> ·
  <a href="LICENSE.md">License</a> ·
  <a href="resources.json">Data (JSON)</a>
</p>

| {free_count} | {paid_count} | {category_count} | Oct 12–13, 2026 |
| :---: | :---: | :---: | :---: |
| free, or free with conditions | affordable paid options | topics | research and review dates |

This is a substantial starting catalog, not a claim that every worthwhile resource on the internet is included. Selection favors authoritative publishers, practical learning value, and accessible entry points. Level assignments, recommendations, and practical-use suggestions are editorial judgments.

**Legend:** 🟢 free · 🟡 free, with conditions (an account, eligibility, a limited tier, or a license to read) · 🔵 paid · ⭐ a good place to start

## Start here: a free learning path

| Step | Resource | Outcome |
| ---: | --- | --- |
| 1 | [Lessons in Industrial Instrumentation](https://www.ibiblio.org/kuphaldt/socratic/sinst/doc/liii.html) | Explain a sensor-to-controller-to-actuator control loop. |
| 2 | [AutomationDirect PLC training](https://www.automationdirect.com/programmable-logic-controllers/plc-training) | Recognize I/O, scan cycles, and ladder logic. |
| 3 | [Inductive University](https://inductiveautomation.com/resources/video/inductive-university) | Understand SCADA and operator-facing applications. |
| 4 | [CISA introductory ICS modules](https://ics-training.inl.gov/) | Describe IT/OT differences and operational cyber risks; eligibility applies. |
| 5 | [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Review a basic OT architecture and its safeguards. |
| 6 | [ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | Navigate the standards series and its stakeholder roles. |
| 7 | [Modbus references](https://www.modbus.org/modbus-specifications) + [Wireshark captures](https://wiki.wireshark.org/SampleCaptures) | Decode an industrial request and response. |
| 8 | [OpenPLC](https://autonomylogic.com/products/openplc) | Run and debug a small control program without physical hardware. |
| 9 | [Malcolm](https://github.com/cisagov/Malcolm) | Inspect a capture and identify devices and communications. |
| 10 | [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) | Connect an observed behavior to a threat technique and possible evidence. |

A suggested progression, not a certification syllabus. Start with offline captures and simulated control programs if equipment or compute resources are limited.

## How to read the entries

- **Foundation:** learning automation or OT security concepts; little OT experience assumed.
- **Practitioner:** comfortable with basic networking/security or automation and ready for applied work.
- **Specialist:** deeper protocol, research, engineering, or assessment work.
- **Program lead / Architect / Sector specialist:** the role the resource best supports, rather than a required seniority.

“Free” means the listed content or software has a no-fee route. It does not mean that hardware, travel, electricity, hosting, all product features, or an unrestricted license are included. Registration, eligibility, limited tiers, and extra costs are called out individually. Paid products with only a short trial remain in the paid section.

For paid resources, the priority is roughly **US$100 or less for a book**, or **about US$30/month or less for personal learning**, plus low annual-cost software. These are editorial budget bands, not universal definitions of affordability. Prices are publisher observations, not guaranteed checkout quotes; taxes, shipping, currency conversion, region, and promotions can change them.

## Topics

{glance}

{catalog}
## Publishing and maintenance

The catalog is kept as [structured JSON](resources.json), which is the source of truth, and this README is generated from it with `python3 scripts/build_readme.py`. The same data drives the filterable page on [OkieOTSec.com](https://okieotsec.com/resources/). See [the data model](docs/DATA_MODEL.md) for the fields, including `access_class` and `audience_tags`, which support the site's filters; keep the detailed conditions visible when filtering.

### Editorial boundaries

- Link to the original resource. Summaries here are original annotations; do not mirror copyrighted books, standards, vendor reports, or packet captures without permission.
- The free ISA overview explains 62443; it is not the normative standards text. Authorized access to individual ISA/IEC standards has separate terms.
- NIST SP 800-82 Rev. 3 remains the final reference in this catalog; Rev. 4 is explicitly a draft. The CSF 2.0 manufacturing profile is also marked as a draft.
- Public research from vendors is valuable, but findings reflect each publisher's visibility and methods. Compare sources before generalizing to the entire industry.
- A public GitHub repository is not automatically fully open source. Labshock includes proprietary components and has use-specific licensing.
- Lab exercises, active assessment tools, and adversary emulation belong in isolated environments you own or are authorized to test. Production changes require site-specific engineering review.
- Public packet captures can be free to download without being licensed for republication. Prefer linking to their source.
- Historical books remain useful for principles; pair them with current official standards, advisories, and software documentation.
- One entry (OT Triage) is a project maintained by the author of this catalog, and says so.

### Research and verification limits

Entries were researched using original publisher pages, official repositories, or publisher search-index evidence. Some CISA/INL pages returned HTTP 403 to the research tool; official indexed material and CISA's 2026 training bulletin supported inclusion. Some other pages could only be reviewed through search-index evidence, as noted. This catalog does not claim successful login, enrollment, checkout, download of every linked file, or hands-on validation of every tool.

Use `python3 scripts/check_links.py` for a link-review report. Check links and access terms quarterly. Recheck subscription prices and promotions before displaying them prominently. Keep resource IDs stable, record changes, and move broken or abandoned resources into an archive rather than silently replacing their identity.

The first 88 entries were researched on October 12, 2026, including 15 from a user-supplied SANS manual ([SANS_MANUAL_ADDITIONS.md](SANS_MANUAL_ADDITIONS.md)). Sixteen more (R089 to R104) were added on October 13, 2026 after opening each official page; see [RESEARCH_NOTES.md](RESEARCH_NOTES.md) for what was and was not verified, and [CHANGELOG.md](CHANGELOG.md).

See [CONTRIBUTING.md](CONTRIBUTING.md) to suggest a resource or report a correction.
