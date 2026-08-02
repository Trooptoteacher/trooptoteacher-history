# WCS QC Checklist — 34 Items

Every QC run must score all 34 items. Items are grouped by the 11 WCS evaluation areas plus structural, DPA, and polish groups.

Pass criteria are **evidence-only**: a Pass requires a published URL, signed document, or explicit quote from the packet. Planned/in-progress = Fail.

---

## Group A — Structural (4 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| A1 | Academic year current | All AY references match current submission cycle | Stale AY from prior draft | 🛑 |
| A2 | Tech stack internally consistent | Web-only OR web+mobile stated once, matches product reality | Template language mixes React Native + web app | 🛑 |
| A3 | Reconciles with prior WCS authorizations | Memory check shows no contradiction, or packet states reason for new submission | Contradicts known prior approval | 🛑 |
| A4 | Zero placeholder tokens in final prose | Search returns zero hits for `[insert`, `[INSERT`, `TBD`, `TODO`, `XXX` | Bracketed placeholders left in | 🛑 |

---

## Group B — Policies (2 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| B1 | Terms of Use at live stable URL | URL loads publicly, no login required, contains required clauses (permitted use, IP, limitation of liability, TN governing law) | URL is placeholder or page returns 404 | 🛑 |
| B2 | Privacy Policy at live stable URL | URL loads publicly, covers data collected/shared/retained, TN DATA Act clause present, parental rights disclosed | URL placeholder or missing COPPA/FERPA/TN DATA Act language | 🛑 |

---

## Group C — COPPA / FERPA (3 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| C1 | COPPA statement published and scoped correctly | Statement at public URL AND grade scope aligns (if grade 7 included, school-consent mechanism under 16 CFR § 312.5(c)(10) documented) | Grade 7 + "no under-13 data collection" contradiction | 🔴 |
| C2 | FERPA School Official three prongs stated | Packet affirms: (a) service the district would use employees for, (b) under district's direct control, (c) subject to FERPA use/redisclosure limits | Only one or two prongs stated | 🛑 |
| C3 | TN Student Data Act (TCA 49-1-701 et seq.) referenced | DPA Article 6 or equivalent cites TN statute with compliance affirmation | Generic "state law compliance" without citation | 🟡 |

---

## Group D — Account Management / SSO / Rostering (4 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| D1 | SSO status accurately stated | Live vs. planned clearly labeled for each provider (ClassLink, Entra ID, Google Workspace) | Claims "Entra ID" live when only email/password is live | 🔴 |
| D2 | Rostering answer is unambiguous | One answer (Yes/No/LTI-NRPS) not both | "Not supported" and "Via LTI" in same response | 🔴 |
| D3 | Account creation flow documented for LTI vs direct | Both paths described with data-collection implications | Only LTI path described | 🟡 |
| D4 | Account deletion process documented | Timeline + mechanism stated | Silent on deletion | 🟡 |

---

## Group E — Interoperability / LTI (3 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| E1 | LTI 1.3 version and endpoints documented | OIDC login URL, LTI launch URL, JWK Set URL, redirect URI all provided | Endpoints missing or placeholder | 🛑 |
| E2 | Schoology compatibility honestly stated | "Compatible via LTI 1.3" (not "Schoology Certified") unless 1EdTech cert in hand | Implies certification via "active workstreams" | 🔴 |
| E3 | Deep linking (Deep Linking 2.0) status stated | Functional OR planned with date | Vague "active workstream" | 🟡 |

---

## Group F — Instructional Materials & Content Governance (3 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| F1 | TN Academic Standards cited by range | "US.01–US.95" (or current cycle) explicit | "Tennessee-aligned" without citation | 🟡 |
| F2 | Scope-and-sequence document at public URL | Actual URL, not placeholder | Listed as action item with no deliverable sized | 🟡 |
| F3 | Age-Appropriate Materials Act (Public Chapter 744 of 2022) addressed | Content-review process, teacher overrides, parent visibility described | Not mentioned | 🔴 |

---

