# Citation Bank — WCS App Approval QC

Reusable citations with exact statute/spec references. Paste directly into QC findings and packet fixes.

---

## Federal Statutes & Regulations

### FERPA
- **20 U.S.C. § 1232g** — Family Educational Rights and Privacy Act
- **34 CFR Part 99** — FERPA regulations
- **34 CFR § 99.31(a)(1)(i)(B)** — School Official exception (three prongs)

Canonical School Official language:
> Provider operates as a "School Official" with a "legitimate educational interest" as defined under 34 CFR § 99.31(a)(1)(i)(B). Provider (a) performs an institutional service for which the District would otherwise use employees, (b) operates under the District's direct control with respect to the use and maintenance of Student Data, and (c) is subject to FERPA's requirements governing the use and redisclosure of personally identifiable information from education records.

### COPPA
- **15 U.S.C. § 6501 et seq.** — Children's Online Privacy Protection Act
- **16 CFR Part 312** — FTC COPPA Rule
- **16 CFR § 312.5(c)(10)** — School-consent exception

Canonical school-consent language:
> For students under 13 years of age, Provider relies on the school-consent exception set forth at 16 CFR § 312.5(c)(10). Provider uses personal information only for educational purposes authorized by the District, does not use such information for commercial purposes, and will delete or return such information upon District request.

### CIPA
- **47 U.S.C. § 254(h)** — Children's Internet Protection Act
- Applies to E-rate funded institutions

### Section 508
- **29 U.S.C. § 794d** — Rehabilitation Act Section 508
- **36 CFR Part 1194** — Section 508 standards (Refresh)
- Harmonized with EN 301 549 and WCAG 2.0 AA (currently under revision for WCAG 2.1+)

### ADA Title II
- **42 U.S.C. § 12131 et seq.** — ADA Title II
- **28 CFR Part 35** — ADA Title II regulations
- **DOJ Final Rule, April 24, 2024** — establishes WCAG 2.2 AA as the technical standard
- Public entities ≥50,000 population: compliance by **April 24, 2026**
- Public entities <50,000 and special district govts: compliance by **April 24, 2027**
- WCS is in the April 24, 2026 cohort

---

## Tennessee Statutes

### TN Student Data Act
- **TCA § 49-1-701 et seq.** — Tennessee Student Data Accessibility, Transparency and Accountability Act (TN DATA Act)
- Requires districts to ensure vendors comply with FERPA, COPPA, and state privacy standards

Canonical compliance statement:
> Provider complies with the Tennessee Student Data Accessibility, Transparency and Accountability Act (TCA § 49-1-701 et seq.) and all applicable Tennessee Department of Education data privacy requirements.

### TN Breach Notification
- **TCA § 47-18-2107** — Release of personal consumer information
- Notification required **immediately but no later than 45 days** from discovery
- Enforced via TN Division of Consumer Affairs; private right of action under TCA § 47-18-2104

Canonical DPA breach language:
> Provider shall notify the District within seventy-two (72) hours of discovering a confirmed or reasonably suspected security incident involving unauthorized access to or disclosure of Student Data. This seventy-two (72) hour commitment exceeds the forty-five (45) day statutory notification period required under TCA § 47-18-2107.

### TN Age-Appropriate Materials Act
- **Public Chapter 744 of 2022** (codified in TCA Title 49)
- Requires districts to review instructional materials for age-appropriateness
- Applies to instructional materials in TN public schools

### TN Supplemental Materials Authority
- **TCA § 49-6-2202(a)(3)** — Authorizes districts to approve supplemental instructional materials outside the state textbook adoption cycle
- Used by WCS for History Hack's AY 25-26 / AY 26-27 authorization

### TN Textbook Commission
- **TCA § 49-6-2201 et seq.** — Textbook and Instructional Materials Quality Commission
- **SBE Policy 2.600** — Textbook and Instructional Materials Selection
- Schedule F (Social Studies) review rubric governs state-level adoption

---

## Accessibility Specifications

