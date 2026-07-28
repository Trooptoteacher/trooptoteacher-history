---
name: history-hack-graphic-organizer-workbook
description: >-
  Builds the TroopToTeacher "U.S. History Hack" Teacher Graphic Organizer Workbook — reproducible,
  on-brand, print-ready graphic organizers for high-impact areas of each unit (US.01–US.95), at the
  platinum quality standard set by Unit 1. Use this whenever the user wants to create, extend, or
  revise graphic organizers, an organizer workbook/toolkit, per-standard "best-fit" organizers, blank
  reusable reproducibles (Venn, T-chart, matrix, timeline, concept web, Frayer, CER, HIPPO, KWL, 5 Ws,
  cause-effect, main idea, problem-solution, Tennessee Connection), a "Which Organizer, When" guide, or
  an SSP crosswalk for any History Hack unit — even if they don't say the word "skill" or "workbook."
  Trigger on requests to make a unit's organizers "match Unit 1," build organizers that align with the
  student/teacher workbooks and slide decks, or pre-make organizers for a unit's high-impact standards.
---

# History Hack — Teacher Graphic Organizer Workbook

You are building one unit's slice of a **10-unit Teacher Graphic Organizer Workbook** for
**TroopToTeacher Technologies — U.S. History Hack™**. Unit 1 is the **platinum standard**; every unit
must match it in structure, quality, brand, and rigor. This skill bundles the *actual working design
system and render pipeline* used to build Unit 1, so you reproduce that quality exactly rather than
reinventing it.

**This is a teacher-facing product for district adoption.** The bar is high: nothing fabricated, every
organizer genuinely useful, every page print-ready and on-brand. Read the guardrails before you build.

## What a unit contains (the fixed structure)

Every unit's organizer set is assembled from these page types, in this order:

1. **"Which Organizer, When" Quick Guide** — a task→organizer→why reference table (find the *verb* in
   the assignment, reach for the matching organizer), with per-organizer time estimates and a class-period
   pacing note. Solves the teacher's real pain point: *which* tool for *this* task.
2. **SSP Crosswalk** — maps each TN Social Studies Practice (SSP.01–06) to the organizers that build it
   and where it lives in the unit. Makes every organizer double as a skills tool.
3. **Blank reproducibles** (course-wide, content-agnostic — reusable in any unit/subject): Venn (2 & 3),
   T-chart, compare/contrast matrix, cause & effect, timeline, concept web, main idea & details, KWL,
   5 Ws, problem–solution, Frayer, CER, HIPPO, **Tennessee Connection**. Add others when a task needs them.
4. **Pre-labeled best-fit organizers** — one per standard in the unit, matched to that standard's task and
   pre-loaded with its sourced content. **Tennessee connections flagged wherever a sourced tie exists.**

## The four things that make it platinum (read the references)

Before building, read these — they are the difference between "some worksheets" and the platinum product:

- **`references/guardrails.md`** — the non-negotiables: source-of-truth only (fabricate nothing), real
  visual organizers (not ruled-line tables), LIGHT writable fields, brand palette + TM/© footer,
  neutral/unbiased framing, accessibility (grayscale-legible, WCAG-AA), reproducible mark, per-page time.
- **`references/sourcing.md`** — **where the content comes from, and how to make it match the student
  workbooks + student/teacher slide decks.** Read this first for any new unit; it prevents drift.
- **`references/design-system.md`** — the house style: page anatomy, brand tokens, the CSS primitives,
  and how the render pipeline works.
- **`references/organizer-catalog.md`** — every organizer type, when it best fits (the task verb), the
  evidence base for its "why," and the Quick Guide / SSP mappings.
- **`references/unit1-platinum-reference.md`** — Unit 1 as the worked gold-standard example: exactly what
  was built, the 7 labeled organizers, and the sourced TN ties. Copy its patterns.

## The build pipeline (bundled — reuse it, don't rebuild it)

The `scripts/` directory *is* the Unit 1 machinery. Work inside a unit folder like
`UnitN_Teacher_Graphic_Organizer_Toolkit/` with `src/` (pack files) and `pages/`, `exports/`.

