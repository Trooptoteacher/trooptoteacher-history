# ReportLab Engine Conventions

The Platinum workbook is built with a single ReportLab script (`build_workbook_template.py`). These are the conventions to preserve across every unit and subject.

## Palette (LOCKED)
```
NAVY   = #1B2A4A   # headers, titles
NAVY2  = #2C3E63   # secondary header band
RED    = #B22234   # sparingly (accents, alerts)
GOLD   = #C89B3C   # rules, accent bars
CARD   = #F7F5EF   # zebra shading / callout backgrounds
LIGHT  = #EEF2F8   # secondary fill
BORDER = #C9C2B4   # dividers, cell borders
INK / MUTED        # body text / secondary text
```
Grayscale-legible: rely on shading + rules + labels, never color alone.

## Fonts
`ensure_fonts()` registers HEAD / HEADM (headings), BODYF (body), SERIFI (italic serif accents). Body ≥ 10.5pt; table cells ~9.5-10pt OK.

## Pagination and orphan control (LOCKED)

The engine must preserve logical learning blocks and prevent one- or two-line spill pages.

- Set heading styles to `keepWithNext=True`.
- Use `widowOrphanControl=True` where the renderer supports it.
- Wrap short logical blocks in `KeepTogether`: heading + first substantive block; question stem + all options; Cornell cue + note area; compact rubric; short prompt + response frame.
- Do not wrap an oversized multi-page section in one `KeepTogether`; split it into meaningful blocks so ReportLab can paginate safely.
- Use `CondPageBreak` or an equivalent preflight spacer when a block needs a minimum remaining height.
- Treat tables carefully: allow long tables to split by row, repeat header rows, and prevent row splitting; keep short tables intact.
- Preserve intentional student workspace. Blank space is acceptable only when the page has a visible prompt/title and the QA log marks it `INTENTIONAL WORKSPACE`.
- After every build, run the sparse-page gate in `references/qc-checklist.md`. Unresolved `LAYOUT DEFECT` pages block release.

## Helpers (reuse, don't reinvent)
- `S(name, **kw)` — makes/caches a ParagraphStyle.
- `accent_bar(text, color, size)` — navy/gold section header bar.
- `full_image_flowable(path, max_w, max_h, caption, credit, alt)` — full-width chart/map with a caption box; `alt` folds a plain-language description into the caption (doubles as accessibility text). **Returns a plain list — the image can break to the next page on its own.**
- `doc_image_flowable(...)` — document image with sourcing furniture.
- `numbered_tasks`, `sentence_starter`, `hbox`, tables with zebra shading + gold rules + navy headers.

## Fixed-footprint white-space activities (LOCKED)

Read `white-space-activity-library.md` before implementing these helpers. The engine must expose reusable activity builders with bounded heights:

- `activity_quarter(kind, context, scaffold_stage, max_h)` for the 20–40% unused band.
- `activity_half(kind, context, scaffold_stage, max_h)` for the 40–65% unused band.
- `activity_three_quarter(kind, context, scaffold_stage, max_h)` for the 65–80% unused band.
- `activity_full_lab(kind, context, scaffold_stage, max_h)` only after an above-80% page has failed a merge/reflow attempt and the page is necessary.

Each builder must:

- fit inside `max_h` without splitting;
- return one `KeepTogether`-safe logical block;
- use essential instructional text at 10.5pt when practical and never below 9.5pt;
- include response space sized to the task;
- produce observable student work;
- accept the source/standard/DBQ context rather than generic filler;
- honor `early`, `middle`, or `late` scaffold stage;
- refuse or fall back to the next-smaller component if it cannot fit without spill.

Do not reduce font size, response usability, or margins to force a component into a page. Reflow, select a smaller component, or classify genuine labeled workspace instead.

## VISUAL SOURCES ARE STANDALONE DOCUMENTS (LOCKED — never regress)
A political cartoon, photograph, or poster that carries its own argument is a **primary source in its own right**: its OWN document (its own Doc letter) with its OWN standalone **OPTIC** analysis box (Overview, Parts, Title/Text, Interrelationships, Conclusion). The College Board scores cartoons and photographs as full documents — so do we. Text documents get **HIPPO**; visual-primary documents get **OPTIC**.

The engine encodes this with:
- `VISUAL_IS_PRIMARY = {...}` — the set of document/source titles whose image IS the source (gets standalone OPTIC).
- `optic_box(title, letter_id, W)` — renders the 5-row OPTIC table + the "This image is a document too" callout. Returns `[]` for titles not in `VISUAL_IS_PRIMARY`.

**Hard rules when templating a new unit:**
- NEVER silently merge a visual primary source into a text document as decorative art.
- NEVER attach an image to a text document it does not genuinely depict (the Unit 2 "Doc F mismatched image" failure). Every image must be verified to match its document during QC.
- A pairing (image beside a text act) is allowed ONLY when the image truly illustrates that act's subject; a source with its own argument must stand alone with OPTIC.
- Do not remove or bypass `VISUAL_IS_PRIMARY` / `optic_box` when adapting the engine.

## THE TWO-PASS MARKER MECHANISM (critical — never hardcode page numbers)
Zero-height `Flowable` subclasses record `self.canv.getPageNumber()` into shared dicts as they are drawn:
- `TOCMarker(key)` -> writes into `TOC_PAGES[key]`. The TOC reads this dict to print its page column.
- `XWMarker(key)` -> writes into `XW[key]`. The standards crosswalk reads `_xw_page(key)` for its "Where in this workbook" cells.
- `US07Marker`, `GeoSectionMarker` -> section-start page flags for running headers.

`make_pdf()` builds repeatedly until `TOC_PAGES` and `XW` stop changing (converges in ~2 passes; a warm-up pass may be run because the TOC precedes the sections it lists). Every page reference — in the TOC and in the crosswalk cells — is pulled live from these dicts. **Adding a section shifts downstream pages; the mechanism reconverges automatically. Never write a literal page number into a cell.**

## THE KEEPTOGETHER MARKER BUG (must-fix pattern)
A zero-height marker placed in the story flow *before* a `KeepTogether([...image...])` block stays on the page where the flow currently is, while the image block may break to the NEXT page as a unit. Result: the captured page is one short of where the image actually renders.

**Fix:** glue the marker INSIDE the KeepTogether with the content it names:
```python
_img = full_image_flowable(path, W, max_h=2.6*inch, caption=..., alt=..., credit=...)
story += [KeepTogether([XWMarker("CHART_URBAN")] + _img)]
```
This is exactly the fix applied when the urbanization chart was cited at p.33 but rendered on p.34. Add a dedicated keyed marker for any specific artifact a cell names by page.

## Page furniture
- `content_page(c, doc)` draws the running header ("U.S. HISTORY HACK • DBQ WORKBOOK" + unit/section right), gold top rule, footer copyright line, and the page number (`doc.page`). Section name in the header is chosen by page-range flags (`GEO_START_PAGE`, `US07_START_PAGE`).
- `cover_page(c, doc)` draws the navy cover with gold rule.

## TOC entries
`TOC_ENTRIES = [(key, label), ...]` in reading order; each key matches a `TOCMarker(key)` registered at that section's start. Add a new tuple in the correct reading-order position when inserting a section.