### WCAG
- **WCAG 2.2 Level AA** (W3C Recommendation, October 5, 2023)
- [WCAG 2.2 URL](https://www.w3.org/TR/WCAG22/)
- Target for ADA Title II compliance and WCS submissions

Key SCs to cite in VPAT:
- 1.4.3 Contrast (Minimum) — 4.5:1 normal, 3:1 large
- 1.4.10 Reflow
- 1.4.11 Non-text Contrast
- 2.1.1 Keyboard
- 2.4.7 Focus Visible
- 2.5.7 Dragging Movements (new in 2.2)
- 2.5.8 Target Size (Minimum) (new in 2.2)
- 3.3.7 Redundant Entry (new in 2.2)
- 3.3.8 Accessible Authentication (Minimum) (new in 2.2)
- 4.1.2 Name, Role, Value

### VPAT
- **VPAT 2.5Rev** — current ITI revision (April 2025)
- [ITI VPAT page](https://www.itic.org/policy/accessibility/vpat)
- Editions: WCAG, Section 508, EN 301 549, INT (all three)
- Use **INT edition** for comprehensive district/federal coverage

### Section 508
- **EN 301 549** — European accessibility standard harmonized with Section 508 Refresh

---

## Interoperability Specifications

### LTI
- **LTI 1.3** — 1EdTech IMS Learning Tools Interoperability Core Specification
- **LTI Advantage** — umbrella for:
  - Assignment and Grade Services (AGS)
  - Names and Role Provisioning Services (NRPS)
  - Deep Linking 2.0
- Required technical endpoints:
  - OIDC login initiation URL
  - LTI launch URL (target link URI)
  - JWK Set URL (public key endpoint, JSON Web Key Set)
  - Redirect URI(s)

### OneRoster
- **OneRoster v1.2** — current 1EdTech rostering spec
- Modes: CSV 1.2, REST API 1.2
- Versions 1.0 and 1.1 are legacy

### SAML / OIDC
- **SAML 2.0** — OASIS standard for SSO
- **OpenID Connect 1.0** — OAuth 2.0 authentication layer
- ClassLink supports both
- Microsoft Entra ID (Azure AD) supports both

---

## Certifications & Pledges

### 1EdTech TrustEd Apps
- [TrustEd Apps](https://www.1edtech.org/program/trusted-apps)
- Vendor pledge, free to sign
- Distinct from LTI and OneRoster interop certifications
- Recognized by many TN districts

### Common Sense Privacy
- [Common Sense Privacy Evaluations](https://privacy.commonsense.org/)
- Free vendor submission
- 6–12 week review typical
- Ratings: Pass / Warning / Fail (plus transparency-only)

### iKeepSafe
- [iKeepSafe Certifications](https://ikeepsafe.org/certifications/)
- COPPA Safe Harbor, FERPA, California Student Privacy, ATLIS certifications
- Paid, multi-step, requires outside counsel review

### SDPC NDPA
- [SDPC NDPA v1r7](https://privacy.a4l.org/ndpa/) — National Data Privacy Agreement template
- Used by many districts as baseline DPA
- WCS may accept signatory status in lieu of separate DPA

---

## WCS-Specific References

- LMS: **Schoology**
- SSO: **ClassLink** and **Microsoft Entra ID** preferred
- Form: WCS Application Evaluation (submitted via Technology Department)
- Approval authority: Williamson County Schools Technology Office

---

## Quick-Paste Snippets

### Encryption statement
> All data is encrypted in transit using TLS 1.2 or higher with HSTS enforcement. All data at rest is encrypted using AES-256 via Azure Storage Service Encryption and Azure SQL Transparent Data Encryption. Azure Key Vault manages all encryption keys.

### US data storage statement
> All Student Data is stored exclusively within data centers located in the United States, specifically Microsoft Azure Central US region. Provider shall not transfer Student Data outside the United States without prior written consent from the District.

### No-sell, no-advertising statement
> Provider does not sell Student Data. Provider does not use Student Data for advertising, marketing, or any commercial purpose unrelated to providing the Service.

### AI-training opt-out
> Student Data is never used to train any artificial intelligence or machine learning model. No student inputs, outputs, or behavioral data are retained or transmitted to any AI provider for model-training purposes.

### TN governing law
> This Agreement shall be governed by and construed in accordance with the laws of the State of Tennessee, without regard to its conflict of law provisions.