- **`scripts/toolkit_lib.py`** — the shared design system. `render_page(...)` produces one standalone,
  print-perfect HTML page with the identical header / when·why blurb / UDL·MTSS strip / footer / time
  chip. **Do not fork the house style — every page must call this.**
- **`scripts/build.py`** — imports every `src/pack_*.py` and writes `pages/<slug>.html` in slug order.
- **`scripts/build_one.py`** — builds only named packs (use while iterating / for parallel authors).
- **`scripts/render.py`** — renders pages to 2× PNG (`render.py png`) and a combined US-Letter PDF
  (`render.py pdf`) using the pre-installed headless Chromium. This is your QC loop and your exporter.
- **`scripts/times.py`** — per-slug time estimates (a `TIMES` dict) surfaced as a header chip + Quick
  Guide column. These are planning estimates (launch + work + share); confirm the framing with the user.

Each organizer is a small `src/pack_<NN>_<name>.py` exposing `ORGANIZERS = [dict(slug, title, kicker,
chips, why, body, extra_css, udl, role, tn), ...]`. The `body` is the visual organizer (HTML + inline
SVG); `extra_css` is its component CSS. See `assets/example_packs/` for a blank (Venn), a labeled
T-chart (with a TN box), a labeled timeline, and the Quick Guide generator.

## Process for building a unit

1. **Source first (do not skip).** Follow `references/sourcing.md`: pull the unit's standards, learning
   targets, and sourced content from the canonical files, and — critically — read the unit's **student
   workbook chapter, student packets, and the student/teacher slide decks** to find the *high-impact
   areas* those materials emphasize. Pre-make organizers for exactly those areas so the workbook aligns.
   Record every fact's source. If you can't source a TN connection or a standard detail, don't print it.

2. **Map best-fit organizers.** For each standard, pick the organizer whose structure matches the task
   (compare 2 → Venn/T-chart; compare 3+ on criteria → matrix; causes/effects → cause-effect; sequence →
   timeline; make a claim → CER; analyze a source → HIPPO; weigh two sides → T-chart/problem-solution;
   local↔national → Tennessee Connection; …). Use `references/organizer-catalog.md`. Don't force a type.

3. **Build the pages.** Copy the `scripts/` into the unit's folder. Author the blank reproducibles (these
   are reusable — copy Unit 1's packs verbatim where content-agnostic), the labeled per-standard packs,
   the Quick Guide, and the SSP crosswalk. For parallel authoring, hand sub-authors
   `assets/authoring-contract.md`.

4. **Render + QC every page.** Run `render.py png` and *open each PNG* (Read tool). Verify: real visual
   structure, writable areas light, nothing clipped at the bottom, footer present, no dead space. Two
   checks fail most often — do them deliberately on every unit:
   - **Venn labels inside the circles.** Region labels/hints must be `<text>` *inside the SVG*; topic
     labels + write-lines go in a legend row *above* the diagram; region captions are small and faded.
     HTML overlays drift into the letterbox margins — see the Venn rule in `references/guardrails.md`.
   - **Wording review pass.** Re-read every title, band label, prompt, and criterion for loaded language
     (win/lose, hero/villain, good/bad, "progress" as fact) and neutralize it — the framing table in
     `references/guardrails.md` has the exact substitutions. Let students reach the judgment.
   Fix and re-render until clean.

5. **Assemble + export + deliver.** `render.py pdf` builds the combined US-Letter PDF. Then commit/push
   the source, import the public PDF URL into **Canva** (brand kit `kAG39-EGTcM`) for an editable design,
   export PDF + PNGs, and give the user the design link + files. See `references/design-system.md` for
   the Canva/export/delivery details and known environment constraints.

## Guardrails you must never relax

Fabricate nothing. Do not print the label "WCS" anywhere. Writable fields stay light. Every page carries
the footer **"U.S. History Hack™ · © 2026 TroopToTeacher Technologies LLC"**. Keep framing neutral — let
students reach judgments (e.g., "Who benefited / Who bore the cost," never "winners/losers"). Only use
sourced Tennessee connections. When in doubt, check `references/guardrails.md`.
