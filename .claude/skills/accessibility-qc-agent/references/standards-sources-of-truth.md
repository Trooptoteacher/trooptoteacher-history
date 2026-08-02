# Sources of Truth — Accessibility & Compliance Standards

**Load this reference at the first invocation of every session. Re-load whenever the user adds standards scope.**

This document is the hardcoded authority list. Every finding in a QC report must cite one of these with the specific section/SC number. Agents must never invent a standard or cite a section number they cannot reproduce from this list.

---

## 1. Web Content Accessibility Guidelines (WCAG) 2.2 AA

**Authority:** World Wide Web Consortium (W3C) Recommendation, October 5, 2023
**Official URL:** https://www.w3.org/TR/WCAG22/
**Quick reference:** https://www.w3.org/WAI/WCAG22/quickref/

**Four principles** — Perceivable, Operable, Understandable, Robust (POUR)

**AA-level Success Criteria** (this is the compliance target for History Hack):

### Perceivable
- 1.1.1 Non-text Content (A)
- 1.2.1–1.2.5 Captions, Audio Description, etc. (A/AA)
- 1.3.1 Info and Relationships (A)
- 1.3.2 Meaningful Sequence (A)
- 1.3.3 Sensory Characteristics (A)
- 1.3.4 Orientation (AA)
- 1.3.5 Identify Input Purpose (AA)
- 1.4.1 Use of Color (A)
- 1.4.2 Audio Control (A)
- 1.4.3 Contrast (Minimum) 4.5:1 text / 3:1 large text (AA)
- 1.4.4 Resize Text up to 200% (AA)
- 1.4.5 Images of Text (AA)
- 1.4.10 Reflow (AA)
- 1.4.11 Non-text Contrast 3:1 (AA)
- 1.4.12 Text Spacing (AA)
- 1.4.13 Content on Hover or Focus (AA)

### Operable
- 2.1.1 Keyboard (A)
- 2.1.2 No Keyboard Trap (A)
- 2.1.4 Character Key Shortcuts (A)
- 2.2.1 Timing Adjustable (A)
- 2.2.2 Pause, Stop, Hide (A)
- 2.3.1 Three Flashes or Below Threshold (A)
- 2.4.1 Bypass Blocks (A)
- 2.4.2 Page Titled (A)
- 2.4.3 Focus Order (A)
- 2.4.4 Link Purpose (In Context) (A)
- 2.4.5 Multiple Ways (AA)
- 2.4.6 Headings and Labels (AA)
- 2.4.7 Focus Visible (AA)
- 2.4.11 Focus Not Obscured (Minimum) (AA) — **new in 2.2**
- 2.5.1–2.5.4 Pointer Gestures, Cancellation, Labels, Motion Actuation (A)
- 2.5.7 Dragging Movements (AA) — **new in 2.2**
- 2.5.8 Target Size (Minimum) 24×24 CSS px (AA) — **new in 2.2**

### Understandable
- 3.1.1 Language of Page (A)
- 3.1.2 Language of Parts (AA)
- 3.2.1 On Focus (A)
- 3.2.2 On Input (A)
- 3.2.3 Consistent Navigation (AA)
- 3.2.4 Consistent Identification (AA)
- 3.2.6 Consistent Help (A) — **new in 2.2**
- 3.3.1 Error Identification (A)
- 3.3.2 Labels or Instructions (A)
- 3.3.3 Error Suggestion (AA)
- 3.3.4 Error Prevention (Legal, Financial, Data) (AA)
- 3.3.7 Redundant Entry (A) — **new in 2.2**
- 3.3.8 Accessible Authentication (Minimum) (AA) — **new in 2.2**

### Robust
- 4.1.1 Parsing (A) — removed in 2.2, do not cite
- 4.1.2 Name, Role, Value (A)
- 4.1.3 Status Messages (AA)

**Citation pattern:** "WCAG 2.2 SC 2.4.7 Focus Visible (AA)" — always include number, title, and level.

---

## 2. Section 508 (Revised, 2018)

**Authority:** U.S. Access Board, 36 CFR Part 1194
**Official URL:** https://www.access-board.gov/ict/
**Relationship to WCAG:** Section 508 incorporates WCAG 2.0 Level A and AA by reference (as of January 2018 revised standards). Updated to WCAG 2.1 in progress.

**Scope for History Hack:** Applies only when selling to federal agencies. For TN district sales, ADA Title II and state law govern. Keep Section 508 in scope for VPAT preparation (districts often request 508 compliance language even when not legally required).

**Key chapters:**
- E205 — Electronic Content (all public-facing content must be WCAG AA)
- E207 — Software
- E208 — Support Documentation and Services
- E209 — Real-Time Text

**Citation pattern:** "Section 508 E205.4" — reference the specific clause.

