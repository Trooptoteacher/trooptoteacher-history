# Administrative Review — Living Compliance Checklist

**Product:** U.S. History Hack™ · TroopToTeacher Technologies, LLC
**Purpose:** A recurring administrative review to confirm that everything which
*changes often* is still current, published, and accurately reflected in our
materials and product. This is the master list the scheduled review runs against.

> **How to use:** On each review, work top to bottom. For every row, check the
> authoritative source, compare to what we ship, and set **Status** to ✅ current,
> ⚠️ changed–needs update, or ⛔ out of date. Log the date in **Last reviewed**
> and set **Next due**. Record findings in the Review Log at the bottom.

**Recommended cadence:** Quarterly — **August, November, February, May** —
aligned to the school year and the Tennessee legislative calendar. The **May**
review is the heavy one: TN laws passed in the winter/spring session typically
take effect **July 1**, so catch them before the new school year.

---

## 1. Tennessee Academic Standards (US.01–US.95)

| Check | Authoritative source | Cadence | Owner |
|---|---|---|---|
| Are the U.S. History standards still in their current adopted version? Any revision/errata published? | TDOE Academic Standards (Social Studies) | Quarterly | Curriculum |
| Standards **revision cycle** status — is U.S. History up for review this cycle? | TN State Board of Education standards review schedule | Annually (spring) | Curriculum |
| Does our per-standard text (workbooks, decks, alignment JSON) match the official wording verbatim? | Official standards PDF vs. `05_STANDARDS_ALIGNMENT/` + `build_unit*/unit*_content.json` | Quarterly | Curriculum |

**Where it lives in our repo:** `05_STANDARDS_ALIGNMENT/`, each unit's
`*_content.json` (`tn`, `criteria`, `std_source` fields), lesson-plan generator.

## 2. TDOE Alignment & Assessment Blueprints

| Check | Authoritative source | Cadence | Owner |
|---|---|---|---|
| TCAP / U.S. History **EOC blueprint** unchanged (item counts, reporting categories, weighting)? | TDOE Assessment — EOC blueprints | Annually (summer) | Assessment |
| **Textbook/instructional-materials adoption** cycle — is Social Studies in the adoption window? Any new submission requirements? | TN Textbook & Instructional Materials Quality Commission | Annually | Leadership |
| Approved-standards codes we cite (US.01–US.95) still valid — none renumbered/retired? | TDOE standards | Quarterly | Curriculum |

**Where it lives:** assessment builds (`04_ASSESSMENTS/`, `build_unit*/*_assessment.json`),
`tn-textbook-adoption-agent` skill, Schedule F docs in `06_COMPLIANCE_INTERNAL/`.

## 3. Use of AI — Disclosures & Policy

| Check | Authoritative source | Cadence | Owner |
|---|---|---|---|
| **TDOE / State Board AI guidance** for schools — any new or updated guidance we must reflect? | TDOE AI guidance for Tennessee schools | Quarterly | Leadership |
| Our **AI-use disclosures** are accurate: which tools generate what (e.g., image generation vs. text), and where AI is used vs. human-authored. | `08_DISTRICT_REFERENCE/District-AI-Disclosure-Correction-Notice.*`, product AI disclosures | Quarterly | Leadership |
| **AI-generated avatars / images** remain paused/default-off per district decision; disclosures match the shipped state. | Product flags + disclosure docs | Quarterly | Product |
| Narrative textbook: **historian/SME accuracy review** report is current and **attached with the book**. | Review report artifact (attach to book) | On content change | Curriculum |

**Where it lives:** `06_COMPLIANCE_INTERNAL/History-Hack-TN-Compliance-Matrix.*`,
`08_DISTRICT_REFERENCE/District-AI-Disclosure-Correction-Notice.*`.

## 4. New Laws (Tennessee & Federal)

| Check | Authoritative source | Cadence | Owner |
|---|---|---|---|
| **New TN laws** from the most recent General Assembly session affecting education technology, curriculum, student data, or AI (most take effect **July 1**). | TN General Assembly — enacted public chapters | **May** (pre-July-1) + Feb (session open) | Leadership |
| **Student data privacy** — TN Student Data Accountability, Transparency and Security ("Data Act") and any amendments. | TN Code + TDOE | Annually | Legal |
| **Federal** — FERPA / COPPA unchanged; any new FTC/ED guidance (esp. ed-tech + AI). | ed.gov / FTC | Annually | Legal |
| **Age-appropriate design / minors' online safety** obligations that reach classroom software. | TN Code + federal | Annually | Legal |

**Where it lives:** `06_COMPLIANCE_INTERNAL/History-Hack-TN-Compliance-Matrix.*`
(TN technology-law matrix), `copyright-integrity-accreditation` skill.

## 5. Legal Review — IP, Privacy, Terms, Licensing

| Check | Authoritative source | Cadence | Owner |
|---|---|---|---|
| **Copyright / IP** — all third-party sources (images, primary sources, quotes) cleared or public-domain; attributions present. | `copyright-integrity-accreditation` skill audit | Annually + on new content | Legal |
| **FERPA / COPPA** posture for any student-data handling still accurate. | Privacy policy vs. product | Annually | Legal |
| **Terms of Service / EULA / copyright notices** current (year, entity name "TroopToTeacher Technologies, LLC", product marks). | Shipped docs + product footers | Annually | Legal |
| **Open-source licenses** for dependencies reviewed; no license conflicts. | Dependency license scan | Annually | Engineering |

**Where it lives:** `copyright-integrity-accreditation` skill,
`06_COMPLIANCE_INTERNAL/`, product footers/EULA.

---

## Scope note

Most of this should **not** change in a given quarter. The three areas most
likely to move — and worth the closest look each cycle — are:

1. **Standards** (revisions, renumbering, blueprint changes),
2. **Use of AI** (fast-moving state guidance + our disclosures staying accurate),
3. **New laws** (TN session → July 1 effective dates).

Everything else is a lighter confirm-still-true pass.

---

## Review Log

| Date | Reviewer | Areas checked | Findings / actions | Next due |
|---|---|---|---|---|
| 2026-08-01 | (initial) | Doc created; §3 AI disclosures corrected (OpenAI = images, not text); TN tech-law matrix shipped. | Baseline established. | 2026-11 |

---
© 2026 TroopToTeacher Technologies, LLC · U.S. History Hack™ · Internal compliance document.
