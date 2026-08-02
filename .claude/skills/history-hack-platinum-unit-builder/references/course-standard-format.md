# Course Standard (Platinum) — Print & Templating Spec

The detailed print/formatting spec for a Course Standard unit, absorbed from the
retired standalone `history-hack-course-standard-builder`. **Unit 6 is the canonical template — every
Course Standard deliverable must match it exactly, no deviation.** `SKILL.md` holds the
decisions and orchestration; this file holds the exact tokens, page structure, build loop, and
the print gotchas. Adapt the *content* per unit; never re-invent the *layout*.

## Deliverables (per unit)

1. **Student Workbook** (DOCX+PDF) — authored to the template with docx-js.
2. **Teacher How-to-Use & MTSS Guide** (DOCX+PDF) — carries the SSP crosswalk, dimension-coverage
   crosswalk, 6-point CER rubric, answer keys, exit-ticket keys + "What's Next" reteach routing.
3. **Student (Lean / Review) Deck** (PPTX+PDF) — UDL/MTSS layer **MERGED into the authentic source
   deck** (never authored from blank).
4. **Teacher (Full / Lecture) Deck** (PPTX+PDF) — same merge pipeline; teacher layer names CAST
   guidelines + MTSS. **Exactly one teacher deck per unit** = the authentic source teacher deck
   with the layer merged in.
5. **Teacher Graphic Organizer Toolkit** (reproducible DOCX / Canva) — this is where the
   four-rung NOTES SUPPORTS ladder (Cornell Guided → Light → independent backs) ships, as
   per-standard reproducibles. See the companion skill `history-hack-graphic-organizer-workbook`.
6. **Unit Assessment Book** (standalone) — Formative checkpoints · Unit Summative Form A/B ·
   Teacher Answer Key + Item Analysis + Reteach. One book unless it exceeds ~35–40 pp, then split
   a separate Summative book. Items pulled from the canonical question bank; never authored.
7. **Cover Wraps — one per book** (DOCX+PDF) — sale-ready front · spine · back + print/listing
   spec for EVERY print deliverable.

Plus reports (crosswalk, deck QA, salvage log, TDOE Schedule F evidence matrix, field-test plan,
revision notes) and a SHA-256-manifest package.

## Design tokens (no deviation)

- **Font:** Calibri throughout.
- **Heritage Blue (primary):** `#1F3A5F` for headings and structure (America 250). (The legacy
  navies `#1B2A4A` / `#0A1F3C` / `#143159` are retired — do not use them.)
- **Patriot Red H3 / accent:** `#B22234` (required accent — red designation bands, red keylines, red
  bullet markers; a blue/gold-only cover is incomplete).
- **Founders Cream callout fill:** `#F8F5EF`. **Muted Gold accent:** `#C9A227` (used sparingly).
  (Legacy gold `#C89B3C` is retired.)
- **Margins:** 0.8" / 0.9"; **content width 6.7"**; US-Letter page size.
- **Gold running header;** footer with a **live page-number field**.

## Source-analysis frame

- **HIPP** for lesson-level source analysis (Activity 5 organizer).
- **HIPPO** reserved for full DBQ work (the standalone DBQ SKU, `history-hack-dbq-workbook`).

## Workbook structure — the per-standard 7-activity spine

Each standard runs the established 7-activity page structure, and **every activity prints on its
OWN page** (`pageBreakBefore` on each Activity heading) so a teacher can print any single activity
alone. The Standard launch/heading shares its page with Activity 1; Activities 2–7 each begin a new
page. Each standard starts on a fresh page.

