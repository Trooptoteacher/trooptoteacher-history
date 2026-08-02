---
name: history-hack-lean-deck-builder
description: "Builds the lean, student-facing U.S. History Hack TCAP deck (PowerPoint .pptx) for any unit, plus its matching printable Teacher Answer Key (PDF), web viewer manifest, and Usage Guide. Assertion-evidence layout: a bold assertion headline (a summary-label of the LOCKED curriculum narrative — never new narrative) over a large public-domain evidence image, with Source It First WHO/WHEN/WHY sourcing bands and the fixed Three Perspectives synthesis (Who benefited? / Who bore the costs? / Who decided?). Sibling to history-hack-tcap-deck-builder (the full teacher deck). Use when asked to build/regenerate the lean deck, lean student deck, or assertion-evidence deck for a History Hack unit, or its lean answer key or manifest."
license: "Proprietary — © 2026 TroopToTeacher Technologies LLC. All rights reserved."
metadata:
  author: TroopToTeacher Technologies LLC
  version: '1.0'
---

# History Hack Lean Deck Builder

Builds the **lean, student-facing** companion to the full History Hack TCAP lecture deck. Where the full deck (`history-hack-tcap-deck-builder`) runs every standard as a complete lesson with teacher cues, word walls, and DOK-tiered checks, the **lean deck is uncluttered for projection**: a bold **assertion headline** over a large **public-domain evidence image**, plus a small fixed set of analysis slides. This is a for-sale "Platinum Standard" product — every deck must be classroom-ready, TDOE-defensible, and visually clean.

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

Fonts: **Georgia** (headlines), **Calibri** (body), **Trebuchet MS** (labels). Footer on every content slide: `U.S. History Hack · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards & TCAP EOC`.

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

1. **Content QC:** `python -m markitdown deck.pptx` — verify slide count, no placeholder text, no truncation, correct order.
2. **Visual QC:** `soffice --headless --convert-to pdf deck.pptx` then `pdftoppm -jpeg -r 150 deck.pdf slide`; review slide images for wrapping/overflow/contrast. Fix-and-verify at least one cycle.
3. **Answer-key gate:** every on-slide question (including the Unit Hook) has a model answer; source links render as clickable hyperlinks (not raw `[text](url)`).
4. **Manifest gates** (from the web repo): run `check-deck-catalog.mjs`, `check-deck-citations.mjs`, `check-deck-permalinks.mjs` against the new manifest.
5. **Imagery audit:** every image public-domain, captioned on-slide, correctly depicts its subject; no mismatches (omit over mismatch).

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
