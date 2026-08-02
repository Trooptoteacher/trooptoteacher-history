---
name: history-hack-tcap-deck-builder
description: "Platinum-standard builder for U.S. History Hack TCAP lecture decks (PowerPoint .pptx) plus a matching printable Teacher Answer Key PDF and teacher Usage Guide, for TroopToTeacher Technologies LLC. Regenerates the Unit 1 gold-standard template for any unit: per-standard lessons (divider/hook/instruction/key figures/primary source/word wall/student activity/two-slide click-reveal TCAP check/wrap-up), public-domain primary-source imagery sourced repo-first then LOC/NARA, the locked navy/red/gold + America250 brand kit, historian-verified citations, EN/ES word-wall support, and layered answer keys (speaker notes + reveal slides + printable PDF). Use when the user says: build the Unit N TCAP deck, build the Unit N lecture deck, mirror the Unit 1 deck pattern, make the EOC slides, build the teacher answer key, regenerate the deck template, or build the slide deck for a History Hack unit."
license: "Proprietary — © 2026 TroopToTeacher Technologies LLC. All rights reserved."
metadata:
  author: TroopToTeacher Technologies LLC
  version: '3.3'
---

# History Hack TCAP Lecture Deck Builder

Builds the **flagship U.S. History Hack TCAP lecture deck** (PowerPoint `.pptx`) for any unit, plus its matching **printable Teacher Answer Key (PDF)** and **teacher Usage Guide (.md)**, in the locked History Hack brand. This skill encodes the Unit 1 gold-standard pattern (v3.2, June 2026 — expert-panel reviewed; pedagogy, TCAP/rigor, accessibility/ELL, and visual sub-scores all independently re-scored to ≥9.5/10) so every future unit (US standards across Units 2–11) is regenerated identically — same structure, brand, imagery rules, click-reveal checks, and layered answer keys.

**v3 quality upgrades baked into the generator** (apply to every unit): per-standard **Quick Review** spaced-retrieval slide (Rosenshine P1/P10); per-standard **exit tickets** with DOK variety + model answers + reteach diagnostics in speaker notes; **DOK badges** (navy/gold pill) on every check slide so checks aren't all recall; **"N of M" numeral on progress dots** (WCAG 1.4.1 — never color-alone); CFUs upgraded across **DOK 1–3**; word walls at **6 terms/standard** with partial last row centered (no half-empty grids); EN/ES Spanish accent/term fixes. Slide-layout fixes locked in: bios use a **taller header + single primary role per card** (pptxgenjs `fit:'shrink'` is unreliable in LibreOffice — trim content instead); long Spanish word-wall terms get a widened ES box + narrowed term box; standard-divider titles auto-shrink when long; the roadmap footer text lives in bottom-right whitespace clear of the standard cards.

**v3.1 pedagogy upgrades baked into the generator** (push the instructional-design/pedagogy sub-score to 9.5/10): per-standard **TN Social Studies Practice (SSP) pills** rendered on each Standard Divider beside the TN standard + "I Can" (e.g. SSP.01 Collect sources, SSP.05 Historical awareness) so every standard is explicitly tied to the practices it builds; a **"We Do" guided-practice slide** inserted between the Word Wall and the Student Activity (modeled prompt → teacher think-aloud → "then you try" — Rosenshine P4/P5, closes the I-Do→We-Do→You-Do gap); a **"SOURCE IT FIRST" WHO / WHEN / WHY band** on every Primary Source slide, tagged to the relevant SSP, giving students a sourcing scaffold before analysis; **exit-ticket 3-way reteach routing** in speaker notes (full-mastery / partial / reteach trigger with a specific reteach move); a **STRATEGY chip** on every Key Figure bio card naming the historical-thinking move that figure exemplifies (e.g. "Vertical integration," "Trust/monopoly"); a **TEACHER CUE box** on Direct Instruction slides with facilitation/think-aloud prompts and cold-call cues; and a **Hook facilitation pill + speaker note** (10-sec silent think → 60-sec Turn & Talk → cold-call 2–3 pairs with sentence starter, ~4-min cap).

