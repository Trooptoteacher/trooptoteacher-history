---
name: history-hack-platinum-unit-builder
description: "THE single orchestrator skill to build, rebuild, format, or fix a History Hack U.S. History 'Course Standard' (Platinum) unit — student workbook, teacher How-to-Use & MTSS guide, and platinum student/teacher slide decks — for ANY unit US.01–US.95 (canonical exemplar: Unit 6, US.45–US.58). Supersedes the standalone print 'history-hack-course-standard-builder,' absorbing its Unit 6 templating and print-formatting rules. Use when asked to 'build the Unit N workbook', 'match the Unit 6 format', 'make the docs look like Unit 6', 'rebuild the decks', 'the formatting is off / there's too much white space', 'the TOC is wrong', 'add the Cornell notes', 'answer key', 'de-bias the questions', or to build a full unit, repeat the platinum workflow, consolidate curriculum assets, create editable Word and print-ready files, build guided Cornell notes, ship the four-rung NOTES SUPPORTS ladder on the verso IN the student workbook, align the teacher (lecture) and student (review) decks by merging the UDL/supports layer into the authentic source decks, connect a unit to the UDL lesson-package generator, prepare district-ready folders or ZIPs, or run Platinum QA. This is the ORCHESTRATION layer: it INVOKES the standalone canonical skills — `history-hack-platinum-standard` (decision rule/mission), `history-hack-unit-content-build` (the 7-activity content engine + `build_guided_notes.py`), and the release-gate skills `history-hack-lesson-flow-qc` + `history-hack-text-integrity-qc` — rather than restating their logic. Enforces direct-file consolidation, UDL 3.0, WIDA, accessibility, bilingual supports, the America 250 brand palette, one unit teacher deck, workbook↔deck DI-segment alignment, source integrity, the Platinum decision rule, the lesson-flow and text-integrity release gates, and gated approval before release."
license: Proprietary
compatibility: "Requires access to the History Hack web app repository and, when used, the user's Google Drive or file connector."
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "2.0"
  reconciliation: "Canonical-set reconciliation: converted to a pure orchestrator — the decision rule (history-hack-platinum-standard), content engine (history-hack-unit-content-build), and release gates (history-hack-lesson-flow-qc, history-hack-text-integrity-qc) are now standalone skills it INVOKES, not inlined. NOTES SUPPORTS restored to the student-book verso (default-included). Brand migrated to the America 250 palette. Rebranded North-Star → Platinum. Retired-name pointers fixed (platinum-workbook → dbq-workbook; tcap-item-writer-v2 → tn-assessment-specialist)."
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
9. **Graphic-organizer toolkit** (built by `history-hack-graphic-organizer-workbook`)
10. **Unit poster pack / wall set** (built by `history-hack-poster-packet-builder`)

## Platinum Decision Rule (default every fork) — from the standalone `history-hack-platinum-standard` skill

Load **`history-hack-platinum-standard`** at the start of any build; it owns the mission, the Gold-vs-Platinum tier convention, and the future-ready principle. Its decision rule is the tie-breaker for every ambiguous fork, applied in order:

1. **100% standards alignment** — the deliverable teaches the verbatim current standard, fully; every activity resolves to an exact slide.
2. **TDOE Schedule F** — score the choice against the adoption rubric; pick what scores higher.
3. **Best path to adoption** — among aligned, rubric-passing options, choose the one most likely to win state/district adoption.

**Accuracy is foundational (Policy 2.600):** factual/citation/standards accuracy is never traded away for any of the three. A choice that lowers accuracy is out, regardless of adoption appeal. Do not restate the rule's internals here — it is a standalone skill; invoke it.

## Unit 6 Platinum Components (authoritative — proven on US.45–US.58)

These extend the eight components above and are **required** for a platinum unit. Two references carry the detail: **`references/unit-content-and-qc-integration.md`** (content-build spec + engineering guardrails + the release gates) and **`references/course-standard-format.md`** (the exact Unit 6 print/templating spec — design tokens, page structure, TOC bake, white-space audit, cover wraps, deck-merge pipeline, the standalone assessment book). Keep this section as decisions and pointers; the DETAIL lives in those two files.

