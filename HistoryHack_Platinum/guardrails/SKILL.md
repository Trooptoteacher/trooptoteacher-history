---
name: history-hack-course-standard-builder
description: >-
  Builds and formats U.S. History Hack "Course Standard" (Platinum) deliverables for
  TroopToTeacher Technologies so every unit is visually IDENTICAL to the canonical Unit 5
  template. Use this whenever the user asks to build, rebuild, format, or fix a History Hack
  Course Standard student workbook, teacher How-to-Use & MTSS guide, or platinum student/teacher
  slide deck for ANY unit (US.01–US.95) — even if they don't say "platinum" or "template."
  Trigger on: "build the Unit N workbook", "match the Unit 5 format", "make the docs look like
  Unit 5", "rebuild the decks", "the formatting is off / there's too much white space", "the TOC
  is wrong", "add the Cornell notes", "answer key", "de-bias the questions", or any HH curriculum
  document that must match the established format. If the task is authoring brand-new lesson
  content (not formatting to the Course Standard template), prefer the instructional-design or
  curriculum-architect skills instead.
---

# History Hack — Course Standard (Platinum) Builder

> ⚑ **Inherits the suite CORE guardrails — [`SOCIAL_STUDIES_CORE_GUARDRAILS.md`](./SOCIAL_STUDIES_CORE_GUARDRAILS.md).**
> Those rules (authoritative sourcing / **no tertiary encyclopedias**, geography-as-priority,
> SME review tracking, verbatim standards alignment, accessibility/de-bias, compliance & currency)
> are **course-agnostic** and apply to **every** Social Studies Hack course — Government Hack,
> World History Hack, and beyond. This file is the U.S. History **format** layer *on top of* that
> core; it may add rules, never weaken them. When building a new course, load the CORE first.

**Unit 5 is the canonical template. Every Course Standard deliverable must match it exactly —
no deviation.** This skill encodes the exact design tokens, document structure, build scripts,
and the hard rules so any unit's workbook, teacher guide, and decks come out identical in
formatting. The scripts in `scripts/` are the canonical builders — adapt the *content*, never
re-invent the *layout*.

## The deliverables (per unit)
1. **Student Workbook** (DOCX+PDF) — authored to the template with docx-js → `scripts/build_workbook.js`
2. **Teacher How-to-Use & MTSS Guide** (DOCX+PDF) — docx-js → `scripts/build_teacher_guide.js`
   (carries the SSP crosswalk, dimension-coverage crosswalk, 6-point CER rubric, answer keys, and the
   exit-ticket keys + "What's Next" reteach routing)
3. **Student (Lean) Deck** (PPTX+PDF) — edited in place → `scripts/build_student_deck.py`
4. **Teacher (Full) Deck** (PPTX+PDF) — edited in place → `scripts/build_teacher_deck.py`
5. **Teacher Graphic Organizer Toolkit** (reproducible DOCX / Canva) → `scripts/build_organizer_toolkit.js`
   (see the Graphic Organizer Toolkit rules below; on-brand Canva build handoff in
   `references/handoff-organizer-toolkit-canva.md`)
6. **Unit Assessment Book** (Formative checkpoints · Unit Summative Form A/B · Teacher Answer Key + Item
   Analysis + Reteach) — items pulled from the canonical question bank; one book unless >~35–40 pp, then split.
   See the Assessment rules below. → `scripts/build_assessment_book.js` (reads `unit<N>_assessment.json`).