---

## 3. Americans with Disabilities Act (ADA) Title II

**Authority:** U.S. Department of Justice Final Rule, 28 CFR Part 35
**Rule published:** April 24, 2024 (89 FR 31320)
**Official URL:** https://www.ada.gov/resources/2024-03-08-web-rule/

**Compliance deadlines:**
- Large public entities (≥50,000 population): **April 26, 2026** — THIS IS ACTIVE NOW
- Smaller public entities (<50,000 population) and special districts: April 26, 2027

**Standard required:** WCAG 2.1 Level AA for web content and mobile apps of state/local government entities (including public school districts — WCS, MNPS, SCS).

**Application to History Hack:** When History Hack content is embedded in or linked from a WCS webpage or LMS, WCS's Title II compliance depends in part on the accessibility of the vendor content. Districts WILL ask vendors to attest that their product meets WCAG 2.1 AA (and increasingly 2.2 AA as the stricter recent standard).

**Citation pattern:** "ADA Title II — 28 CFR § 35.200 (2024 Final Rule)"

---

## 4. ISTE Standards

**Authority:** International Society for Technology in Education
**Official URL:** https://www.iste.org/standards

**Three relevant sets:**
- **ISTE Standards for Students** (2016, reaffirmed)
  - https://www.iste.org/standards/iste-standards-for-students
  - 7 standards: Empowered Learner, Digital Citizen, Knowledge Constructor, Innovative Designer, Computational Thinker, Creative Communicator, Global Collaborator
- **ISTE Standards for Educators** (2017)
  - https://www.iste.org/standards/iste-standards-for-teachers
  - 7 standards: Learner, Leader, Citizen, Collaborator, Designer, Facilitator, Analyst
- **ISTE Standards for Education Leaders / Coaches** (2019)

**Application:** ISTE is pedagogy/practice-oriented, NOT a conformance standard. In QC reports, cite ISTE only for alignment/quality claims (e.g., "supports ISTE Student Standard 3.b Knowledge Constructor") — never for WCAG/508/ADA compliance assertions. Confusing the two is a fabrication tripwire.

**Citation pattern:** "ISTE Standards for Students 3.b Knowledge Constructor"

---

## 5. CAST Universal Design for Learning (UDL) Guidelines 3.0

**Authority:** CAST (Center for Applied Special Technology)
**Release date:** July 30, 2024
**Official URL:** https://udlguidelines.cast.org/

**Three principles:**
1. **Design Multiple Means of Engagement** — the "Why" of learning
2. **Design Multiple Means of Representation** — the "What" of learning
3. **Design Multiple Means of Action and Expression** — the "How" of learning

**Each principle has three guidelines and multiple considerations.** Version 3.0 replaced the "checkpoint" language with "considerations" and reframed around barrier reduction and learner agency.

**Application:** UDL is framework, not compliance. Use it to describe content quality, not legal conformance. Pairs well with WIDA and ELPA21 for ELL content.

**Citation pattern:** "CAST UDL 3.0 — Guideline 2.1 Access (Representation)"

---

## 6. WIDA English Language Development Standards Framework

**Authority:** WIDA Consortium, University of Wisconsin-Madison
**Edition:** 2020 Edition (replaced 2012)
**Official URL:** https://wida.wisc.edu/teach/standards/eld
**Key document:** https://wida.wisc.edu/sites/default/files/resource/2020-WIDA-ELD-Standards-Framework-2020.pdf

**Five standards (ELD-SS = Social Studies):**
- ELD-SI (Social & Instructional Language)
- ELD-LA (Language Arts)
- ELD-MA (Mathematics)
- ELD-SC (Science)
- **ELD-SS (Social Studies)** ← primary for History Hack

**Four Key Language Uses:** Narrate, Inform, Explain, Argue
**Six proficiency levels:** Entering (1), Emerging (2), Developing (3), Expanding (4), Bridging (5), Reaching (6)

**Citation pattern:** "WIDA ELD-SS.9-12.Explain.Interpretive, Proficiency Level 3 (Developing)"

---

## 7. ELPA21 (English Language Proficiency Assessment for the 21st Century)

**Authority:** ELPA21 Consortium (hosted by CCSSO)
**Official URL:** https://elpa21.org/

**Use case in History Hack:** Tennessee uses WIDA (not ELPA21) for ELL identification/exit. ELPA21 descriptors are useful as a secondary reference for rubric design, especially when content will be used outside TN.

**Citation pattern:** "ELPA21 Proficiency Descriptors, Level 3"

---

## 8. Children's Online Privacy Protection Act (COPPA)

**Authority:** Federal Trade Commission, 16 CFR Part 312
**Most recent revision:** FTC Final Rule, January 2025 (amended data retention, parental consent mechanisms)
**Official URL:** https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy

