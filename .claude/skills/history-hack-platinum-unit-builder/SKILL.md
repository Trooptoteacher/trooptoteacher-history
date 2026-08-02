---
name: history-hack-platinum-unit-builder
description: "Build or complete History Hack U.S. History Units 2 onward to the Platinum Standard (canonical exemplar: Unit 6, US.45–US.58). Use when asked to build a full unit, repeat the platinum workflow, consolidate existing curriculum assets, create editable Word and print-ready files, build guided Cornell notes with the four-rung supports ladder, align the teacher (lecture) and student (review) decks, connect a unit to the UDL lesson-package generator, prepare district-ready folders or ZIPs, or run Platinum QA. Enforces direct-file consolidation, UDL 3.0, WIDA, accessibility, bilingual supports, dark History Hack branding, one unit teacher deck, workbook↔deck DI-segment alignment, source integrity, the north-star decision rule, the lesson-flow and text-integrity QC gates, and gated approval before release."
license: Proprietary
compatibility: "Requires access to the History Hack web app repository and, when used, the user's Google Drive or file connector."
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "1.1"
---

# History Hack Platinum Unit Builder

## Purpose

Repeat the approved Unit 1 production system for every remaining History Hack U.S. History unit without recreating strong existing assets or introducing inconsistent structures.

The unit is a coordinated instructional product, not a loose collection of worksheets. Its authoritative components are:

1. Standards and assessment map
2. One complete teacher presentation
3. Editable Word instructional files
4. Print-ready PDF exports
5. UDL/WIDA/accessibility overlays built into instruction
6. Lesson-package generator entries backed by physical files
7. District-ready folder and download structure
8. Evidence-based Platinum QA

## North-Star Decision Rule (default every fork)

When any choice is ambiguous, default to **`history-hack-north-star`**, in order:

1. **100% standards alignment** — the deliverable teaches the verbatim current standard, fully.
2. **TDOE Schedule F** — score the choice against the adoption rubric; pick what scores higher.
3. **Best path to adoption** — among aligned, rubric-passing options, choose the one most likely to win district adoption.

**Accuracy is foundational (Policy 2.600):** factual/citation/standards accuracy is never traded away for any of the three. A choice that lowers accuracy is out, regardless of adoption appeal.

## Unit 6 Platinum Components (authoritative — proven on US.45–US.58)

These extend the eight components above and are **required** for a platinum unit. Full spec + engineering guardrails + sibling-skill links: **`references/unit-content-and-qc-integration.md`**. Reference/invoke the sibling skills named below — do not re-implement them.

- **Student Workbook — 7-activity spine + guided Cornell.** The Cornell notes are **keyed to the teacher deck's Direct-Instruction (DI) segments** — each notes block is captioned **`▶ Deck · DI k of M`** — and carry the **four-rung NOTES SUPPORTS ladder**: (1) frames → (2) cloze + word bank → (3) how-to + worked model → (4) try-it on ruled paper + self-check. **Notes on the recto, supports on the verso.** Built via **`history-hack-unit-content-build`** (engine `build_guided_notes.py`); do not hand-author the ruled notebook tables.
- **Aligned Teacher (lecture) + Student (review) decks.** **Vocabulary BEFORE instruction.** The student deck has **one review slide per teacher DI segment**, captioned **`US.xx · DI k of M`**. The **DI count matches across workbook, teacher deck, and student deck.** The teacher deck carries **`✍ In your workbook · <activity>`** write-cues, and per-standard slide blocks are **contiguous** (no interleaving).
- **Teacher Guide & MTSS, Teacher Answer Key, and a commercial-use-safe Visual Asset package.** Visual assets are **PD / US-gov / CC0 / CC-BY only**, each with a **citation sidecar + alt text**. **Never build political or boundary maps in-house** (accuracy + neutrality risk) — source them from an authoritative repository.

## When to Use

Use this skill when the user asks to:

- Build, complete, upgrade, or package a History Hack unit
- Create Units 2 onward using Unit 1 as the model
- Salvage and consolidate existing History Hack curriculum
- Prepare standard-specific MagicSchool worksheet prompts for genuine unit gaps
- Add a unit to the History Hack UDL lesson-package generator
- Produce district-ready unit folders or complete-unit ZIPs
- Audit a unit against the History Hack Platinum Standard
- Create missing student materials, teacher materials, assessments, exit tickets, primary-source materials, Cornell notes, or graphic organizers
- Build guided Cornell notes with the four-rung NOTES SUPPORTS ladder, or key the notes to the teacher deck's DI segments
- Align the teacher (lecture) and student (review) decks — DI-segment parity, vocab-before-instruction, workbook write-cues
- Assemble the commercial-use-safe visual asset package (licensing sidecar + alt text)
- Run the lesson-flow and text-integrity QC gates, or score a unit/section against Schedule F as-built

Do not use this skill for one isolated slide or document edit unless the user explicitly wants the entire unit workflow applied.

## Non-Negotiable Product Rules

- Never describe History Hack as a marketplace or third-party marketplace resource.
- Use the official History Hack emblem. Never invent a double-HH mark.
- Use the approved brand system: dark navy `#0A1F3C`, secondary navy `#143159`, and established red/gold accents.
- Produce one complete teacher deck per unit, stored once. Do not create redundant per-standard decks.
- Editable Word originals are authoritative. PDFs are print-ready delivery exports.
- Teacher lesson plans use landscape orientation.
- Consolidate physical files. Move approved assets into the unit structure; do not create shortcuts.
- Do not duplicate authoritative Word originals.
- Use HIPP for lesson-level source analysis. Reserve HIPPO for full DBQ work.
- Avoid “master” terminology. Use “editable Word original,” “source document,” or “authoritative original.”
- Treat factual accuracy, copyright/licensing, citations, accessibility, and standards alignment as release gates.
- Keep code changes on a draft branch/PR until the user approves release.
- Use the verified, verbatim standards data source. Never reconstruct standards from chat summaries.
- Preserve three approved schedule variants: 46-minute regular day, 43-minute activities schedule, and 41-minute late-start schedule.
- Protect the exit ticket in every schedule variant.
- Maintain English/Spanish parity for student-facing materials. Teacher planning artifacts remain English unless a Spanish teacher edition is separately commissioned.
- Use verbatim TDOE TEAM General Educator Rubric language when a section is labeled TEAM. Label content-mastery criteria separately.
- **Default every ambiguous fork to `history-hack-north-star`** (100% alignment → Schedule F → best path to adoption); accuracy (Policy 2.600) is foundational and never traded.
- **Vocabulary is taught before instruction** in the deck flow; the guided Cornell notes are **keyed to the teacher deck's DI segments** (`▶ Deck · DI k of M`), and the **DI count matches across workbook, teacher deck, and student deck**.
- **Guided notes ship the four-rung NOTES SUPPORTS ladder** (frames → cloze+word bank → how-to+model → try-it + self-check), notes recto / supports verso, built by `history-hack-unit-content-build` (`build_guided_notes.py`) — never hand-authored.
- **Visual assets are commercial-use-safe only** (PD / US-gov / CC0 / CC-BY) with a citation sidecar + alt text. **Never build political or boundary maps in-house.**
- **Engineering guardrails (see `references/unit-content-and-qc-integration.md`):** duplicate `.pptx` slides only with the `pptx` skill's `add_slide.py` — **never `python-pptx` `add_slide`** (it can orphan a slide part and corrupt the package on re-save); validate with a load/save round-trip dup check. Notebook paper is a **borderless table with a per-row bottom border**, and **exactly one `w:spacing` per paragraph**.

## Required Skill Composition

Before execution, load all applicable skills:

- `instructional-design-specialist`
- `udl-cast-expert`
- `ell-bilingual-review-specialist`
- `accessibility-qc-agent`
- `copyright-integrity-accreditation`
- `historian-factcheck-agent`
- `tn-textbook-adoption-agent`
- `history-hack-unit-qc`
- `office/docx`
- `office/pdf` when exporting PDFs
- `office/pptx` when creating or revising the unit deck
- `coding` and `website-building/webapp` when connecting the generator
- `gws-best-practices` when organizing or moving Google Drive files
- `history-hack-north-star` — the decision rule for every ambiguous fork
- `history-hack-unit-content-build` — builds the content JSON + guided notes (`build_guided_notes.py`)
- `history-hack-lesson-flow-qc` — workbook↔deck flow gate (release gate below)
- `history-hack-text-integrity-qc` — truncation/clipping/placeholder gate (release gate below)
- `pptx` — for all slide duplication (`add_slide.py`); never `python-pptx add_slide`

