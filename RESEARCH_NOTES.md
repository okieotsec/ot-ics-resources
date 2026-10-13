# Research notes

Research performed October 12, 2026. This document records material access/version distinctions for maintainers.

## High-value checks

- [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) is a final publication. The publisher points to the [Rev. 4 initial public draft](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd), published September 21, 2026, with comments due November 30, 2026.
- [NIST IR 8183 Rev. 2](https://csrc.nist.gov/pubs/ir/8183/r2/ipd) is labeled an initial public draft. The earlier [CSF 1.1 manufacturing profile](https://www.nist.gov/publications/cybersecurity-framework-version-11-manufacturing-profile) is provided as a related resource.
- [CISA's July–August 2026 training bulletin](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/41d85e1) lists on-demand OPSEC/210W, FRE2115, ICS300, and ICS401, and describes eligible audiences. It is evidence of the program, not a promise of current seats for the expired in-person dates in that bulletin.
- CISA calendar and individual program pages were also found in official search indexes, but direct CISA/INL retrieval often returned HTTP 403. The catalog records this limitation rather than claiming live enrollment was tested.
- [WaterISAC's current fundamentals page](https://www.waterisac.org/fundamentals) links a public [12-fundamentals PDF](https://www.waterisac.org/wp-content/uploads/2024/12/WaterISAC_12-Fundamentals_FULL-12-High-Res.pdf) and a [small-systems PDF](https://www.waterisac.org/wp-content/uploads/2024/12/WaterISAC-Cybersecurity-Fundamentals-Small-System-Compendium.pdf). These were accessible through the public publisher links; WaterISAC's other services may be membership restricted.
- [Labshock pricing](https://labshocksecurity.com/pricing/) lists a limited free tier and introductory Pro cards of $24/month or $14/month billed yearly. Standard rates in its comparison table differ. The [official repository](https://github.com/zakharb/labshock) describes a five-minute initialization delay and forty-minute free session limit. The README therefore avoids promising a specific free session length across releases.
- [Factory I/O editions](https://factoryio.com/editions/) distinguish Starter's included control simulator from external Modbus/OPC connectivity. A thirty-day trial is not classified as unrestricted free software.
- [Ackerman's book page](https://www.packtpub.com/en-us/product/industrial-cybersecurity-9781800202092) showed discounted prices; [Brooks/Craig's publisher page](https://www.wiley-vch.de/en/areas-interest/computing-computer-sciences/practical-industrial-cybersecurity-978-1-119-88302-9) displayed $42.90. Both are older publications, identified by date.
- [Wiley's US ISA catalog](https://www.wiley.com/en-us/shop/international-society-of-automation-c-6473) lists Mustard's book starting at $95. A different regional publisher listing showed a higher price; use the US catalog as the stated source and confirm format at checkout.
- [Packt Premium](https://www.packtpub.com/en-us/subscribe-premium-access) advertised $29.99/month in publisher-indexed evidence. Direct page retrieval failed; do not imply checkout verification.
- RealPars and SolisPLC paid full-course memberships were researched but omitted from the primary paid picks because their PLC plans were around $60/$59 monthly. Their genuinely free public/limited content remains in the free catalog.
- Expensive professional certification courses, commercial monitoring platforms, and quote-only organization licenses were not selected as low-cost resources.

## Selection method

Prefer the organization that publishes a standard or guide, the project's official repository, and public research by the team that performed it. Avoid unofficial PDF mirrors and expired sale bundles. Include community capture collections as secondary practice resources, while flagging provenance and license limits.

Audience labels and learning-path ordering are curator judgments. The practical-use field suggests what a learner could do with a resource; it does not state that the publisher supplies every proposed exercise.

## Data

`resources.json` contains 104 entries (88 from the first batch and 16 added on October 13, 2026), each with a stable ID, category, title, URL, summary, practical use, level, cost group, cost, access description, verification note, and research date. Some entries include a publication status, supporting evidence URL, related URL, recommendation, or buying-priority field.

The data and Markdown cover the same entries. They are delivered for review and reuse; nothing has been pushed to GitHub.


## October 13, 2026 additions (R089 to R104)

Sixteen entries were added after opening each official page; the `verification` field of each record says exactly what was read. In short:

- **Fetched and read on October 13, 2026:** MITRE EMB3D (R089, showed version 2.0.2 of June 1, 2026), CISA ICSNPP (R090, BSD-3-Clause, protocol list read), Snap7 (R091, a framed site; the license name was not shown), GRFICS (R092, GPL-3.0, VirtualBox setup, older Ubuntu 16.04 images, pre-built VMs no longer hosted), Mike Holcomb's site (R093), the Unsolicited Response podcast page (R094), ICS Village (R095), NIST SP 1800-10 (R096, final, March 2022), FIRST's CVSS v4.0 and EPSS pages (R097, R098), CISA's KEV catalog page (R099, 1,739 entries that day), CISA's Primary Mitigations fact sheet (R102, May 6, 2025), the Awesome ICS list (R103, Apache-2.0) and ICS-Security-Tools (R104, CC BY 4.0).
- **Other evidence:** the CSAF repository (R100) was inspected through the GitHub API (OT advisory folders, an index, per-advisory files; no license file detected); the podcast's activity dates (R094) come from podcast-directory listings; OT Triage (R101) is the maintainer's own project, checked by the maintainer.
- **Not done:** no video, e-book, challenge, data file, API or software was opened, downloaded, built or run; no account was created; prices were not checked because none of these entries is paid.
- **Why these:** they fill gaps in the first 88 entries (embedded-device threat modeling, protocol parsing for monitoring, hands-on simulators, vulnerability prioritization data and standards, community-curated lists) and are official or well-known community sources.

## Advisory link review, October 13, 2026

`python3 scripts/check_links.py` checked the 100 unique primary URLs once: 92 responded normally and 8 were flagged for manual review. No resource was removed, reclassified or re-dated because of this. A response (or its absence) proves nothing about enrollment, checkout, content quality or safety.

| Flagged URL | What was seen | Reading |
| --- | --- | --- |
| automationdirect.com PLC training | A redirect to a single-sign-on callback ("login required") | The page works in a browser; the redirect is automated-access handling. |
| codesys.com development system | HTTP 429 | Rate limiting of an automated request. |
| cyber.gov.au (two ASD publications) | No connection from the research network | Could not be reached from here; both pages were reachable in the first research pass. Recheck from another network. |
| inl.gov CIE resource library and CCE pages | HTTP 403 | Known to block automated access (see above). |
| packtpub.com (book page and Premium subscription) | HTTP 403 | Automated-access blocking; prices stay marked as observed publisher listings. |

## SANS manual follow-up

Added 15 free entries from the uploaded manual, with PDF/printed page provenance and current official destinations. See [SANS_MANUAL_ADDITIONS.md](SANS_MANUAL_ADDITIONS.md). GRASSMARLIN and unverified old links are recorded separately; existing resources were not duplicated.
