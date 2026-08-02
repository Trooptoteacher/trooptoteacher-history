# WCS Evaluation Areas — Detailed Spec

Load when QC'ing a specific evaluation area and need the full WCS-expected response shape.

Source: WCS Application Evaluation Form (AY 2025–26 baseline; update each cycle).

---

## Area 1 — Policies (ToU + Privacy Policy)

**WCS expects:**
- Terms of Use at a public URL, no login required
- Privacy Policy at a public URL, no login required
- Both URLs submitted on the WCS form

**ToU must address:**
- Permitted use (educational only)
- Age restrictions (13+ direct, or school-consent for under-13)
- District licensing terms
- IP ownership (student and teacher content)
- Limitation of liability
- Governing law — **Tennessee**

**Privacy Policy must address:**
- Categories of data collected (exhaustive)
- Categories of data shared (ideally none)
- Data retention schedule
- Parental rights and deletion process
- TN DATA Act (TCA 49-1-701 et seq.) compliance clause
- COPPA compliance statement
- FERPA School Official designation

---

## Area 2 — COPPA / FERPA Compliance

**COPPA (15 U.S.C. § 6501 et seq.; 16 CFR Part 312):**
- If any user is under 13, must rely on school-consent exception under 16 CFR § 312.5(c)(10):
  - (i) Operator uses personal information only for educational purposes authorized by the school
  - (ii) Provides notice to the school of collection practices
  - (iii) Does not use PI for commercial purposes
  - (iv) Permits deletion on district request

**FERPA (20 U.S.C. § 1232g; 34 CFR Part 99):**
- Vendor operates as **School Official** under 34 CFR § 99.31(a)(1)(i)(B):
  - (a) Performs institutional service for which the district would otherwise use employees
  - (b) Under the district's **direct control** regarding data use and maintenance
  - (c) Subject to FERPA's use and redisclosure requirements

All three prongs must appear in the statement or DPA.

---

## Area 3 — Account Management / SSO / Rostering

**Required documentation:**
- Does the app require student accounts? (Yes/No, what data at creation)
- SSO protocols supported (SAML 2.0, OAuth 2.0, OIDC)
- Identity providers supported (ClassLink, Entra ID, Google Workspace) — WCS prefers ClassLink and Entra ID
- Rostering mechanisms (OneRoster CSV, OneRoster REST, SCIM, Clever, LTI NRPS)
- Account-creation path for non-LTI vs LTI launches
- Account deletion timeline and mechanism

**Red flag:** Claiming SSO is "integrated" when only email/password is live. Use "planned Q3 2026" style honesty.

---

## Area 4 — Interoperability / LTI / Schoology

**WCS uses Schoology.** Preferred stack:
- LTI 1.3 / LTI Advantage
- Deep Linking 2.0 (content picker)
- Assignment and Grade Services (AGS)
- Names and Role Provisioning Services (NRPS)

**Required technical details:**
- LTI version
- OIDC login initiation URL
- LTI launch URL (tool URL)
- JWK Set URL (public key endpoint)
- Redirect URI
- Schoology Tool Consumer Key (if live)

**Certifications — do NOT conflate:**
- 1EdTech LTI certification = interop conformance
- 1EdTech TrustEd Apps = separate privacy pledge
- Schoology Certified = partner-program status
State each separately and honestly.

---

## Area 5 — Instructional Materials & Content Governance

**Required documentation:**
- Scope and sequence at a stable URL
- TN Academic Standards citation (e.g., US.01–US.95 for high school US History)
- Content governance policy (citations, source authenticity, AI-generated imagery policy)
- District content controls (can districts/teachers enable/disable modules?)
- **Age-Appropriate Materials Act (TN Public Chapter 744 of 2022):**
  - Content review process
  - Teacher override controls
  - Parent visibility mechanism

---

## Area 6 — Installation / Hosting / Whitelist

**Required:**
- Local-install answer (typically "No, web-based")
- Complete whitelist table of all FQDNs:
  - Primary app domain
  - API domain
  - Auth/identity domain
  - Azure-hosted services (with region)
  - CDN endpoints
  - Video host (Vimeo/YouTube/self-hosted)
  - Third-party AI services (ElevenLabs API, HeyGen CDN, etc.)
  - Font/asset CDNs
- Mobile-app URLs (only if genuine mobile apps exist)

Network admins cannot whitelist without this. Missing = Blocker.

---

## Area 7 — Accessibility / VPAT / WCAG

