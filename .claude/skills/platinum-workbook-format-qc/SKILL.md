---
name: platinum-workbook-format-qc
description: "Platinum brand-lock formatting spec + render-based QC for Course Standard STUDENT WORKBOOK .docx files (docx-js builders) across any subject edition — U.S. History Hack, Government Hack, World History Hack, etc. Use when: building the docx workbook for a new unit; matching the U.S. History Hack workbook look exactly (margins, sizes, spacing, boxes, Cornell notes, ruled writing lines); adding or restructuring an activity; fixing a page that BLEEDS to a second nearly-empty page; making writing lines VISIBLE/notebook-like; filling dead white space; or running a print/format QC pass on existing workbooks. This is the DOCX layout + visual-QC authority; it does NOT author content, standards, items, or sources (those are other skills). NOT for the standalone DBQ product (use history-hack-platinum-workbook)."
license: MIT
metadata:
  author: TroopToTeacher Technologies LLC
  version: '1.0'
  canonical_reference: U.S. History Hack — Unit 6 & Unit 8 Student Workbook (Course Standard Edition)
  applies_to: Course Standard student workbooks (Cornell-note, 7-activity per-standard architecture) for ALL subject editions
---

# Platinum Workbook — Formatting & Render-QC

The DOCX layout authority for Course Standard student workbooks. Every subject edition's workbook
must match the U.S. History Hack flagship **feature-for-feature and pixel-for-pixel**. This skill is
the hard-won spec: the exact brand-lock measurements, the per-standard activity architecture, the
writing-line rendering trick, and — critically — the **render-before-you-send** QC pipeline that
catches invisible lines and page bleed *before* anything reaches the user.

> **Prime directive (learned the hard way): NEVER send a workbook you have not RENDERED and looked at.**
> The estimator is not enough; LibreOffice's Word filter is broken in-sandbox. Use the Spire.Doc →
> PNG pipeline in `assets/render_check.py` and actually read the images. See
> `references/render-qc-pipeline.md`.

## When to use
- Building the `build_workbook.js` docx for a new unit, or a whole new course edition.
- "Match the U.S. History Hack format exactly" / "copy these margins, sizes, boxes, spacing."
- "Every place a student writes needs visible notebook lines."
- "This activity is bleeding onto a second page" / "fill the white space at the bottom."
- Adding/restructuring an activity (opener supports, Sketch Studio, self-check, CER back, etc.).
- Running a print/format QC gate before packaging.

## The engine (how these workbooks are built)
- **docx-js** (`const D=require('docx')`) builders named `build_workbook.js`, one per unit, under
  `<course>/BUILD/unit<N>/`. A canonical copy lives in `<course>/BUILD/engine/`. The per-standard
  layout function `block(code)` and all the helpers (`ruled`, `writeTable`, `writeBox`, `cornell`,
  `callout`, `coreCallout`, `dataTable`, `table`, `cell`, `H`, `P`, `R`) are **identical across all
  units** — edit them with one string-replace pass over every unit + engine, so they never drift.
- Content is data-driven: `analysis/unit<N>_content.json` (standards, vocab, frayer terms, close
  text, TDQs, cues, hooks, targets…). The builder never hardcodes subject content.
- Build: `NODE_PATH="../unit1/node_modules" node build_workbook.js` (unit1 holds `node_modules`;
  some units have none — always set NODE_PATH). Output → `deliverables/`.
- Flags: `LARGEPRINT=1.5` (scales every size via `SZ()`), `SAMPLE=N` (first N standards),
  `ONLYSTD=<code>` (one standard) → both write a small `*_PREVIEW_*.docx` for fast render-QC.
- ⚠️ `unit1/build_workbook.js` is commonly **.gitignored** (regenerate it from unit2 by swapping
  `unit2_*`→`unit1_*` in the header). The built **.docx deliverables ARE tracked**. See troubleshooting.

## BRAND-LOCK — the LOCKED spec (never deviate; verify after any copy)
Page & frame (US-Letter portrait):
- Page size `12240 × 15840` twips. Margins `top 1152 · bottom 1152 · left 1224 · right 1224`,
  `header 720 · footer 720`.
- **Printable width `CW = 9792`** (`12240 − 1224 − 1224`). **Every top-level table width = 9792.**
  Column widths must sum to 9792 (e.g. `4896|4896`, `3264·3` , `2723·4347·2722`, cornell `2448|7344`).