If a referenced sibling skill is not installed in the current environment, invoke it by name where available and note the gap in the completion report — do not re-implement its logic here.

For a full unit build, use parallel agents for independent audits or asset families when possible. Do not parallelize edits to the same authoritative file.

## Source-of-Truth Order

Use this precedence when materials conflict:

1. Approved current standards and user decisions
2. Current History Hack web app repository
3. Approved Unit 1 Platinum patterns
4. Existing History Hack Platinum-ready print folders and editable originals
5. Other existing History Hack assets
6. Newly created content

Never use the stale standalone textbook repository as the source of truth.

## Execution Workflow

Read `references/workflow.md` before starting a full unit.

### Intake Gate

Confirm:

- Target unit number and title
- Current standards and any future-standard crosswalk
- Existing unit assets and locations
- Approved deck or slide ranges, if they exist
- Whether the user wants audit-only, build, generator connection, or district release

If the user asks for a plan before work, present the action plan for approval and do not execute until approved.

### Audit Before Creation

Inventory all existing assets first. Search the web app, connected storage, Platinum-ready folders, worksheet libraries, and prior unit folders. Record each candidate as:

- Keep as authoritative
- Move and consolidate
- Revise
- Export only
- Archive
- Genuine gap
- Reject, with reason

Do not create a replacement until the audit proves the asset is missing or unusable.

### Build the Standards Spine

Create the unit standards map before materials:

- Standard ID and official text
- Learning target / “I can” statement
- Essential question
- Evidence of mastery
- Deck slide range
- Lesson sequence
- Primary source or stimulus
- Assessment coverage
- Vocabulary
- UDL/WIDA/accessibility supports
- Current-to-future standards crosswalk when applicable

Build the unit shell before individual lessons: unit overview, standards map, learning goals and success criteria, vocabulary spine, spaced review plan, assessment blueprint, differentiation plan, and geography only when the Social Studies Practice includes geographic reasoning.

Separate current standards from future standards visibly. Never mislabel one as the other.

### Complete Each Standard Package

Every standard should have the required physical, editable student and teacher files. Use the Unit 1 file-backed category model and only mark an item “Included” when the file exists and opens.

Use one repeatable lesson spine: what this is, objective and success criteria, instructional-design focus, SSP focus, vocabulary, content, retrieval practice, lesson sequence, assessment/deliverable, differentiation/supports, and downloadables.

At minimum, evaluate the need for:

- Landscape teacher lesson plan
- Guided notes
- Cornell notes
- Primary-source student handout
- Primary-source teacher guide
- HIPP organizer
- Vocabulary support
- Graphic organizer appropriate to the content
- Formative assessment student edition
- Formative assessment teacher key
- Exit ticket in English
- Exit ticket in Spanish
- Accommodation/differentiation support
- Extension or action/expression option

Do not force a redundant worksheet merely to hit a count. If a category is not instructionally appropriate, document the substitute and rationale.

### Prepare MagicSchool Drafting Prompts

When the user chooses to draft worksheets independently in MagicSchool, read `references/magic-school-prompt-workflow.md`.

Never give the user a blank prompt that asks them to locate or paste the standard. Each prompt must already contain:

- Verified standard ID and exact official wording
- Applicable Social Studies Practice code(s) and the skill students must demonstrate
- Student-facing learning target and success criteria
- Worksheet type and its instructional purpose
- Relevant UDL 3.0 design requirements
- MTSS tier and explicit scaffolds
- WIDA L1–2, L3–4, and L5–6 language supports
- Accessibility and English/Spanish parity requirements
- Required student edition, teacher key, and implementation note
- Fact, citation, copyright, and no-invention guardrails

Generate these prompts only for genuine gaps identified by the salvage audit. MagicSchool output is a draft source, never an authoritative standards or historical source.

### Apply UDL, WIDA, and Accessibility

UDL is embedded, not a decorative appendix:

