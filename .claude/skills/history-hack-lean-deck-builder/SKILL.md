---
name: history-hack-lean-deck-builder
description: "Builds the lean, student-facing History Hack deck (PowerPoint .pptx) for any unit, plus its matching printable Teacher Answer Key (PDF), web viewer manifest, and Usage Guide. **Course-parameterized** via `courses/<id>/course.json` — U.S. History (TCAP EOC) is the reference/default; also builds World History (W.01–W.89) and other editions as benchmark student decks with identical layout and rigor (footer/check labels derived from the course, not hardcoded 'TCAP EOC'). Assertion-evidence layout: a bold assertion headline (a summary-label of the LOCKED curriculum narrative — never new narrative) over a large public-domain evidence image, with Source It First WHO/WHEN/WHY sourcing bands and the fixed Three Perspectives synthesis (Who benefited? / Who bore the costs? / Who decided?). Sibling to history-hack-tcap-deck-builder (the full teacher deck). Use when asked to build/regenerate the lean deck, lean student deck, or assertion-evidence deck for a History Hack unit, or its lean answer key or manifest."
license: "Proprietary — © 2026 TroopToTeacher Technologies LLC. All rights reserved."
metadata:
  author: TroopToTeacher Technologies LLC
  version: '1.1'
  changelog_1_1: "Course-parameterized. Resolves a course config from courses/<id>/course.json (id, displayName, standardsPrefix, standardsFile, assessmentSource, eocTestable); derives the deck title, footer, standard codes, and check-slide source/label from it instead of hardcoding U.S. History / TCAP EOC. Defaults to the U.S. History flagship. For non-EOC courses (e.g., World History) the footer drops 'TCAP EOC' and check items come from the course's equated parallel-forms bank; layout and rigor are unchanged."
---

# History Hack Lean Deck Builder

Builds the **lean, student-facing** companion to the full History Hack lecture deck. Where the full deck (`history-hack-tcap-deck-builder`) runs every standard as a complete lesson with teacher cues, word walls, and DOK-tiered checks, the **lean deck is uncluttered for projection**: a bold **assertion headline** over a large **public-domain evidence image**, plus a small fixed set of analysis slides. This is a for-sale "Platinum Standard" product — every deck must be classroom-ready, TDOE-defensible, and visually clean.

## Course configuration (parameterized — resolve BEFORE building)

**Course-parameterized.** Resolve the course config from `courses/<course-id>/course.json` and derive the deck
title, **footer**, standard codes, and check-slide source/label from it — **never hardcode** "U.S. History"
or "TCAP EOC." Default to the **U.S. History flagship** when no course is named. Same contract as the sibling
`history-hack-tcap-deck-builder`: keys `id`/`displayName`, `standardsPrefix`/`standardsFile`,
`assessmentSource`, and `eocTestable`. For **non-EOC courses (`eocTestable: false`)** the footer reads
`{displayName} · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards` (no "TCAP EOC"), the
check items come from the course's **equated parallel-forms** bank, and check slides are labeled
"Standard-Mastery Check" — the assertion-evidence layout, Source-It-First bands, Three Perspectives, and
brand are all unchanged.

## When to Use This Skill

Trigger when the user asks to:
- "Build the Unit N lean deck" / "lean student deck" / "assertion-evidence deck"
- "Regenerate the lean deck" / "rebuild the lean answer key"
- "Update the lean deck manifest / web viewer entry"
- "Mirror the lean deck pattern" for a new unit

For the **full teacher deck**, use the sibling skill `history-hack-tcap-deck-builder` instead.

## Non-Negotiable Rules (the locked lean pattern)