- **Standard launch page** (own page): Standard text · `LEARNING TARGETS — I can…` (verbatim from
  the instructional guide's right-hand column — never synthesized) · `Lenses for this standard` ·
  **CORE PATH** (leads, prominent — navy block, gold label, white text; states "core and rigor are
  the SAME for every student; UDL/MTSS are the flexible means, never lowering the bar" as a chunked
  3-line array) · `★ Tennessee Connection` (secondary, cream callout, below CORE PATH, where sourced)
  · SET YOUR GOAL · HOOK (text question) · ACTIVATE · PREVIEW & PREDICT.
- **Cornell notes = Universal Front, exactly ONE page.** Cues are standard-specific, tied to the
  learning targets. The **student workbook prints the front only** — the supports ladder does NOT
  print here. Size the front's row heights so it fills one page without overflowing.
- **Close Read** must fit ONE page: the passage is chunked into titled bold-navy sections; the
  text-dependent questions ARE the Evidence Lab rows (3-column table: TDQ *given* · exact passage
  evidence *blank* · what it shows *blank*). Never list TDQs separately then add an empty table.
- **Geographer's Lens** (only where a standard is genuinely spatial) = geographic *reasoning*, not
  map-drawing: a Place/Where/What-happened *given* + **Why HERE?** *analysis* table, Movement &
  Region, Geography as a force (C3 Dim. 2), Read-it-like-a-source. Never a blank "sketch a map" box.
  Color maps live on the projector/deck (print-safe interior).
- **Activity 5 (source analysis)** uses the **HIPP** organizer with a captioned, cited image from
  the verified image bank (cap by HEIGHT ~330 px so the image + all HIPP rows fit one page).
- **Student Progress Check:** clean stem, options A–D indented on their own lines, no DOK tag, no
  "answer key is in the teacher guide" line.
- **Exit Ticket per standard:** ONE vetted DOK-2/3 item on the CER page (never its own page),
  UDL capture (mark / say / explain) + `☐ Not yet ☐ Getting there ☐ Got it`. Key + reteach are
  teacher-side only.

**Page economy:** repeat instructional scaffolds ONCE at unit level (back matter), not per standard.
Guarantee per-standard floors: **vocab = 3**, **quiz ≥ 2** (supplement thin standards from the
question bank, filtered to the standard's distinctive title terms). Never fabricate a TN connection.

## Grounding & integrity rules

- **Fabricate nothing.** All facts from verified source decks or public-domain primary sources.
  Close-Read passages are authored synthesis and carry the label "History Hack-authored
  instructional synthesis. This is not a primary source."
- **NEVER pull from `textbook/` folders** (`public/images/textbook/**`,
  `public/data/us-history/textbook/**`) — not canonical, filenames unreliable/mislabeled.
- **Images from the VERIFIED public-domain bank** at
  `public/data/us-history/primary-sources/images/unit-N.json` (LoC/NARA Chicago citations,
  `rightsLabel="Public Domain"`, `commercialUse="permitted"`). **Eye-verify EVERY image before
  captioning** — a minority of records are mislabeled (some classroom-inappropriate). Captioning a
  mislabeled image fabricates a citation. If no verified image set exists, use the bank's cited TEXT
  sources — never substitute textbook images.
- **Answer keys are separate.** Student materials show questions with no answers; keys live only in
  the teacher guide. The student deck exposes zero keys.
- **Never print the label "WCS"** in any student- or teacher-facing product.
- **Print-safe interior (B&W).** Choose images whose meaning survives grayscale. When color
  *encodes* information (choropleth/shaded maps), set `colorKey:true` so the page prints a "view
  the full-color version on the projection slide" note and the color original lives in the deck.

## Deck merge pipeline (canonical — never author from blank)

The user attaches (or you download from Drive) the district's authentic source `.pptx` decks (the
connector can't transfer the binary). Copy each to a **read-only** working copy, record its
**SHA-256**, and edit working copies only — the source slides and images are never touched.

Build the UDL/MTSS/vocab/progress/map slides as a **pptxgenjs "layer"** and **MERGE** them into the
authentic source deck. The layer adds: vocabulary-before-instruction slides, per-DI-segment student
review slides (`US.xx · DI k of M`), teacher `✍ In your workbook · <activity>` write-cues, the
per-standard map slide (color originals live here), CAST/MTSS naming (teacher deck). Then de-bias in
sync, strip fixed-track labels (bodies AND speaker notes → SUPPORT OPTION(S) / EXTENSION / LANGUAGE
SUPPORT), set alt text, and renumber.

- **Slide duplication:** use the **`pptx` skill's `add_slide.py`** — **never `python-pptx`
  `add_slide`** (it can orphan a slide part and corrupt the package on re-save). Validate with a
  load/save round-trip dup check.
- Per-standard slide blocks stay **contiguous**; DI count matches workbook = teacher = student.
- The teacher↔workbook LESSON→WORKBOOK MAP is verified by `history-hack-lesson-flow-qc`
  (workbook↔deck exact-slide alignment) after this merge.

## The TOC rule (page numbers must be baked)

A docx-js Table of Contents shows a placeholder ("1" for every entry) until an app updates its
fields. After building the DOCX, run it through LibreOffice to update indexes + fields and **save
back to DOCX** (bakes real page numbers into the field result). Use `uno_fields.py`:

```
python3 scripts/uno_fields.py in.docx out.docx out.pdf   # bakes TOC + exports PDF
cp out.docx in.docx                                       # keep the baked version
```

Verify: unzip the DOCX and confirm the TOC entries carry real page numbers (not all 1) and that
`PAGEREF` fields resolved to static text.

## The white-space fill rule (no dead space) + audit thresholds

Leftover blank space on an activity page is a **defect**. Because each activity is on its own page,
"fill" means making that single page look full and intentional. Fill by gap size:

| Blank on the page | Fill with (meaningful, not filler) |
|---|---|
| ~¼ page (25–40%) | Quick Write · Make a Connection · a 2-line prediction/retrieval |
| ~½ page (40–60%) | Quick Write + Sketch It · a labeled mini-organizer · Spaced Retrieval table |
| ~¾ page (60%+) | Retrieval + Quick Write + Stretch (extension) — a full mini-activity |

- **Tall, intentional writing areas** (`HeightRule.ATLEAST`, ~560–1800 DXA) — the writing space *is*
  the activity. Use `ruled(n)` for baselines (it inserts a border-less spacer so N lines all render;
  a response area with one visible line is a defect).
- **Every prompt a student sees gets ruled answer space** (`writeTable(..., {lines:n})`).
- Don't force activities onto reference/title pages (cover, copyright, TOC, Source Library).
- **No-bleed rule:** a few lines spilling to a near-empty next page is a defect — TIGHTEN to fit,
  don't spill. `whitespace_audit.py` flags any page >85% blank.
- **The loop:** build → `uno_fields.py` (bake TOC) → `whitespace_audit.py` → for each flagged page,
  tighten (bleed) or add a sized fill (short) → rebuild → re-audit until clean. Target: no activity
  page over ~25% blank.

### Close Read — adaptive formula (fits ONE page, no front/back split)

`_pf = _cl>2000?18:(_cl>1500?19:21)` (shrink long passages), `_rows = _cl>1900?2:3` (never 4 — the
tall "whose perspective" 4th question orphans), `_wl = _cl>1900?1:2`, pass `noSplit:true` to
`writeTable`. Drop the per-standard quiz STRETCH and the launch-page ruled fill when they spill.

## De-bias rule (answer positions)

Source-deck CFU items are usually keyed mostly to "A". Choose a balanced target position per item and
apply the SAME permutation across the Student Progress Check, the Teacher CFU + Answer Reveal (move
option text, gold highlight bar, ✓, and "Correct answer:" line together), and the workbook Transfer
Check. Keep one `debiased_options()` helper and reuse it everywhere so the surfaces can't drift.

## Cover wraps

Front: trademark title, unit, B&W-safe hero image, framework badge row (UDL·MTSS·CER·Cornell·HIPP·DOK),
a red designation band (STUDENT WORKBOOK / TEACHER EDITION / ASSESSMENT BOOK / GRAPHIC ORGANIZER
TOOLKIT), audience tag, publisher. Spine: vertical brand text + per-book spine-width math (white
60-lb ≈ 0.002252 in/pg) — perfect-bind at ≥ ~48 pp, else state saddle-stitch honestly. Back:
book-specific "what's inside" bullets, the unit's standards list, © + trademark + business block,
ISBN/barcode box. Plus a per-book listing-spec sheet (trim, spine, binding, categories, keywords,
blurb). **Brand: navy + red + gold** (red required).

- **Hero art:** the app's own hero set at `public/images/units/unit-N.jpg` — NOT the textbook bank.
  Confirm each hero by eye. **Licensing is a hard gate** (commercial, sellable covers): only clearly
  public-domain federal/LoC/FSA/NASA photos. Unit 6's app hero is Rosenthal's Iwo Jima flag-raising,
  which the AP holds in copyright — **DO NOT embed it**; substitute a PD WWII photo (e.g. "Into the
  Jaws of Death," D-Day, U.S. Coast Guard). When in doubt, skip and flag rather than ship infringing.

## Build gotchas (critical)

- **soffice bake RACE:** `uno_fields.py` kills+relaunches soffice; back-to-back bakes leave a STALE
  PDF. `pkill -9 soffice; sleep 1` before each bake; build serially. Symptom: edits appear to have
  "no effect" on the rendered PDF.
- **`whitespace_audit.py`** renders into a shared `/tmp/wsa` and globs it — `rm -rf /tmp/wsa` before
  every run or stale JPEGs inflate the page count.
- `cd` into the workspace before `node analysis/build_*.js` (relative paths).
- **docx-js:** US-Letter page size, dual table widths (columnWidths + per-cell width, both DXA),
  `ShadingType.CLEAR` (never SOLID), no literal `\n` (separate Paragraphs), PageBreak inside a
  Paragraph, headings via built-in `HeadingLevel.*` with `outlineLevel` so the TOC sees them.
- **Notebook paper (ruled tables):** borderless table with a per-row bottom border, **exactly one
  `w:spacing` per paragraph** (multiple runs collapse/double lines).

## Per-unit config that MUST change when cloning a derive script

- `ORDER = sorted(codes, key=lambda c:int(c.split('.')[1]))` when the ican file lists a standard out
  of numeric order.
- `GEO_TASKS` / `GEO_PLACES` — rewrite per unit; give a Geographer's Lens only to standards with a
  real spatial dimension. Remove the generic "locate the places" fallback. After deriving, print the
  geo standards and confirm they belong to THIS unit (a fragile regex swap can silently carry a prior
  unit's block over).
- Assessment `DISTINCT{}` keyword map — rewrite per standard with distinctive title terms.

## Vocabulary sourcing (topic-match guarantee)

`vocabulary/unit-N.json` is under- and sometimes mis-tagged. `vocab_for()` guarantees topic match:
(1) bank terms tagged to the standard AND appearing in its reading content; (2) any bank term
appearing in the reading content; (3) the standard's own factcards (matched by `standardId` FIELD,
kept only when a distinctive title/summary word appears in the passage); (4) only if still <2, pad
from the bank. Dedupe on a parenthetical-stripped key.

## Adapting to a new unit — quick checklist

1. Get the unit's verified source decks (attached) + read their text for vocab, sources, CFU keys.
2. Build the content JSON (grounded; de-biased keys chosen).
3. Run `build_workbook.js` → `uno_fields.py` (bake TOC) → `whitespace_audit.py` → fill → re-bake.
4. Run `build_teacher_guide.js` → `uno_fields.py`.
5. Attach + MERGE the decks with the deck builders; render + de-bias verify.
6. Reports + Schedule F matrix + SHA-256 package.
7. Render-and-inspect every artifact; one fix-and-recheck cycle minimum.