**Scope:** Personal information from children under 13. History Hack users are high-school juniors (~16), generally outside COPPA's direct scope — BUT if any Middle School content or under-13 users exist, COPPA applies.

**Six key obligations (for audit purposes):**
1. Post a clear, comprehensive privacy policy
2. Provide direct notice to parents before collection
3. Obtain verifiable parental consent
4. Allow parents to review information collected
5. Reasonable procedures to protect data
6. Retain data only as long as necessary

**Citation pattern:** "COPPA 16 CFR § 312.5 (Parental Consent)"

---

## 9. Family Educational Rights and Privacy Act (FERPA)

**Authority:** 20 U.S.C. § 1232g; 34 CFR Part 99
**Official URL:** https://studentprivacy.ed.gov/ferpa

**Scope:** Education records of students. Applies to History Hack because districts share student data (roster, grades) with the platform.

**Key provisions:**
- § 99.31(a)(1) — School official exception (the primary basis for vendor data sharing)
- § 99.33 — Re-disclosure prohibition
- § 99.34 — Directory information exceptions

**Citation pattern:** "FERPA 34 CFR § 99.31(a)(1)(i)(B) (School Official)"

---

## 10. Children's Internet Protection Act (CIPA)

**Authority:** 47 U.S.C. § 254(h), (l)
**Official URL:** https://www.fcc.gov/consumers/guides/childrens-internet-protection-act

**Scope:** Applies to schools receiving E-Rate discounts. Requires internet safety policy, filtering, monitoring of minors' online activity.

**Relevance to History Hack:** Content must not contain images/material inappropriate for minors (obscene, harmful to minors, child pornography per CIPA's definition). Low risk for a U.S. History platform but audit-relevant when adding primary sources (some historical imagery — lynching photos, battlefield images — requires content warnings and instructional context).

**Citation pattern:** "CIPA 47 U.S.C. § 254(h)(5)(B)"

---

## 11. Tennessee Student Data Accessibility, Transparency, and Accountability Act

**Authority:** T.C.A. § 49-1-701 et seq.
**Official URL:** https://www.tn.gov/education/families/student-data-privacy.html

**Scope:** TN-specific; governs how districts and vendors handle TN student data. More restrictive than federal baseline in some areas (data residency, breach notification).

**Key provisions:**
- § 49-1-702 — Definitions (including "operator" and "covered information")
- § 49-1-703 — Prohibited activities (no targeted ads, no selling student data)
- § 49-1-704 — Data security requirements

**Citation pattern:** "T.C.A. § 49-1-704(a) (Data Security)"

---

## 12. TN Age-Appropriate Materials Act of 2022 (Public Chapter 744)

**Authority:** Public Chapter 744 (2022)
**Official URL:** https://publications.tnsosfiles.com/acts/112/pub/pc0744.pdf

**Scope:** Applies to instructional materials in TN public schools. Requires age-appropriate review of materials.

**Application to History Hack:** Content must be reviewed for age-appropriateness at the target grade band (11th grade U.S. History). Primary sources with mature content (slavery narratives, wartime imagery) require instructional framing.

**Citation pattern:** "TN Public Chapter 744 (2022)"

---

## 13. TDOE Textbook and Instructional Materials Quality Commission — Policy 2.600

**Authority:** Tennessee Department of Education, State Board Policy 2.600
**Official URL:** https://www.tn.gov/sbe/rules--policies-and-guidance/policies.html

**Scope:** Governs state adoption of instructional materials. Includes accessibility and UDL requirements in the Social Studies scoring rubric.

**Citation pattern:** "TDOE Policy 2.600, Social Studies Rubric Criterion [X]"

---

## Citation Cross-Check Rules

When a finding cites multiple standards (common — e.g., a missing label violates WCAG 1.3.1 AND Section 508 E205.4 AND ADA Title II):

1. Cite the **primary** standard (the one with the sharpest requirement)
2. List others as "Also cited under: …"
3. Do NOT double-count findings across standards — one violation, one finding, multiple citations

## Fabrication Tripwires (Standards Edition)

You WILL refuse to:

- Cite "WCAG 2.3" or any version that doesn't exist (current is 2.2; draft 3.0 is not cite-able)
- Cite a Success Criterion number without a matching title from the WCAG 2.2 list above
- Cite "Section 508 compliant" without naming the specific clause (E205, E207, etc.)
- Cite "ADA compliant" — ADA has Titles I–V; say "ADA Title II" or similar
- Cite ISTE as a compliance basis (ISTE is pedagogy, not law)
- Cite FERPA without naming the subsection (34 CFR Part 99, with § number)

If you are unsure which SC applies, cite "Unverified — specific WCAG SC needed" in the finding rather than guessing.
