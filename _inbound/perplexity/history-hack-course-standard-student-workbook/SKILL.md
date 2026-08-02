---
name: history-hack-course-standard-student-workbook
description: "Build History Hack Course Standard UDL/MTSS student workbooks and teacher implementation guides. Use for full standards-based unit workbooks, universal Cornell notes aligned to Lean student decks, legacy Base/Support/EL/Modified/Honors consolidation, canonical question-bank assessment integration, editable DOCX/PDF production, MTSS decision guidance, and Unit 8-style course workbook builds. Do not use for standalone DBQ or primary-source packet SKUs."
license: MIT
metadata:
  author: TroopToTeacher Technologies LLC
  version: '1.0'
  canonical_template: Unit 8 Course Standard UDL-MTSS Workbook
  source_of_truth_repo: https://github.com/Trooptoteacher/History-Hack-US-History-Workbooks
---

# History Hack Course Standard Student Workbook Builder

This skill builds the full Course Standard UDL/MTSS student-workbook product. Unit 8, “A Nation in Transition, 1950s–1963,” is the reference implementation.

## Product Boundary Gate (LOCKED)

- **This skill owns:** standards-based lesson sequences, universal Cornell notes, optional Guided and Light support backs, close reads, vocabulary work, primary-source analysis within lessons, application tasks, progress checks, canonical assessments, editable DOCX/PDF student books, and the teacher How-to-Use and MTSS guide.
- **This skill excludes:** standalone DBQ packages, a single investigation question with a curated DBQ document set, DBQ essay-only products, DBQ language-access companions, and standalone DBQ pricing/packaging.
- Primary sources may appear within Course Standard lessons, and a Course Standard workbook may link to a separate DBQ. It must not absorb the DBQ package or market itself as the DBQ SKU.
- If the user requests a standalone DBQ, primary-source packet, HIPPO/OPTIC document investigation, DBQ teacher scoring guide, or DBQ language companion, stop and load `history-hack-platinum-workbook`.

## Product Model

- Produce one common Course Standard workbook, not fixed Base, Support, EL, Modified, and Honors student tracks.
- Hold Tennessee standards, historical reasoning, and the mastery ceiling firm. Vary access, practice, language, and expression.
- Preserve useful legacy content as universally available options.
- Use student-facing labels: `CORE PATH`, `SUPPORT OPTION`, `LANGUAGE SUPPORT`, `RESPONSE CHOICE`, `PROGRESS CHECK`, and `EXTENSION`.
- Never label students by MTSS tier.
- State that supports work alongside, never in place of, required IEP/504 accommodations.

## Word-First Production Rule (LOCKED)

- The editable DOCX is the source of truth.
- Author semantically with real headings, editable tables, repeated non-splitting table headers, image alt text, hyperlinks, live page fields, and an updateable TOC.
- Convert DOCX to PDF automatically with LibreOffice.
- Inspect the DOCX-rendered PDF as the print master.
- Revise the DOCX, regenerate the PDF, and rerun QA after every substantive change.
- Deliver student DOCX/PDF, teacher DOCX/PDF, build/QA report, and assessment audit.

## Drive-First Gate

Before web sourcing, search Google Drive for the unit standards, citations, images, Lean student deck, Full Teacher Deck, existing workbooks, canonical assessments, and DBQ resources. Reuse verified material and document web gap-fills.

## Required Opening Blurb

> This workbook is designed for learner variability. Every student works toward the same Tennessee standards, while the workbook offers flexible ways to engage with content, understand information, and show learning. Look for Core Path, Support Option, Language Support, Response Choice, Progress Check, and Extension labels. These options are available by design; they support access without lowering the learning goal.
>
> Within an MTSS framework, Core Path materials support whole-class instruction, Support Options provide targeted practice, and Progress Checks help teachers decide when additional instruction or extension is needed.

## Front Matter

