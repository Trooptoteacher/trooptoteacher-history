# Content Audit Checklist — Printables, PDFs, Question Items, Bilingual

**Load this reference when `artifact_type: printable | question-item | narrative | bilingual-pair`.**

History Hack content artifacts serve teachers and students directly — printables handed out in classrooms, question items in high-stakes practice tests, narrative text in textbook-style readings, bilingual pairs for Spanish-dominant English Learners. These artifacts face TDOE Textbook Commission review and district vetting.

---

## Section A — Printables (HTML/PDF documents)

Apply when artifact_type is `printable` or a PDF document.

### A-1 Structural Accessibility

| ID | Criterion | Evidence required |
|---|---|---|
| PR-01 | PDF is tagged (not image-only) | Tags present in PDF structure tree |
| PR-02 | Document has a title in metadata (2.4.2 Page Titled, A) | `<title>` in HTML head; Title property in PDF |
| PR-03 | Language set at document level (3.1.1) | `lang` attribute or PDF /Lang entry |
| PR-04 | Headings use real heading markup (1.3.1) | `<h1>`-`<h6>` in HTML; H1-H6 tags in PDF |
| PR-05 | Heading hierarchy valid, no skips (1.3.1) | Read order H1 → H2 → H3 |
| PR-06 | Logical reading order matches visual order (1.3.2 Meaningful Sequence, A) | Tab order + screen reader order traced |
| PR-07 | Lists use list markup (1.3.1) | `<ul>/<ol>` or LI tags in PDF |
| PR-08 | Tables have proper headers and scope (1.3.1) | `<th scope>` or Table Header cells |
| PR-09 | Decorative images marked as artifacts (1.1.1) | Empty alt / Artifact role |
| PR-10 | Informative images have alt text (1.1.1) | Non-empty alt; describes content AND purpose |

### A-2 Print Behavior (History Hack specific, from April 2 QC experience)

| ID | Criterion | Evidence required |
|---|---|---|
| PR-11 | No `overflow: hidden` clipping content in print | CSS inspection; print preview check |
| PR-12 | No sticky/fixed elements appearing on printed page | `@media print { .sticky { position: static; } }` |
| PR-13 | No hidden tabs/panels printing unexpectedly | `@media print { .hidden-tab { display: none; } }` |
| PR-14 | Tables don't split mid-row | `page-break-inside: avoid` on `<tr>` |
| PR-15 | No ASCII art / fake lines — real `<hr>` or borders | Real HTML elements |
| PR-16 | Writing spaces sized for real student use | Minimum 0.5" per answer line; 0.75" preferred |
| PR-17 | Dark fills only where intentional (ink cost) | Headers have ≤15% fill; body has none |
| PR-18 | Page numbers present on multi-page documents | Footer with "Page X of Y" |
| PR-19 | Page breaks intentional, not orphaned headings | `page-break-after: avoid` on headings |
| PR-20 | Print margins ≥ 0.5" all sides | `@page { margin: 0.5in }` minimum |

### A-3 Color / Contrast for Print + Screen

| ID | Criterion | Evidence required |
|---|---|---|
| PR-21 | Text contrast ≥ 4.5:1 on screen (1.4.3, AA) | Measured ratio |
| PR-22 | Content legible when printed grayscale | Color-to-grayscale simulation |
| PR-23 | Information not conveyed by color alone (1.4.1, A) | Labels/patterns/icons in addition to color |

### A-4 Typography and Readability