- **Student Workbook — 7-activity spine + guided Cornell (built by `history-hack-unit-content-build`).** Each standard runs the established **7-activity page structure**; every activity **prints on its own page** so a teacher can print any one alone. The Cornell notes are **keyed to the teacher deck's Direct-Instruction (DI) segments** — each notes block is captioned **`▶ Deck · DI k of M`**. The **four-rung NOTES SUPPORTS ladder** — (1) frames → (2) cloze + word bank → (3) how-to + worked model → (4) try-it on ruled paper + self-check — **prints on the VERSO, IN the student workbook, default-included** (panel-locked decision: supports belong to the student for self-access; the "gate into the teacher pack" model is rejected). Scaffold **fading** (Guided → Light → Independent) is a *content property* that graduates across standards on the verso, never a relocation out of the book. A "lighter book" is delivered as a **print flag** (duplex = notes + supports; single-sided = notes only), not by removing supports. Build the content JSON + guided notes + verso supports with the engine `history-hack-unit-content-build` (`build_guided_notes.py`); do not hand-author the ruled notebook tables. Front/print spec: `00_START_HERE/STUDENT_WORKBOOK_PLATINUM_STANDARD.md` (§7.1 verso, §7.9 NOTES SUPPORTS) + `references/course-standard-format.md`.
- **Aligned Teacher (lecture) + Student (review) decks — MERGE, never author-from-scratch.** Both decks are produced by **merging the UDL/supports layer into the district's authentic source `.pptx` decks** (attached by the user or downloaded from Drive) — never generated from blank. The **one teacher deck per unit is the authentic source teacher deck with the layer merged in**; the student (review) deck is the same merge on the student layer. **Vocabulary BEFORE instruction.** The student deck has **one review slide per teacher DI segment**, captioned **`US.xx · DI k of M`**. The **DI count matches across workbook, teacher deck, and student deck.** The teacher deck carries **`✍ In your workbook · <activity>`** write-cues, and per-standard slide blocks are **contiguous** (no interleaving). Merge pipeline: `references/course-standard-format.md`.
- **Teacher Guide & MTSS, Teacher Answer Key, and a commercial-use-safe Visual Asset package.** Visual assets are **PD / US-gov / CC0 / CC-BY only**, each with a **citation sidecar + alt text**. **Never build political or boundary maps in-house** (accuracy + neutrality risk) — source them from an authoritative repository.
- **Graphic-organizer toolkit (REQUIRED — built by `history-hack-graphic-organizer-workbook`).** Real interactive organizers (Venn = actual overlapping circles, concept web, timeline spine, Frayer, CER boxes) — never a grid of ruled lines. **The layout parameters were hard-won and are LOCKED** — honor them exactly, never re-derive: the **Venn label rule** (region labels + in-lobe hints live INSIDE the `<svg>` at viewBox coordinates, anchored at lobe centers — for two circles at `cx 330/570 r 245`, ≈ `x 250` left / `650` right, lens ≈ `450`; drop wide captions ≈ 8–12% below the apex so they clear the arc; **never** HTML overlays over the circles), light/writable fields (labels dark, writing areas white/cream), fill-the-page-no-dead-space, US-Letter portrait. See `history-hack-graphic-organizer-workbook/references/guardrails.md` + `design-system.md` and the reference Venn packs in `assets/example_packs/`. Verify every label sits inside its shape **at render**.
- **Unit poster pack / wall set (REQUIRED — built by `history-hack-poster-packet-builder`).** 24×36 vector wall posters (Track A) + Letter station activities (Track B) + teacher guides + assembled bundle PDFs. **LOCKED layout constants** (hard-won — do not change): `PW,PH = 24×36 in`, outer frame `MAR = 0.75 in`, gold-hairline gap `FR = 0.20 in`, header band + chip geometry per `history-hack-poster-packet-builder/references/engine-reference.md`. Posters stay 24×36; margins/safe-area are non-negotiable so nothing clips at print.

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
- Use the **America 250 brand palette** — canonical tokens in `00_START_HERE/BRAND_PALETTE.md`: Heritage Blue `#1F3A5F` (structure), Patriot Red `#B22234` (emphasis), Founders Cream `#F8F5EF` (dominant field), Muted Gold `#C9A227` (sparingly). Use cream-dominant, blue-structure, red-emphasis, gold-sparingly. The legacy navies `#1B2A4A`, `#0A1F3C`, `#143159` and legacy gold `#C89B3C` are **retired** — do not introduce them.
- Produce one complete teacher deck per unit, stored once. Do not create redundant per-standard decks. That one teacher deck is the **authentic source teacher deck with the UDL/supports layer MERGED in** — decks are never authored from blank.
- **DOCX-native → PDF (LOCKED — print-first).** Author every document (workbook, teacher guide, answer key) as a **native `.docx`** with the docx engine (`build_guided_notes.py` / `build_teacher_guide.py` / `engine.js`), then convert to PDF with LibreOffice (`soffice --headless --convert-to pdf`). **Never generate the document as HTML and render it to PDF** — HTML→PDF mangles page breaks, headers/footers, and page numbers; native docx paginates correctly. Editable Word originals are authoritative; PDFs are a **faithful convert** of them — teachers get both. (24×36 posters are the only direct-vector exception; they are not documents.) See `00_START_HERE/BUILD_STANDARD.md` §4.
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
- **Default every ambiguous fork to the Platinum decision rule** (from the standalone `history-hack-platinum-standard` skill: 100% alignment → Schedule F → best path to adoption); accuracy (Policy 2.600) is foundational and never traded.
- **Vocabulary is taught before instruction** in the deck flow; the guided Cornell notes are **keyed to the teacher deck's DI segments** (`▶ Deck · DI k of M`), and the **DI count matches across workbook, teacher deck, and student deck**.
- **The four-rung NOTES SUPPORTS ladder prints on the VERSO, IN the student workbook, default-included** (panel-locked): frames → cloze+word bank → how-to+model → try-it + self-check, with scaffold **fading** (Guided → Light → Independent) as a content property across standards. The "gate the supports into the teacher pack" model is **rejected**. A lighter book is a **print flag** (duplex = notes+supports; single-sided = notes only), not a relocation. Workbook + verso supports are built by the standalone engine `history-hack-unit-content-build` (`build_guided_notes.py`) — never hand-authored.
- **Decks are MERGED, never authored from blank.** Both the student (review) and teacher (lecture) decks are the district's authentic source `.pptx` decks with the UDL/supports layer merged in.
- **Visual assets are commercial-use-safe only** (PD / US-gov / CC0 / CC-BY) with a citation sidecar + alt text. **Never build political or boundary maps in-house.**
- **Data charts & graphs — build them wherever the content warrants** (economic/demographic/electoral/production data). Original, accurate, generated from a **verified dataset** by `history-hack-unit-content-build`; each used as a read-the-data stimulus AND a student create/represent activity; each with a citation sidecar, alt text + data-table fallback, honest axes, grayscale-legible. Do not ration them — more real, relevant charts is better (STUDENT_WORKBOOK_PLATINUM_STANDARD §7.11). Large-format Data & Economics wall posters come from `history-hack-poster-packet-builder`.
- **Graphic organizers + poster pack are PART OF THE BUILD, not extras** — every unit ships the organizer toolkit (`history-hack-graphic-organizer-workbook`) and the poster/wall set (`history-hack-poster-packet-builder`). Their **layout, margin, and Venn parameters are LOCKED and hard-won** — honor the skills' own guardrails exactly (Venn labels inside the `<svg>` at viewBox coords, light writable fields, organizer fill-the-page; poster `MAR = 0.75 in` frame + `FR = 0.20 in` hairline gap on the 24×36 master). Never re-derive these by hand or "eyeball" a layout; regressions here were the most-flagged defects. Verify at render that no label drifts outside its Venn circle and nothing clips the poster margin.
- **Engineering guardrails (see `references/unit-content-and-qc-integration.md`):** duplicate `.pptx` slides only with the `pptx` skill's `add_slide.py` — **never `python-pptx` `add_slide`** (it can orphan a slide part and corrupt the package on re-save); validate with a load/save round-trip dup check. Notebook paper is a **borderless table with a per-row bottom border**, and **exactly one `w:spacing` per paragraph**.