1. **Narrative is LOCKED.** Assertion headlines are **summary-labels of the locked curriculum narrative only** (Unit 1 = v3.2 / repo v2.9). Never write new narrative. Metadata, attribution, and label fixes are fine.
2. **Keep student-facing decks lean.** Spanish scaffolding, DOK-tiered checks, and full teacher notes live in the **teacher's guide / full deck**, not on the student slides.
3. **PowerPoint (.pptx) is the source of truth**, built with `pptxgenjs`, 16:9 (13.333" × 7.5"), importing cleanly into Google Slides. System fonts only (Georgia / Calibri / Trebuchet MS).
4. **All imagery is public-domain**, source-captioned on-slide, historian-verified (LOC / NARA / Smithsonian). **No AI-generated imagery.** Every image slide gets a gold **ZOOM IN** pill so the teacher can zoom in while presenting.
5. **If we ask a question on a slide, we answer it** — every on-slide question has a model answer or exemplar in the Teacher Answer Key (including the Unit Hook).
6. **Three Perspectives lenses are verbatim:** "Who benefited?" · "Who bore the costs?" · "Who decided?"
7. **Deck must be downloadable AND live in the web app viewer** — regenerate the manifest and downloads block whenever the deck changes.
8. **Brand kit is locked** (see below). Run QC before delivery.

## Brand System (locked — do not change)

| Token | Hex | Use |
|---|---|---|
| NAVY | `#1A2332` | Dividers, dark bands |
| A250BLUE | `#002858` | America250 accent (primary-source slides) |
| RED | `#C62828` | Emphasis pills |
| GOLD | `#C9A84C` | Rules, standard badge, ZOOM IN pill |
| GOLDBR | `#F9A825` | Brighter gold accent |
| CREAM | `#F7F4EC` | Content background |
| INK | `#1F2430` | Body text |
| MUTE | `#5C6470` | Captions, footers |
| KEYGRN | `#1B5E20` | Teacher-key accent (PDF) |

Fonts: **Georgia** (headlines), **Calibri** (body), **Trebuchet MS** (labels). Footer on every content slide is **course-derived** from the resolved config: `{displayName} Hack · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards` — append ` & TCAP EOC` **only when `eocTestable: true`**. Flagship (default): `U.S. History Hack · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards & TCAP EOC`. World History (non-EOC): `World History Hack · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards`.

## Lean Deck Structure (fixed sequence)

**Unit open:** Cover / Unit Hook (Turn & Talk provocation, returned to at the end).

**Per standard (repeat for each US.NN):**
1. **Standard Divider** — code + official TN standard text + "I Can" objective (gold bar).
2. **Direct Instruction** — assertion-evidence slides: bold assertion headline + large evidence image + ZOOM IN pill.
3. **Primary Source Analysis** — the "SOURCE IT FIRST" WHO / WHEN / WHY sourcing band + clickable sources, tagged to a TN Social Studies Practice.
4. **Three Perspectives Synthesis** — the three verbatim lenses applied to a primary-source anchor.
5. **We Do (Guided Practice)** — modeled prompt → think-aloud → "then you try" (US.01 example).
6. **Tennessee Connection** — celebrated, "pop with bold" (e.g. George Jordan / Williamson County).

## Data Contract

The generator reads one `_build.json` (`meta`, `imageRefs`, `slides`). Read `references/data-contract.md` for the full field-by-field contract and per-`kind` shapes, and see `assets/unit1-lean-example/_build.json` for the complete working Unit 1 (US.01–US.07, 48 slides) file.

## Workflow

1. **Confirm the unit + standards** and pull content + imagery from the repo (`Trooptoteacher/history-hack-web-app`) first. Narrative stays locked — only summarize it into assertion headlines.
2. **Author `_build.json`** for the unit (mirror the example). Fill imagery gaps from public-domain archives; caption + cite each.
3. **Build the deck:**
   ```bash
   UNIT_SUBJECT='Unit 1 — Lean Student Deck (US.01–US.07)' \
     node scripts/build_lean_deck.js <DATA_DIR> <OUT.pptx> <IMG_DIR>
   ```
   Args: `<DATA_DIR>` holds `_build.json`; `<OUT.pptx>` output path; `<IMG_DIR>` root for `imageRefs` paths (defaults to `hh-web/public`).