7. **Cover Wraps — one per book** (DOCX+PDF) — sale-ready front · spine · back + print/listing spec for
   EVERY print deliverable (Student Workbook, Teacher Edition, Assessment Book, Organizer Toolkit) →
   `scripts/build_cover.js` (a `buildCover(spec)` loop over a `SPECS` array). Brand: **navy + red + gold**
   (red is a required accent — red designation bands, red keylines, red bullet markers; a navy/gold-only
   cover is incomplete). Front: trademark title, unit, B&W-safe hero image, framework badge row
   (UDL·MTSS·CER·Cornell·HIPPO·DOK), a red designation band (STUDENT WORKBOOK / TEACHER EDITION / ASSESSMENT
   BOOK / GRAPHIC ORGANIZER TOOLKIT), audience tag, publisher. Spine: vertical brand text + **per-book
   spine-width math** (white 60-lb ≈ 0.002252 in/pg) — perfect-bind at ≥ ~48 pp, else state saddle-stitch
   honestly (thin teacher books can't print a spine). Back: book-specific "what's inside" selling bullets,
   the unit's standards list, © + trademark + business block, ISBN/barcode box. Plus a per-book listing-spec
   sheet (trim, spine, binding, categories, keywords, blurb). Copy must name the frameworks the book uses.

Plus reports (crosswalk, deck QA, salvage log, TDOE Schedule F evidence matrix, field-test plan,
revision notes) and a SHA-256-manifest package.

## Read these before building
- `references/design-tokens.md` — exact colors, fonts, sizes, margins, cover, callouts (DOCS)
- `references/workbook-structure.md` — the front / 7-activity-per-standard / back structure
- `references/teacher-guide.md` — the 11-section guide structure
- `references/deck-platinum.md` — the edit-in-place deck layer and de-bias rule
- `references/primary-source-bank.md` — **canonical primary-source & image bank** (pull ALL images/citations from here)

## Golden rules (the invariants that keep every unit identical)

1. **No formatting deviation.** Use the exact tokens in `design-tokens.md`. Calibri; NAVY
   `1B2A4A` headings, RED `B22234` H3, CREAM `F7F5EF` callouts, GOLD `C89B3C` accents; 0.8"/0.9"
   margins; 6.7" content width; gold running header; footer with a live page-number field.
2. **Ground everything; fabricate nothing.** All facts come from the verified source decks or
   public-domain primary sources. Close-Read passages are authored synthesis and carry the
   "History Hack-authored instructional synthesis. This is not a primary source." label. Never
   invent primary sources, translations, or facts.
3. **Answer keys are separate.** Student materials show questions with NO answers. Keys live only
   in the teacher guide. Decks: the Student deck exposes zero keys.
4. **De-bias answer positions, synced across all surfaces.** See "De-bias rule" below.
5. **No fixed-track labels anywhere** (bodies AND speaker notes). Replace with universal labels:
   SUPPORT OPTION(S) / EXTENSION / LANGUAGE SUPPORT. Supports are optional and never lower the
   goal; they work alongside — never in place of — required IEP/504 accommodations.
6. **Preserve source decks.** Copy to read-only, record SHA-256, edit working copies only.
7. **Verify by rendering.** Nothing is "done" on successful generation — render to PDF and
   inspect, with at least one fix-and-recheck cycle.
8. **Label release status honestly.** Keep the pre-field-test assessment disclosure regardless of
   release label — approving a package for release does not make its items secure/calibrated.
9. **Standards AND learning targets come from the source of truth — verbatim.** The TN standard
   text and dimension tags (C,E,G,H,P,T,TCA) come from the state standards column; the "I can…"
   **learning targets come from the instructional guide's right-hand column** (stored per unit as
   `targets`). Never synthesize an "I can" — if you show one, it must be a real instructional-guide
   target. **Never print the label "WCS"** in any student- or teacher-facing product.
10. **Primary sources & images come from the canonical bank.** See `references/primary-source-bank.md`.
    Pull every image/map/photo/cartoon and its citation from `history-hack-web-app`'s primary-source
    bank; embed with the full citation + **alt text**. Never source images ad hoc or invent a citation.
11. **Writing areas are ruled baselines.** Use `ruled(n)`. NOTE the fixed bug: LibreOffice/Word merge
    adjacent identical paragraph borders, collapsing N lines to one — `ruled()` inserts a tiny
    border-less spacer between lines so every baseline renders. A response area with one visible line
    is a defect.
12. **Highlight the Tennessee connection** per standard where sourced (e.g., US.01 = George Jordan of
    Williamson County), and surface the **dimension lenses** (student-friendly) + **SSP** coverage.
