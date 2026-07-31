# Per-Standard Activity Architecture

Each standard is built by `block(code)` and is a **fixed sequence of self-contained, printable
worksheets**. Every page must (a) show visible notebook lines everywhere a student writes, (b) fit
its page(s) with no bleed, and (c) keep MTSS/UDL jargon off the student page. Below is the locked
sequence with the **why** behind each recent design decision (so future edits don't undo them).

## Opener — FRONT page (standard launch)
Order: `H1` standard heading → TN standard line (bold label + verbatim text) → **LEARNING TARGETS**
callout ("I can…") → optional `Lenses` line → **CORE PATH** `coreCallout` → optional ★ Tennessee
Connection → **SET YOUR GOAL** callout + `ruled(3)` → **HOOK** callout + `ruled(3)` → **ACTIVATE**
callout + `ruled(4)` → **FIRST IMPRESSIONS** callout + `ruled(3)`.
- **CORE PATH is simplified for students** — it says everyone works the same standard at the same
  rigor and points to the back page for supports. It does **not** name UDL/MTSS. (Students shouldn't
  see the framework jargon; the mechanism stays teacher-side.)
- Front prompts each get real writing lines (3–4) so the launch page fills (~75%) without bleeding.

## Opener — BACK page: "Getting Started — supports for this page"
`H2 {brk:true}` then cream callouts, each a support for a front prompt:
- **WHAT "CORE PATH" MEANS** — plain-language: same standard, same level; "support options" are extra
  ways in (starters, example, partner, recording); they never lower the bar.
- **SET YOUR GOAL — how to write a strong one** — bolded inline labels (array-of-runs): *Example
  goal* / *How to build it* / *Sentence starters*.
- **HOOK — sentence starters** · **ACTIVATE — what it means & starters** · **FIRST IMPRESSIONS —
  what to write**.
- **KEY WORDS TO WATCH FOR** — `s.vocab.map(v=>v.term).join('   ·   ')`.
- **NOW TRY IT — draft your goal** callout + `ruled(6)` at the bottom, so the reference page carries a
  real workspace and doesn't leave "excess empty space at the bottom."
- Rationale: the user wanted supports *available but not cluttering the front*, and specifically "be
  mindful not to have excess empty space at the bottom of any page." The goal-draft lines are the fill.

## Activity 1 — Vocabulary (Word Bank / Reference)
`H2 {brk:true, mins:10}` → intro line (Spanish column = access, not assessment translation) →
`dataTable(['Term','Student-friendly meaning','Spanish'], …, [2723,4347,2722])` →
**LANGUAGE SUPPORT** callout with **bolded** `Pronunciations:` label (array-of-runs) →
`vocabSelfCheck` knowledge-rating table (`[3092,1675,1675,1675,1675]`, 1–4 ruled cells) →
**MAKE IT YOURS (RESPONSE CHOICE)** bold inline label → QUICK WRITE (`ruled` notebook lines).
- Bold the label on any "meaning / response choice / pronunciations" line — user standard across all
  worksheets.

## Activity 2 — Vocabulary Studio (Frayer) — FRONT
`H2 {brk:true, mins:7}` → **RESPONSE CHOICE — three ways to complete each studio** with **concrete,
bolded** options: **WRITE** (fill the four boxes), **SAY IT** (partner / teacher / 20–30s voice note —
term, meaning, example), **DIAGRAM** (Sketch Studio on the back). Then per frayer term: `priorityBar`
(navy term bar) → **Word-bank meaning to build on:** (bold label) → Frayer `writeTable`
`[['',''],['Examples','Non-examples'],['','']]` `[4896,4896]` → **Use it to explain** + `ruled(1)`.
Finish with **CONNECT THE TERMS** callout + `ruled(2)` ("write on the lines — or map it in the Sketch
Studio on the back").
- Rationale: the generic "write, speak, or diagram" gave no room to diagram and no *how* for
  speaking. The front now tells students exactly how; the drawing space lives on the back.

## Activity 2 — Sketch Studio — BACK (draw it or say it)
`H2 {brk:true}` → **SAY IT** callout listing concrete speak options (shoulder partner both ways /
teacher check-in / voice note / stand-and-share) → for **each** frayer term: **DIAGRAM: <term>**
callout + open draw box (~2000–2100) → **CONNECT THE TERMS — concept map** callout + open box
(~2500) for arrows between the two terms.
- Rationale: gives real, labeled space to diagram every priority term and to map how they connect —
  the missing "diagram" affordance.

## Activity 3 — Direct-Teaching Cornell Notes — FRONT + BACK
- FRONT: `H2 {brk:true, mins:20}` → deck/slide reference line → `cornell(cues, notesLabel, n)` (navy
  header, `2448|7344`, ruled notes column) → `ruled(4)` continuation → **DOODLE ZONE** (open box).
- BACK: "keep going, then process & check" → **UDL · CHOOSE HOW YOU CAPTURE IDEAS** →
  `splitDrawWrite(...)` (left open draw box | right ruled lines) → **Key terms to list** →
  `writeBox('Summary — In your own words', 4)` → one **PROGRESS CHECK** question.
- **Name/Class/Date line was REMOVED** — it only appeared on Cornell, was inconsistent, and ate space.
- Guided Support and Light Support backs are optional scaffolds (kept teacher-optional).

## Activity 4 — Close Read (+ Spaced Retrieval & self-check)
`H2 {brk:true, mins:15}` → reading-type disclaimer (authored synthesis, *not* a primary source) →
**CORE PATH** callout carrying the `a.close` passage → **LANGUAGE SUPPORT** → text-dependent questions
→ RESPONSE CHOICE line → **CLOSE-READ EVIDENCE LAB** `writeTable [3264,3264,3264]` (2 rows, lines:2).
Then, when the standard has no map/geo, `retrievalBox(code)`:
- **SPACED RETRIEVAL** callout + 2-row recall `writeTable [3857,5935]` (rowH ~400, lines:1) →
- **CHECK YOURSELF — look back and score how it went** compact self-eval: **2 physical lines** —
  line 1 `Got it right? ☐…  Answer it from memory? ☐…`, line 2 `How did it feel? ☐…`.
- **Rationale + the hard constraint:** the self-check must fit even the FULLEST close-read page
  (longest passage). It was first built tall (header + 3 lines + a writeBox) and **bled onto a nearly
  empty next page** on the longest standard. It was compressed to two inline checkbox lines (dropping
  the extra write box, tightening retrieval/evidence rowH) and verified on the worst-case standard.
  Keep it at two lines. If you add anything here, re-render the fullest standard.

## Activity 5 — Primary Source / Data Analysis (2-page spread)
- FRONT: `H2 {brk:true}` source (image + caption + full public-domain citation) → **FIRST LOOK**
  `ruled(4)` → HIPPO `writeTable` (lines:4).
- BACK: `H2 {brk:true}` "go deeper" → SUPPORT OPTION → SOURCE SYNTHESIS `ruled(5)` → THINK LIKE A
  HISTORIAN `ruled(5)` → SO WHAT `ruled(4)` → CONFIDENCE CHECK-IN.

## Activity 6 — Core Application: Practice Quiz (+ write your own DOK-3)
`H2 {brk:true}` MC practice items (answer key is teacher-side, never printed) → then a separated
"write a DOK-3 question" section: how-to (kept distinct) then **expanded** write boxes —
`writeBox('NOW WRITE YOUR DOK-3 QUESTION HERE',5)` + `writeBox('YOUR ANSWER KEY — one clear,
defensible sentence',4)`.
- Rationale: user asked to separate the how-to from the student's own question/answer and to expand
  the boxes to consume blank space.

## Activity 7 — Constructed Response (CER) — FRONT writing, BACK self-grade
- FRONT: `H2 {brk:true}` CER table (Claim `ruled(4)` / Evidence `ruled(6)` / Reasoning `ruled(5)`).
- BACK: `H2 {brk:true}` "self-grade & supports" → SELF-GRADE → rubric `dataTable [1800,2664,2664,2664]`
  → MY SCORE → sentence-frame SUPPORTS → REVISE → `ruled(6)`.
- Rationale: the rubric + supports on the back are perfect for self-grading; fill white space on BOTH
  the front and after the rubric on the back.

## Removed (do not reintroduce on the student page)
- The per-standard **UDL Access/Choice/Reflection page** (teacher-side only now).
- The **Name/Class/Date** line on Cornell.
- **MTSS/UDL framework labels** visible to students (say "core path" / "support options").
