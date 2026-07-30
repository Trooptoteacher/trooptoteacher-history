# Design system, pipeline, and delivery

The house style lives in `scripts/toolkit_lib.py`. Every organizer page is produced by `render_page(...)`
so the header, when·why blurb, UDL·MTSS strip, footer, and time chip are pixel-identical across the whole
workbook. Do not fork it; extend via each organizer's `extra_css`.

## Brand tokens
Navy `#1B2A4A` · red `#B22234` · gold `#C89B3C` · cream `#F7F5EF` · white. Light tints for writable
surfaces: navy `#EEF1F7`, red `#FBEEEF`, gold `#FAF3E2`, green `#EAF2EC`. Rule `#CBD2DE`, muted `#5A6579`,
writing-line `#C4CCDA`. Headline font Georgia serif; body Helvetica/Arial. US-Letter portrait (8.5×11in).

## Page anatomy (top to bottom)
1. **Header** — kicker (unit·standard or "Reusable Organizer"), Georgia title, Name/Class/Date line;
   right side: **Reproducible** badge, **time chip** (clock SVG + estimate), optional **★ Tennessee
   Connection** badge, and skill/DOK chips.
2. **When · Why** strip — cream, gold left-border; the teach-the-teacher blurb + an italic evidence cite.
3. **Organizer** — a centered `prompt` line + the visual organizer (`body`), filling the page.
4. **Make it work for every student (UDL · MTSS)** — 3 columns: Scaffold / Extend / Show it your way.
5. **Footer** — `U.S. History Hack™ · © 2026 TroopToTeacher Technologies LLC` + a role label.

## A pack file (one organizer)
`src/pack_<NN>_<name>.py` exposes `ORGANIZERS = [dict(...)]`. Keys map to `render_page` kwargs:
`slug` (NN prefix sets page order), `title`, `kicker`, `chips` (list of `(text, "navy"|"skill")`), `why`
(HTML ending in `<span class='cite'>…</span>`), `body` (HTML + inline SVG), `extra_css`, `udl`
(`dict(scaffold, extend, show)`), `role`, and `tn=True` to show the TN badge. HTML entities: use
`&mdash; &middot; &amp; &rarr; &#9733;`. See `assets/example_packs/` for real, working examples.

## CSS primitives (in SHARED_CSS — compose these; add `extra_css` for bespoke shapes)
- Layout: `.row` / `.col` (flex + gap), `.fill` (flex:1), `.canvas` (full-height flex column).
- `.prompt` — centered instruction. Put at top of `body`.
- `.band navy|red|gold sm` — a dark **label** bar (labels only; never a writing area).
- `.well [navy|red|gold] [tint-*] [cream] [lines] [top]` — a **light writable** box; `.lines` adds faint
  dotted guides; `.top` rounds all corners. `.cue` = tiny caps label inside a well; `.wpad`, `.hint`.
- Arrows: `.arr-d` (down triangle), `.arr-r` (right triangle), `.arr-lbl`. Or draw connectors in SVG.
- **Inline SVG** for circles/hubs/lenses/timelines. Light fills + colored strokes; faint dashed writing
  guides (`stroke="#B9C2D0" stroke-dasharray="2 5"`). **Keep all text labels inside the SVG** (viewBox
  coords) so they track the geometry when it scales — HTML overlays drift outside the shapes.

Bespoke reference pages (Quick Guide, SSP Crosswalk) don't use `render_page` (they have no UDL strip);
build them as standalone HTML importing `SHARED_CSS` + `FOOTER_BRAND`. See `assets/example_packs/make_quickguide.py`.

## Render pipeline (bundled scripts)
Rendering uses the environment's pre-installed headless Chromium (no npm Playwright needed). Key facts
learned the hard way:
- `render.py` renders each page at **2×** and crops to the exact letter box (1632×2112). `--window-size`
  is in **CSS pixels**, so page width must equal the window width or the page centers and clips. It uses
  Pillow to crop; the combined PDF is merged with **pikepdf** (avoid `pypdf` — its crypto import is broken
  in this environment).
- Commands: `python3 render.py png [file.html …]` (all pages if none named) and `python3 render.py pdf`
  (combined US-Letter PDF). `build_one.py pack_x.py` builds just those packs (safe for parallel authors);
  `build.py` builds everything in slug order.
- **QC loop:** after rendering, open each PNG with the Read tool and inspect: real visual structure,
  writable areas light, nothing clipped at the bottom, labels inside their shapes, footer present, no dead
  space. Fix and re-render until clean. A contact sheet (tile PNGs with Pillow) reviews many pages per look.

## Delivery: Canva + exports
1. Commit and push the unit folder (source + the combined PDF) to the repo branch. The repo is public, so
   the file gets a permanent `raw.githubusercontent.com` URL.
2. Import that PDF URL into Canva with `import-design-from-url` (brand kit **`kAG39-EGTcM`**,
   `intended_design_type: "us_letter"`) → an editable 24-page design. Re-importing makes a *new* design
   (new link) — treat the GitHub PDF as the always-current master and refresh Canva only on request to
   avoid piling up versions.
3. Export from Canva (`get-export-formats` then `export-design`) as PDF + PNGs; give the user the design
   link + files. Optionally place a labeled index Google Doc (links) in the user's Drive folder — note that
   the Drive connector can't upload multi-MB binaries inline, so the doc links to the permanent PDF URL.

## Environment constraints (so you don't get stuck)
- GitHub write may be gated: if `git push` / MCP returns 403 "Resource not accessible by integration," the
  Claude GitHub App needs **Contents: write** granted by a repo admin; report it, don't hammer.
- Egress policy may 403 some hosts (e.g., Canva's export-download domain) — you may be unable to fetch
  Canva exports back to verify; rely on your own vector PDF (which Canva imports faithfully) and have the
  user eyeball the design.
- A Word (.docx) version is best delivered as image-per-page via python-docx (print/annotate only). True
  editable-Word rebuilds of these vector organizers are lossy; recommend Canva or source edits for real
  changes. LibreOffice PDF→DOCX conversion is unreliable here.