14. **One standard = one 45-minute period, but the workbook holds more than one period fits.** Each
    activity header shows an HONEST `⏱ ~N min` estimate (via `H(title,2,{mins:N})`) — do NOT tune the
    numbers to make a set sum to 45. Unit-1 estimates: launch 5 · vocab 10 · Frayer 7 · Cornell 20 ·
    Close Read 15 · Geographer's map 10 · Primary Source 15 · Quiz 8 · CER+Exit 15 (≈105 min if all run).
    Framing is a **menu, not a checklist**: the teacher chooses which activities fill the period; whatever
    isn't run becomes a bell-ringer, station, homework, reteach, or extension. Never prescribe a fixed
    "do exactly these" lane. Rigor stays the same for every learner; UDL/MTSS layer on without lowering the
    bar. Student front matter carries a one-line pacing note; teacher guide §8 carries the honest estimate
    table + a "how to fill the period — your call" callout.
13. **Print-safe images (interior is black-and-white).** Choose images whose meaning survives grayscale —
    photographs, engravings, and line cartoons are safe (color there is decorative). When color *encodes*
    the information (choropleth/shaded maps, color-keyed charts), set `colorKey:true` on the image record:
    `sourceImage()` then prints a "view the full-color version on the projection slide" note, and the color
    original must live in the deck. Never let a printed page depend on a color-only distinction. Political
    cartoons and photos need no note; the Freedmen's Bureau engraving and all photos print cleanly. Flagged in
    Unit 1: the 1890 railroad map (US.01) and the 1890 foreign-born map (US.06).

## Today's structural additions (fold into every unit)
- **Standard launch page** (own page): Standard text · `LEARNING TARGETS — I can…` (from the guide) ·
  `Lenses for this standard` · **CORE PATH** (leads, prominent) · `★ Tennessee Connection` (secondary,
  where sourced) · SET YOUR GOAL · HOOK (text question) · ACTIVATE · PREVIEW & PREDICT. Activity 1 starts fresh.
- **CORE PATH is first and foremost, and it stands out** (navy block, gold label, white text — `coreCallout()`,
  not the cream `callout()`). It states the philosophy: **the core and the rigor are the SAME for every
  student; UDL and MTSS are the flexible means in — they never lower the bar.** The Tennessee Connection is
  secondary and sits BELOW it in the ordinary cream callout. Never let the TN callout outweigh CORE PATH.
- **Cornell cues are standard-specific**, tied to the learning targets (not the generic who-questions).
  The who-benefited/bore-costs/decided throughline becomes the **CER Big-Question Organizer**.
- **Geographer's Lens (G · SSP.06):** a text task on the Close Read for G-tagged standards; a **dedicated
  map page** (from the bank) where a period map exists. **Every standard that carries geography data
  (`geo` set) MUST render a Geographer's Lens page — never silently skip it** (this was a real bug in
  Units 6/7/8). Geography is one of the most-missed EOC skills, so the page opens with the gold
  **`geoPriorityBar()`** ("PRIORITY SKILL · Geography — do not skip it") — the same prominence the
  Vocabulary priority terms get. `geo` with an empty `geo_places` still renders the page (the places
  table is simply omitted); it does not degrade to nothing.
- **Geography provenance & SME sign-off.** `geo_places` are authored (not retrieved). Each authored set
  should carry `geo_sources` (authoritative citations backing the anchor facts) and a `geo_review`
  object: `{"status": "drafted|sme_approved|needs_fix|n/a", "by": "", "date": "", "note": ""}`. **A
  subject-matter expert signs off by setting `geo_review.status` to `sme_approved` (with `by`/`date`)
  in the content JSON** — that is where sign-off is recorded.
  - **Provenance ledger (source of truth):** `guardrails/geo_provenance.json` holds citations + review
    status for every geo standard. `guardrails/apply_geo_provenance.py` stamps it into all unit content
    JSONs — **run it after any re-derive** (places live in the derive `GEO_PLACES`; sources + review
    status come from the stamp, so a re-derive never drops provenance). Idempotent; never overwrites a
    standard already `sme_approved`.
  - **Audit / gate:** `guardrails/geo_review_audit.py` prints the ledger across all units;
    `--require-approved` exits non-zero if any geo standard is not yet approved, so it can gate a build
    or the quarterly Administrative Review.
  - As of this pass, all 20 geo standards are `drafted` with verified citations (Office of the
    Historian, National Archives, Library of Congress, NPS, U.S. Army/Navy history, FHWA, JFK Library,
    9/11 Memorial, Tennessee Encyclopedia, Britannica) — pending SME sign-off.
