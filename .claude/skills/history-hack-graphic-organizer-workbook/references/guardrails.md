# Guardrails — non-negotiable

These are the rules that separate the platinum product from generic worksheets. They were set for Unit 1
and every unit must hold them. When a request conflicts with a guardrail, surface it rather than break it.

## Source of truth — fabricate nothing
- Standards, learning targets, topics, dates, names, statutes, and Tennessee connections come from the
  official sources (see `sourcing.md`). Never invent a historical detail, a citation, or a TN tie.
- If you cannot source something, leave it as a student-completed blank or omit it — do not guess.
- Do **not** print the label "WCS" anywhere in a deliverable (internal alignment only).

## Real, interactive visual organizers — not tables of ruled lines
- A Venn is actual overlapping circles; a concept web is a center hub with connected bubbles; a timeline
  is a line/spine with ticks and event cards; Frayer is a 4-quadrant box with a center oval; CER is
  linked boxes with arrows. The *shape* carries the thinking. Never substitute a grid of blank rows.
- Fill the page. Each organizer plus its support strip should occupy the sheet with no dead space.

## Writable fields must be LIGHT
- Anywhere a student writes is white or cream (optionally a very light tint), ideally with faint dotted
  guide lines. **Never** put a dark bar where a student is expected to write.
- Dark navy/red bands are for **labels only**. Pre-filled labels on labeled organizers may be dark; the
  writing areas next to them stay light.
- Keep prompt/label text *out of* the writing space: put a cue in the label strip or fade it to a
  watermark, so the student has room. (Watch the center of hubs/ovals — a common offender.)

## Venn diagrams — the label rule (learned the hard way; check this every time)
Venns are the most-flagged organizer. Text kept drifting *outside* the circles because HTML overlay labels
are positioned to the full frame, but the SVG letterboxes (scales to fit, leaving side margins) — so a
label at, say, `left:12%` lands in the empty margin, not in the lobe. **Never position Venn text as HTML
overlays over the circles.** The rule:
- **Region labels and in-lobe hints go INSIDE the `<svg>`** as `<text>` at viewBox coordinates, so they
  track the geometry no matter how it scales. Anchor at the lobe centers — the non-overlapping part of
  each circle, roughly halfway between the outer edge and the lens (for two circles at cx 330/570 r 245,
  that's ≈ x 250 left / 650 right; lens ≈ 450). **Watch the vertical, too:** a circle is narrow near its
  top and bottom, so a wide caption like "ONLY WASHINGTON" placed near the apex will run past the arc even
  though its center is inside. Drop region captions down to where the chord is wide enough for the full
  string (≈ 8–12% below the top), or shorten them — then confirm at render that both ends clear the arc.
- **Topic identity labels + write-lines go in a legend row ABOVE the diagram** (HTML, clearly outside the
  circles): a colored swatch/dot + "Topic A: ____", one line for A/B/C. Do not float "Topic A:" over a
  circle's edge.
- **Region captions (ONLY A / A&B / ALL 3 / BOTH) are minimized and faded** (small, light gray, ~11–13pt)
  so they read as watermarks and leave the lobes open to write in.
- Keep dotted writing guides in each lobe; verify at render that every label sits *inside* its circle.
The corrected US.07 Venn and the Venn-3 legend in `assets/example_packs/` are the reference implementations.

## Neutral, unbiased framing — tighten the wording every time
Let students reach their own judgments; the organizer stays descriptive and even-handed. This applies to
**titles, band labels, prompts, and criteria** — not just body text. Concrete calls from Unit 1:

| Don't write (editorializing) | Write instead (neutral, sourced) |
|---|---|
| "Winners & Costs of Westward Expansion" | "Westward Expansion — Who Benefited, Who Bore the Cost" |
| a criterion "A win or a loss" | "Where things stood by 1900 — what had changed?" |
| "who lost land?" | "whose land was taken?" (states the sourced fact) |
| "good vs. bad," "hero/villain," value verdicts baked into a label | present both lenses evenly; let the student decide (e.g., "Captain of Industry _or_ Robber Baron?") |

Rules of thumb: avoid win/lose, hero/villain, good/bad, and "progress" stated as fact. Two-sided
organizers give each side equal visual weight and identical prompt structure. A judgment belongs in a
student's response line ("your verdict, because…"), never pre-decided in the design.

## Teach the teacher (the "why")
- Every organizer carries a short **"When · Why"** blurb: when to reach for it and why it works, ending
  with a cited evidence hook. Approved evidence base: Marzano (identifying similarities/differences =
  highest-yield), the TN Social Studies Practices (e.g., SSP.05 for cause-effect & chronology), UDL 3.0,
  MTSS. Cite only these; never invent a study.

## Differentiation on every page — "Make it work for every student (UDL · MTSS)"
- A three-part strip: **Scaffold** (sentence starter / word bank / partner-first), **Extend** (a
  higher-DOK push), **Show it your way** (UDL response choice: write / say / draw / build).

## Tennessee connections — a foundation and a differentiator
- Include the dedicated **Tennessee Connection** organizer (local ↔ national + "why the local story
  matters"), call it "our signature move" in the Quick Guide, and flag the ★ TN tie on any labeled
  organizer with a sourced connection. Only sourced ties (see `sourcing.md`).

## Brand + reproducibility + accessibility
- Palette: navy `#1B2A4A`, red `#B22234`, gold `#C89B3C`, white, cream `#F7F5EF`.
- Footer on **every** page: **"U.S. History Hack™ · © 2026 TroopToTeacher Technologies LLC"** (trademark
  + copyright).
- Mark reproducibles **Reproducible** (teachers may copy).
- Legible in grayscale when printed; WCAG-AA text contrast; alt text on exported images. US-Letter portrait.
- Carry a per-page **time estimate** so teachers can pace a class period (see `times.py`). These are
  planning estimates (launch + independent work + share); confirm the framing the user wants.
