# Workbook Format QC Gate

Run this before any workbook (new unit, whole course, or a QC pass on existing units) is called done.
Each item is pass/fail; a fail blocks shipment. Verify by **rendering**, not by reading code.

## A. Brand-lock (grep + one render)
- [ ] `const CW=9792;` present; every `table(...,widths)` columnWidths sum to 9792.
- [ ] Page `12240×15840`; margins `top/bottom 1152`, `left/right 1224`, `header/footer 720`.
- [ ] Font `Calibri`; body size 22; H1/H2/H3 = 36/28/24; H1/H2 NAVY, H3 RED.
- [ ] Palette exact: NAVY `1B2A4A`, RED `B22234`, GOLD `C89B3C`, CREAM `F7F5EF`, GREY `6B7280`,
      BORD `D9D5C8`.
- [ ] Cornell present with `2448|7344` body and a navy header row.

## B. Writing lines (render + look)
- [ ] Every place a student writes has **visible** notebook lines (color `8892A0`), including Cornell
      notes column, summaries, CER, retrieval, prompts, self-check write areas.
- [ ] Lines render as **separate** lines (anti-merge spacer present) — not one thick rule.
- [ ] Open draw/diagram areas are tall empty boxes (no lines), clearly labeled.

## C. Layout / no bleed (render the WORST-case standard)
- [ ] No activity page bleeds onto a mostly-empty next page (`pagefit.py` clean on activity segments;
      the `(front)` segment flag is ignored).
- [ ] Nothing sits at the very bottom edge of a Spire page (Word renders taller → would bleed).
- [ ] No "excess empty space at the bottom" — dead space filled with *useful* workspace, not filler.
- [ ] Each activity is a self-contained printable worksheet.

## D. Content-placement rules (student vs teacher)
- [ ] **No answer keys / teacher notes in the student workbook** (practice-quiz key, CER model, etc.
      are teacher-side only).
- [ ] MTSS/UDL framework jargon is **not** on the student page (student text says "core path" /
      "support options"; supports live on a back page).
- [ ] No Name/Class/Date line; no per-standard UDL Access/Choice/Reflection page.
- [ ] Bold labels applied consistently (e.g. `Pronunciations:`, `Word-bank meaning to build on:`,
      `RESPONSE CHOICE:`, `MAKE IT YOURS:`) across **all** worksheets, not just one.

## E. Accessibility / print
- [ ] Every image has alt text and a full public-domain citation + rights line.
- [ ] Spanish column framed as access, not assessment translation.
- [ ] `LARGEPRINT=1.5` edition builds and still lays out (sizes scale via `SZ()`; near-identical byte
      count is expected — sz values change, element count doesn't).

## F. Build integrity
- [ ] All units build (remember `NODE_PATH="../unit1/node_modules"` for units without local modules).
- [ ] Helper functions are **identical** across `unit2..7` + `engine` (edits applied by one pass).
- [ ] `unit1/build_workbook.js` regenerated from unit2 if it was gitignored/wiped; header points at
      `unit1_*` content and `Unit1_*` output.
- [ ] Preview/TMP artifacts deleted; deliverables (std + large print) rebuilt and present.

## G. Commit
- [ ] Commit the tracked builders (`engine` + `unit2..7`) and the `.docx` deliverables.
- [ ] Do NOT rely on `unit1/build_workbook.js` being committed (commonly gitignored) — its deliverables
      carry the output.