- **Student Progress Check**: clean stem, options A–D indented on their own lines, no DOK tag, no
  "answer key is in the teacher guide" line.
- **MTSS labels are teacher-side.** Student self-checks read plainly ("How am I doing?", "Ready check").
- **Teacher edition** carries the **SSP crosswalk**, the **dimension-coverage crosswalk**, and the
  canonical **6-point CER rubric** (6 Exemplary · 5 Advanced · 4 Proficient · 3 Adequate · 2 · 1).

## Graphic Organizer Toolkit (teacher pack — reproducible)
- **Separate, reproducible teacher deliverable** — NOT embedded in the student workbook (keeps it lean;
  teachers deploy as needed = MTSS differentiation). Evidence base: identifying similarities/differences is
  **Marzano's highest-yield strategy**.
- **Three parts:** (1) a **"Which Organizer, When" quick guide** (task signal → organizer → why — this solves
  the teacher's real pain point); (2) **course-wide blank reproducibles** (content-agnostic: Venn 2/3, T-chart,
  compare/contrast matrix, cause–effect, timeline, concept web, main idea/details, KWL, 5 Ws, problem–solution,
  Frayer, CER, HIPPO, **Tennessee Connection**); (3) **per-unit pre-labeled** best-fit organizers, one for the
  standard whose task each best fits. **Do not limit to a fixed list — pick whatever best fits the task.**
- **Every organizer carries a brief "when to use · why it works" blurb** (teach the teacher the WHY).
- **Highlight Tennessee connections throughout** — the local-to-national move is a HistoryHack signature and a
  deliberate differentiator; flag it wherever a standard has a TN tie. Builder: `scripts/build_organizer_toolkit.js`.

## Assessment rules (formative + summative)
- **Question bank is a canonical source of truth** — like the primary-source bank. Pull every
  assessment item from `history-hack-web-app`'s bank (`public/data/us-history/questions/unit-<N>/dok-*.json`;
  45–55 items/standard; MCQ + constructed-response + document-based; bilingual; `irtParameters`,
  `dokRationale`, per-distractor explanations, `reportingCategory`, `tdoeTags`). Never author items.
- **Items are pre-calibrated, not calibrated.** Always carry the disclosure "classroom-formative ·
  pre-field-test (pre-calibration) — not a secure TCAP form." First administration is what calibrates them.
- **Exit Ticket per standard (in the workbook):** ONE vetted item (DOK-2/3, distinct from the Progress
  Check) at the end of the standard, on the CER page — **never its own page, never crowded** (trim CER
  lines to fit). UDL capture: mark / say / explain + a `☐ Not yet ☐ Getting there ☐ Got it` self-rating
  (this is the MTSS tracking signal). **Answer key and the "What's Next" reteach live in the teacher
  edition only.** Do NOT add an exit ticket to each of the 7 sub-activities — that is over-testing.
- **"What's Next" (reteach routing) is teacher-side.** For each exit-ticket/checkpoint, the teacher
  edition states what to do if students miss it (distractor-based reteach + spiral rule), using the bank's
  distractor explanations and `dokRationale`.
- **Standalone Unit Assessment Book (5th deliverable):** one book, three sections — Formative checkpoints ·
  Unit Summative (Form A + Form B) · Teacher Answer Key + Item Analysis + Reteach. Keep it **one book unless
  it exceeds ~35–40 pp**, then split out a separate Summative book. Two printed parallel forms is enough
  (the web app generates more, minimal-overlap, on demand). Summative items/keys never live in the student
  workbook (assessment integrity, Schedule F Criterion 7).

## Build process