**v3.2 upgrades baked into the generator** (push TCAP/rigor, accessibility/ELL, and visual sub-scores to ≥9.5/10): a per-standard **Confidence Check / Warm-Up slide** (DOK 1 low-stakes recall with a one-slide reveal — secures an early win and surfaces shaky students before new content); a **DOK 3 Honors / Extension band** on every Wrap-Up slide (argument-based prompt tagged to SSP.04, also appended to speaker notes) so the rigor ramps DOK 1→3 within each standard; **ELL scaffolds on the Word Wall** — a `say:` pronunciation respelling (stressed syllable in CAPS) under each English term and a per-term gold initials "visual anchor" chip for dual-coding; an **ELL sentence-frame strip** on the first Direct-Instruction slide of each standard (academic-language scaffold for EL + striving writers, auto-sized so 2–3 wrapped lines never clip); a **two-row Key Figures layout** that auto-engages when a standard has 4+ figures (keeps back-row bios legible); a **"ZOOM IN" close-looking pill** on primary-source images (Mayer signaling); and roadmap standard-to-standard **connection cues**. **All decorative emoji/symbol glyphs were removed** — labels are plain text or drawn shapes only, because emoji render unreliably (tofu boxes / odd glyphs) in LibreOffice and on school computers. The CONTEXT box on text-only primary sources auto-tiers its font and caps length so the last sentence never clips, and the slide-number counter starts after the unnumbered cover.

This is a for-sale "Platinum Standard" product (TpT and direct download). Every deck must be classroom-ready, TDOE-defensible, and visually engaging.

## When to Use This Skill

Trigger when the user asks to:
- "Build the Unit N TCAP deck" / "Unit N lecture deck" / "slide deck for Unit N"
- "Mirror the Unit 1 deck pattern" / "use the deck template"
- "Make the EOC / TCAP check slides" with click-reveal
- "Build the teacher answer key" (PDF) for a deck
- "Regenerate the deck" or "rebuild the usage guide"

## Non-Negotiable Rules (the locked pattern)

**GATE 0 — RUN BEFORE AUTHORING ANY NEW UNIT (two hard prerequisites; both must pass first).** These are the front-of-checklist gates. Do NOT write a single line of deck content, JSON, or narrative until BOTH are satisfied.