Type & color (hex, no `#`):
- Font `Calibri` everywhere. Body text size `22` (=11pt; docx half-points, `SZ(n)` applies large-print).
- Headings: `H1 sz36`, `H2 sz28`, `H3 sz24`. H1/H2 color NAVY `1B2A4A`; H3 color RED `B22234`.
  Headings: `keepNext:true`; H1 `spacing before 220`, H2 `before 150`, `after 90`; `pageBreakBefore`
  via the `{brk:true}` option. Optional `⏱ ~N min` chip in GOLD.
- Palette: NAVY `1B2A4A` · RED `B22234` · GOLD `C89B3C` · INK `1A1A1A` · CREAM `F7F5EF` (callout fill) ·
  WHITE `FFFFFF` · GREY `6B7280` · border BORD `D9D5C8`.
- Cell padding: body cells `top/bottom 55, left/right 110`; cornell cells `top/bottom 50, left/right 80`.

Writing lines (**the #1 recurring bug — read `references/render-qc-pipeline.md` §lines**):
- Ruled line color is **`8892A0` (medium gray), size 8**. The old `C9C2B4` was invisible on screen —
  do not use it for in-flow lines.
- Word/Spire **merge adjacent identical bottom-border paragraphs** into one visible line. The `ruled(n)`
  helper defeats this with a border-less **anti-merge spacer** paragraph between each line. Never emit
  stacked bordered paragraphs without the spacer.
- **Every place a student writes must have visible notebook lines** — prompts, summaries, Cornell notes,
  CER, retrieval, all of it. Open draw/diagram areas use a tall empty single-cell table instead.

Canonical helper contracts (signatures are LOCKED — match exactly): see `references/brand-lock-spec.md`.

## Per-standard architecture (the 7-activity spine + supports)
Each standard = opener → 7 activities, each activity a **self-contained printable worksheet**.
Full structure, page-by-page, with the design rationale for every recent change (opener supports
back page, concrete WRITE/SAY-IT/DIAGRAM, Sketch Studio, DOK write boxes, CER-back self-grade,
compact retrieval self-check): `references/activity-architecture.md`.

## Anti-bleed method (LOCKED discipline)
1. Every activity must fit its page(s) with **no page that bleeds to a mostly-empty next page**.
2. **The estimator lies high on open boxes and low on text** — trust the *render*, not the number.
3. **Word renders TALLER than Spire.** Leave headroom: if the render shows a page comfortably full
   (~65–90%) you're safe; if content sits at the very bottom edge in Spire, it WILL bleed in Word.
4. **Test the worst case, not the first case.** Close-read passages and TDQ counts vary per standard.
   Find the fullest standard (longest `close` text) and render *that* one. If it fits, shorter ones do.
5. To inspect a page past Spire's ~10-page cap, build a **temp slice** that starts `block()` at the
   activity you need (see render-qc-pipeline §deep-page). Then size the content so even the worst
   standard fits, and propagate.
6. Fill dead space with *useful* content (goal-draft lines, self-check, retrieval, sketch box) — never
   filler. A supports/reference page at ~65% with a real workspace at the bottom is "full enough."

## Fast path
1. Read `references/brand-lock-spec.md` (constants + helper contracts) and
   `references/activity-architecture.md` (what each page is).
2. Make edits with ONE python/string-replace pass across `unit2..7` + `engine` (unit1 is regenerated).
3. `pip install spire.doc PyMuPDF` if needed. Build a `ONLYSTD=<fullest-std>` preview.
4. `python3 assets/render_check.py <preview.docx> <outdir>` → **open the PNGs and look.**
5. `python3 assets/pagefit.py <full.docx>` → scan for `<-- BLEED` flags (activity segments only;
   the `(front)` segment is an estimator artifact — it uses run-level breaks the estimator can't see).
6. Iterate until worst-case fits with headroom. Rebuild all units (std + `LARGEPRINT=1.5`).
7. Run `references/qc-checklist.md`. Then commit the builders (`engine` + `unit2..7`) and deliverables.

## Guardrails
- Brand-lock is not negotiable — after copying a builder into a new course, re-verify `CW=9792`,
  margins `1224`, the palette, and a `cornell()` function before building.
- Teacher keys/answers NEVER appear in the student workbook (they live teacher-side).
- Same rigor for every student; UDL/MTSS are *ways in*, never lowered bars, and MTSS/UDL jargon is
  kept off the student page (say "core path," "support options"; supports on a back page).
- Do not ship without a render pass. "It builds" ≠ "it's correct."

Reference index: `brand-lock-spec.md` · `activity-architecture.md` · `render-qc-pipeline.md` ·
`qc-checklist.md` · `troubleshooting.md`. Tools: `assets/render_check.py` · `assets/pagefit.py`.
