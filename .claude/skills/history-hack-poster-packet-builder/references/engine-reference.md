# Engine Reference — ReportLab Poster/Station Engines

This is the API and design DNA for the four engines that power the packet. All sizes use
`from reportlab.lib.units import inch`.

## Design DNA (approved Unit 1 sample)

Deep navy frame + inner gold hairline, warm paper field (`PAPER`), red standard chips with gold
rings, DM Sans display / Inter body, circle logo top-left of the header band, brand footer with
copyright on every page. Posters print sharp from 18x24 up to 36x48.

## brand.py (single source of truth)

```python
NAVY="#1F3A5F"; NAVY2="#14315A"; RED="#B22234"; RED_D="#8E1B29"
GOLD="#C8A04B"; GOLD_L="#E8C97A"; INK="#1C1C1C"; SLATE="#4A5568"
PAPER="#F8F5EF"; LINE="#D8D2C4"; WHITE=white
COPYRIGHT_YEAR="2026"
LLC="TroopToTeacher Technologies LLC"
COPYRIGHT="© 2026 TroopToTeacher Technologies LLC. All rights reserved."
COPYRIGHT_SHORT="© 2026 TroopToTeacher Technologies LLC"
LOGO="/home/user/workspace/engine/channel_logo_circle.png"
def register_fonts(): ...  # registers DM Sans, Inter + handwriting family
```

`register_fonts()` registers: `DMSans`, `DMSans-Med`, `DMSans-Bold`, `Inter`, `Inter-Med`, and
(if present) the sketch-note family `Marker` (Bangers/PermanentMarkerAlt), `HandBold` (Kalam-Bold),
`Hand` (Kalam), `HandPrint` (Patrick Hand), `HandScript` (Caveat-VF), `HandArch` (Architects Daughter).

## poster_engine.py — P01–P11 (24x36 master)

Constants: `PW,PH = 24*inch, 36*inch`; `MAR=0.75in` outer frame; `FR=0.20in` gap to gold hairline;
`PAD=1.05in` content pad; `IL/IR/IW` inner content left/right/width; `CX=PW/2`.
`DISPLAY="DMSans-Bold"`, `DISP_MED="DMSans-Med"`, `BODY="Inter"`, `BODY_MED="Inter-Med"`.

Key helpers:

- `new_canvas(out_name, title)` → canvas; writes into `../posters/`; sets author "Perplexity Computer".
- `draw_frame(c, paper=PAPER)` → navy 12pt frame + 2.5pt gold inner hairline on paper field.
- `footer(c, extra=None)` → centered base line "U.S. History Hack · Aligned to Tennessee U.S.
  History Standards" + **COPYRIGHT line below it** (always present). Optional `extra` provenance line.
- `header_band(c, unit_label, std_label, topic, height=4.4*inch, topic_size=40, chip=True)` →
  navy header band, gold top accent, logo top-left, gold unit label, red standard chip with gold
  ring, auto-wrapped white topic. Returns `by` (band bottom y).
- `wrap_fit(c, text, font, size, max_w, max_lines=3, min_size=10)` → `(lines, final_size)`; shrinks
  font until it fits. Use everywhere text could overflow.
- `para(c, text, x, y, w, font=BODY, size=16, leading=None, color=INK, max_lines=99, align="left")` →
  draws a wrapped paragraph top-down; returns y after last line.
- `fit_single(c, text, font, max_w, size, min_size=8)` → shrink a single line to fit; returns size.
- `img_path(name)` → path under `poster_assets/img/`.
- `draw_image_cover(c, path, x,y,w,h, radius=0)` → center-crop COVER, clipped to (rounded) rect.
- `draw_image_contain(c, path, x,y,w,h, bg=WHITE)` → letterbox whole image.
- `photo_card(c, path, x,y,w,h, caption=None, cap_size=12, frame_color=NAVY)` → cover image in a
  navy-bordered white card with optional gold-accented caption bar.
- `section_title(c, text, x, y, w=None, size=30, rule=True, color=NAVY)` → title + gold underline rule.
- `chip(c, text, x, y, font=BODY_MED, size=15, fill=GOLD_L, fg=NAVY, padx=0.30*inch, h=0.55*inch)` →
  rounded chip; returns its width.
- `finish(c)` → `showPage()` + `save()`; returns out path.
- `qc_render(pdf_path, scale=0.5)` → render page 1 to PNG in `../assets/` for visual QC (pypdfium2).

Builder skeleton (each P0x file):

```python
import poster_engine as E
c = E.new_canvas("P01_Unit_Overview.pdf", "Unit Overview")
E.draw_frame(c)
by = E.header_band(c, "UNIT 1 · The Rise of Industrialization", "US.01", "Unit Overview")
# ... content using E.section_title / E.para / E.chip / E.photo_card ...
E.footer(c)
path = E.finish(c)
png = E.qc_render(path)   # then `read` the PNG to visually QC
```

## sketchnote_engine.py — P13 flagship anchor chart

Handwriting fonts: `MARKER`/`HBOLD`/`HAND`/`HPRINT`/`HSCRIPT`. Has an `icon()` dispatcher for
hand-drawn vector icons. Footer draws "U.S. History Hack · trooptoteacher.com" with the COPYRIGHT
line below, right-aligned. The flagship intentionally uses a hand-drawn sketch-note aesthetic.
Caption zones must dodge subjects; verify the subtle corporate mark is legible; no top logo.

## engine_v2.py — P12 (Whose Story) + P06 (Word Wall)

Provides `provenance_footer(...)` (uses the COPYRIGHT constant) and a set of vector icons drawn
in code. Used by the perspective wall and the bilingual word wall.

## station_engine.py — Track B (Letter)

Letter-size gradeable station engine. `footer()`: left = `COPYRIGHT_SHORT`, center = page label,
right = "trooptoteacher.com". Stations are designed to be printed, completed by students, and graded.
(The HIPP station is 2 pages — guard against a stray trailing `showPage()` that creates a blank 3rd page.)

## platinum_plus.py — teacher guides (Letter)

Three Letter-size documents into `../guides/`: Standards Alignment Map (1pg), Print & Display Guide
(1pg), Facilitation Guide (2pg). Navy header band + gold hairline, DM Sans/Inter, COPYRIGHT footer
on every page, App Store callout. Run: `python3 platinum_plus.py`.

## assemble_bundle.py — final assembly

`pypdf` merge. Produces in `../assembled/`:
- `UnitN_Wall_Set.pdf` — all 13 posters P01→P13.
- `UnitN_Complete_Bundle.pdf` — branded Letter cover + 3 section dividers (Teacher Guides / Wall
  Posters / Station Activities) + 3 guides + 13 posters + 2 stations. Cover/dividers are Letter;
  poster pages stay 24x36. Copyright on every generated cover/divider page. Run: `python3 assemble_bundle.py`.