- Engagement: choice, relevance, collaboration, goal clarity, and feedback
- Representation: readable text, visuals, vocabulary, bilingual support, chunking, audio/read-aloud options, and primary-language access
- Action and expression: writing, speaking, visual, organizer, and supported response options

Provide WIDA supports for L1–2, L3–4, and L5–6, including sentence frames and graduated language demands. Apply WCAG 2.2 AA, keyboard access, readable contrast, proper headings, alt text, and accessible document structure.

### Build or Correct the Unit Deck

Create one continuous teacher deck:

- Accurate standard dividers and lesson flow
- Correct slide references in lesson plans
- Direct instruction, primary sources, student practice, checks for understanding, and closure
- Speaker notes and teacher guidance where needed
- Citations and licensing information
- Official emblem and approved dark-blue brand system

Visually inspect every slide referenced by a lesson plan. A lesson plan may not cite a slide that lacks the named content.

### Connect the Lesson-Package Generator

Each selectable “Included” material must point to a real file. The generator must support:

- Current-lesson Word ZIP
- Complete-unit Word ZIP
- Selected merged PDF print package
- Separate complete teacher deck download
- Clear Included / Teacher-Implemented / External labels
- Progress, success, and error states

Worksheet records must retain approval state, student-visible status, version, and revision date. Existing approved student interactions must not disappear merely because folders or manifests are reorganized.

The complete-unit ZIP must contain:

```text
README.txt
US.xx/
  Student Materials/
  Teacher Materials/
...
Unit Presentation/
  History-Hack-Unit-N-Teacher-Deck.pptx
```

The deck appears exactly once. Verify counts, uniqueness, filenames, HTTP availability, and ZIP extraction.

### District Delivery

Follow `references/folder-architecture.md`. The district package must be understandable without the creator present, preserve editable originals, and avoid shortcuts or duplicate source documents.

### Platinum QA

Run `references/platinum-qa.md`. No unit is complete until all critical gates pass and every generator-backed file has been opened or programmatically validated.

**Hard release gates (all must pass — proven on Unit 6). Detail in `references/unit-content-and-qc-integration.md`:**

- **`history-hack-lesson-flow-qc` → 0 blocker / 0 major.** Produces the workbook→exact-slide matrix; verifies DI-segment parity across workbook/teacher/student and vocab-before-instruction.
- **`history-hack-text-integrity-qc` → 0 BLOCKER.** No truncated, clipped, or placeholder text anywhere; render-confirm every MAJOR.
- **Schedule F self-score, scored as-built, ≥ 80%** — per section **and** per unit (not a design-time estimate; score what actually renders).
- **Zero blank pages on every rendered PDF; notebook lines visible** on every ruled page.

These gates are release-blocking: a unit with any lesson-flow blocker/major, any text-integrity BLOCKER, a Schedule F section/unit under 80% as-built, a blank page, or invisible notebook lines is **not** platinum and does not ship.

## Status and Approval Gates

Use these gates:

1. **Audit approved**: salvage ledger and genuine gaps
2. **Standards spine approved**: map and lesson sequence
3. **Representative package approved**: one standard proves design and file model
4. **Full build complete**: all standards and files
5. **Generator QA complete**: current-lesson and complete-unit downloads
6. **District release approved**: final package ready to move or share

Do not merge a PR, publish publicly, or move district files into a live shared location without user approval.

## Completion Report

Report:

- Unit and standards completed
- Existing assets salvaged, moved, revised, archived, and newly created
- Physical file counts by DOCX, PDF, PPTX, and other types
- Student/teacher file counts
- Deck slide count and QA status
- Generator download counts and ZIP structure
- UDL/WIDA/accessibility coverage
- MagicSchool prompt packet and returned-draft status, when used
- Fact-check, citation, copyright, and standards-alignment status
- **Lesson-flow QC (blocker/major counts), text-integrity QC (BLOCKER count), Schedule F as-built score per section + unit, blank-page + notebook-line check, and DI-segment parity across workbook/teacher/student**
- Any referenced sibling skill that was unavailable in the environment
- Remaining blockers
- Draft PR or preview link, if applicable

Never report a material as complete because a manifest entry exists. Completion requires the physical file, correct connection, and successful validation.
