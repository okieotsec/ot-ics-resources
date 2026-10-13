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
  <img alt="104 resources" src="https://img.shields.io/badge/resources-104-2E6CB5">
  <img alt="License: CC BY 4.0 and MIT" src="https://img.shields.io/badge/license-CC%20BY%204.0%20%C2%B7%20MIT-lightgrey">
</p>

<p align="center">
  <a href="https://okieotsec.com/resources/">Browse and filter on OkieOTSec.com</a> ·
  <a href="CONTRIBUTING.md">Contribute</a> ·
  <a href="LICENSE.md">License</a> ·
  <a href="resources.json">Data (JSON)</a>
</p>

| 98 | 6 | 11 | Oct 12–13, 2026 |
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

| Topic | Resources |
| --- | ---: |
| [Automation fundamentals](#automation-fundamentals) | 8 |
| [Security learning and reference](#security-learning-and-reference) | 18 |
| [Frameworks and architecture](#frameworks-and-architecture) | 15 |
| [Engineering and sector guidance](#engineering-and-sector-guidance) | 7 |
| [Industrial protocol references](#industrial-protocol-references) | 5 |
| [Labs and protocol tooling](#labs-and-protocol-tooling) | 14 |
| [Monitoring and investigation](#monitoring-and-investigation) | 10 |
| [Packet captures and datasets](#packet-captures-and-datasets) | 2 |
| [Threat intelligence and research](#threat-intelligence-and-research) | 11 |
| [Incident response and exercises](#incident-response-and-exercises) | 3 |
| [Vulnerability management and prioritization](#vulnerability-management-and-prioritization) | 5 |
| [Affordable paid resources](#affordable-paid-resources) | 6 |

## Free resources

Entries with forms, registration, eligibility or limited tiers keep those conditions in their cards. Hardware and setup requirements stay visible in each access note.

### Automation fundamentals

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R001 | [Lessons in Industrial Instrumentation — Tony R. Kuphaldt](https://www.ibiblio.org/kuphaldt/socratic/sinst/doc/liii.html) ⭐ | Foundation → Practitioner | 🟢 Free |
| R002 | [Lessons in Electric Circuits — All About Circuits](https://www.allaboutcircuits.com/textbook/) | Foundation | 🟢 Free |
| R003 | [AutomationDirect free PLC training](https://www.automationdirect.com/programmable-logic-controllers/plc-training) ⭐ | Foundation → Practitioner | 🟡 Free, with conditions |
| R004 | [Inductive University — Ignition](https://inductiveautomation.com/resources/video/inductive-university) ⭐ | Foundation → Practitioner | 🟡 Free, with conditions |
| R005 | [Siemens SCE learning and training documents](https://www.siemens.com/en-us/content/sce-educational-institutions/learning-modules/) | Foundation → Practitioner | 🟡 Free, with conditions |
| R006 | [RealPars public videos](https://www.youtube.com/@RealPars) | Foundation | 🟢 Free |
| R007 | [SolisPLC free plan](https://www.solisplc.com/join) | Foundation | 🟡 Free, with conditions |
| R008 | [CODESYS Development System](https://www.codesys.com/products/engineering/development-system/) | Foundation → Practitioner | 🟡 Free, with conditions |

<details>
<summary>Details for the 8 resources above</summary>

#### R001 · [Lessons in Industrial Instrumentation — Tony R. Kuphaldt](https://www.ibiblio.org/kuphaldt/socratic/sinst/doc/liii.html) — ⭐ Recommended starting point

**Best fit:** Foundation → Practitioner  
**Access:** 🟢 Free. Free downloadable textbook; select the stable edition  
**Cost:** $0

An extensive open textbook covering industrial measurement, control loops, instrumentation, PLCs, and process safety. Available as downloadable material for deeper study.

**Use it for:** Learn what sensors, actuators, and control systems actually do before analyzing their security.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R002 · [Lessons in Electric Circuits — All About Circuits](https://www.allaboutcircuits.com/textbook/)

**Best fit:** Foundation  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

A free electrical and electronics textbook covering DC/AC circuits, semiconductors, digital circuits, and practical experiments.

**Use it for:** Build the electrical background needed to understand industrial I/O and field devices.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R003 · [AutomationDirect free PLC training](https://www.automationdirect.com/programmable-logic-controllers/plc-training) — ⭐ Recommended starting point

**Best fit:** Foundation → Practitioner  
**Access:** 🟡 Free, with conditions. Training free; registration may be required; physical controllers are extra  
**Cost:** $0

Video libraries introduce PLC control and provide product-specific instruction for AutomationDirect controller families. The provider also links free programming software.

**Use it for:** Learn scan cycles, I/O, ladder logic, and basic controller programming.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R004 · [Inductive University — Ignition](https://inductiveautomation.com/resources/video/inductive-university) — ⭐ Recommended starting point

**Best fit:** Foundation → Practitioner  
**Access:** 🟡 Free, with conditions. Training free; account for progress/credentials; production Ignition licensing separate  
**Cost:** $0

Free online training for Ignition, a widely used SCADA platform. Lessons explain the software and its use in industrial visualization and automation.

**Use it for:** Understand SCADA projects, operator interfaces, data collection, and application structure.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R005 · [Siemens SCE learning and training documents](https://www.siemens.com/en-us/content/sce-educational-institutions/learning-modules/)

**Best fit:** Foundation → Practitioner  
**Access:** 🟡 Free, with conditions. Documents free with Siemens ID and extended SiePortal rights; software/hardware for exercises may cost extra  
**Cost:** $0

Modular educational materials teach Siemens automation technologies through documents and projects. Modules can be selected according to existing knowledge.

**Use it for:** Study Siemens PLC engineering workflows and build structured automation exercises.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R006 · [RealPars public videos](https://www.youtube.com/@RealPars)

**Best fit:** Foundation  
**Access:** 🟢 Free. Public videos free; full structured courses paid  
**Cost:** $0

Short public videos explain industrial automation components and concepts with visual examples. The public channel is separate from the subscription course catalog.

**Use it for:** Quickly understand PLCs, sensors, control panels, and common automation terminology.

**Supporting publisher source:** [Open link](https://www.realpars.com/)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R007 · [SolisPLC free plan](https://www.solisplc.com/join)

**Best fit:** Foundation  
**Access:** 🟡 Free, with conditions. Free account; limited basic courses/projects; no credit card advertised as required  
**Cost:** $0

An always-free plan supplies limited access to basic automation courses and projects. The broader PLC and robotics course libraries require paid plans.

**Use it for:** Sample introductory PLC instruction before buying hardware or a training subscription.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R008 · [CODESYS Development System](https://www.codesys.com/products/engineering/development-system/)

**Best fit:** Foundation → Practitioner  
**Access:** 🟡 Free, with conditions. IDE free; store registration may be required; target runtimes and add-ons can require licenses  
**Cost:** $0

A freely downloadable IEC 61131-3 development environment for creating industrial control programs. It gives learners exposure to a real automation engineering tool.

**Use it for:** Practice PLC programming and explore project structure and control logic.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

</details>

### Security learning and reference

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R009 | [CISA introductory ICS online modules](https://ics-training.inl.gov/) ⭐ | Foundation | 🟡 Free, with conditions |
| R010 | [CISA ICS300 — Advanced Cybersecurity for ICS](https://ics-training.inl.gov/) | Practitioner | 🟡 Free, with conditions |
| R011 | [CISA ICS401 — Industrial Control Systems Evaluation](https://ics-training.inl.gov/) | Practitioner → Specialist | 🟡 Free, with conditions |
| R012 | [CISA FRE2115 — ICS Cybersecurity Landscape for Managers](https://ics-training.inl.gov/) | Program lead | 🟡 Free, with conditions |
| R013 | [CISA/INL in-person ICS301 and ICS311](https://www.cisa.gov/ics-training-calendar) | Practitioner → Specialist | 🟡 Free, with conditions |
| R014 | [SANS ICS Cybersecurity Field Manuals](https://www.sans.org/mlp/ics-field-manual) ⭐ | Foundation → Practitioner | 🟡 Free, with conditions |
| R015 | [The Five ICS Cybersecurity Critical Controls — SANS](https://www.sans.org/white-papers/five-ics-cybersecurity-critical-controls) ⭐ | Practitioner / Program lead | 🟡 Free, with conditions |
| R016 | [SANS Industrial NSM and Incident Response Cheat Sheet](https://www.sans.org/posters/industrial-network-security-monitoring-incident-response-cheat-sheet) | Practitioner | 🟡 Free, with conditions |
| R017 | [ISA/IEC 62443 Quick Start Guide and series overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) ⭐ | Foundation → Program lead | 🟢 Free |
| R018 | [S4 conference session recordings](https://s4xevents.com/s4x23/) | Practitioner → Specialist | 🟢 Free |
| R074 | [SANS Introduction to ICS Security series](https://www.sans.org/blog/introduction-to-ics-security) ⭐ | Foundation | 🟢 Free |
| R075 | [SANS ICS Site Visit Plan](https://www.sans.org/blog/sans-ics-site-visit-plan) ⭐ | Foundation → Practitioner / Program lead | 🟢 Free |
| R078 | [The Differences Between ICS/OT and IT Security — SANS poster](https://www.sans.org/posters/the-differences-between-ics-ot-and-it-security) ⭐ | Foundation / Program lead | 🟡 Free, with conditions |
| R079 | [Control Systems Are a Target — SANS poster](https://www.sans.org/posters/control-systems-are-a-target) | Foundation → Practitioner | 🟡 Free, with conditions |
| R093 | [Mike Holcomb — free OT/ICS cybersecurity course content, e-books and infographics](https://www.mikeholcomb.com/) | Foundation → Practitioner | 🟢 Free |
| R094 | [Unsolicited Response podcast — Dale Peterson](https://dale-peterson.com/podcast-2/) | Practitioner → Program lead | 🟢 Free |
| R095 | [ICS Village](https://www.icsvillage.com/) | Foundation → Practitioner | 🟡 Free, with conditions |
| R103 | [Awesome Industrial Control System Security — community list](https://github.com/hslatman/awesome-industrial-control-system-security) | Practitioner → Specialist | 🟢 Free |

<details>
<summary>Details for the 18 resources above</summary>

#### R009 · [CISA introductory ICS online modules](https://ics-training.inl.gov/) — ⭐ Recommended starting point

**Best fit:** Foundation  
**Access:** 🟡 Free, with conditions. No tuition; registration and critical-infrastructure audience/eligibility conditions apply  
**Cost:** $0

The CISA catalog lists OPSEC and 210W modules covering ICS components, IT/OT differences, risk, threats, vulnerabilities, impacts, and defense in depth.

**Use it for:** Use the introductory modules as a structured bridge from IT security to OT.

**Supporting publisher source:** [Open link](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/41d85e1)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R010 · [CISA ICS300 — Advanced Cybersecurity for ICS](https://ics-training.inl.gov/)

**Best fit:** Practitioner  
**Access:** 🟡 Free, with conditions. No tuition; portal account and eligibility conditions apply  
**Cost:** $0

An on-demand online course focused on skills for protecting ICS and OT networks. CISA lists it as a prerequisite for the in-person ICS301 course.

**Use it for:** Build technical readiness for more involved ICS security exercises.

**Supporting publisher source:** [Open link](https://www.cisa.gov/ics-training-calendar)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R011 · [CISA ICS401 — Industrial Control Systems Evaluation](https://ics-training.inl.gov/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟡 Free, with conditions. No tuition for online course; portal registration/eligibility; in-person format separate  
**Cost:** $0

CISA offers industrial control system evaluation training online and in person. The online catalog entry is an option for learning assessment-oriented ICS security.

**Use it for:** Develop assessment vocabulary and a structured approach to evaluating industrial environments.

**Supporting publisher source:** [Open link](https://www.cisa.gov/ics-training-calendar)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R012 · [CISA FRE2115 — ICS Cybersecurity Landscape for Managers](https://ics-training.inl.gov/)

**Best fit:** Program lead  
**Access:** 🟡 Free, with conditions. No tuition; portal registration and eligibility conditions apply  
**Cost:** $0

An on-demand offering aimed at managers in the industrial cybersecurity landscape rather than solely hands-on technical operators.

**Use it for:** Give managers and program stakeholders an entry point into ICS cybersecurity.

**Supporting publisher source:** [Open link](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/41d85e1)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R013 · [CISA/INL in-person ICS301 and ICS311](https://www.cisa.gov/ics-training-calendar)

**Best fit:** Practitioner → Specialist  
**Access:** 🟡 Free, with conditions. No tuition; prerequisites, approval, dates, and seats apply; travel/lodging are extra  
**Cost:** $0

Instructor-led ICS301 includes a red/blue exercise; ICS311 focuses on detecting an attacker. These offer hands-on experience beyond self-paced reading.

**Use it for:** Practice technical defense and investigation in an industrial training environment.

**Supporting publisher source:** [Open link](https://inl.gov/national-security/ics-cybersecurity-training)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R014 · [SANS ICS Cybersecurity Field Manuals](https://www.sans.org/mlp/ics-field-manual) — ⭐ Recommended starting point

**Best fit:** Foundation → Practitioner  
**Access:** 🟡 Free, with conditions. Free resource; download form or account may be required  
**Cost:** $0

Volumes 1–3 introduce and organize ICS security concepts in a compact practitioner reference format.

**Use it for:** Use as a glossary and desk reference while learning architecture and defensive practice.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R015 · [The Five ICS Cybersecurity Critical Controls — SANS](https://www.sans.org/white-papers/five-ics-cybersecurity-critical-controls) — ⭐ Recommended starting point

**Best fit:** Practitioner / Program lead  
**Access:** 🟡 Free, with conditions. Free paper; download form or login may apply  
**Cost:** $0

A strategy paper explains five ICS priorities: incident response, defensible architecture, visibility, secure remote access, and risk-based vulnerability management.

**Use it for:** Turn a broad OT program into a short set of defensible priorities.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R016 · [SANS Industrial NSM and Incident Response Cheat Sheet](https://www.sans.org/posters/industrial-network-security-monitoring-incident-response-cheat-sheet)

**Best fit:** Practitioner  
**Access:** 🟡 Free, with conditions. Free poster/PDF; download form or account may apply  
**Cost:** $0

A compact reference provides guidance for network security monitoring and incident response in control system environments.

**Use it for:** Keep an OT-oriented monitoring and response reference alongside incident procedures.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R017 · [ISA/IEC 62443 Quick Start Guide and series overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) — ⭐ Recommended starting point

**Best fit:** Foundation → Program lead  
**Access:** 🟢 Free. Overview/guide free; normative standards are separate licensed documents  
**Cost:** $0

ISA's overview and linked Quick Start Guide explain the organization and purpose of the 62443 series and how to navigate its documents.

**Use it for:** Understand which parts concern asset owners, service providers, systems, and products.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R018 · [S4 conference session recordings](https://s4xevents.com/s4x23/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Published recordings free; attending the conference is paid  
**Cost:** $0

Public recordings of industry talks cover industrial security research, operational problems, architecture, and program decisions. The event page links the S4 Events video channel.

**Use it for:** Learn from technical presentations and compare practitioners' approaches to difficult OT problems.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R074 · [SANS Introduction to ICS Security series](https://www.sans.org/blog/introduction-to-ics-security) — ⭐ Recommended starting point

**Best fit:** Foundation  
**Access:** 🟢 Free. Public articles free; paid course promotions are separate  
**Cost:** $0

A free article series introduces industrial systems and the distinctive challenges of securing them. Later installments cover remote-access connections and protective practices.

**Use it for:** Give people entering OT a short reading route before longer standards and technical books.

**Related official source/project:** [Open link](https://www.sans.org/blog/introduction-to-ics-security-part-3)

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 84 (printed page(s) 80).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R075 · [SANS ICS Site Visit Plan](https://www.sans.org/blog/sans-ics-site-visit-plan) — ⭐ Recommended starting point

**Best fit:** Foundation → Practitioner / Program lead  
**Access:** 🟢 Free. Public guide free; field activities require site permissions and safety procedures  
**Cost:** $0

A practical guide covers visit preparation, coordination with safety and engineering, plant-floor discussions, asset inventory fields, and passive traffic analysis.

**Use it for:** Prepare a useful site-assessment checklist and gather operational context, especially when visiting unfamiliar plants.

**Publication status:** 2021 article; use current site procedures

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 61, 84 (printed page(s) 57, 80).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R078 · [The Differences Between ICS/OT and IT Security — SANS poster](https://www.sans.org/posters/the-differences-between-ics-ot-and-it-security) — ⭐ Recommended starting point

**Best fit:** Foundation / Program lead  
**Access:** 🟡 Free, with conditions. Free downloadable poster; account/download requirements may apply  
**Cost:** $0

A visual comparison explains differences in mission, operational context, priorities, and risk between traditional IT and industrial security.

**Use it for:** Brief IT staff and leadership on why security decisions need operational and engineering context.

**Publication status:** Publisher landing page currently dated May 2025; manual referenced an earlier version

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 84 (printed page(s) 80).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R079 · [Control Systems Are a Target — SANS poster](https://www.sans.org/posters/control-systems-are-a-target)

**Best fit:** Foundation → Practitioner  
**Access:** 🟡 Free, with conditions. Free downloadable poster; account/download requirements may apply  
**Cost:** $0

An awareness poster illustrates access paths into ICS and layered defenses using the Purdue model.

**Use it for:** Support plant-floor awareness conversations and explain why engineering assets attract attackers.

**Publication status:** Publisher landing page currently dated May 2025; manual referenced an earlier version

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 12, 80 (printed page(s) 8, 76).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R093 · [Mike Holcomb — free OT/ICS cybersecurity course content, e-books and infographics](https://www.mikeholcomb.com/)

**Best fit:** Foundation → Practitioner  
**Access:** 🟢 Free. Free videos, e-books and infographics (no account stated for these); an optional newsletter is offered; paid classes, trainings and consulting are separate; TryHackMe rooms are listed but their cost was not stated  
**Cost:** $0

An independent OT/ICS security consultant and educator's site lists free e-books on getting started in OT/ICS cybersecurity, more than 30 infographics, and over 50 YouTube videos, including more than 40 hours of free course content in its Getting Started in ICS/OT Cyber Security playlists.

**Use it for:** Follow a structured, video-based self-study path that connects IT security skills to industrial systems.

**Review date:** 2026-10-13

**Verification:** Site fetched on October 13, 2026; the free-content claims are the site's own description; videos and e-books not opened or evaluated; prices for paid classes not shown

#### R094 · [Unsolicited Response podcast — Dale Peterson](https://dale-peterson.com/podcast-2/)

**Best fit:** Practitioner → Program lead  
**Access:** 🟢 Free. Audio episodes through the website, an RSS feed and common podcast apps; podcast directories list it as free to listen; sponsor and vendor perspectives apply  
**Cost:** $0

An interview podcast on OT and ICS security hosted by Dale Peterson, mixing his opening commentary, guest conversations and listener questions.

**Use it for:** Hear practitioners and vendors discuss industry problems, then follow up on topics relevant to your own program.

**Publication status:** Directory listings show episodes through 2025; check the feed for current activity

**Review date:** 2026-10-13

**Verification:** Podcast page fetched on October 13, 2026; free-to-listen status and activity dates come from podcast-directory listings; no episodes were listened to

#### R095 · [ICS Village](https://www.icsvillage.com/)

**Best fit:** Foundation → Practitioner  
**Access:** 🟡 Free, with conditions. Online resources described as free to access; registration, fees and capacity for in-person trainings and events were not stated; hardware for the trainer kit is extra  
**Cost:** $0

A non-profit that builds hands-on awareness and training for industrial security. Its site lists free online resources, including open courseware, capture-the-flag challenges, an OT trainer-kit build guide and plant-level case studies, alongside a podcast and in-person demonstrations at conferences.

**Use it for:** Use the challenges and trainer-kit guide for hands-on practice, and the case studies to explain plant-level risk to others.

**Review date:** 2026-10-13

**Verification:** Site fetched on October 13, 2026; the descriptions are the site's own; courseware, challenges and the build guide not opened or evaluated

#### R103 · [Awesome Industrial Control System Security — community list](https://github.com/hslatman/awesome-industrial-control-system-security)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free public GitHub list (Apache-2.0); the items link to third-party material with its own terms  
**Cost:** $0

A community-curated list of industrial control system security resources, with sections for tools, honeypots, data, feeds and news, conferences, literature and education.

**Use it for:** Discover tools and papers beyond this catalog, treating it as a lead generator: check each item's source, license and age before relying on it.

**Publication status:** Community list; completeness and currency of individual links not verified

**Review date:** 2026-10-13

**Verification:** Official repository page fetched on October 13, 2026; the page did not show a date for the latest change, so currency of individual links was not verified

</details>

### Frameworks and architecture

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R019 | [NIST SP 800-82 Revision 3 — Guide to OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) ⭐ | Foundation → Specialist | 🟢 Free |
| R020 | [NIST SP 800-82 Revision 4 — initial public draft](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd) | Practitioner / Program lead | 🟢 Free |
| R021 | [NIST Cybersecurity Framework 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) | Foundation → Program lead | 🟢 Free |
| R022 | [NIST Manufacturing Cybersecurity Profiles](https://csrc.nist.gov/pubs/ir/8183/r2/ipd) | Practitioner / Program lead | 🟢 Free |
| R023 | [CIS Controls v8.1 Industrial Control Systems Guide](https://www.cisecurity.org/insights/white-papers/cis-critical-security-controls-v8-1-industrial-control-systems-ics-guide) | Practitioner / Program lead | 🟡 Free, with conditions |
| R024 | [CISA Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cybersecurity-performance-goals) | Foundation → Program lead | 🟢 Free |
| R025 | [DOE Cybersecurity Capability Maturity Model — C2M2](https://www.energy.gov/ceser/cybersecurity-capability-maturity-model-c2m2) | Practitioner / Program lead | 🟢 Free |
| R026 | [Principles of Operational Technology Cyber Security — ASD and partners](https://www.cyber.gov.au/publication/principles-of-operational-technology-cyber-security) ⭐ | Foundation → Program lead | 🟢 Free |
| R027 | [Secure Connectivity Principles for OT — ASD and partners](https://www.cyber.gov.au/publication/secure-connectivity-principles-for-operational-technology) | Practitioner / Architect | 🟢 Free |
| R028 | [Foundations for OT Cybersecurity: Asset Inventory — joint guidance](https://www.cisa.gov/sites/default/files/2025-08/joint-guide-foundations-for-OT-cybersecurity-asset-inventory-guidance_508c.pdf) ⭐ | Foundation → Practitioner | 🟢 Free |
| R029 | [NCSC: Creating and Maintaining a Definitive View of OT Architecture](https://www.ncsc.gov.uk/collection/operational-technology/definitive-architecture-view) | Practitioner / Architect | 🟢 Free |
| R030 | [NCSC: Using Privileged Access Workstations in OT](https://www.ncsc.gov.uk/collection/operational-technology/using-paws-in-ot-environments) | Practitioner / Architect | 🟢 Free |
| R031 | [CISA Cybersecurity Evaluation Tool — CSET](https://github.com/cisagov/cset) | Practitioner / Program lead | 🟢 Free |
| R076 | [The Sliding Scale of Cyber Security — Robert M. Lee](https://www.sans.org/white-papers/36240) | Practitioner / Program lead | 🟡 Free, with conditions |
| R102 | [Primary Mitigations to Reduce Cyber Threats to Operational Technology — CISA, FBI, EPA and DOE](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology) | Foundation → Program lead | 🟢 Free |

<details>
<summary>Details for the 15 resources above</summary>

#### R019 · [NIST SP 800-82 Revision 3 — Guide to OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — ⭐ Recommended starting point

**Best fit:** Foundation → Specialist  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

The final OT security guide explains OT characteristics, architectures, threats, and safeguards, with attention to performance, reliability, and safety constraints.

**Use it for:** Use as the central reference for architecture reviews, control selection, and program documentation.

**Publication status:** Final, September 2023

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R020 · [NIST SP 800-82 Revision 4 — initial public draft](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd)

**Best fit:** Practitioner / Program lead  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

The September 2026 draft expands sector coverage and restructures the guide around CSF 2.0, including governance.

**Use it for:** Track proposed changes and prepare informed feedback; keep final guidance clearly distinguished.

**Publication status:** Initial public draft, September 21, 2026; comments due November 30, 2026

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R021 · [NIST Cybersecurity Framework 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)

**Best fit:** Foundation → Program lead  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

A cross-sector framework organizes cybersecurity outcomes around Govern, Identify, Protect, Detect, Respond, and Recover.

**Use it for:** Describe target outcomes, communicate with leadership, and structure a program roadmap.

**Publication status:** Final

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R022 · [NIST Manufacturing Cybersecurity Profiles](https://csrc.nist.gov/pubs/ir/8183/r2/ipd)

**Best fit:** Practitioner / Program lead  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

The CSF 2.0 manufacturing profile adapts cybersecurity outcomes to manufacturing environments. Revision 2's landing page identifies the publication as an initial public draft.

**Use it for:** Connect enterprise cybersecurity outcomes with manufacturing operations and risks.

**Publication status:** Rev. 2 initial public draft, September 2025; comment period closed

**Related official source/project:** [Open link](https://www.nist.gov/publications/cybersecurity-framework-version-11-manufacturing-profile)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R023 · [CIS Controls v8.1 Industrial Control Systems Guide](https://www.cisecurity.org/insights/white-papers/cis-critical-security-controls-v8-1-industrial-control-systems-ics-guide)

**Best fit:** Practitioner / Program lead  
**Access:** 🟡 Free, with conditions. Free guide; download form may apply  
**Cost:** $0

An ICS-specific guide applies CIS Controls to industrial environments instead of assuming ordinary enterprise IT implementation.

**Use it for:** Translate familiar safeguards into an OT-specific improvement plan.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R024 · [CISA Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cybersecurity-performance-goals)

**Best fit:** Foundation → Program lead  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

A prioritized baseline of cybersecurity practices helps critical infrastructure organizations focus on actions with risk-reduction value. Covers both IT and OT.

**Use it for:** Build a practical initial backlog for organizations with limited staff and budget.

**Review date:** 2026-10-12

**Verification:** Publisher search-index evidence reviewed; direct CISA page retrieval blocked with HTTP 403; use current landing-page version

#### R025 · [DOE Cybersecurity Capability Maturity Model — C2M2](https://www.energy.gov/ceser/cybersecurity-capability-maturity-model-c2m2)

**Best fit:** Practitioner / Program lead  
**Access:** 🟢 Free. Public model/resources free; some evaluation resources may require a request  
**Cost:** $0

A maturity model and self-evaluation resources help organizations assess IT/OT cybersecurity capabilities and prioritize investments. Although developed in energy, other industries can use it.

**Use it for:** Run a maturity workshop and identify specific program gaps.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R026 · [Principles of Operational Technology Cyber Security — ASD and partners](https://www.cyber.gov.au/publication/principles-of-operational-technology-cyber-security) — ⭐ Recommended starting point

**Best fit:** Foundation → Program lead  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

Joint international guidance presents six principles for decisions affecting a safe, secure OT environment.

**Use it for:** Use as common ground for security, engineering, operations, and leadership.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R027 · [Secure Connectivity Principles for OT — ASD and partners](https://www.cyber.gov.au/publication/secure-connectivity-principles-for-operational-technology)

**Best fit:** Practitioner / Architect  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

Joint guidance addresses the security of connections into and within industrial environments.

**Use it for:** Review external access, connectivity decisions, and boundary protections against a consistent reference.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R028 · [Foundations for OT Cybersecurity: Asset Inventory — joint guidance](https://www.cisa.gov/sites/default/files/2025-08/joint-guide-foundations-for-OT-cybersecurity-asset-inventory-guidance_508c.pdf) — ⭐ Recommended starting point

**Best fit:** Foundation → Practitioner  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

A guide explains a systematic approach to OT asset inventories and supplemental taxonomies, including recommended inventory fields.

**Use it for:** Create a useful inventory schema tied to function, criticality, and security activities.

**Supporting publisher source:** [Open link](https://media.defense.gov/2025/Aug/13/2003779777/-1/-1/0/JOINT-GUIDE-FOUNDATIONS-FOR-OT-CYBERSECURITY-ASSET-INVENTORY-GUIDANCE.PDF)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R029 · [NCSC: Creating and Maintaining a Definitive View of OT Architecture](https://www.ncsc.gov.uk/collection/operational-technology/definitive-architecture-view)

**Best fit:** Practitioner / Architect  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

Guidance helps organizations establish and maintain an accurate view of industrial architecture for both existing and new environments.

**Use it for:** Improve network diagrams and the relationship between documented architecture and operational reality.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R030 · [NCSC: Using Privileged Access Workstations in OT](https://www.ncsc.gov.uk/collection/operational-technology/using-paws-in-ot-environments)

**Best fit:** Practitioner / Architect  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

OT-focused guidance addresses using privileged access workstations for high-risk administrative access.

**Use it for:** Develop secure engineering and administration workflows.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R031 · [CISA Cybersecurity Evaluation Tool — CSET](https://github.com/cisagov/cset)

**Best fit:** Practitioner / Program lead  
**Access:** 🟢 Free. Software free; deployment and local computing resources required  
**Cost:** $0

A freely available evaluation tool supports systematic cybersecurity assessments. The official repository provides releases, documentation, and issue tracking.

**Use it for:** Organize assessment questions and record improvement priorities.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R076 · [The Sliding Scale of Cyber Security — Robert M. Lee](https://www.sans.org/white-papers/36240)

**Best fit:** Practitioner / Program lead  
**Access:** 🟡 Free, with conditions. Free whitepaper; download/account requirements may apply  
**Cost:** $0

A conceptual model distinguishes architecture, passive defense, active defense, intelligence, and offense. It supports discussion of how security actions and investments build on one another.

**Use it for:** Explain why architecture and visibility should underpin later hunting and intelligence investments.

**Publication status:** 2015 foundational paper; conceptual model, not a compliance standard

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 31, 54, 82 (printed page(s) 27, 50, 78).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R102 · [Primary Mitigations to Reduce Cyber Threats to Operational Technology — CISA, FBI, EPA and DOE](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology)

**Best fit:** Foundation → Program lead  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

A joint fact sheet urging operators to take OT systems off the public internet, replace default passwords, tighten remote access, separate IT and OT networks, and keep the ability to operate manually.

**Use it for:** Use it as a short, prioritized checklist for a first review of exposed or weakly protected OT.

**Publication status:** Published May 6, 2025

**Review date:** 2026-10-13

**Verification:** CISA page fetched on October 13, 2026; the linked PDF was not opened

</details>

### Engineering and sector guidance

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R032 | [DOE Cyber-Informed Engineering and Implementation Guide](https://www.energy.gov/ceser/cyber-informed-engineering) | Practitioner → Specialist | 🟢 Free |
| R033 | [INL Cyber-Informed Engineering Resource Library](https://inl.gov/national-security/cie/resource-library/) | Practitioner → Specialist | 🟢 Free |
| R034 | [INL Consequence-driven Cyber-informed Engineering — CCE](https://inl.gov/national-security/cce/) | Practitioner → Specialist | 🟢 Free |
| R035 | [NERC CIP Reliability Standards](https://www.nerc.com/standards/reliability-standards/cip) | Practitioner / Sector specialist | 🟢 Free |
| R036 | [WaterISAC 12 Cybersecurity Fundamentals and Small Systems Compendium](https://www.waterisac.org/fundamentals) | Foundation → Program lead | 🟢 Free |
| R037 | [EPA Water Cybersecurity Assessments and Templates](https://www.epa.gov/cyberwater/cybersecurity-assessments) | Foundation → Practitioner | 🟢 Free |
| R096 | [NIST SP 1800-10 — Protecting information and system integrity in ICS environments (manufacturing)](https://csrc.nist.gov/pubs/sp/1800/10/final) | Practitioner / Architect | 🟢 Free |

<details>
<summary>Details for the 7 resources above</summary>

#### R032 · [DOE Cyber-Informed Engineering and Implementation Guide](https://www.energy.gov/ceser/cyber-informed-engineering)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

CIE incorporates cyber considerations into physical-system design and operations. The linked implementation guide supplies questions engineering teams can consider throughout the lifecycle.

**Use it for:** Translate cyber threats into engineering decisions that reduce physical consequences.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R033 · [INL Cyber-Informed Engineering Resource Library](https://inl.gov/national-security/cie/resource-library/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

A collection of technical materials, practical guidance, case studies, and lessons supports applying CIE principles.

**Use it for:** Find deeper engineering examples after studying the CIE implementation guide.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R034 · [INL Consequence-driven Cyber-informed Engineering — CCE](https://inl.gov/national-security/cce/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Public reference materials free; training dates/eligibility and engagement access are separate  
**Cost:** $0

Public methodology materials introduce a consequence-focused approach to protecting critical infrastructure, alongside information about training and engagements.

**Use it for:** Identify critical functions and study engineering approaches to reducing high-consequence cyber risk.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R035 · [NERC CIP Reliability Standards](https://www.nerc.com/standards/reliability-standards/cip)

**Best fit:** Practitioner / Sector specialist  
**Access:** 🟢 Free. Public standards free to read; applicability is sector/jurisdiction-specific  
**Cost:** $0

Official standards pages provide CIP documents and distinguish enforced versions from those scheduled for future enforcement.

**Use it for:** Study electricity-sector security requirements and use the correct standard/version.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R036 · [WaterISAC 12 Cybersecurity Fundamentals and Small Systems Compendium](https://www.waterisac.org/fundamentals)

**Best fit:** Foundation → Program lead  
**Access:** 🟢 Free. These public PDFs free; WaterISAC membership and restricted intelligence are separate  
**Cost:** $0

Public TLP:CLEAR guides summarize cybersecurity practices for water and wastewater utilities, with a dedicated small-systems compendium. The updated collection uses 12 fundamentals.

**Use it for:** Build a practical water-sector improvement plan suited to resource-constrained operators.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R037 · [EPA Water Cybersecurity Assessments and Templates](https://www.epa.gov/cyberwater/cybersecurity-assessments)

**Best fit:** Foundation → Practitioner  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

EPA provides cybersecurity guidance, a self-assessment tool, risk-mitigation templates, and checklist fact sheets for water systems; some resources also have Spanish versions.

**Use it for:** Conduct an accessible water-system assessment and document corrective actions.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R096 · [NIST SP 1800-10 — Protecting information and system integrity in ICS environments (manufacturing)](https://csrc.nist.gov/pubs/sp/1800/10/final)

**Best fit:** Practitioner / Architect  
**Access:** 🟢 Free. NIST publication with a PDF download link; no account indicated; the products named are examples and may differ from what you run  
**Cost:** $0

A NIST National Cybersecurity Center of Excellence practice guide showing how commercially available, standards-based products can provide behavioral anomaly detection, application allowlisting and file-integrity checking in manufacturing control system environments.

**Use it for:** Use it as a worked reference architecture when planning detection and integrity controls for a manufacturing OT network.

**Publication status:** Final, March 2022; products and versions in the guide reflect that date

**Review date:** 2026-10-13

**Verification:** NIST publication page fetched on October 13, 2026; date and download link observed; the PDF was not opened

</details>

### Industrial protocol references

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R038 | [Modbus Specifications and Implementation Guides](https://www.modbus.org/modbus-specifications) ⭐ | Practitioner → Specialist | 🟢 Free |
| R039 | [OPC UA Online Reference](https://reference.opcfoundation.org/) | Practitioner → Specialist | 🟢 Free |
| R040 | [OASIS MQTT 5.0 Specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) | Practitioner → Specialist | 🟢 Free |
| R041 | [PROFINET Technology and Application — PI North America](https://us.profinet.com/document/system-description-profinet-technology-and-application/) | Foundation → Practitioner | 🟢 Free |
| R042 | [ODVA EtherNet/IP Technology Overview](https://www.odva.org/wp-content/uploads/2024/04/PUB00138R8_Ethernet.pdf) | Foundation → Practitioner | 🟢 Free |

<details>
<summary>Details for the 5 resources above</summary>

#### R038 · [Modbus Specifications and Implementation Guides](https://www.modbus.org/modbus-specifications) — ⭐ Recommended starting point

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Public references; download/use subject to publisher terms  
**Cost:** $0

Official protocol and implementation references provide the authoritative detail behind Modbus communication and message behavior.

**Use it for:** Decode function codes, addressing, requests, and responses accurately.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R039 · [OPC UA Online Reference](https://reference.opcfoundation.org/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

A searchable, hyperlinked reference supplies OPC UA core specifications and companion information models.

**Use it for:** Understand services, information models, security concepts, and industry-specific data structures.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R040 · [OASIS MQTT 5.0 Specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

The public MQTT standard defines publish/subscribe behavior, packet formats, and protocol features used in IoT and industrial integrations.

**Use it for:** Study broker/client behavior, QoS, sessions, and protocol semantics.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R041 · [PROFINET Technology and Application — PI North America](https://us.profinet.com/document/system-description-profinet-technology-and-application/)

**Best fit:** Foundation → Practitioner  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

A technology/system description introduces PROFINET and its place in distributed industrial automation.

**Use it for:** Understand PROFINET networks before investigating or segmenting them.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R042 · [ODVA EtherNet/IP Technology Overview](https://www.odva.org/wp-content/uploads/2024/04/PUB00138R8_Ethernet.pdf)

**Best fit:** Foundation → Practitioner  
**Access:** 🟢 Free. Overview free; full specifications and some developer resources have separate access terms  
**Cost:** $0

ODVA's public overview describes EtherNet/IP and the use of CIP in Ethernet-based industrial communication.

**Use it for:** Build a working conceptual model of EtherNet/IP and its role in automation.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

</details>

### Labs and protocol tooling

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R043 | [OpenPLC Editor and Simulator](https://autonomylogic.com/products/openplc) ⭐ | Foundation → Practitioner | 🟢 Free |
| R044 | [Scada-LTS](https://github.com/SCADA-LTS/Scada-LTS) | Practitioner | 🟢 Free |
| R045 | [Node-RED](https://nodered.org/about/) | Foundation → Practitioner | 🟢 Free |
| R046 | [PyModbus](https://github.com/pymodbus-dev/pymodbus) | Practitioner | 🟢 Free |
| R047 | [open62541 and its documentation](https://open62541.org/doc/master/toc.html) | Practitioner → Specialist | 🟢 Free |
| R048 | [libIEC61850 documentation and examples](https://libiec61850.com/documentation/) | Specialist | 🟢 Free |
| R049 | [ControlThings tools](https://www.controlthings.io/tools) | Practitioner → Specialist | 🟢 Free |
| R050 | [MITRE Caldera for OT](https://github.com/mitre/caldera-ot) | Specialist | 🟢 Free |
| R051 | [Conpot ICS/SCADA honeypot](https://github.com/mushorg/conpot) | Practitioner → Specialist | 🟢 Free |
| R052 | [Labshock limited free tier](https://labshocksecurity.com/pricing/) | Foundation → Practitioner | 🟡 Free, with conditions |
| R082 | [Tcpreplay](https://tcpreplay.appneta.com/) | Practitioner → Specialist | 🟢 Free |
| R091 | [Snap7 — open-source S7 communication library](https://snap7.sourceforge.net/) | Practitioner → Specialist | 🟡 Free, with conditions |
| R092 | [GRFICS — Graphical Realism Framework for Industrial Control Simulations](https://github.com/djformby/GRFICS) | Practitioner | 🟡 Free, with conditions |
| R104 | [ICS-Security-Tools — community collection (ITI)](https://github.com/ITI/ICS-Security-Tools) | Practitioner → Specialist | 🟡 Free, with conditions |

<details>
<summary>Details for the 14 resources above</summary>

#### R043 · [OpenPLC Editor and Simulator](https://autonomylogic.com/products/openplc) — ⭐ Recommended starting point

**Best fit:** Foundation → Practitioner  
**Access:** 🟢 Free. Free editor/simulator; other hosted services and hardware are separate  
**Cost:** $0

Free open-source PLC tooling supports IEC 61131-3 programming and includes a simulator for running and debugging logic without hardware.

**Use it for:** Practice control programming before assembling a networked PLC/SCADA lab.

**Related official source/project:** [Open link](https://github.com/Autonomy-Logic/openplc-editor)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R044 · [Scada-LTS](https://github.com/SCADA-LTS/Scada-LTS)

**Best fit:** Practitioner  
**Access:** 🟢 Free. Open-source software; local host and setup effort required  
**Cost:** $0

An open-source, web-based, multi-platform SCADA project provides code and setup documentation.

**Use it for:** Build an HMI/data-acquisition lab and observe interactions with simulated field systems.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R045 · [Node-RED](https://nodered.org/about/)

**Best fit:** Foundation → Practitioner  
**Access:** 🟢 Free. Open-source core; review third-party node licenses, quality, and dependencies  
**Cost:** $0

A flow-based, browser-edited programming tool connects data sources and services. Its extensible node ecosystem is useful for building industrial lab integrations.

**Use it for:** Create lab data flows and connect simulated processes to dashboards or protocol clients.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R046 · [PyModbus](https://github.com/pymodbus-dev/pymodbus)

**Best fit:** Practitioner  
**Access:** 🟢 Free. Open-source library; Python skills and local lab required  
**Cost:** $0

A Python Modbus implementation offers clients, servers, and simulation with synchronous and asynchronous APIs.

**Use it for:** Generate controlled Modbus traffic and create repeatable protocol exercises.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R047 · [open62541 and its documentation](https://open62541.org/doc/master/toc.html)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Open-source software/docs; C/C++ build skills useful; master documentation may describe unreleased behavior  
**Cost:** $0

An OPC UA implementation and detailed documentation explain services, information modeling, and client/server construction.

**Use it for:** Build OPC UA lab endpoints and examine certificate/security behavior.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R048 · [libIEC61850 documentation and examples](https://libiec61850.com/documentation/)

**Best fit:** Specialist  
**Access:** 🟢 Free. Documentation free; open-source library and commercial licensing options have distinct terms  
**Cost:** $0

Client/server tutorials and API documentation cover MMS and publisher/subscriber functions for GOOSE and sampled values.

**Use it for:** Create IEC 61850 learning exercises and inspect substation-related communications.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R049 · [ControlThings tools](https://www.controlthings.io/tools)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free tool collection; hardware adapters may be required for serial/embedded exercises  
**Cost:** $0

A collection of assessment tools interacts with Modbus, serial devices, embedded SPI/I2C components, and selected PLCs.

**Use it for:** Explore protocol/device behavior in an isolated assessment lab.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R050 · [MITRE Caldera for OT](https://github.com/mitre/caldera-ot)

**Best fit:** Specialist  
**Access:** 🟢 Free. Free plugins; substantial setup; use isolated authorized systems  
**Cost:** $0

Open-source plugins extend Caldera with industrial protocol capabilities mapped to ATT&CK for ICS.

**Use it for:** Emulate selected behaviors in a lab and evaluate telemetry/detections.

**Supporting publisher source:** [Open link](https://www.mitre.org/resources/caldera-ot)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R051 · [Conpot ICS/SCADA honeypot](https://github.com/mushorg/conpot)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Open-source software; host/deployment required; emulation is not a complete process testbed  
**Cost:** $0

An ICS/SCADA honeypot project provides emulated services for observing interactions and exploring deception concepts.

**Use it for:** Learn how industrial service exposure appears to scanners and how to analyze honeypot events.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R052 · [Labshock limited free tier](https://labshocksecurity.com/pricing/)

**Best fit:** Foundation → Practitioner  
**Access:** 🟡 Free, with conditions. $0 limited tier; time restrictions; local Docker host; personal-learning license scope  
**Cost:** $0

A local OT security lab platform offers real protocol and telemetry exercises. The free tier limits labs, guides, progression, and session access.

**Use it for:** Try a ready-made environment before paying for extended personal practice.

**Related official source/project:** [Open link](https://github.com/zakharb/labshock)

**Review date:** 2026-10-12

**Verification:** Pricing page and official repository reviewed; their wording/limits differ, so check current release and plan before deployment

#### R082 · [Tcpreplay](https://tcpreplay.appneta.com/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. GPLv3 tools free; replay onto isolated authorized lab interfaces, since traffic is actually transmitted  
**Cost:** $0

A free suite edits and replays previously captured network traffic with selectable timing/rates.

**Use it for:** Run repeatable tests of lab IDS signatures and traffic-analysis pipelines.

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 52 (printed page(s) 48).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R091 · [Snap7 — open-source S7 communication library](https://snap7.sourceforge.net/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟡 Free, with conditions. Free download from the project site; the license name was not shown on the pages retrieved, so confirm it before redistributing; check the project documentation for supported controllers and settings; use only on systems you own or are authorized to test  
**Cost:** $0

An open-source Ethernet communication suite with client, server and partner objects for talking to Siemens S7 controllers from your own code. It is multi-platform and usable from several languages, including C#, Pascal, LabVIEW and C++.

**Use it for:** Write small scripts that read from or serve S7 data in an isolated lab, and learn what S7 communication looks like on the wire.

**Review date:** 2026-10-13

**Verification:** Project site fetched on October 13, 2026 (a framed site; the main description and platform list were read); software not downloaded or run

#### R092 · [GRFICS — Graphical Realism Framework for Industrial Control Simulations](https://github.com/djformby/GRFICS)

**Best fit:** Practitioner  
**Access:** 🟡 Free, with conditions. Free open source (GPL-3.0; the 3D simulation is supplied only as a compiled executable); about 25 GB of disk, 8 GB of RAM and a quad-core CPU; uses older Ubuntu 16.04 images, and the author no longer hosts pre-built VMs, so setup is from scratch  
**Cost:** $0

A virtual ICS lab with a 3D chemical-process simulation, a soft PLC and an HMI, run as three virtual machines. It is built for practicing attacks such as command injection and man-in-the-middle, and defenses such as segmentation, firewall rules and intrusion-detection rules.

**Use it for:** Build a self-contained attack-and-defend exercise with visible physical consequences, entirely on a host-only network.

**Publication status:** Older project; its README points to a Version 2 in a separate repository. The PLC is intentionally vulnerable, so run it only on an isolated host-only network

**Review date:** 2026-10-13

**Verification:** Official repository page fetched on October 13, 2026; requirements, license and notices observed; no last-update date shown; not built or run

#### R104 · [ICS-Security-Tools — community collection (ITI)](https://github.com/ITI/ICS-Security-Tools)

**Best fit:** Practitioner → Specialist  
**Access:** 🟡 Free, with conditions. Free public repository (CC BY 4.0 for the collection); the tools and captures it points to keep their own licenses and provenance; no maintenance statement on the page  
**Cost:** $0

A community collection of tools, tips, packet captures, protocol notes, configurations, guides, feeds, hardware notes and scripts for exploring ICS security, described by its authors as developed as a community asset.

**Use it for:** Find practice captures and starter tooling for a lab, then follow each item back to its original source.

**Review date:** 2026-10-13

**Verification:** Official repository page fetched on October 13, 2026; contents not individually reviewed

</details>

### Monitoring and investigation

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R053 | [Wireshark and official documentation](https://www.wireshark.org/docs/) ⭐ | Foundation → Specialist | 🟢 Free |
| R054 | [Malcolm](https://github.com/cisagov/Malcolm) ⭐ | Practitioner | 🟢 Free |
| R055 | [Zeek and Book of Zeek](https://docs.zeek.org/en/current/) | Practitioner → Specialist | 🟢 Free |
| R056 | [Suricata User Guide](https://docs.suricata.io/en/latest/) | Practitioner → Specialist | 🟢 Free |
| R057 | [Security Onion](https://securityonionsolutions.com/software/) | Practitioner → Specialist | 🟢 Free |
| R080 | [NetworkMiner — free edition](https://www.netresec.com/?page=NetworkMiner) | Practitioner | 🟢 Free |
| R081 | [Snort engine and documentation](https://snort.org/) | Practitioner → Specialist | 🟢 Free |
| R083 | [TShark command-line reference](https://www.wireshark.org/docs/man-pages/tshark) | Practitioner → Specialist | 🟢 Free |
| R088 | [tcpdump](https://github.com/the-tcpdump-group/tcpdump) | Practitioner | 🟢 Free |
| R090 | [CISA ICSNPP — industrial protocol parsers for Zeek](https://github.com/cisagov/ICSNPP) | Practitioner → Specialist | 🟢 Free |

<details>
<summary>Details for the 10 resources above</summary>

#### R053 · [Wireshark and official documentation](https://www.wireshark.org/docs/) — ⭐ Recommended starting point

**Best fit:** Foundation → Specialist  
**Access:** 🟢 Free. Free software/docs; live capture requires an appropriate capture point  
**Cost:** $0

A free packet-analysis tool and user documentation support traffic capture, filtering, and protocol inspection.

**Use it for:** Analyze authorized industrial captures and learn what a controller actually exchanges.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R054 · [Malcolm](https://github.com/cisagov/Malcolm) — ⭐ Recommended starting point

**Best fit:** Practitioner  
**Access:** 🟢 Free. Open-source software; local CPU/RAM/storage required  
**Cost:** $0

A containerized traffic-analysis suite ingests PCAPs, Zeek logs, and Suricata alerts, combining dashboards and session analysis.

**Use it for:** Investigate industrial traffic offline or build passive visibility in a lab.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R055 · [Zeek and Book of Zeek](https://docs.zeek.org/en/current/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Open-source software/docs; protocol coverage depends on version/plugins  
**Cost:** $0

A network security monitoring framework and manual explain deployment, generated logs, scripting, and customization.

**Use it for:** Turn packet activity into structured metadata for baselining and detection.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R056 · [Suricata User Guide](https://docs.suricata.io/en/latest/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free software/docs; latest documentation can describe a development version  
**Cost:** $0

Documentation explains the IDS/IPS engine, rule development, protocol handling, and EVE event output.

**Use it for:** Develop and tune lab detections, then examine how alerts relate to industrial operations.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R057 · [Security Onion](https://securityonionsolutions.com/software/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free platform; significant hardware/storage may be needed; paid services/features separate  
**Cost:** $0

A free and open platform combines monitoring, hunting, packet/log analysis, and case management. Commercial appliances and support are separate offerings.

**Use it for:** Practice SOC workflows using captured or mirrored lab traffic.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R080 · [NetworkMiner — free edition](https://www.netresec.com/?page=NetworkMiner)

**Best fit:** Practitioner  
**Access:** 🟢 Free. Free open-source edition; feature limits compared with Professional; primarily Windows/.NET tooling  
**Cost:** $0

A passive network-forensics application identifies hosts and reconstructs supported artifacts from packet captures. The free open-source edition is distinct from NetworkMiner Professional.

**Use it for:** Examine hosts, sessions, and supported extracted files in authorized captures during an investigation.

**Supporting publisher source:** [Open link](https://www.netresec.com/?page=NetworkMinerSourceCode)

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 53 (printed page(s) 49).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R081 · [Snort engine and documentation](https://snort.org/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Engine free; Community rules available; registered/subscriber rule access differs; verify protocol support for your version  
**Cost:** $0

A free open-source detection engine evaluates traffic against rules and can operate as a sniffer, logger, or IDS/IPS.

**Use it for:** Build a lab IDS and compare alerts against known industrial protocol activity.

**Supporting publisher source:** [Open link](https://snort.org/faq/how-is-the-snort-software-licensed)

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 52 (printed page(s) 48).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R083 · [TShark command-line reference](https://www.wireshark.org/docs/man-pages/tshark)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free tool/docs; included in the Wireshark ecosystem; field names and capabilities depend on version  
**Cost:** $0

Wireshark's command-line analyzer uses its packet-dissection code for capture and offline analysis, enabling filtering and field extraction.

**Use it for:** Automate extraction of controller addresses, protocol fields, and communication patterns from PCAPs.

**Related official source/project:** [Open link](https://www.wireshark.org/docs/man-pages/)

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 45, 53 (printed page(s) 41, 49).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R088 · [tcpdump](https://github.com/the-tcpdump-group/tcpdump)

**Best fit:** Practitioner  
**Access:** 🟢 Free. Open-source software; live capture requires suitable privileges and an authorized TAP/SPAN/interface  
**Cost:** $0

A lightweight command-line packet-capture and network-dissection tool provides PCAPs for later analysis.

**Use it for:** Collect traffic from an approved capture point when a graphical workstation is impractical.

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 49 (printed page(s) 45).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R090 · [CISA ICSNPP — industrial protocol parsers for Zeek](https://github.com/cisagov/ICSNPP)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Open source (BSD-3-Clause); needs a working Zeek installation, build effort and your own packet captures  
**Cost:** $0

Open-source parsers that teach Zeek to read industrial protocols, including BACnet, EtherNet/IP and CIP, S7comm, OPC UA Binary and Synchrophasor (C37.118), turning captured traffic into structured logs.

**Use it for:** Add industrial protocol visibility to a Zeek lab or monitoring pipeline, then compare the logs with the packet captures they came from.

**Review date:** 2026-10-13

**Verification:** Official repository page fetched on October 13, 2026; protocol list and license observed; last-update date not shown on the page; parsers not built or run

</details>

### Packet captures and datasets

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R058 | [Wireshark SampleCaptures](https://wiki.wireshark.org/SampleCaptures) ⭐ | Foundation → Practitioner | 🟢 Free |
| R059 | [ICS-pcap collection](https://github.com/automayt/ICS-pcap) | Practitioner | 🟢 Free |

<details>
<summary>Details for the 2 resources above</summary>

#### R058 · [Wireshark SampleCaptures](https://wiki.wireshark.org/SampleCaptures) — ⭐ Recommended starting point

**Best fit:** Foundation → Practitioner  
**Access:** 🟢 Free. Public samples; licenses/provenance vary by capture; a download is not permission to redistribute  
**Cost:** $0

A public collection of protocol captures includes industrial examples such as DNP3, alongside many other protocols.

**Use it for:** Practice decoding messages without purchasing industrial hardware.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R059 · [ICS-pcap collection](https://github.com/automayt/ICS-pcap)

**Best fit:** Practitioner  
**Access:** 🟢 Free. Public collection; some downloads use Git LFS; verify each capture's provenance/license  
**Cost:** $0

A community-maintained collection indexes ICS/SCADA packet captures for protocol study.

**Use it for:** Find industrial examples for Wireshark and monitoring-tool exercises.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

</details>

### Threat intelligence and research

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R060 | [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) ⭐ | Practitioner → Specialist | 🟢 Free |
| R061 | [CISA ICS Advisories](https://www.cisa.gov/news-events/ics-advisories) | Practitioner | 🟢 Free |
| R062 | [Dragos public research and Year in Review](https://www.dragos.com/resources) | Practitioner / Program lead | 🟡 Free, with conditions |
| R063 | [Claroty Team82 research](https://www.claroty.com/team82/research) | Practitioner → Specialist | 🟡 Free, with conditions |
| R064 | [Nozomi Networks research reports](https://www.nozominetworks.com/research-reports) | Practitioner / Program lead | 🟡 Free, with conditions |
| R065 | [Kaspersky ICS CERT public research](https://ics-cert.kaspersky.com/) | Practitioner → Specialist | 🟢 Free |
| R066 | [Operational Technology Cybersecurity Coalition resources](https://www.otcybercoalition.org/resources) | Program lead / Policy | 🟢 Free |
| R077 | [The Industrial Control System Cyber Kill Chain — Assante and Lee](https://www.sans.org/white-papers/36297) ⭐ | Practitioner → Specialist | 🟡 Free, with conditions |
| R086 | [CRASHOVERRIDE analysis and lessons — Dragos](https://www.dragos.com/blog/ukraine-power-grid-cyberattack-crashoverride-10-year-lessons) | Practitioner → Specialist / Electric sector | 🟢 Free |
| R087 | [PIPEDREAM / CHERNOVITE public whitepaper — Dragos](https://hub.dragos.com/whitepaper/chernovite-pipedream) | Practitioner → Specialist | 🟡 Free, with conditions |
| R089 | [MITRE EMB3D threat model for embedded devices](https://emb3d.mitre.org/) | Practitioner → Specialist | 🟢 Free |

<details>
<summary>Details for the 11 resources above</summary>

#### R060 · [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) — ⭐ Recommended starting point

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

A public knowledge base describes observed adversary behaviors in industrial environments, with techniques and supporting references.

**Use it for:** Map incidents and detection coverage to specific behaviors rather than generic threat labels.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R061 · [CISA ICS Advisories](https://www.cisa.gov/news-events/ics-advisories)

**Best fit:** Practitioner  
**Access:** 🟢 Free. Free; no account required  
**Cost:** $0

Official advisories publish affected products, technical vulnerability details, and mitigation information for industrial systems.

**Use it for:** Check whether an advisory affects installed assets and track vendor remedies.

**Supporting publisher source:** [Open link](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/422d143)

**Review date:** 2026-10-12

**Verification:** Publisher bulletin reviewed; direct advisory index retrieval blocked with HTTP 403

#### R062 · [Dragos public research and Year in Review](https://www.dragos.com/resources)

**Best fit:** Practitioner / Program lead  
**Access:** 🟡 Free, with conditions. Public articles free; some reports require an email/form; paid intelligence/platform separate  
**Cost:** $0

Public reports, technical research, and annual reviews discuss industrial threats, vulnerability observations, and field findings.

**Use it for:** Inform threat modeling, leadership briefings, and the selection of defensive priorities.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R063 · [Claroty Team82 research](https://www.claroty.com/team82/research)

**Best fit:** Practitioner → Specialist  
**Access:** 🟡 Free, with conditions. Public articles free; some downloads may require a form; vendor perspective  
**Cost:** $0

Public technical research covers industrial and other cyber-physical vulnerabilities, protocol behavior, and exploitation findings.

**Use it for:** Understand device-level weaknesses and build better vendor/asset risk discussions.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R064 · [Nozomi Networks research reports](https://www.nozominetworks.com/research-reports)

**Best fit:** Practitioner / Program lead  
**Access:** 🟡 Free, with conditions. Free report access may require registration/email; paid products separate  
**Cost:** $0

Public reports cover OT/IoT security trends and research from a commercial security vendor.

**Use it for:** Compare findings with other intelligence sources and improve monitoring priorities.

**Review date:** 2026-10-12

**Verification:** Publisher search-index evidence reviewed; direct report-index retrieval failed; report forms not exercised

#### R065 · [Kaspersky ICS CERT public research](https://ics-cert.kaspersky.com/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Public reading free; commercial products/intelligence separate; dataset and vendor perspective matter  
**Cost:** $0

Public reports and technical articles examine industrial threats, malware, and vulnerability research.

**Use it for:** Compare threat observations and study technical investigations.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R066 · [Operational Technology Cybersecurity Coalition resources](https://www.otcybercoalition.org/resources)

**Best fit:** Program lead / Policy  
**Access:** 🟢 Free. Public resources free; coalition membership is separate; policy/industry perspective  
**Cost:** $0

Public papers address OT cybersecurity policy and standards-based approaches. OTCC represents a coalition of industry companies.

**Use it for:** Track policy arguments and standards alignment discussions relevant to program leadership.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R077 · [The Industrial Control System Cyber Kill Chain — Assante and Lee](https://www.sans.org/white-papers/36297) — ⭐ Recommended starting point

**Best fit:** Practitioner → Specialist  
**Access:** 🟡 Free, with conditions. Free whitepaper; download/account requirements may apply  
**Cost:** $0

A two-stage model explains adversary campaigns against ICS, supported by Havex and Stuxnet case studies.

**Use it for:** Analyze the steps between an initial compromise and an attack on a physical process; identify intervention points.

**Publication status:** 2015 foundational paper; supplement with current ATT&CK for ICS

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 65, 82 (printed page(s) 61, 78).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R086 · [CRASHOVERRIDE analysis and lessons — Dragos](https://www.dragos.com/blog/ukraine-power-grid-cyberattack-crashoverride-10-year-lessons)

**Best fit:** Practitioner → Specialist / Electric sector  
**Access:** 🟢 Free. Public article free; vendor research perspective  
**Cost:** $0

Public Dragos analysis discusses the Ukraine power-grid attacks, CRASHOVERRIDE, and lessons for industrial defense. It provides a current accessible route into the case referenced by the manual.

**Use it for:** Study protocol-aware malware and connect technical behavior with potential operational consequences.

**Publication status:** 2026 retrospective of historical incidents

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 60 (printed page(s) 56).

**Review date:** 2026-10-12

**Verification:** Official article found; original manual-linked CrashOverride-01.pdf could not be retrieved

#### R087 · [PIPEDREAM / CHERNOVITE public whitepaper — Dragos](https://hub.dragos.com/whitepaper/chernovite-pipedream)

**Best fit:** Practitioner → Specialist  
**Access:** 🟡 Free, with conditions. Whitepaper advertised free; form/email may be required; paid intelligence/platform separate  
**Cost:** $0

A public whitepaper analyzes a modular ICS attack framework and supplies mitigation guidance. The public threat-group page offers additional context.

**Use it for:** Understand industrial attack capabilities and review protocol exposure and detection assumptions.

**Publication status:** Historical research; distinguish described capability from observed deployment

**Related official source/project:** [Open link](https://www.dragos.com/threat/chernovite)

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 61 (printed page(s) 57).

**Review date:** 2026-10-12

**Verification:** Official report landing page and threat-group page indexed; original direct PDF retrieval failed

#### R089 · [MITRE EMB3D threat model for embedded devices](https://emb3d.mitre.org/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free to read; MITRE Terms of Use apply; no account indicated  
**Cost:** $0

A MITRE knowledge base of cyber threats to embedded devices, such as controllers and field devices, paired with mitigations. It gives device-level threats a common vocabulary.

**Use it for:** Threat-model a PLC, RTU or gateway by looking up the device-level threats that apply and the mitigations that answer them.

**Publication status:** Living knowledge base; the site showed version 2.0.2 (June 1, 2026)

**Review date:** 2026-10-13

**Verification:** Official site fetched on October 13, 2026; version and Terms of Use link observed; downloads and any data exports not exercised

</details>

### Incident response and exercises

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R067 | [CISA Tabletop Exercise Packages — CTEPs](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages) | Practitioner / Program lead | 🟢 Free |
| R084 | [REMnux malware-analysis toolkit](https://docs.remnux.org/) | Practitioner → Specialist | 🟢 Free |
| R085 | [SANS SIFT Workstation](https://www.sans.org/tools/sift-workstation) | Practitioner → Specialist | 🟡 Free, with conditions |

<details>
<summary>Details for the 3 resources above</summary>

#### R067 · [CISA Tabletop Exercise Packages — CTEPs](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages)

**Best fit:** Practitioner / Program lead  
**Access:** 🟢 Free. Public exercise resources free; facilitation and customization take staff time  
**Cost:** $0

Exercise packages help organizations run discussion-based scenarios and assess response capabilities.

**Use it for:** Build a tabletop exercise and add site-specific process, safety, and restoration decisions.

**Supporting publisher source:** [Open link](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience)

**Review date:** 2026-10-12

**Verification:** Publisher services-page evidence reviewed; individual package availability varies

#### R084 · [REMnux malware-analysis toolkit](https://docs.remnux.org/)

**Best fit:** Practitioner → Specialist  
**Access:** 🟢 Free. Free toolkit; local VM/storage required; general malware analysis, not a universal PLC-forensics toolkit  
**Cost:** $0

A Linux distribution and documented toolkit collect free tools for examining malicious software and related artifacts.

**Use it for:** Analyze suspicious files recovered from engineering workstations and other OT-supporting computers in a dedicated malware lab.

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 70 (printed page(s) 66).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

#### R085 · [SANS SIFT Workstation](https://www.sans.org/tools/sift-workstation)

**Best fit:** Practitioner → Specialist  
**Access:** 🟡 Free, with conditions. Toolkit free; download/account requirements may apply; local VM/storage required; paid SANS training separate  
**Cost:** $0

A free open-source workstation collects incident-response and digital-forensics tools for detailed examinations.

**Use it for:** Investigate disk images and artifacts from industrial Windows/Linux systems or supporting infrastructure.

**Discovery source:** SANS 2023 ICS Field Manual; PDF page(s) 70 (printed page(s) 66).

**Review date:** 2026-10-12

**Verification:** Official publisher/project page or publisher search-index evidence reviewed; software and download flows not exercised

</details>

### Vulnerability management and prioritization

| ID | Resource | Best fit | Access |
| --- | --- | --- | --- |
| R097 | [CVSS v4.0 specification, user guide and calculator — FIRST](https://www.first.org/cvss/v4-0/) | Practitioner / Program lead | 🟢 Free |
| R098 | [EPSS — Exploit Prediction Scoring System, FIRST](https://www.first.org/epss/) | Practitioner / Program lead | 🟢 Free |
| R099 | [CISA Known Exploited Vulnerabilities (KEV) catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Practitioner / Program lead | 🟢 Free |
| R100 | [CISA CSAF repository — machine-readable security advisories](https://github.com/cisagov/CSAF) | Practitioner → Specialist | 🟡 Free, with conditions |
| R101 | [OT Triage — Now / Next / Never triage for OT/ICS vulnerabilities (maintainer's tool)](https://github.com/okieotsec/ot-triage) | Practitioner / Program lead | 🟢 Free |

<details>
<summary>Details for the 5 resources above</summary>

#### R097 · [CVSS v4.0 specification, user guide and calculator — FIRST](https://www.first.org/cvss/v4-0/)

**Best fit:** Practitioner / Program lead  
**Access:** 🟢 Free. Public hub page; the page does not state license terms for each document, so check them before redistributing  
**Cost:** $0

FIRST's hub for CVSS v4.0 links the specification document, user guide, implementation guide, examples, FAQ and an online calculator for scoring vulnerabilities.

**Use it for:** Learn how the base, threat and environmental metrics are defined, and check a score you worked out by hand or in a tool.

**Review date:** 2026-10-13

**Verification:** FIRST page fetched on October 13, 2026; the linked documents and calculator were not opened or exercised

#### R098 · [EPSS — Exploit Prediction Scoring System, FIRST](https://www.first.org/epss/)

**Best fit:** Practitioner / Program lead  
**Access:** 🟢 Free. Data described as freely and openly available through CSV files and an API; the license of the documentation was not stated on the page  
**Cost:** $0

A model maintained by a FIRST special interest group that estimates the probability that a published CVE will be exploited in the wild within the next 30 days. The page says the scores are freely and openly available as daily CSV downloads and through an API, with model documentation and research linked.

**Use it for:** Add exploitation likelihood to patch-prioritization decisions, remembering that it scores CVEs generally and says nothing about operational consequence.

**Review date:** 2026-10-13

**Verification:** FIRST page fetched on October 13, 2026; data files and API not downloaded or called

#### R099 · [CISA Known Exploited Vulnerabilities (KEV) catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

**Best fit:** Practitioner / Program lead  
**Access:** 🟢 Free. Public; no account; machine-readable downloads; the due dates and required actions come from a CISA directive that binds US federal agencies and are context for everyone else  
**Cost:** $0

CISA's catalog of vulnerabilities that are known to be exploited in the wild. Each entry carries a CVE identifier, the date it was added, a due date and a required action; the page offers CSV and JSON downloads, a print view and a JSON schema.

**Use it for:** Check whether a vulnerability in your asset inventory is known to be actively exploited, and feed the JSON into your own prioritization.

**Review date:** 2026-10-13

**Verification:** CISA page fetched on October 13, 2026, showing 1,739 entries at that time; downloads not exercised

#### R100 · [CISA CSAF repository — machine-readable security advisories](https://github.com/cisagov/CSAF)

**Best fit:** Practitioner → Specialist  
**Access:** 🟡 Free, with conditions. Public repository; no account; reading and downloading are free; GitHub did not detect a license file on October 12, 2026, so check before redistributing  
**Cost:** $0

CISA's public repository of security advisories in the OASIS CSAF 2.0 format, with the industrial control systems (OT) advisories kept in their own folder, organized by year, together with an index and per-file signature and checksum files.

**Use it for:** Pull advisories into your own tooling, or look up which published advisories name a CVE, a vendor or a product.

**Review date:** 2026-10-13

**Verification:** Repository structure inspected through the GitHub API on October 12–13, 2026 (OT advisory folders by year, an index and per-advisory files); advisory content not independently assessed

#### R101 · [OT Triage — Now / Next / Never triage for OT/ICS vulnerabilities (maintainer's tool)](https://github.com/okieotsec/ot-triage)

**Best fit:** Practitioner / Program lead  
**Access:** 🟢 Free. Free and open source (MIT for the code; the OkieOTSec name and logo are excluded from that license); needs Python 3.12 or newer with Tkinter; no third-party packages  
**Cost:** $0

An open-source desktop tool maintained by the author of this catalog. It ranks an OT vulnerability as NOW, NEXT or NEVER from its CVSS score or vector, the asset's criticality and exposure, patch availability and compensating controls, and shows its reasoning. It works offline and uses CISA KEV, EPSS and CISA's ICS advisories as context.

**Use it for:** Try a transparent, explainable triage on the sample findings, or read its policy document to see how each rule was reasoned.

**Publication status:** Maintained by the catalog's author; not independently reviewed

**Review date:** 2026-10-13

**Verification:** Repository and releases checked by the maintainer on October 13, 2026; included as the maintainer's own project, so judge its rules for yourself

</details>

## Affordable paid resources

Prices are observed publisher listings. Check billing periods, promotions, regional pricing and checkout before buying.

| ID | Resource | Best fit | Observed cost | Buying priority |
| --- | --- | --- | --- | --- |
| R068 | [Industrial Cybersecurity, Second Edition — Pascal Ackerman](https://www.packtpub.com/en-us/product/industrial-cybersecurity-9781800202092) | Practitioner → Specialist | Observed: eBook $39.59; paperback $43.99 (discounted); list $43.99/$54.99 | Strong technical value |
| R069 | [Practical Industrial Cybersecurity — Charles J. Brooks and Philip A. Craig Jr.](https://www.wiley-vch.de/en/areas-interest/computing-computer-sciences/practical-industrial-cybersecurity-978-1-119-88302-9) | Foundation → Practitioner | Observed publisher listing: $42.90 | Strong introductory value |
| R070 | [Labshock Pro — individual personal use](https://labshocksecurity.com/pricing/) | Foundation → Practitioner | Introductory: $24/month or $14/month billed yearly ($168/year); standard comparison shows $30/month or $20/month yearly ($240/year) | Strong lab value |
| R071 | [Factory I/O — Starter or Modbus & OPC editions](https://factoryio.com/editions/) | Foundation → Practitioner | Starter: €40/year or €109 once; Modbus & OPC: €17/month, €158/year, or €435 once | Strong process-visualization value |
| R072 | [Packt Premium monthly subscription](https://www.packtpub.com/en-us/subscribe-premium-access) | Practitioner → Specialist | Advertised: $29.99/month | Optional alternative to individual book purchases |
| R073 | [Industrial Cybersecurity: Case Studies and Best Practices — Steve Mustard](https://www.wiley.com/en-us/shop/international-society-of-automation-c-6473) | Practitioner / Program lead | US publisher catalog: starting at $95 | Budget stretch |

<details>
<summary>Details for the 6 resources above</summary>

#### R068 · [Industrial Cybersecurity, Second Edition — Pascal Ackerman](https://www.packtpub.com/en-us/product/industrial-cybersecurity-9781800202092)

**Best fit:** Practitioner → Specialist  
**Access:** 🔵 Paid. One-time purchase; 2021 edition; lab/software instructions and standards references need version checking  
**Cost:** Observed: eBook $39.59; paperback $43.99 (discounted); list $43.99/$54.99

A substantial technical book covers architecture, monitoring, threat intelligence, SIEM, response, assessments, and threat hunting.

**Use it for:** Choose for hands-on defensive depth and building an ICS monitoring practice.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R069 · [Practical Industrial Cybersecurity — Charles J. Brooks and Philip A. Craig Jr.](https://www.wiley-vch.de/en/areas-interest/computing-computer-sciences/practical-industrial-cybersecurity-978-1-119-88302-9)

**Best fit:** Foundation → Practitioner  
**Access:** 🔵 Paid. One-time book purchase; 2022 edition; regional format/checkout pricing may differ  
**Cost:** Observed publisher listing: $42.90

A broad ICS/Industry 4.0/IIoT book covers architecture, hardening, governance, assessment, monitoring, response, and continuity, with review questions.

**Use it for:** Choose for a structured entry into OT security and a broad reference.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R070 · [Labshock Pro — individual personal use](https://labshocksecurity.com/pricing/)

**Best fit:** Foundation → Practitioner  
**Access:** 🔵 Paid. Recurring plan; own hardware required; one named individual; company deployment and training delivery require organization licensing  
**Cost:** Introductory: $24/month or $14/month billed yearly ($168/year); standard comparison shows $30/month or $20/month yearly ($240/year)

The paid personal plan removes session limits and unlocks the full lab progression, guides, quests, and scenarios.

**Use it for:** Choose when ready-made local industrial exercises are more useful than assembling a lab from scratch.

**Review date:** 2026-10-12

**Verification:** Current pricing cards and standard-rate comparison reviewed; introductory offer duration not stated

#### R071 · [Factory I/O — Starter or Modbus & OPC editions](https://factoryio.com/editions/)

**Best fit:** Foundation → Practitioner  
**Access:** 🔵 Paid. Windows software; 30-day Ultimate trial separate; edition determines connectivity; taxes and currency conversion extra  
**Cost:** Starter: €40/year or €109 once; Modbus & OPC: €17/month, €158/year, or €435 once

A 3D factory simulator provides visible process behavior for PLC exercises. Starter includes an integrated control simulator; Modbus & OPC provides external protocol connectivity.

**Use it for:** Choose Starter for control fundamentals or Modbus & OPC for protocol-connected security labs.

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

#### R072 · [Packt Premium monthly subscription](https://www.packtpub.com/en-us/subscribe-premium-access)

**Best fit:** Practitioner → Specialist  
**Access:** 🔵 Paid. Recurring subscription; confirm target book/format and credit eligibility; broad library, not a dedicated OT curriculum  
**Cost:** Advertised: $29.99/month

A broad technical library subscription includes online access plus a monthly credit for an eligible eBook/video to download and keep.

**Use it for:** Consider when studying multiple titles; compare one month with purchasing the specific book directly.

**Review date:** 2026-10-12

**Verification:** Publisher search-index evidence reviewed; direct page retrieval failed; checkout price not exercised

#### R073 · [Industrial Cybersecurity: Case Studies and Best Practices — Steve Mustard](https://www.wiley.com/en-us/shop/international-society-of-automation-c-6473)

**Best fit:** Practitioner / Program lead  
**Access:** 🔵 Paid. One-time purchase; format prices vary; upper end of this catalog's budget range  
**Cost:** US publisher catalog: starting at $95

A practical industrial-security book follows governance through design, implementation, and operation, using case studies.

**Use it for:** Choose for program leadership and applied management; try a library copy first if budget is tight.

**Related official source/project:** [Open link](https://www.isa.org/standards-and-publications/isa-publications/isa-books/authors-corner/author-q-a-industrial-cybersecurity-case-studies-a)

**Review date:** 2026-10-12

**Verification:** Publisher page or publisher search-index evidence reviewed; access and software not independently exercised

</details>

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
