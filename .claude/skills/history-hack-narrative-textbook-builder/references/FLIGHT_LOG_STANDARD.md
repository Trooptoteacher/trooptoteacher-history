# Flight Log & Narrative-Textbook Build Standard — CODIFIED

> **Standard version:** `FL-2026.08.10`  ·  **Build date:** **2026-08-10**
> This is the single source of truth for how the *To Form a More Perfect Union*
> Flight Logs and narrative textbook are built. The version + date are stamped into
> **every PDF's metadata** and printed **on-page** (Flight-Log intro + textbook
> credits colophon) via `bookmeta.BUILD_DATE` / `bookmeta.BUILD_VERSION`, so the
> most-recent build is always identifiable at a glance. **When the standard changes,
> bump `BUILD_DATE` and `BUILD_VERSION` in `bookmeta.py` and update this file.**

Owner: Sean Reynolds ("Sam Calloway" narrative voice), TroopToTeacher Technologies LLC.
Builders: `build_flightlog.py` (Flight Logs), `render_proof.py` (Unit 1 reader),
`build_unit.py` (Units 2+), `assemble_web.py` (serves to `public/`), `bookmeta.py`
(shared colophon, credits, folios, metadata + **build stamp**).

---

## 0. What the Flight Log IS (do not lose this)

The Flight Log is the **engagement surface** — the place students interact when they
"show up to the thing." The high-value loop is non-negotiable:

1. **Textbook, Stop N** — the flight crew engages the student *inside the narrative*
   and hands them a primary source and a call to make.
2. **"Capture it in your Flight Log."** The crew (the Debriefer, **MSgt "Muck"**)
   points the student to **Flight Log Entry N**.
3. **Flight Log, Entry N** — the crew **re-engages** the student and they **CAPTURE
   DATA**: what the source showed, their claim, evidence on both sides, the tension,
   vocabulary, and a self-grade.
4. **Fly it to the app** — the student types the call into **History Hack online →
   Writing Lab** for instant feedback, then revises.

**Entry N always equals Stop N** — the Flight Log stop index is derived from the same
stop list as the reader (`resolve()` in `build_flightlog.py`), so the cross-reference
can never drift.

The Flight Log is **not** a page of blank lines. It is a **data-capture instrument**
wrapped in the crew's voice. If a page reads as "a prompt and then white space," it
has regressed and must be rebuilt.

---

## 1. LOCKED guardrails (every page, every unit)

| # | Guardrail | Enforced by |
|---|-----------|-------------|
| G1 | **≤10% white space** (≥90% page fill) on every content page. Cover is exempt (full-bleed). Write-in room is **framed by structure**, never a blank bottom. | `verify_fill()` in `build_flightlog.py` — prints `PASS`/`WARN` per build; enforced on **both** student and teacher editions. |
| G2 | **Data capture first.** Every student entry captures: source read → claim (with sentence frame) → evidence **both sides** (BOUGHT/COST organizer) → name-the-tension line → Word Wall → self-grade → app handoff. | `entry_student()` card template. |
| G3 | **UDL embedded** — multiple means of engagement (crew voice, relevance), representation (sentence frames, graphic organizer, Word Wall, visual rubric), and action/expression (**write · sketch · say-it-in-the-app** choice). | Card + `STUDENT_CSS`; UDL chip on capture step 1. |
| G4 | **Crew re-engagement.** Each entry opens with **MSgt "Muck" · radio in**, tying back to Stop N. | `entry_student()` `.crewcall`. |
| G5 | **Arc = a real graph.** Student plots on a **blank labelled coordinate grid** (−3…+3, one dot per milestone, connect the arc). Teacher key shows the **plotted exemplar** (points + connected line + dashed mean). | `_arc_svg(..., plot=False)` student grid / `plot=True` teacher exemplar. |
| G6 | **Teacher-side stays teacher-side.** Exemplar CERs, answer keys, historian's-read Arc scores, misconception/reteach/extension appear **only** in the Teacher Edition, never the student edition. | `EXEMPLARS`, `APPENDIX`, `ARC_SCORES` gated on `teacher`. |
| G7 | **Source of truth only; disclose status.** No fabricated history. Assessment/exemplar content labeled **classroom-formative · pre-field-test**; flag for `tn-content-specialist` before adoption print. | Colophon + teacher `tnote`. |
| G8 | **Every page numbered; copyright + author attribution embedded** (on-page + PDF metadata). | `bookmeta.paginate()`, `bookmeta.stamp_metadata()`, colophon. |
| G9 | **Build stamp** — dated version on-page and in metadata so the most-recent build is identifiable. | `bookmeta.build_stamp_html()` + `BUILD_DATE`/`BUILD_VERSION`. |
| G10 | **B&W print-safe** — meaning survives grayscale; navy/gold structure prints as gray, never color-only distinctions. | `style.css` palette. |
| G11 | **Specific cross-surface handoff (LOCKED).** The crew always tells the student *where to write and what it pairs with* — never a page that leaves them guessing. Every **Cornell page** names its **deck DI slides**; every **Entry's** Muck radio-in cites its **reader Stop N** and says "capture it here"; the **reader** cues "**Open your Flight Log to Entry N**" (Box 2 at the Climb, Boxes 1,3–5 at Wheels Down); the **teacher deck's FOLLOW ALONG** divider + first-DI Cornell cue + Student-Activity cue name the **Mission Book Stop N + Flight Log Entry N**. **Stop N = Entry N = US.0N** across reader ⇄ deck ⇄ Flight Log, derived from one stop list — it can never drift. | `resolve()` stop index; `cornell_page` banner; `entry_*` `.crewcall`; reader Flight-Log cues (`render_proof.py`); deck FOLLOW ALONG / Cornell / activity cues. Audit with `history-hack-lesson-flow-qc`. |
| G12 | **Merged per-Stop order (LOCKED).** Cornell Notes for Stop N sit **immediately before** Entry N; the log never batches all notes then all entries. | assembly line in `build_flightlog.py` (`cornell_page(n)+entry(n)` per stop). |