1. Cover with U.S. History Hack™, unit title, Course Standard Edition, Tennessee Connection, and ISBN `[to be assigned]`.
2. Copyright and public-domain/open-license statement.
3. Updateable table of contents.
4. Tennessee standards and SSP crosswalk with honest Full/Context labels.
5. Accessibility, UDL, MTSS, language-support, and accommodations matrix.
6. Student How-to-Use page with the required blurb and label legend.

UDL must be visible in the body, not merely claimed in front matter.

## Standard Lesson Sequence

For each Tennessee content standard:

1. Standard opener and learning target.
2. Direct Teaching Cornell Notes aligned to the verified Lean student deck.
3. Close Read.
4. Vocabulary Reference / Word Bank.
5. Vocabulary Studio.
6. Standalone primary-source or data analysis with HIPPO for text and OPTIC for visual sources.
7. Core application, response choice, progress check, and optional extension.
8. Canonical formative assessment and safe support form.

## Cornell Notes Contract

### Universal front

- Same front for every student, with no tier label.
- Include name/class/date, standard, verified Lean slide range, stable lesson identifier, learning target, essential question, 25/75 cue-to-notes layout, three or four cues, key-term strip, summary, and progress check.
- Never guess slide references or substitute Full Teacher Deck numbers.

### Optional backs

Sequence `Universal Front → Guided Support Back → Light Support Back` so teachers can choose duplex ranges.

- **Front only:** independent notes.
- **Front + Light Back:** vocabulary hints and guiding questions without full frames.
- **Front + Guided Back:** definitions, verified Spanish translations/cognates, chunking prompts, one frame, and one model.

### Fading

- Fade from Guided to Light to Front only based on student evidence.
- Reintroduce support for a new barrier.
- Legally required IEP/504 accommodations do not fade unless the authorized team changes them.
- Fade temporary scaffolds, not access tools or the learning goal.

## Teacher Guide

Create a concise implementation guide, not a duplicate student book. Include firm goals/flexible means, label-to-action table, print ranges, Cornell duplex options, evidence-based fading, Tier 1/2/3 guidance, the teach-check-barrier-support-reteach/check cycle, Lean-to-Full deck crosswalk, response-mode validity, reduced-choice guardrails, and CAST UDL 3.0 connections.

## Assessment Integration

- Use the canonical History Hack web-app question bank, not legacy hardcoded quiz tuples.
- Audit actual items, not manifest counts.
- Verify stem, options, explanation, standard, DOK, and content alignment.
- Preserve canonical IDs, metadata, option order, and answer keys unless a governed bank revision authorizes changes.
- A two-choice support form must contain the correct answer plus one strong distractor, then be relettered A/B.
- Include teacher keys, rationales, and rubrics.
- Never invent field-test, bias, Bloom, Hess, or C3 metadata.
- Mark DBQ/extended-response items classroom-only when they are not TCAP-format.

## Print and Layout Contract

- Student workbook target: no more than 120 rendered pages.
- Body at least 10.5 pt, preferably 11 pt; tables at least 9.5 pt.
- Grayscale-legible and not color-dependent.
- Keep headings with content, stems with options, Cornell rows together, and short tables/rubrics intact.
- No sparse carryovers, orphaned headings, detached options, or isolated table fragments.
- Intentional workspace must have a visible purpose.

## Mandatory QA

- Inspect the DOCX-rendered PDF and any retained native PDF.
- Verify page count, placeholders, TOC, crosswalk references, hyperlinks, and source attribution.
- Run a full-document sparse-page scan and visually inspect every flag.
- Inspect all Cornell fronts/backs and each following page.
- Inspect every image page for caption, task, historical subject, and medium accuracy.
- Verify HIPPO/OPTIC correctness and scan for tofu glyphs.
- Cross-check assessment IDs, answer keys, DOK, and support forms between student and teacher files.
- Confirm UDL/MTSS labels, opening blurb, teacher decision cycle, and IEP/504 guardrail.
- Record page counts, fixes, limitations, and acceptance status in the final QA report.

## Drive Filing

Store Course Standard workbooks in a dedicated sibling folder, never inside a unit’s `01_DBQ_Workbook` folder. Update stable filenames in place on revision.