## Required Skill Composition (this is an ORCHESTRATOR — invoke, never inline)

This skill is the orchestration layer. The mission/decision rule, the content engine, and the release gates are **standalone canonical skills with one owner each** — invoke them; do **not** restate or inline their logic. This is the anti-drift contract: a single owner per job means a fix to a gate or the engine propagates to every unit and every course automatically.

**Canonical core (always load — the spine of every build):**
- `history-hack-platinum-standard` — mission, Gold-vs-Platinum tier, future-ready principle, and the decision rule (the tie-breaker for every fork).
- `history-hack-unit-content-build` — the 7-activity content engine (`build_guided_notes.py`, verso NOTES SUPPORTS, deck-keying); it owns how the workbook and its companions are built.
- `history-hack-lesson-flow-qc` — release gate: workbook↔deck exact-slide alignment, DI parity, vocab-first (0 blocker / 0 major to ship).
- `history-hack-text-integrity-qc` — release gate: no truncated/clipped/placeholder text (0 BLOCKER to ship).

**Specialist skills (load when their scope is in play):**
- `instructional-design-specialist` · `udl-cast-expert` · `learning-experience-designer` (digital/app UX) · `ell-bilingual-review-specialist` · `accessibility-qc-agent` · `copyright-integrity-accreditation` · `historian-factcheck-agent` · `tn-textbook-adoption-agent` · `tn-assessment-specialist` (all assessment items; supersedes the retired tcap-item-writer-v2) · `spaced-repetition-engine` (spiral/retrieval scheduling) · `history-hack-unit-qc` (end-to-end QC workflow that **orchestrates** the gate skills above — it does not duplicate them).
- Deck generators: `history-hack-tcap-deck-builder` (teacher lecture deck) · `history-hack-lean-deck-builder` (student review deck).
- Toolkit builders (**required components of a full unit** — invoke, honor their locked layouts): `history-hack-graphic-organizer-workbook` (organizer toolkit; Venn/margin guardrails) · `history-hack-poster-packet-builder` (24×36 wall set + stations; `0.75 in` frame).
- `office/docx` · `office/pdf` (PDF export) · `office/pptx` and `pptx` (all slide duplication via `add_slide.py`; never `python-pptx add_slide`) · `coding` + `website-building/webapp` (generator) · `gws-best-practices` (Drive).

