# Narrative Textbook — Build & Edit Conventions (LOCKED)

The single spec for the History Hack narrative illustrated textbook ("To Form a More Perfect Union"
line). `render_textbook.py` + `print-contract.css` implement it. Build to this; do not re-derive from a
rendered PDF.

## Page order (per part)

1. **Cover** — full-bleed hero art (`@page cover`, margin 0). Real illustrated cover; swappable image asset.
2. **Foreword** — the founder's "why & vision," in the house-author voice, signed, closing on the
   dedication line. *Page-fill-exempt* (fills once personalized).
3. **Contents (TOC)** — B&W-safe, generously spaced; a primary-source image fills residual space.
4. **Meet the Crew** — ALL crew on **one** page (dedup; never repeat the crew spread). Portrait or a
   monogram placeholder ("SC" / "MM") until real art lands. Carries a "Your Seat on the Crew" self-check.
5. **How This Book Works** — the method + an **evidence-based, cross-curricular matrix** + a
   "Ready-Graduate / ACT" check.
6. **Unit divider** — **Arabic** unit number (never Roman — "UNIT 2", not "UNIT II"); B&W-safe standards
   **chips** (no dark block); Essential Question; a **"Before You Fly"** anticipation guide + SMART goal +
   ACT self-rating.
7. **Who you'll travel with** — the unit's era-friends (composite, marked fiction) + Witness Lens; a
   **"Make Your Call" prediction** block.
8. **Stops** — one per standard (see template).
9. **Arc of the Union** — its own section: the coordinate-plot activity (see spec).
10. **Back matter** — image credits, a note on sources, About. **Strip** the internal Permissions/Publishing
    checklist and spine/production notes from any distributed file.

## Stop template (one per standard)

- Header: `N` + short stop title; standard code + verbatim learning target.
- **Spark hook** callout ("What do you notice?") + a 2-line **first-glance jot**.
- **Media row (two columns)**: left = the primary-source image (repo-first; LOC/NARA fallback; public-domain,
  cited). Right column stacks, top to bottom:
  - **Source It First** band — **WHO / WHEN / WHY** + one "read it closer" question.
  - **HVT — "High-Value Target"** box (gold-accented, `◎ HVT · lock this in`): the single **must-know
    takeaway** for that standard (the EOC-tested core), written as a concise summary-label of the LOCKED
    content — never new narrative or a new fact. The HVT balances the tall image and gives every stop a
    tested-essential anchor. HVT lines are builder synthesis → flag for `tn-content-specialist` review.
- **Word Wall · EN/ES** — the stop's vocabulary from the canonical vocab bank, bilingual (3–4 terms; trim to
  3 on the single densest stop so the page passes the fill gate).
- **State Connection** (Tennessee for the flagship; derive per course; verified fact or an honest inquiry
  prompt flagged `[pending historian-verified fill]` — never fabricate).
- A **▶ Flight Log** bridge cue at the foot, leading into the facing writing page.
- A facing **writing page** (see below).

Deterministic page-fill: scale the source-image height inversely to each stop's content weight (hook +
vocab) so every stop self-levels to ≥ 90% without a manual pass; the build gate confirms it.

## Writing page (CER + app handoff)

Claim (one sentence) → **two-column evidence** (one per perspective) → **self-grade rubric** (4/3/2/1,
crew-voiced) → the debriefer's **one-sentence debrief** → **Writing Lab** handoff:
"go to History Hack online → Writing Lab, type your response, check it against the rubric for instant
feedback." This is the workbook⇄app hand-off; keep it on every stop.

## Arc of the Union — coordinate-plot section (cross-curricular)

Two pages:
- **Chart it:** a capture table of the unit's milestones (year + label from the course narrative
  `arcPoints`); students score each **−3 (Away) … +3 (Toward the promise)**; an **SVG coordinate grid**
  (Y = Away↔Toward with a bold 0 baseline; X = milestones 1..n by year) to plot each score and **connect the
  points into the arc**.
- **Read it:** **Math** (each call is an ordered pair; connected points = a line graph; find the
  trend/slope; compute the **mean**), **Science** (plotting reveals the pattern a table hides; name the
  steepest climb/drop and the turning point), **Correlate** (compare a partner's arc — same evidence, different
  plot), **Extrapolate → next unit** (extend the trend to predict the next era), and the **Essential-Question
  answer defended with the graph**. This is the anchor cross-curricular math/science correlation; every unit's
  Arc works the same way.

## Flight Log companion (write-in student log) — `build_flightlog.py`

Every unit ships a **Flight Log**: the write-in student companion to the reader. LOCKED structure:
- **Brand cover** — the course hero art, full-bleed, with a gold-bordered navy band overlay
  (`✈ Student Flight Log · Unit N · <title> · <span>` + NAME/PERIOD lines). Reuse the same cover asset as
  the reader; this is the "badass brand cover on top."
- **SMART goals** page (short/mid/long-term ladder + how-the-cross-check-works note).
- **One log entry per stop**, each carrying the **bidirectional cross-reference** — the entry names exactly
  where in the narrative to write from (*"write from <Debriefer>'s debrief on the Stop N page (Unit N,
  US.xx)"*), and the reader's Stop-N writing cue names the matching entry (*"log it as Flight Log · Entry
  N"*). **Both sides are generated from the SAME stop list**, so the cross-reference is accurate by
  construction and can never drift. Each entry = claim + evidence write-in + self-grade + Writing-Lab handoff.
- **Arc-of-the-Union capture** — points back to the reader's Arc section; student brings the mean/verdict home.

Course-parameterized identically to the reader (per-unit stop list from `courses/<id>/course.json` +
narrative source). Same B&W-safe contract; teacher-key edition adds answers (teacher-side only).

## Value-block menu (white-space value rule)

When a page is short of 90%, insert a `.value` block — pick for fit and impact, never filler:
`Before You Fly` (anticipation guide + goal + self-rating) · `Make Your Call` (prediction) ·
`Your Seat on the Crew` (metacognitive self-check) · `Ready-Graduate Check` (ACT tie + reflection) ·
`Source It First` (WHO/WHEN/WHY) · `Correlate` / `Extrapolate` (data reasoning) · a first-glance jot ·
extra CER writing room. All are research-anchored (anticipation guides, prediction, retrieval, goal-setting,
metacognition — Hattie ≥ 0.40).

## Page-fill QC gate

`render_textbook.py` measures each page's filled height below the footer and **fails the build** if any
non-exempt page < `TARGET_FILL` (90). Cover + foreword exempt. On failure, add a value block or enlarge
sourced media — then re-render until QC PASS. Never ship a short page.

## Edit-in-code workflow (existing ad-hoc PDFs)

1. Extract images from the target PDF into `references/assets` (dedup by xref).
2. Capture narrative + front-matter text into the course `content-build/<course>/narrative/unit-NN.json`
   (this is the durable source the ad-hoc PDFs lacked).
3. Apply the requested edits in the content + `print-contract.css` (never in the flattened PDF).
4. Re-render; pass the page-fill gate + the shared release gates.
5. Split per unit (cover + How-This-Book-Works + unit + credits) and export the full part; replace the
   served files in `history-hack-web-app/public/textbook-pdf/` and register in `app/textbook/page.tsx`.

## Assets still required per course

Real Flight-Crew portraits for **Sam Calloway** and **MSgt "Muck"** (others exist); commit them to the repo
(`public/images/textbook/crew/`) — never Azure-only. Cover art per course.