### Workbooks & teacher guide (docx-js)
`docx` (npm) is preinstalled; `require('docx')` directly. Follow the docx-js gotchas: US-Letter
page size, dual table widths (columnWidths + per-cell width, both DXA), `ShadingType.CLEAR`
(never SOLID), no literal `\n` (separate Paragraphs), PageBreak inside a Paragraph, headings via
built-in `HeadingLevel.*` with `outlineLevel` so the TOC sees them.

1. Assemble the unit's grounded content into a JSON (see `scripts/content_TEMPLATE.json` and the
   data shape in `scripts/unit_data_TEMPLATE.py`): per standard — title, TN text, "I can",
   deck-slide refs, vocab (term/say/es/def), primary sources (public-domain, cited), the CFU item
   with its de-biased key, and authored activity content (close read, TDQs, Frayer terms, quiz
   items, CER prompt).
2. Run the builder → DOCX. Then **bake the TOC** and render (see TOC rule).
3. Audit white space (see white-space rule) and fill.

### Decks (python-pptx, edit-in-place)
The user must attach the two source `.pptx` files (the connector can't transfer the binary).
Then run the deck builders — see `references/deck-platinum.md`. They read the working copies,
add the platinum slides, de-bias in sync, strip fixed-track labels, set alt text, renumber, and
save; the originals stay untouched.

## The TOC rule (page numbers must be baked)
A docx-js Table of Contents shows a placeholder — **every entry reads "1"** — until an app
updates its fields. Word/Google Docs won't do that automatically, so the user sees a broken TOC.
Fix it: after building the DOCX, run it through LibreOffice to update indexes + fields and
**save back to DOCX**, which bakes real page numbers into the field result (correct on open,
no "update field" needed). Use `scripts/uno_fields.py`:

```
python3 scripts/uno_fields.py in.docx out.docx out.pdf   # bakes TOC + exports PDF
cp out.docx in.docx                                       # keep the baked version
```

Verify: unzip the DOCX and confirm the standard TOC entries carry real page numbers (not all 1),
and that `PAGEREF` fields were resolved to static text.

## The print-layout rule (each activity must print stand-alone)
These are **printable** classroom documents, so pagination is not cosmetic — it is the spec.
Study the canonical Unit 5 pagination (`pdftotext -layout` the PDF and map headings to pages)
and match it:

- **Every activity starts on its own page** (`pageBreakBefore` on each Activity heading), so a
  teacher can print any single activity by itself. The Standard heading shares its page with
  Activity 1; Activities 2–7 and the two Support Backs each begin a new page.
- **The Cornell Notes "Universal Front" (Activity 3) is exactly ONE page**, and the **Guided
  Support Back is the very next page** — it prints on the *reverse* of the Cornell front when
  duplexed (that's why its label says "reverse"). The Light Support Back follows. Size the
  Cornell front's content/row heights so it fills one page without overflowing to a second.
- **Each standard starts on a fresh page.** Never let two activities or a front/back pair split
  across a page boundary the wrong way.

Do NOT flow activities together with fillers between them — that makes single-activity printing
impossible. Instead, each activity fills its OWN page (next rule).

## The white-space fill rule (no dead space)
Leftover blank space on an activity page is a defect — fill it with a right-sized activity, the
way Unit 5 does. Because each activity is on its own page, "fill" means making that single page
look full and intentional (not flowing content across activities). Two mechanisms:

- **Tall, intentional writing areas.** The writing space *is* the activity. Give Cornell notes,
  Evidence Labs, HIPPO, CER, and Frayer generous row heights (`HeightRule.ATLEAST`, ~560–1800
  DXA) so activities fill their pages instead of trailing off.
- **A right-sized filler library** inserted where a page would otherwise run short: Quick Write,
  Sketch It, Retrieval, Stretch (extension), Make a Connection — sized to the gap (≈¾, ½, ¼
  page). `build_workbook.js` includes `FILL_LIB` and `fillGap()`, plus named fillers used on
  short pages (Before You Begin, My Support Plan, Local History Investigation, Unit Reflection).
- **Don't force activities onto reference/title pages** (cover, copyright, TOC, Source Library) —
  those are legitimately airy.

**Sized-fill library (match the fill to the gap).** Pick the fill by how much blank a page has:
| Blank on the page | Fill with (meaningful, not filler) |
|---|---|
| ~¼ page (25–40%) | Quick Write · Make a Connection · a 2-line prediction/retrieval |
| ~½ page (40–60%) | Quick Write + Sketch It · a labeled mini-organizer · Spaced Retrieval table |
| ~¾ page (60%+) | Retrieval + Quick Write + Stretch (extension) — a full mini-activity |
Every fill must bring value (UDL response choice, retrieval, extension, connection) — never dead filler.
- **Doodle / Sketch Zone** (`doodle()`): a labeled open box for drawing/diagramming — a strong UDL “draw your
  thinking” fill for the bottom of the Cornell front, the Geographer’s Lens (“mark up the map”), or any page
  with a tall gap. Serves visual learners and fills space meaningfully.

**No-bleed rule (a few lines spilling to a near-empty next page is a defect).** Each activity must
sit on ONE page. If it overflows by a little, TIGHTEN (reduce line counts / merge callouts / drop a
redundant element) so it fits — do NOT let it spill. If a page runs short, ADD a sized fill above.

**Every prompt a student sees gets space to answer.** If an analysis frame (HIPPO, TDQ, CER, map task)
shows a question, it MUST provide ruled writing lines for the response — put the prompt in the label
column and blank ruled lines in the answer column (`writeTable(..., {lines:n})`). A visible prompt with
no answer space is a defect (this was the HIPPO bug).

**Launch-page hook.** Each standard's opening (launch) page carries a **text HOOK** — a provocative,
standard-specific question (stored per standard as `hook`) + a couple of ruled lines — to engage and fill
the page. Do NOT shrink a primary-source image onto the launch page: a small dropped-in image reads as
out of place. Images belong in the analysis activities (Activity 5, Geographer's Lens) where they are
full-size, framed, captioned, and cited.

**The loop:** build → `uno_fields.py` (bake TOC) → `whitespace_audit.py` → for each flagged page, tighten
(bleed) or add a sized fill (short) → rebuild → re-audit until clean. Target: no activity page over ~25%.

## Cornell notes ↔ slide deck alignment (guardrail)
The Cornell notes exist to **capture the data the slide deck presents.** The deck teaches the standard and
its "I can" learning targets; the Cornell page must (1) cite the exact deck slide range it captures
(`Lean Student Deck slides <range> · direct-teaching slides <dt>`), (2) use cues tied to those targets, and
(3) list the same key terms the deck introduces. When the deck changes, update the Cornell cues/range to
match. Never let the notes drift from what the deck actually presents.

## De-bias rule (answer positions)
Source-deck CFU items are usually keyed mostly to "A". Choose a balanced target position per item
and apply the SAME permutation across the Student Progress Check, the Teacher CFU + Answer Reveal
(move option text, the gold highlight bar, the ✓, and the "Correct answer:" line together), and
the workbook Transfer Check. Keep one `debiased_options()` helper (see
`scripts/unit_data_TEMPLATE.py`) and reuse it everywhere so the three surfaces can never drift.

## Package & deliver
Copy all artifacts + reports + scripts + source hashes into
`<Unit>_CourseStandard_Pilot_<status>/`, write a `SHA256_MANIFEST.txt`, zip it, and (if the zip
exceeds the attach limit) `split -b 24m`. Deliver the individual DOCX/PDF/PPTX plus the package.

## Adapting to a new unit — quick checklist
1. Get the unit's verified source decks (attached) + read their text for vocab, sources, CFU keys.
2. Build the content JSON (grounded; de-biased keys chosen).
3. Run `build_workbook.js` → `uno_fields.py` (bake TOC) → `whitespace_audit.py` → fill → re-bake.
4. Run `build_teacher_guide.js` → `uno_fields.py`.
5. Attach + edit the decks with the deck builders; render + de-bias verify.
6. Reports + Schedule F matrix + SHA-256 package.
7. Render-and-inspect every artifact; one fix-and-recheck cycle minimum.