4. **Build the printable Teacher Answer Key:** `python3 scripts/build_lean_answer_key.py` (writes the markdown) then `python3 scripts/make_lean_key_pdf.py` (branded PDF, clickable source links). The key covers every Source It First (WHO/WHEN/WHY + excerpts + sources) and Three Perspectives model answer, plus the Unit Hook question + exemplar and any We Do / Tennessee Connection models.
5. **Regenerate the web viewer manifest + downloads:** `python3 scripts/gen_manifest.py` (48-slide manifest, standards list, downloads block pointing at the current filenames). Convert slides to web JPGs with `python3 scripts/convert_slides.py` (deckimg-NNN.jpg).
6. **Refresh the Usage Guide** (slide count, unit title, structure table, teaching flow).
7. **Run QC** (next section), then **deliver**: the `.pptx`, the answer-key `.pdf`, the usage guide, and the updated manifest/viewer entry. Share with stable names so versions stack.

## QC (required — do not skip)

**Build invariant:** generated **natively as `.pptx` via pptxgenjs**, never from HTML or markdown;
set **`pres.layout` BEFORE adding any slides** (16:9 `13.333"×7.5"`). **LOCKED gates, in order**
(`00_START_HERE/BUILD_STANDARD.md` §4a): markitdown → `validate.py` → render-and-inspect-every-slide.
**Gate 3 (visual) is MANDATORY — clipped/overflowing text passes markitdown and validate.py silently.**

1. **Content QC (gate 1):** `python -m markitdown deck.pptx` — verify slide count, no placeholder text, no truncation, correct order.
2. **File-integrity QC (gate 2):** the `pptx` skill's `scripts/office/validate.py` + a python-pptx load→save round-trip (no duplicate zip parts). Duplicate slides only via `add_slide.py`, never python-pptx `add_slide`.
3. **Visual QC (gate 3 — MANDATORY):** `soffice --headless --convert-to pdf deck.pptx` then `pdftoppm -jpeg -r 150 deck.pdf slide`; read **every** slide image for wrapping/overflow/clipping/contrast. Fix-and-verify at least one cycle.
4. **Answer-key gate:** every on-slide question (including the Unit Hook) has a model answer; source links render as clickable hyperlinks (not raw `[text](url)`).
5. **Manifest gates** (from the web repo): run `check-deck-catalog.mjs`, `check-deck-citations.mjs`, `check-deck-permalinks.mjs` against the new manifest.
6. **Imagery audit:** every image public-domain, captioned on-slide, correctly depicts its subject; no mismatches (omit over mismatch).

## Companion Skills (run alongside, do not duplicate)

- `history-hack-tcap-deck-builder` — the full teacher deck (sibling; same brand kit).
- `historian-factcheck-agent` — verify every date, statute, case, number, name, quote.
- `ell-bilingual-review-specialist` — EN/ES scaffolding (lives in teacher's guide).
- `accessibility-qc-agent` — WCAG / UDL final gate.
- `tn-textbook-adoption-agent` — Policy 2.600 / Schedule F readiness.

## Bundled Resources

- `scripts/build_lean_deck.js` — the pptxgenjs lean-deck generator (brand kit, assertion-evidence + Standard Divider + Source It First + Three Perspectives + We Do + Tennessee slide functions, ZOOM IN pill). Parameterized via CLI args (`<DATA_DIR> <OUT.pptx> <IMG_DIR>`) and `UNIT_SUBJECT` env.
- `scripts/build_lean_answer_key.py` — writes the answer-key markdown from `_build.json` (Unit Hook exemplar + Source It First + Three Perspectives + We Do + TN models).
- `scripts/make_lean_key_pdf.py` — ReportLab branded Teacher Answer Key PDF renderer (markdown → PDF, clickable source links).
- `scripts/gen_manifest.py` — regenerates the web viewer manifest + downloads block.
- `scripts/convert_slides.py` — renders slides to web JPGs (deckimg-NNN.jpg).
- `assets/unit1-lean-example/_build.json` — the complete, working Unit 1 (US.01–US.07, 48 slides) data-contract reference.

---

© 2026 TroopToTeacher Technologies LLC. Proprietary. All rights reserved.