**"Names the tension" is the rubric spine.** A **4** names the trade-off (what a moment
**cost** vs. what it **bought**) with evidence on **both** sides; one-sided caps at **2**.
The BOUGHT/COST two-column organizer exists to make that move physical.

---

## 2. Student Flight Log — page structure (LOCKED · per-Stop MERGE)

Front matter first; then the unit runs **Stop-by-Stop** — each Stop's **Cornell Notes
page is immediately followed by that Stop's Data-Capture card**, so the log flows with
the slide deck and the reader. **Never** all-Cornell-then-all-entries (that reads as
"just Cornell notes" and is a regression). Assembly order in `build_flightlog.py`:
`{cover}{how}{wherestand}{readiness}{cornell_intro}{ per Stop: cornell_page(n)+entry(n) }{geo}{arc}`.

1. **Cover** — hero art + Flight Log band + NAME/PERIOD (exempt from fill gate).
2. **How it works** — the engagement **loop** (Stop N → Entry N → Writing Lab), UDL
   choice menu, SMART goals (Ready Graduate), habit commitment, colophon + build stamp.
3. **Where You Stand** — unit flight map / mastery landing strip (self-plot after each exit ticket).
4. **Flight Readiness** — the Ready-Graduate flight plan.
5. **Cornell intro** — the Cornell method (notes → self-quiz → summary) + the
   **Deck ⇄ Cornell map** (Cornell Stop N = Standard US.0N's Direct-Instruction slides).
6. **Per Stop, N = 1…7 (MERGED, in order):**
   - a. **Cornell Notes · Stop N** (`cornell_page`) — cue / notes / summary grid; the
     banner names the **exact deck DI slides** (e.g. "Teacher Deck slides 9–11"). Take **during** the lesson.
   - b. **Data-Capture Card · Entry N** (`entry_student`), immediately after its Cornell:
     - `.crewcall` — **MSgt "Muck" · radio in** + `US.0N` pin, citing **Stop N** in the reader.
     - ① **The source — what did it show you?** (write / sketch / say-it-in-the-app)
     - ② **Your call — one-sentence claim** + sentence frame.
     - ③ **Your evidence — both sides:** BOUGHT (gain) | COST (price) two-column.
     - ④ **Name the tension:** "It **cost** ____ but it **bought** ____."
     - ⑤ **Word Wall** (3 terms) + **Self-grade → fly it** (4-3-2-1 + score box).
     - **Web · Writing Lab** app handoff.
7. **Geography Waypoints** (Unit 1: US.03 Exodusters, US.06 industrial centers) — the
   map lives in the reader/deck; the **marking/writing task** lives here (read-the-land capture).
8. **Arc of the Union — plot your Arc** — blank coordinate grid + numbered milestone
   legend + read-your-graph capture (mean / trend / steepest) + make-the-call writing
   + debrief-for-Muck + Writing Lab handoff.

## 3. Teacher Flight Log (Answer Key) — page structure

1. **Cover** (teacher band; "not for student distribution").
2. **How to use** — master 4-3-2-1 rubric, "three moves that raise any score,"
   grade-fast note, what's-on-each-stop-page legend, disclosure, colophon + build stamp.
3. **Answer Key & Teacher Guide, one per Stop** (`entry_teacher`): exemplar CER
   (claim + 2 evidence + Muck's debrief) + self-grade anchor + 4-3-2-1 rubric +
   **common misconception / reteach / extension** + **facilitate / watch-for /
   differentiate / time** + EL·MTSS sentence frame + app handoff.
4. **Arc of the Union — a historian's read** — the **plotted exemplar graph**
   (points + line + dashed mean) + "one defensible arc — not an answer key"
   disclaimer + a historian's-read narrative + run-it-in-class. Then the **scoring
   table** (per-milestone read) + what-to-look-for + cross-curricular (math/science)
   + verdict sentence stems + score band + debrief prompt.

Teacher graph and scores are **one defensible reading**, not an answer key: a student
who scores a milestone differently is **not wrong** if they defend it with evidence.

---

## 4. Build & verify

```bash
# Student + teacher, one unit:
python3 build_flightlog.py <N>            # student
python3 build_flightlog.py <N> teacher    # teacher key
# Everything (textbook readers + all flight logs) served into public/:
python3 assemble_web.py
```

`verify_fill()` prints a `PASS`/`WARN` line per build (target 90%). **A `WARN` is a
build failure to fix, not to ship** — densify with real capture/teacher content or
scale the element (grid height / table row padding / milestone legend) to the unit's
milestone count. Never fill by relocating a gap above the footer — that games the
metric and violates the integrity standard. Confirm visually by rendering pages to
images (pixels are authoritative for what a student sees).

## Reference-unit additions (Unit 1 platinum reference build)

A reference Flight Log mirrors the reader's structure:
- **Geography Waypoints** — the write-in mirror of the reader's Geography section: a **real blank U.S.-outline
  plot box** (never a placeholder) + locate/interpret prompts, run through the same `verify_fill()` gate as
  every other page. **Fill status (honest):** a few geography/goals pages sit just under 90% (student FL
  ~66–80%, teacher FL ~89%) — the same fill-engine gap held on the reader; not yet a full PASS.
- **Dimension chip per entry**, matching the reader stop's chip (same content-dimension tag on both surfaces).
- Same accessibility floor as the reader: tagged/UA, `/Lang`, ≥9pt (decorative glyphs as artifacts), data grids
  expose axes/scale as live on-page text; Flight-Log outlines may start at H2 but never skip a heading level.
  Accessibility re-verified Grade A on the America 250 palette (2026-08-09).

## 5. Change log

- **`FL-2026.08.09` (2026-08-09)** — America 250 re-skin (Heritage Blue / Patriot Red / Muted Gold / Founders
  Cream, inherited from the shared `style.css`); THE LOOP expanded to the self-grade → compare-to-app cycle;
  accessibility re-verified Grade A. Fill gate still held on a few geography/goals pages (see above).
- **`FL-2026.08.08` (2026-08-08)** — Added Geography Waypoints (blank U.S.-outline plot box) + per-entry
  dimension chips. Governing skill: `history-hack-narrative-textbook-builder`.
- **`FL-2026.08.06` (2026-08-06)** — Codified this standard. Student Flight Log rebuilt
  from thin blank-line entries into full-page **UDL data-capture cards** with the crew
  re-engagement loop; Arc page rebuilt as a **plot-it-yourself coordinate grid**;
  `verify_fill()` gate enforced on **both** editions; dated build stamp added to
  on-page colophon + PDF metadata. All six flight logs (student + teacher, Units 1–3)
  and the Unit 1–3 textbook readers PASS ≥90% fill.