## Group G — Installation / Hosting / Whitelist (3 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| G1 | Full whitelist URL list compiled | Every FQDN + region for app, API, auth, CDN, video, third-party AI services | Listed as action, not provided | 🛑 |
| G2 | Local install requirement answered | Clear "web-only, no local install" OR enumerated installed clients | App Store URLs for a web product | 🛑 |
| G3 | Video hosting disclosed | Provider + CDN domain | Silent on video | 🟡 |

---

## Group H — Accessibility / VPAT (3 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| H1 | VPAT 2.5Rev (current ITI version, April 2025) referenced | Explicit version cited | VPAT 2.4 or older | 🛑 |
| H2 | WCAG 2.2 AA target stated | Matches ADA Title II DOJ April 2024 rule | WCAG 2.1 AA | 🛑 |
| H3 | Schoology iframe accessibility tested | Keyboard, screen reader, contrast results documented | Action item without results | 🔴 |

---

## Group I — Terms of Use / Data Practices (4 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| I1 | Data-collected list exhaustive and categorized | Every field listed, PII vs. non-PII flagged | Partial list | 🔴 |
| I2 | Data-sharing list complete | All subprocessors named; "no commercial sharing" explicit | Silent on third-party AI SDKs | 🛑 |
| I3 | Data retention and disposal documented | Retention schedule + deletion mechanism + timeline | Action item only | 🔴 |
| I4 | IP ownership covers students AND teachers | Student-data and teacher-authored content both addressed | Student-only clause | 🔴 |

---

## Group J — Data Security (4 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| J1 | Encryption documented (transit + rest) | TLS 1.2+ in transit, AES-256 at rest, named mechanism (e.g., Azure SSE) | "Industry standard encryption" without spec | 🔴 |
| J2 | US data storage with region | Cloud provider + region (e.g., Azure Central US) | Provider as placeholder | 🛑 |
| J3 | Breach notification correctly cites TN statute | 45-day TN statutory floor (TCA § 47-18-2107) acknowledged; vendor commitment to stricter window (e.g., 72h) stated | 72h cited as TN law | 🛑 |
| J4 | Data export capability documented | Admin export function described | Silent | 🟡 |

---

## Group K — AI Disclosure (1 item, critical)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| K1 | AI disclosure enumerates every AI system | Production features AND authoring-time tools listed; provider, data sent, retention, training opt-out for each; student-data-for-training = No | Only ElevenLabs/HeyGen listed when product has LLM features | 🔴 |

---

## Group L — Ratings / Pledges (2 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| L1 | Common Sense Privacy status accurate | Submitted (with reference #) OR honestly "not yet submitted, planned by [date]" | Overclaims rating | 🔴 |
| L2 | 1EdTech TrustEd Apps pledge status accurate, separate from LTI cert | Pledge and LTI certification treated as distinct | Conflates the two | 🟡 |

---

## Group M — DPA Framework (4 items)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| M1 | DPA Article 2 Definitions complete | Minimum: Student Data, District, Provider, PII, De-identified Data, Authorized User, Service, Subprocessor, Effective Date | Only one term defined | 🟡 |
| M2 | DPA Article 9 breach language aligns with TN + district expectation | 72h vendor commitment, TN 45-day floor acknowledged | GDPR language without TN reference | 🛑 |
| M3 | DPA Article 12 Subprocessors enumerated | Every subprocessor listed with purpose and data categories | Placeholder list | 🛑 |
| M4 | DPA Article 13 Survival clause complete | Survives: Articles 3 (Use), 7 (Security), 9 (Breach), 10 (Retention), 11 (Portability), 14 (Governing Law) | Missing Article 11 or 14 | 🔴 |

---

## Group N — Document Polish (1 aggregate item)

| # | Item | Pass Criteria | Common Failure | Severity if Fail |
|---|---|---|---|---|
| N1 | Document metadata and polish | Version number, ToC, vendor contact block, one prominent draft banner, clean typography | Multiple banners, no ToC, no version, internal PM speak ("WEEK 1 priority") | 🟢 |

---

## Scoring Rubric

- Each item = Pass / Fail / Cannot Verify
- Fail severity comes from the table above
- Cannot Verify = counted as Fail at stated severity until evidence provided

**Disposition:**
- Zero Blocker fails AND ≤2 High fails = ✅ READY (pending legal counsel)
- Any Blocker fail OR >2 High fails = ❌ NOT READY