**Companion skills (reference when in scope):** `history-hack-print-qc-auditor` (print-defect audit; external plugin) · `history-hack-dbq-workbook` (standalone DBQ SKUs — a *different product*, not the Course Standard unit workbook).

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

### Build or Correct the Unit Deck (merge, never author-from-scratch)

The user attaches (or you download from Drive) the district's **authentic source `.pptx` decks** — the connector can't transfer the binary. Copy each to a read-only working copy, record its SHA-256, and **merge the UDL/supports layer into the working copy**; the source slides and images are never touched. The full merge pipeline (layer build → `deck_merge`, the Drive-image base64 trick, the per-standard map slide, de-bias sync, fixed-track-label strip, alt text, renumber) is in `references/course-standard-format.md`. The result is one continuous teacher deck that has:

- Accurate standard dividers and lesson flow (per-standard blocks contiguous)
- Correct slide references in lesson plans
- Direct instruction, primary sources, student practice, checks for understanding, and closure
- Speaker notes and teacher guidance where needed
- Citations and licensing information
- Official emblem and approved dark-blue brand system

Visually inspect every slide referenced by a lesson plan. A lesson plan may not cite a slide that lacks the named content.

### Build the Graphic-Organizer Toolkit and Poster Pack (part of every unit)

Invoke `history-hack-graphic-organizer-workbook` to produce the unit's organizer toolkit and `history-hack-poster-packet-builder` to produce the 24×36 wall set + station packets. **Do not re-implement or eyeball these layouts** — the two skills own hard-won, LOCKED parameters (Venn viewBox label rule, light writable fields, poster `0.75 in` frame / `0.20 in` hairline gap on the 24×36 master). Run each skill's own render check and confirm at the pixel level: no Venn label outside its circle, no dark bar under a writing field, organizers fill the page, and nothing clips a poster margin. These pieces belong in the unit's district-ready folder alongside the workbook and decks.

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

**Hard release gates (all must pass — proven on Unit 6). Each is a STANDALONE skill this orchestrator invokes — never an inlined copy. Engineering detail in `references/unit-content-and-qc-integration.md`:**

- **`history-hack-lesson-flow-qc` → 0 blocker / 0 major.** Produces the workbook→exact-slide matrix; verifies DI-segment parity across workbook/teacher/student and vocab-before-instruction.
- **`history-hack-text-integrity-qc` → 0 BLOCKER.** No truncated, clipped, or placeholder text anywhere; render-confirm every MAJOR.
- **Schedule F self-score, scored as-built, ≥ 80%** — per section **and** per unit (not a design-time estimate; score what actually renders).
- **Zero blank pages on every rendered PDF; notebook lines visible** on every ruled page.
- **Organizer & poster layout gate (render-confirmed).** Every graphic organizer and poster is rendered and inspected: **no Venn label outside its circle**, writable fields light (never a dark bar under writing), organizers fill the page (no dead space), and every 24×36 poster holds the `0.75 in` frame with nothing clipping the margin/safe-area. Honor `history-hack-graphic-organizer-workbook` and `history-hack-poster-packet-builder` guardrails — a layout regression here does not ship.

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
- **Lesson-flow gate (blocker/major counts), text-integrity gate (BLOCKER count), Schedule F as-built score per section + unit, blank-page + notebook-line check, and DI-segment parity across workbook/teacher/student**
- **Graphic-organizer toolkit + poster pack: piece counts, and the layout gate result** (Venn labels inside circles, light writable fields, no dead space; posters hold the `0.75 in` frame with no margin clip)
- Any companion skill (e.g. `history-hack-print-qc-auditor`) whose scope was in play but was unavailable in the environment
- Remaining blockers
- Draft PR or preview link, if applicable

Never report a material as complete because a manifest entry exists. Completion requires the physical file, correct connection, and successful validation.
