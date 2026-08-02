# Organizer authoring contract — Unit 1 Teacher Graphic Organizer Toolkit

You are building **blank, reusable, content-agnostic** graphic organizers for
TroopToTeacher Technologies — U.S. History Hack™. Each is ONE US-Letter portrait
page. They must be **real visual organizers a student can write on**, not tables
of ruled lines.

## How the system works
- `src/toolkit_lib.py` renders every page identically (header, when/why blurb,
  UDL/MTSS strip, footer). **Do not edit it.** You only write a `pack_*.py`.
- Create `src/pack_<NN>_<name>.py` exposing `ORGANIZERS = [ dict(...), ... ]`.
  One dict = one page. Keys (all strings are HTML; use `&mdash; &middot; &amp;`):
  - `slug` — e.g. `"04_tchart_blank"` (the NN numeric prefix sets page order; use the number I assign)
  - `title` — organizer name, e.g. `"T&#8209;Chart &mdash; Compare Two"`
  - `kicker` — `"Reusable Organizer &middot; Any Unit &middot; Any Subject"`
  - `chips` — list of `(text, kind)`; kind is `"navy"` or `"skill"` (red). e.g. `[("Compare 2","navy"),("DOK 2 &middot; Comparison","skill")]`
  - `why` — 1–2 sentences: when to use it + why it works, ending with an italic
    `<span class='cite'>…(evidence)</span>`. Evidence to draw on: Marzano
    (similarities/differences = highest yield), TN Social Studies Practices
    (SSP.05 cause-effect & chronology), UDL 3.0, MTSS. Never invent citations.
  - `body` — the organizer HTML (see primitives). MUST fill the page, no dead space.
  - `extra_css` — component CSS specific to this body (optional).
  - `udl` — `dict(scaffold="…", extend="…", show="…")`. Scaffold = sentence
    starter/word bank/partner-first. Extend = a higher-DOK push. Show = UDL
    response choice (write/say/draw/build). `show` may be omitted for a default.
  - `role` — `"Teacher Graphic Organizer Toolkit &middot; Blank Reproducible"`
  - `tn=True` only for the Tennessee Connection organizer (not your set).

## NON-NEGOTIABLE design rules
1. **Writable fields must be LIGHT** (white or cream `.well`). NEVER put a dark
   bar where a student writes. Dark navy/red bands are for **labels only**.
2. **Real visual structure**: overlapping circles, boxes linked by arrows,
   a center oval with quadrants, a timeline with a line + ticks, a hub with
   spokes — not a grid of blank ruled rows pretending to be an organizer.
3. **Fill the page.** The `.organizer` area is flex; make your body stretch to
   fill it (use `flex:1`, the `.fill` helper, `height:100%`). No large empty gaps.
4. Content-agnostic: use generic placeholders (Topic A/B, Category, Cause,
   Idea…), NOT Unit 1 history content.
5. Legible in grayscale, AA contrast. Keep body text ≥ 8pt.

## CSS primitives available (from SHARED_CSS — use these, add extra_css as needed)
- Layout: `.row` (flex row, gap), `.col` (flex col, gap), `.fill` (flex:1, min-0).
- `.canvas` — a flex-column full-height wrapper; put your structure inside so it fills.
- `.prompt` — centered instruction line (use `<b>` for emphasis). Put at top of body.
- Label band: `<div class="band navy|red|gold sm">LABEL</div>` (dark = OK, it's a label).
- Writable well: `<div class="well [navy|red|gold] [tint-navy|tint-red|tint-gold|tint-green|cream] [lines] [top]"></div>`
  - `.well` is light with a subtle border; `.lines` adds faint dotted writing guides;
    `.top` gives all-round rounded corners (use when there is no band above it);
    tint-* is a very light wash (still writable). Put a band + well together to make a titled box.
  - `.cue` (absolute, top-left tiny caps label inside a well) and `.wpad` (padding) and `.hint` (italic helper) are available.
- Arrows: `<div class="arr-d"></div>` (down triangle), `<div class="arr-r"></div>`
  (right triangle), `.arr-lbl` for a small caption. Or draw connectors in inline SVG.
- Colors as CSS vars: `var(--navy) var(--red) var(--gold) var(--cream)` plus tints
  `var(--navy-tint) var(--red-tint) var(--gold-tint) var(--green-tint)`.
- Inline SVG is encouraged for circles/hubs/lenses/timelines. Use light fills
  (`#EEF1F7` navy-tint, `#FBEEEF` red-tint, `#FAF3E2` gold-tint) with colored
  strokes (`#1F3A5F #B22234 #C9A227`). Add faint dashed writing guides
  (`stroke="#B9C2D0" stroke-dasharray="2 5"`).

## Build + self-QC loop (REQUIRED — iterate until each page looks right)
```
cd /home/user/trooptoteacher-history/Unit1_Teacher_Graphic_Organizer_Toolkit
python3 src/build_one.py pack_04_tchart.py          # build ONLY your pack(s)
python3 render.py png 04_tchart_blank.html          # -> exports/04_tchart_blank.png (1632x2112)
```
Then **open the PNG with the Read tool and inspect it**. Check: nothing clipped
at the page bottom, no big empty space, writable areas are light, labels legible,
footer present. Fix your pack and re-render until it is clean. Only build/render
YOUR pack files (do not run src/build.py — it imports everyone's packs).

## Deliverable
Write your `pack_*.py` file(s) and iterate until every assigned page renders
cleanly. Report the slugs completed and confirm each passed visual QC.