| ID | Criterion | Evidence required |
|---|---|---|
| PR-24 | Body text ≥ 11pt for print | Font-size CSS |
| PR-25 | Line height ≥ 1.4x font size | line-height CSS |
| PR-26 | Line length 45-80 characters preferred | max-width or column width |
| PR-27 | Dyslexic-friendly fonts available for student-facing (optional — Lexend, Atkinson, OpenDyslexic) | Referenced from Reading Preferences panel (PR #40) |

---

## Section B — Question Items (Assessment Bank)

Apply when artifact_type is `question-item`. This builds on the `tn-assessment-specialist` user skill (which supersedes the retired `tcap-item-writer-v2`) but focuses on accessibility-specific concerns.

### B-1 Stem + Option Accessibility

| ID | Criterion | Evidence required |
|---|---|---|
| QI-01 | Stem is a complete question or completion prompt (TCAP convention) | Direct quote; no sentence fragments |
| QI-02 | No "All of the above" / "None of the above" | Stem + options inspection |
| QI-03 | Options are parallel in structure and length | Side-by-side quote |
| QI-04 | No cultural, gender, socioeconomic bias | Bias flag in item metadata |
| QI-05 | Reading level appropriate to grade 11 (6th-9th grade Lexile) | Lexile score on file |
| QI-06 | Primary sources with archaic language have footnoted simplifications | Footnote present and linguistically accurate |
| QI-07 | No duplicate or near-identical options | Text diff of options |
| QI-08 | No truncated text (historic issue from April 12 audit) | Full sentence review |

### B-2 Item-Level Accessibility Metadata

| ID | Criterion | Evidence required |
|---|---|---|
| QI-09 | DOK level correctly tagged (matches cognitive demand) | Hess CRM verification if available |
| QI-10 | Standard code is a valid US.01-US.95 | Cross-reference TN standards file |
| QI-11 | Item type tag is TCAP-allowed (MC, MS, TE only for state test) | Metadata check |
| QI-12 | Distractor tags present (PK / MC / PE / NE) | Distractor metadata complete |
| QI-13 | Evidence citation present (primary source URL or textbook page) | URL resolves; page number valid |
| QI-14 | Bilingual/Spanish version linked if available | Metadata field + file exists |
| QI-15 | Read-aloud TTS compatible (no image-only stems) | Text can be extracted without OCR |

---

## Section C — Narrative Text Pages

Apply when artifact_type is `narrative`.

| ID | Criterion | Evidence required |
|---|---|---|
| N-01 | Reading level calibrated to grade 11 (Lexile 1050-1335) | Lexile analyzer output |
| N-02 | Tier 3 vocabulary footnoted or defined inline | First use definitions present |
| N-03 | Text chunks ≤ 250 words per section (Mayer multimedia) | Section count + word count |
| N-04 | Headings every ≤ 300 words | Heading density check |
| N-05 | Primary sources quoted verbatim with citation | Source URL + accuracy check |
| N-06 | Claims sourced (no fabricated history, no presentism without note) | Citation per contested claim |
| N-07 | Content age-appropriate under TN Public Chapter 744 | Mature content flagged and contextualized |
| N-08 | UDL multiple means of representation (CAST UDL 2.x) | Text + image + (optional) audio |
| N-09 | WIDA ELD scaffolding present (proficiency levels 2-4 supported) | Scaffolding cues (glossary, sentence frames) |

---

## Section D — Bilingual Pairs (EN/ES)

Apply when artifact_type is `bilingual-pair`. These are the hardest audits — both languages must pass independently AND together.

### D-1 Translation Fidelity

| ID | Criterion | Evidence required |
|---|---|---|
| BI-01 | Spanish version conveys same content, same standard alignment | Side-by-side semantic comparison |
| BI-02 | Spanish reading level appropriate (WIDA ELD Level 3+ accessible) | Vocabulary analysis |
| BI-03 | Primary source terms translated with historical accuracy | Domain-expert check (e.g., "Jim Crow" context-preserved) |
| BI-04 | Simplified definitions provided for Tier 3 terms in Spanish | Glossary present |
| BI-05 | No machine-translation artifacts (wrong verb tense, false cognates) | Native-speaker review indicator |
| BI-06 | Cultural context preserved across both versions | Named examples appropriate in both |

### D-2 Technical Bilingual Accessibility

| ID | Criterion | Evidence required |
|---|---|---|
| BI-07 | `<html lang>` updates when user toggles to Spanish (3.1.1) | Code verification from History Hack app |
| BI-08 | Language of parts marked when mixing EN/ES (3.1.2, AA) | `<span lang="es">` or `<span lang="en">` on mixed segments |
| BI-09 | TTS pronunciation correct in target language | Voice selection matches language tag |
| BI-10 | Spanish translation has its own primary-source pairings (not shared from English) | Separate source cards |
| BI-11 | Both versions have same scaffolding types | Parallel supports across languages |

### D-3 WIDA ELD Standards Alignment

| ID | Criterion | Evidence required |
|---|---|---|
| BI-12 | Content aligns to ELD-SS (Social Studies) standard | Crosswalk present |
| BI-13 | Key Language Uses (Narrate/Inform/Explain/Argue) identified | Metadata field |
| BI-14 | Scaffolds for Proficiency Levels 2-4 at minimum | Level tag on each scaffold |

---

## Severity Rubric for Content

| Severity | Example | Submission impact |
|---|---|---|
| **Critical** | Fabricated historical fact; untagged PDF; missing primary source citation; untranslated Spanish version that claims to be complete | Blocks district + TDOE submission |
| **High** | Missing alt text on informative image; heading skip; contrast failure; missing Spanish scaffolds at proficiency level 3 | Blocks TDOE submission |
| **Medium** | Suboptimal line length; missing Lexile tag; UDL representation gap | Non-blocking |
| **Low** | Typography polish; icon inconsistency | Non-blocking |

---

## Finding Template (for Content)

```markdown
### Finding [seq] — [short title]

**Severity:** Critical / High / Medium / Low
**Standard(s):** [Primary: WCAG / Section 508 / ADA Title II / UDL / WIDA / TDOE 2.600 / TN Public Chapter 744]
**Location:** [File path / printable name] [Page N] [Item ID]
**Evidence:**
> [exact quoted content]
**Finding:** [what is wrong, plain language]
**User impact:** [who is affected — ELL students, screen reader users, teachers printing the packet, etc.]
**Remediation:** [specific fix]
**Estimated effort:** [S / M / L]
```

---

## Printable-Specific Pre-Audit Checks

Before auditing any printable, verify:

- [ ] The file is readable (PDF tags visible; HTML opens without error)
- [ ] You know the intended print size (US Letter default; some packets are legal or tabloid)
- [ ] You know the grade band and content unit
- [ ] Simulate browser print preview mentally — what will actually appear on paper?

If the printable is HTML with `@media print` styles, verify BOTH screen AND print layouts. The April 2 QC audit exposed that printables can look fine on screen but clip content, split tables, or waste ink on paper.

---

## Question Item Batch Rules

- Default batch: 25 items per session
- Items must belong to the same Unit (prevents cross-unit contamination)
- Items must be from the same DOK band OR explicitly mixed (flag if mixed — harder to batch-review consistently)
- For Tennessee standards, always cross-reference US.01-US.95 codes

Reference the April 12 QC defect pattern:
- Cross-contaminated distractors (98 flags across one unit)
- Wrong unit placement (64 flags)
- Near-identical options, truncated text, boilerplate explanations

These patterns should appear in finding categories if the item bank hasn't been re-audited post-remediation.