- **GATE 0A — Primary sources & images must already exist, be verified, and be downloaded.** Before authoring, confirm we hold an *extensive, complete, downloaded* set of primary sources and images for the unit: (1) the catalog `hh-web/public/data/us-history/primary-sources/unit-N.json` exists and validates; (2) every referenced image file is physically present in BOTH `unitN-full/img/` AND `hh-web/public/images/textbook/unit-N/`; (3) every item is public-domain, historian-verified to actually depict its subject (never trust filenames), and source-captioned. **If ANY primary source or image is missing, source and download it FIRST from public-domain archives (LOC / NARA / Smithsonian / Wikimedia), caption + cite it, and add it back into the repo catalog + image folders — THEN proceed.** No authoring on an incomplete source/image inventory. (This is the user's standing hard rule: "make sure that we have an extensive list of primary sources and images downloaded" and "if we have to source more images and primary sources, do that first. Then make changes.")
- **GATE 0B — Reuse existing web-app/textbook content first; align, never invent.** Before authoring, pull ALL existing locked content already stored in the web app / repo / textbook for the unit — standards text, "I Can" objectives, sections/narrative, biographies, primary-source excerpts, vocabulary, and matching Cornell Notes printables — and build the deck from THAT. Deck content must match the repo/textbook content verbatim; **never invent or paraphrase content that already exists.** Only after the existing content is pulled and aligned does authoring proceed. (User's standing hard rule: "you use all of that content that we already have stored in the web app or textbook first. That stuff needs to be aligned" and "always check the content. It's already been built for the Web app or textbook.")

1. **PowerPoint (.pptx) is the single source of truth.** Built with `pptxgenjs`, 16:9 (W=13.333", H=7.5"). It must import cleanly into Google Slides — so the click-reveal is a **two-slide pair**, never a fragile entrance animation.
2. **Repo is the source of truth for content + imagery.** Pull standards text, objectives, sections, biographies, primary sources, vocabulary, and images from the `Trooptoteacher/history-hack-web-app` repo / web app first. Only source missing imagery externally (public-domain LOC/NARA/Smithsonian), caption + cite it, and add it back to the repo.
3. **It's TCAP, not "tap."** Purpose: surface TCAP-EOC-relevant content and Tennessee connections.
4. **Every standard runs as a full lesson** in a fixed repeating sequence (see Deck Structure). When a new standard starts, highlight the standard code, the official TN standard text, and the "I Can" objective.
5. **All imagery is public-domain, source-captioned on-slide, and historian-verified.** No AI-generated imagery. No decorative clip art. Every image carries a caption + clickable archive source.
6. **Brand kit is locked** (see Brand System). System fonts only (Georgia / Calibri / Trebuchet MS) so it renders on any school computer.
7. **Layered answer keys are mandatory** (speaker notes + reveal slides + printable PDF). This is the "Platinum" differentiator for the for-sale product.
8. **Mandatory QC before delivery** (markitdown integrity + subagent visual review + fix-and-verify cycle). See QC section.

## Brand System (locked — do not change)

| Token | Hex | Use |
|---|---|---|
| NAVY | `#1A2332` | Section bands, dividers, title/closing backgrounds |
| A250BLUE | `#002858` | America250 accent on primary-source slides |
| RED | `#C62828` | Emphasis, subtitles |
| GOLD | `#C9A84C` | Rules, "I Can" bar, correct-answer highlight |
| GOLDBR | `#F9A825` | Brighter gold accent (PDF uses `#B8860B`) |
| CREAM | `#F7F4EC` | Warm content background |
| INK | `#1F2430` | Body text |
| MUTE | `#5C6470` | Captions, footers |
| KEYGRN | `#1B5E20` | Teacher-key / CORRECT accent (deep green) |

Fonts (slides, system only): **Georgia** (headlines), **Calibri** (body), **Trebuchet MS** (labels). PDF answer key uses Helvetica family.

Every content slide carries the copyright/brand footer: `U.S. History Hack · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards & TCAP EOC`.

## Deck Structure (fixed sequence)

**Unit open:** Cover → Unit Agenda (all standards) → Unit Hook (Turn & Talk bell-ringer returned to at the end).

**Per standard (repeat for each US.NN):**
1. **Standard Divider** — code highlighted + official TN standard text + "I Can" objective (gold bar) + **TN Social Studies Practice (SSP) pills** for that standard. Font auto-sizes to fit the objective.
1a. **Quick Review** — spaced-retrieval recall of the prior standard (Rosenshine P1/P10).
1b. **Confidence Check / Warm-Up** (`confidenceCheckSlide`, v3.2) — a DOK 1 low-stakes recall with a one-slide answer reveal. Establishes the DOK floor before the lesson's graded check rises to DOK 2–3.
2. **Hook** — short provocation/quote + discussion prompt, with a **facilitation pill** (timing + cold-call routine) and a speaker note pacing the Turn & Talk.
3. **Direct Instruction** — chunked content slides with progress dots + period imagery, each carrying a **TEACHER CUE box** (facilitation/think-aloud + cold-call prompts). Tennessee Connection call-outs where relevant.
4. **Key Figure(s)** — bio cards (label is singular "Key Figure" when only one), each with a **STRATEGY chip** naming the historical-thinking move the figure exemplifies.
5. **Primary Source Analysis** — actual document/photo + context + analyze question + a **"SOURCE IT FIRST" WHO/WHEN/WHY sourcing band tagged to the relevant SSP** + clickable source. America250 blue accent.
6. **Word Wall** — vocabulary with Spanish term for EL support, plus (v3.2) a `say:` pronunciation respelling under each English term and a per-term gold initials visual-anchor chip for dual-coding. Partial last row is centered (never leave empty grid cells).
7. **We Do (Guided Practice)** — modeled prompt → teacher think-aloud → "then you try," inserted before the Student Activity (Rosenshine P4/P5).
8. **Student Activity** — grouping/time, task, expected deliverable, entry/honors differentiation, paired companion printable (Cornell Notes).
9. **Check for Understanding — TWO SLIDES:**
   - Slide A (`checkQuestionSlide`): question + choices only, with a reveal prompt. Students attempt it.
   - Slide B (`checkRevealSlide`): correct choice highlighted in gold + "Why" explanation.
10. **Wrap-Up** — "What You Need to Know for TCAP" key takeaways + written exit ticket + (v3.2) a **DOK 3 Honors / Extension band** (argument prompt tagged to SSP.04), with **3-way reteach routing** (full-mastery / partial / reteach trigger) in speaker notes.

Note: the first Direct-Instruction slide of each standard also carries an **ELL sentence-frame strip** (v3.2 — auto-sized so it never clips), and primary-source image slides carry a **"ZOOM IN" close-looking pill** (v3.2).

**Unit close:** return to the unit hook for an evidence-based answer.

## Layered Answer Keys (the Platinum differentiator)

Provide the key three ways for every check:
1. **Speaker notes** under each check slide (`slide.addNotes(...)`) — answer + rationale for live teaching.
2. **Reveal slides** in-deck — answer + "Why" for students.
3. **Printable Teacher Answer Key PDF** — per standard: TN standard + "I Can," the check item with correct answer + explanation, the primary-source analyze prompt + suggested answer, the activity's expected deliverable, and an exit-ticket model answer. Branded (navy/red/gold), with a closing sourcing/verification note. Built with `scripts/make_key_pdf.py` from a markdown source (see `references/answer-key-template-example.md`).

## Data Contract (input JSON the build reads)

The build script (`scripts/build_deck.js`) reads three JSON files. See `assets/unit1-example/` for complete, working examples.

- **`_build.json`** — object keyed by standard code (`"US.NN"`). Each value: `{ title, iCan, tnStandard, ssps:["01","05",...], sections:[{heading, content, tn(bool)}], keyFigures:[{...,strategy}], primarySource{..., }, vocab[], weDo{skill, modeledPrompt, modeled, think, thenYou}, sourceItFirst{who, when, why}, facilitation, check{question, choices[], correct, why}, wrapUp{...} }`. **(v3.1)** `ssps` lists the TN Social Studies Practice codes for the standard (rendered as pills on the divider); `weDo` powers the guided-practice slide; `sourceItFirst` powers the WHO/WHEN/WHY band on the primary-source slide; `facilitation` feeds the Hook facilitation note; each `keyFigures` entry carries a `strategy` chip. The SSP code→label map lives in `build_deck.js` (`SSP_LABEL`).
- **`_images.json`** — array of image records: `{ id, file (absolute path), title, creator, year, medium, standardIds[], caption, alt, hostingInstitution, catalogUrl, rightsLabel, citationChicago }`. `rightsLabel` must confirm public domain.
- **`_activities.json`** — per-standard student activities, each paired to a real repo printable (Cornell Notes), with grouping/time, task, deliverable, and entry/honors differentiation.

Image→standard mapping is by `standardIds`. In `build_deck.js`, `PS_IMAGE` maps a standard to its primary-source image (set to `null` to force a clean wide-text layout when no correct image exists — never show a mismatched image). `SECTION_IMG` and `ACT_IMAGE` map instruction/activity imagery.

## Workflow

**0. GATE 0 (mandatory, before everything else) — run the two front-of-checklist prerequisites from the Non-Negotiable Rules:**
   - **0A Inventory audit:** confirm the unit's primary-source catalog (`hh-web/public/data/us-history/primary-sources/unit-N.json`) validates and every referenced image is downloaded into BOTH `unitN-full/img/` AND `hh-web/public/images/textbook/unit-N/`, public-domain + verified + captioned. If anything is missing, **source & download it first** (LOC/NARA/Smithsonian/Wikimedia), cite it, add it to the repo, and re-audit until complete.
   - **0B Content-reuse audit:** pull the existing locked content for the unit from the web app / repo / textbook (standards text, "I Can", narrative/sections, bios, primary sources, vocab, Cornell Notes) and confirm the deck will reuse and align to it verbatim — never invent. Only when 0A and 0B both pass do you continue to step 1.

1. **Confirm the unit + standards.** Identify which US.NN standards belong to the unit.
2. **Pull content + imagery from the repo first** (`Trooptoteacher/history-hack-web-app`, e.g. `public/images/textbook/unit-N/`). Use existing standards text, primary sources, vocab, bios, and the matching Cornell Notes printables.
3. **Fill imagery gaps** from public-domain archives (Library of Congress, National Archives, Smithsonian). Caption + cite each; verify it actually depicts the right subject (do not trust filenames). Add new images back to the repo.
4. **Reframe sensitive standards historian-grade / TCAP-neutral** — students analyze documented intent and consequences from evidence rather than being handed a conclusion. Run claims through the historian fact-check lens (see Companion Skills).
5. **Author the three JSON files** for the unit (mirror `assets/unit1-example/`).
6. **Build the deck:** `node scripts/build_deck.js <UNIT_DATA_DIR> <OUT.pptx>` → produces the `.pptx`. The generator is **parameterized** — it reads the data dir from the first CLI arg (or `UNIT_DATA_DIR` env var) and the output path from the second arg (or `DECK_OUT`), and the document subject from `UNIT_SUBJECT`. With no args it defaults to the bundled Unit 1 example (`assets/unit1-example/`). Image `file` paths in `_images.json` may be absolute or relative to the data dir. Example: `UNIT_SUBJECT='Unit 2 — Progressivism & Imperialism (US.08–US.15)' node scripts/build_deck.js ./us02 ./Unit2_Deck.pptx`.
7. **Build the printable answer key:** author the answer-key markdown (mirror `references/answer-key-template-example.md`), then `python3 scripts/make_key_pdf.py` → produces the branded PDF. The PDF script renders markdown links `[text](url)` as clickable hyperlinks — keep source notes in that form.
8. **Write/refresh the Usage Guide** from `references/usage-guide-template.md` (update file names, slide count, unit title).
9. **Run full QC** (next section).
10. **Deliver** the `.pptx`, the answer-key `.pdf`, and the usage guide `.md`. Use stable share names so versions stack: `unit{N}_tcap_deck`, `unit{N}_teacher_answer_key`, `unit{N}_deck_usage_guide`.

## Credit-Conservation Guardrails (v3.3 — apply to every unit)

These four rules cut wasted spend without lowering quality. They amend GATE 0A and the QC section.

1. **Front-load image-content verification ONCE, before authoring.** As part of GATE 0A, verify in a single up-front batch pass that every image actually depicts its stated subject — open each candidate image and confirm the content matches the person/place/event/program it will illustrate. NEVER trust filenames. Reject or null anything that does not clearly depict its subject, and record the verification result per image alongside `_images.json`. This is mandatory so we never enter the expensive build → QC → rebuild → re-QC loop. (Unit 5 slipped precisely because a couple images were trusted by filename and only caught at visual QC, forcing a rebuild.)
2. **One full visual QC pass, then changed-slides-only.** Run the full-deck visual QC subagent exactly once. After any rebuild, re-QC ONLY the slides that actually changed — never re-review all N slides.
3. **Cheap model for routine QC, premium only at the final gate.** Use a cheaper/faster model for routine visual defect-spotting; reserve premium reasoning for the single final confirmation.
4. **Lean deck: spot-check reused-image slides only.** The lean deck is derived from already-QC'd teacher content — skip the separate full QC subagent and spot-check only the slides that reuse teacher-deck images.

## QC (required — do not skip)

**Build invariant:** the deck is generated **natively as `.pptx` via pptxgenjs**, never from HTML or
markdown; set **`pres.layout` BEFORE adding any slides** (16:9 `13.333"×7.5"`) — it can't change once
slides exist. Then convert to PDF via LibreOffice.

**LOCKED QA gates, in order** (`00_START_HERE/BUILD_STANDARD.md` §4a): (1) markitdown content dump →
(2) `validate.py` file check → (3) render to images and visually inspect **every** slide for
overflow/clipping. **Gate 3 is MANDATORY — clipped/overflowing text passes gates 1 and 2 silently**
(markitdown reads the text that exists; validate.py checks the package, not the layout). Detail below:

1. **Content QC (gate 1):** `python -m markitdown deck.pptx` — verify slide count, no placeholder/lorem text, no truncation, correct order, names consistent with `tnStandard`.
2. **File-integrity QC (gate 2):** run the `pptx` skill's `scripts/office/validate.py` on the deck (package integrity — no orphan/duplicate parts) **and** a python-pptx load→save round-trip, confirming the zip has no duplicate entries. Duplicate slides only with the `pptx` skill's `add_slide.py` — never python-pptx `add_slide`.
3. **Visual QC (gate 3 — MANDATORY) via subagent (fresh eyes) — FIRST pass only:** `soffice --headless --convert-to pdf deck.pptx` then `pdftoppm -jpeg -r 150 deck.pdf slide`; send slide images to a `run_subagent` visual reviewer and read **every** slide for overflow/clipping. Subagent slide N = PDF page N = `slide-NN.jpg`. **Use a cheaper/faster model for this routine defect-spotting pass** (visual defect-spotting does not need top-tier reasoning) — reserve the premium model only for the final gate.
4. **Targeted fix-and-verify cycle (credit-saver):** fix every issue, then **re-QC ONLY the slides that actually changed** — render just the changed slides and self-inspect them (or hand only those slide images to the reviewer). **Do NOT re-review all N slides after a rebuild.** Image fixes are almost always confined to a handful of slides; a full second visual QC pass across the whole deck is wasteful. Do the full-deck pass exactly once (gate 3); every subsequent cycle is changed-slides-only.
5. **Final gate:** once no defects remain, a single premium-model confirmation of the changed slides is sufficient. Do not run repeated full-deck passes.
6. **Imagery audit:** every image is public-domain, captioned on-slide, correctly depicts its subject, and the primary-source image matches the standard (no duplicates across slides; null over mismatch). Most of this is already satisfied by GATE 0A above.
7. **Answer-key PDF QC:** read every page; confirm no overlap/cutoff and that source links render as clickable hyperlinks (not raw `[text](url)`).

### Lean deck QC (derived deck — do NOT full-QC)

The lean student deck is derived from already-QC'd teacher-deck content and images. **Skip the separate full QC subagent.** Instead, **spot-check only the slides that reuse teacher-deck images** (render just those slides and self-inspect). Because the source content and imagery were already verified in the teacher deck, a full independent visual QC of the lean deck is redundant.

Render command (zero-padded, adjust slide count):
```
cd <workspace> && node scripts/build_deck.js <UNIT_DATA_DIR> <deck>.pptx && rm -f slide-*.jpg *.pdf \
 && soffice --headless --convert-to pdf <deck>.pptx \
 && pdftoppm -jpeg -r 110 <deck>.pdf slide
```

## Companion Skills (run alongside, do not duplicate)

- `historian-factcheck-agent` — verify every date, statute, case, number, name, quote before publication.
- `tn-textbook-adoption-agent` — interpretive balance, rubric, Policy 2.600 / Schedule F readiness.
- `ell-bilingual-review-specialist` — EN/ES word-wall and scaffolding.
- `accessibility-qc-agent` — WCAG / UDL final gate.
- `history-hack-poster-packet-builder` — sibling brand-locked print product (same brand kit).

## Bundled Resources

- `scripts/build_deck.js` — the pptxgenjs deck generator (brand kit, all slide functions, two-slide reveal, layered notes, imagery maps, Quick Review + exit tickets + DOK badges, plus the **v3.1 pedagogy functions**: `weDoSlide`, SSP-pill rendering on `standardDivider`, the SOURCE-IT-FIRST band on `primarySourceSlide`, the STRATEGY chip on `bioSlide`, the TEACHER CUE box on `contentSlide`, and the Hook facilitation pill; plus the **v3.2 functions**: `confidenceCheckSlide` (DOK 1 warm-up), the Wrap-Up Honors/Extension band, Word-Wall `say:` pronunciation + initials visual-anchor chip, the auto-sized ELL sentence-frame strip and ZOOM IN pill, and the two-row Key Figures layout for 4+ figures. **No emoji/symbol glyphs anywhere** — labels are text or drawn shapes for reliable rendering). The canonical generator. **Parameterized** via CLI args / `UNIT_DATA_DIR` / `DECK_OUT` / `UNIT_SUBJECT` env vars; defaults to the bundled Unit 1 example.
- `scripts/make_key_pdf.py` — ReportLab branded Teacher Answer Key PDF renderer (markdown → PDF, clickable source links).
- `assets/unit1-example/` — working `_build.json`, `_images.json`, `_activities.json` + `img/` (15 public-domain JPEGs) for Unit 1 (the self-contained data-contract reference; `node scripts/build_deck.js` builds it with no args).
- `references/usage-guide-template.md` — the teacher usage guide to adapt per unit.
- `references/answer-key-template-example.md` — the Unit 1 answer-key markdown source to mirror.

---

© 2026 TroopToTeacher Technologies LLC. Proprietary. All rights reserved.