**Current standard (April 2026):**
- VPAT **2.5Rev** (ITI, April 2025) — [VPAT page](https://www.itic.org/policy/accessibility/vpat)
- WCAG **2.2 Level AA** (W3C)
- Section 508 Refresh
- ADA Title II DOJ Rule (April 2024; public entity compliance deadline April 24, 2026 for 50k+ population / April 24, 2027 for smaller — WCS is in the 2026 cohort)

**VPAT must cover:**
- WCAG 2.2 Level A and Level AA success criteria
- Section 508 EN 301 549 criteria
- Conformance levels per SC: Supports / Partially Supports / Does Not Support / Not Applicable
- Remediation plan for any Partial/Does Not Support

**Schoology iframe testing:**
- Keyboard nav works inside iframe
- Screen reader labels read correctly
- Color contrast inside iframe context meets 4.5:1 normal / 3:1 large

---

## Area 8 — Terms of Use / Data Practices

**Data collected list (exhaustive):**
- Name, email, school, grade, student ID
- Usage data, assessment scores, timestamps
- Any device/IP data
- Anything from LTI claims (roster data via NRPS)

**Categorize:** PII vs. non-PII.

**Data sharing:** Ideally "No" for all commercial. Must disclose all subprocessors.

**Data retention:**
- How long during contract
- What happens at end of school year
- What happens at contract termination (delete within N days)

**IP ownership:**
- Students retain IP to student-created content
- Teachers retain IP (or WCS retains, per employment policy) to teacher-authored content
- District retains IP to district data

---

## Area 9 — Data Security

**Encryption:**
- In transit: TLS 1.2 or higher (1.3 preferred), HSTS enforced
- At rest: AES-256, named mechanism (Azure SSE, Azure SQL TDE, etc.)

**Storage location:**
- US-based data centers, no exceptions
- Specify cloud provider + region (e.g., Microsoft Azure, Central US)

**Access controls:**
- RBAC, least-privilege
- MFA required for staff with production access
- Background checks for staff with student-data access

**Breach notification:**
- TN statutory floor: **45 days** (TCA § 47-18-2107)
- WCS-style contractual requirement: **72 hours** (vendor commits to stricter)
- DPA Article 9 must state both

**Other:**
- Penetration testing (annual recommended)
- Vulnerability management cadence
- SOC 2 Type II status (or honest "planned" / "inherited from Azure")

---

## Area 10 — AI Disclosure

**Every AI system must be disclosed:**

| AI System | Used For | Data Sent | Retention | Training Opt-Out | Human Review |
|---|---|---|---|---|---|

Categories to enumerate:
- **Production AI** students interact with (voice synthesis, avatars, chatbots, tutoring)
- **Authoring-time AI** that shapes content before release (no student data, but disclose for transparency)
- **None** categories (explicit confirmation, e.g., "No LLM features in production student experience")

**Critical answers:**
- Is student data used to train AI? → Must be "No"
- Can AI features be disabled by district/teacher? → Describe controls
- Who reviews AI outputs? → Describe QA pipeline

---

## Area 11 — Ratings / Pledges

- **Common Sense Privacy rating** (privacy.commonsense.org) — free vendor submission, 6–12 week review
- **1EdTech TrustEd Apps Pledge** (imsglobal.org) — vendor commitment, separate from LTI cert
- **iKeepSafe COPPA+ and FERPA certifications** — paid, multi-step
- **SDPC NDPA** signatory status

State each accurately. Never overclaim. "Not yet pursued" is acceptable if honest.

---

## DPA — 14 Articles (standard structure)

| # | Article | Must Include |
|---|---|---|
| 1 | Purpose | Product name, district name |
| 2 | Definitions | Student Data, District, Provider, PII, De-identified, Authorized User, Service, Subprocessor, Effective Date |
| 3 | Authorized Use | No sell, no advertising, no non-service disclosure |
| 4 | FERPA Compliance | Three School Official prongs |
| 5 | COPPA Compliance | School-consent mechanism for under-13 |
| 6 | TN Student Data Act | TCA 49-1-701 et seq. citation |
| 7 | Data Security | TLS 1.2+, AES-256, RBAC, MFA, background checks |
| 8 | Data Storage Location | US only, no cross-border without consent |
| 9 | Breach Notification | 72h vendor commitment + 45-day TN floor acknowledgment |
| 10 | Data Retention & Disposal | Retention schedule + disposal timeline + certification |
| 11 | Data Portability | District owns data, export on demand in standard format |
| 12 | Subprocessors | Enumerated list with change-notification obligation |
| 13 | Term and Termination | Survives: Articles 3, 7, 9, 10, 11, 14 |
| 14 | Governing Law | Tennessee; venue TBD with WCS |
