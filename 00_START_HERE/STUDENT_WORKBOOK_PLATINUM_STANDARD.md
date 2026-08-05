# U.S. History Hack — Student Workbook Platinum Standard

**Version:** 1.0 — **LOCKED** (approved by Sean)
**Owner:** TroopToTeacher Technologies LLC
**Status:** Authoritative spec. This governs **every** U.S. History Hack Course Standard student workbook — every unit, every standard. Geometry, typography, palette, sections, and all guardrails below are locked to the **Unit 6 reference build** (`00_START_HERE/PLATINUM_REFERENCE_BUILD/`), which was rendered and QC'd page-by-page. Any change to a future workbook that deviates from this doc is a defect unless this doc is updated first.

---

## 0. How this document works (the collaboration loop)

This is the single control document for how every U.S. History Hack **student workbook** is laid out and what goes into empty space. It is deliberately written in plain language with concrete numbers so you can edit it without touching code.

The loop:

1. **You edit this file.** Change any number, rule, or activity. Strike what you don't like, add what you want. Use the `DECISION NEEDED` flags — those are places where the current assets disagree and only you can settle it.
2. **You hand it back to me.**
3. **I encode it.** Every value here maps to a specific place in the build engine and the web CSS (see §9, "Where each value lives"). I change the code to match this file, rebuild a sample, and show you the result.
4. **This file wins.** When the code and this document disagree, this document is correct and the code gets fixed — not the other way around.

Everything below reflects what the engine and skills **currently** do, so you're editing reality, not a wish list. Anything I inferred or that is inconsistent across assets is flagged.

---

## 1. Page geometry & margins

| Parameter | Current value | Notes |
|---|---|---|
| Trim size | **8.5 in × 11 in (US Letter), portrait** | Fixed. Do not change without re-checking every table width. |
| Margins | **0.8 in top/bottom · 0.9 in left/right** | LOCKED (Unit 6 reference build). |
| Printable body width | **6.7 in** | = 8.5 − (2 × 0.9). All content boxes size to this. |
| Header / footer distance | **0.5 in each** | Running header (unit · edition) top-right; footer bottom. |
| Header content | Right: `U.S. History Hack™ · Unit N · Course Standard Edition` | |
| Footer content | Left: `U.S. History Hack™ · Unit N (Course Standard) · © 2026 TroopToTeacher Technologies LLC` · Right: **dynamic page number** | Page numbers never hardcoded. |
| Printable **body** (for white-space math) | Everything **between the header and footer**, inside the side margins | The area §5 measures. |

---

## 2. Typography

**One type family — Calibri — used throughout** (Course Standard reference; LOCKED).

| Element | Font / size | Color |
|---|---|---|
| Title (cover / section) | Calibri 28 pt bold | Navy |
| H1 section head | Calibri 18 pt bold | Heritage Blue `#1F3A5F` |
| H2 sub-head | Calibri 14 pt bold | Heritage Blue `#1F3A5F` |
| H3 / activity label | Calibri 12 pt bold | Red `#B22234` |
| **Body text** | **Calibri 10.5–11 pt** | Ink |
| Table cell / compact furniture | Calibri 9.5–10.5 pt | Ink |
| Fine print (caption, credit, footer) | Calibri 7–9 pt | Muted |

**Font floors (hard rules):**

- Essential student-facing instructional text: **≥ 10.5 pt** whenever practical.
- Never below **9.5 pt** in compact activity furniture (table cells, response frames).
- Fine print (captions, credits, footers): 7–9 pt is acceptable.
- **Never shrink essential instructional text just to make an activity fit.** If it won't fit at size, use a smaller activity or reflow (see §5).
- **Strip the leftover Word-default blue (`#2E74B5`) heading styles** — only the branded Calibri navy/red headings ship.

---

## 3. Brand palette

Light writable surfaces are intentionally pale so students can write on them and everything stays grayscale-legible.

| Token | Hex | Use |
|---|---|---|
| Heritage Blue (navy) | `#1F3A5F` | Headers, bands, rules |
| Patriot Red | `#B22234` | H2, accents, emphasis |
| Muted Gold | `#C9A227` | Kickers, badges, Tennessee accent (sparingly) |
| Founders Cream | `#F8F5EF` | Callout and content-box fill (dominant field) |
| Navy 2 (secondary) | `#2C3E63` | Panels |
| Light | `#EEF2F8` | Tints |
| Border | `#CBD2DE` | Box rules |
| Writing-line | `#9AA0AB` | Faint response guide-lines |

**Canonical palette (LOCKED — America 250; migrated Aug 2026 per CLAUDE.md production guardrail):**
Heritage Blue **`#1F3A5F`** · Patriot Red **`#B22234`** · Muted Gold **`#C9A227`** · Founders Cream **`#F8F5EF`** · writing-line **`#9AA0AB`**. Cream-dominant, blue-structure, red-emphasis, gold-sparingly. The legacy tokens `#1B2A4A`/`#0A1F3C`/`#143159` (navy), `#C89B3C`/`#C9A84C` (gold), `#F7F5EF` (cream), `#C4CCDA` (line) are **retired** — migrate any lingering use to the canonical set. Full spec: `00_START_HERE/BRAND_PALETTE.md`.

**Grayscale rule (locked):** no color-only encoding. Anything communicated by color must *also* be communicated by shading, a rule/border, or a text label, so the book photocopies clean in black and white.

---

## 4. Section order & page anatomy

### 4.1 Every content page, top to bottom
1. **Running header** (unit · section).
2. **Page kicker + heading** (Georgia).
3. **Name / Class / Date** line where the page is student work.
4. **Content** — instruction, source, organizer, or task, sized to the 7.06 in body width.
5. **UDL · MTSS supports** where the page is instructional (Scaffold / Extend / Show-it-your-way).
6. **Running footer** (copyright · page number).

### 4.2 Workbook section order (reading order)
1. **Cover** — unit title, product name ™, Tennessee Connection line, `[to be assigned]` ISBN.
2. **Copyright page** — TroopToTeacher Technologies LLC; public-domain rights statement; single-classroom license; framework-stack sentence.
3. **Table of Contents** — page numbers captured dynamically.
4. **Tennessee Standards Alignment crosswalk** — content standards (verbatim text) → page(s), plus Social Studies Practices (SSP) → page(s); each labeled **Full** or **Context** honestly.
5. **Accessibility & Accommodations matrix** — learner need → built-in support → where → teacher action; includes the IEP/504 non-replacement guardrail.
6. **How to Use This Workbook.**
7. **Instructional core** — lesson/source sequence for the unit's standards.
8. **Reading the Data / Mapping the Nation** where the standard calls for it.
9. **Tennessee Connection** — the differentiator; must be prominent.
10. **Reusable graphic organizer.**

> **RESOLVED (Sean) — unit workbook and DBQ are two separate products, two separate standards.** This document governs the **unit (Course Standard) student workbook ONLY** — the lesson-by-lesson book with Cornell/guided notes, the 7-activity spine, and the deck-aligned sequence, built by the `history-hack-unit-content-build` skill. The **standalone DBQ workbook** (a Document-Based-Question SKU: one investigation question, curated document set, HIPPO/OPTIC, essay + rubric) is a different product governed by the `history-hack-dbq-workbook` skill. Do not merge the two vernaculars or let this standard absorb the DBQ architecture (or vice-versa). A unit workbook may *link* to a standalone DBQ, but neither embeds the other.

**Non-negotiables carried from the skills:**
- Trademarks use **™**, never ®.
- Never fabricate an ISBN or any identifier.
- Public-domain / openly-licensed sources only; honest provenance on every asset.
- Accommodations language: supports work **alongside — never in place of** — a student's IEP/504 accommodations.
- Preserve scaffold fading across a unit (explicit prompts early → independent analysis late). **Available space never justifies restoring an earlier scaffold on a later page.**

---

## 5. White-space standard — what to do with empty space at the bottom of a page

This is the part you specifically asked to formalize. The rule is: **empty space is either intentional workspace or a defect — never accidental blank.**

### 5.1 First, is the space intentional?
**Exempt (leave it):** any space that is *labeled* writing, drawing, mapping, graphing, planning, or note-taking room. Intentional workspace is a feature.

**Defects (must be fixed):** unlabeled emptiness, an orphaned heading, a detached question option, a rubric or table fragment carried over alone, or one or two stray lines at the top of a page.

### 5.2 Measure, then fill by band
After the page renders, measure the **unused printable-body area** (the §1 body, excluding header/footer/margins) and apply:

| Unused body area | Required disposition |
|---|---|
| **Under 20%** | Pass — leave it. |
| **20–40%** | Add a **quarter-page** activity. |
| **40–65%** | Add a **half-page** activity. |
| **65–80%** | Add a **three-quarter-page** activity. |
| **Over 80%** | **Merge / reflow first.** Use a full-page activity only if the page is genuinely necessary. |

### 5.3 Rules for anything you add
1. **Context-matched** — fits this page's content, standard, and source type (see §5.5).
2. **Standards-aligned** — tied to a US.xx standard and/or an SSP practice.
3. **Produces observable thinking** — writing, sorting, graphing, mapping, sourcing, or argument, never passive filler.
4. **Never creates a new page.** If it would spill, pick a smaller component or reflow.
5. **Respects scaffold fading** — early pages may give frames/word banks; later pages require independence. Do not add a scaffold a later page has intentionally dropped.
6. **Respects the font floors** (§2). Never shrink essential text to fit an activity.
7. **No filler, no decorative art, no repeated comprehension questions, no busywork.**

### 5.4 The activity library (by footprint)

**Quarter-page (20–40%)** — one compact thinking move, 2–4 response lines:
- Evidence → inference → significance.
- Sourcing quick check (creator / audience / purpose → effect on usefulness).
- One-sentence data claim (trend + one number + connection).
- Counterclaim check (strongest opposing claim + supporting source).
- Vocabulary / cognate connection (define + use in a claim; cognate for multilingual access).
- Best-evidence selection (choose strongest detail + why it beats another).

**Half-page (40–65%)** — multi-step analysis with student choice:
- Claim–Evidence–Reasoning builder (claim + two details + reasoning).
- Compare-and-corroborate matrix (Source A / B / agree / disagree / more useful).
- Thesis stress test (draft → test against a contradicting source → revise).
- Context ladder (event → unit development → national context → back to source).
- Data transformation task (sketch trend, label turning point, write a data claim).
- Student-choice processing lab (pick one: 15-word headline / labeled sketch / paraphrase / cause-effect chain).

**Three-quarter-page (65–80%)** — a substantial lab that stands alone:
- Source investigation lab (identify → explain → contextualize → corroborate → claim).
- Cluster synthesis lab (sort into interpretations, rank evidence, name a contradiction, provisional thesis).
- Data & map reasoning lab (read the graphic, transform it, pattern, one cause + one consequence, connect).
- Historical decision lab (problem → options → evidence available then → defend a decision → compare to outcome).
- **Tennessee Connection investigation** (TN source/stat/map → connect to national development → confirm/complicate/challenge the pattern).

**Full-page (only after a documented reflow attempt, >80% on a necessary page):** expand a three-quarter lab's response space, evidence tables, or structured reflection. Never invent a new reading passage just to fill a page.

### 5.5 Which activity fits which page

| Page type | Preferred fills |
|---|---|
| Text primary source | Sourcing quick check, CER builder, compare/corroborate, source investigation lab |
| Visual primary source | Evidence sketch, inference chain, independent source analysis |
| Data table / chart | One-sentence data claim, data transformation, data reasoning lab |
| Map | Map reasoning lab, geographic inference, Tennessee Connection |
| Prewriting / essay planning | Thesis stress test, counterclaim check, evidence route planner |
| Vocabulary / language access | Cognate connection, self-use checklist, sentence-frame choice |
| Teacher-facing page | Decision rules, scoring calibration — **never** student busywork |

### 5.6 Spaced repetition & check-ins (the supports you asked to add)

Two families to reach for when the page's own content is complete but space remains — they turn dead space into retention and self-regulation:

**Spaced retrieval / distributed practice (quarter- or half-page):**
- **"3 from before"** — three quick retrieval prompts pulled from *earlier* standards in the unit (not this page's content), answered from memory. Interleaving old material is what makes it spaced, not massed.
- **Cumulative timeline stitch** — add today's event to a running unit timeline printed at the page foot; connect it to one prior event with a because-statement.
- **Vocabulary spiral** — one current term + one term from two lessons back, each used in a sentence that links them.
- **Two-week callback** — a single prompt flagged for the teacher to revisit ~10–14 days later (supports the unit-level spaced-review plan; the book seeds it, the curriculum layer schedules it).

**Metacognitive check-ins (quarter-page):**
- **Confidence + next action** — "ready / almost / need support," then name the next move (reread, use the companion, compare a source, ask a partner, revise).
- **Muddiest point** — one sentence on what's still unclear + where the student will look.
- **Goal check** — restate the page's learning target in the student's own words and rate progress against the success criteria.

> Honesty guardrail (from the Schedule F posture): a single workbook seeds spaced review; it does not *own* the schedule. Sustained spaced repetition is a **curriculum-layer** responsibility. Keep the in-book spaced items as callbacks and seeds, and don't overclaim the book as a complete spaced-repetition system.

### 5.7 QC log (record for every page ≥ 20% unused)
`page | unused_% | band | original issue | disposition | activity | context | scaffold stage | min instructional font | page count before→after | visual pass`

No workbook is Platinum-ready until every flagged page has a defensible disposition and **no added activity created a spill page.**

---

### 7.11 Data visualization — charts, graphs & data literacy (LOCKED — build them wherever the content warrants)

Data literacy is a tested C3 / Social Studies Practice skill, and TCAP leans heavily on chart / graph / map stimuli. The Platinum bar is to **teach students to both read AND make** data representations — so **wherever a standard carries quantitative or spatial data, the workbook includes an original, accurate, sourced visualization.** Do not ration these: build a chart/graph **every time the content genuinely calls for one** (economic indicators, unemployment/GDP, immigration and demographic shifts, election results, war production/casualty figures, urbanization, spending, etc.). More is better when the data is real and relevant — never decorative filler.

- **Types:** bar, line, pie/100%-stacked, histogram, simple scatter, and point-location/thematic map schematics (on a PD Census/US-gov basemap — never a hand-built political/boundary map; accuracy + neutrality rule from §visual sourcing still applies).
- **Two uses per data set:** (1) a **stimulus** the student interprets (a "read the data" prompt: trend, compare, infer, "what does this NOT tell you?"), and (2) a **create/represent** move where the student completes or builds a small chart from given numbers — the SSP "construct a visual representation" skill.
- **Accuracy (Policy 2.600):** every chart is generated from a **verified dataset** with a **Sources & Method sidecar attached to the chart** — data source (agency + URL), the method/formula with variables defined, the computed figures, units, N, and a verification line. No invented numbers, no misleading axes (zero-baseline for bar charts; label units and breaks). Run values past `historian-factcheck-agent`/source when non-obvious. Reference build: `FutureReady_Loan_Math` (loan-cost chart with full Sources & Method).
- **Time-sensitive figures → annual currency guardrail (LOCKED Aug 2026):** any chart whose numbers age (federal loan rates, Pell max, FAFSA timing, tax/wage data) registers those figures in a **single source-of-truth JSON** (`future_ready_data.json`) with per-figure provenance (`source`/`source_url`/`last_verified`) and a `_meta.review_by` date. The generator **reads the JSON** (never hard-codes a rate twice); the **`verify_future_ready_currency.py`** guardrail fails the build when a figure lacks provenance or the annual review is overdue, and its CI workflow runs on every PR **and monthly** so staleness surfaces within ~30 days. Annual update = edit one JSON file, bump the dates.
- **Accessibility (WCAG 2.2 AA):** every chart ships with **alt text AND a plain data-table fallback** so it is not the only way to get the information; grayscale-legible (pattern/label, not color alone — see §3).
- **Owner:** `history-hack-unit-content-build` generates and embeds workbook/deck charts programmatically from datasets; `history-hack-poster-packet-builder` owns the large-format Data & Economics wall poster. Charts are counted in the visual-asset package and QC'd on render like any other visual.

## 6. Print & production rules

- **DOCX-native → PDF (LOCKED). Print-first platform.** Author the workbook (and every teacher
  guide / answer key) as a **native `.docx`** with the docx engine (`build_guided_notes.py` /
  `build_teacher_guide.py` / `engine.js`), then **convert to PDF with LibreOffice**
  (`HOME=/root/lohome soffice --headless --convert-to pdf`). **Never author the document as HTML and
  render it to PDF** — HTML→PDF mangles page breaks, running headers/footers, and page numbers. The
  **editable `.docx` is the author's archive / master** (TroopToTeacher's source of truth, kept for
  future edits); **the PDF is the distribution artifact teachers receive and print** — a faithful
  convert of the `.docx`. Teachers do not edit the Word master. (Direct vector generation is reserved
  for 24×36 posters, which are not documents.)
- **300 DPI**; grayscale-legible (see §3 grayscale rule).
- Workbook **≤ 120 pages**.
- Two-pass build so the TOC and crosswalk page references reconverge after any white-space insert (never hardcode a page number).
- **Keep-with-next / widow-orphan control:** headings stay with their first block; question stems stay with their options; short tables, rubrics, prompts, and response frames never split across pages.
- Every image is verified against its own caption *and* the surrounding tasks before shipping (medium labeled honestly — engraving ≠ photograph).
- **Pagination-fidelity check (gate):** after the convert, confirm page breaks land where authored, the running header/footer + **live page-number field** survive, per-activity page isolation holds, and there are zero blank pages.

---

## 7. Accessibility & UDL (built in, not appended)

- **Engagement:** choice, relevance, goal clarity, feedback.
- **Representation:** readable text, visuals, vocabulary support, chunking, bilingual/primary-language access, read-aloud-friendly structure.
- **Action & expression:** write / say / diagram response options on tasks.
- WIDA supports at L1–2, L3–4, L5–6 (sentence frames, graduated demand).
- WCAG 2.2 AA for the web edition: contrast, headings, alt text, keyboard access.
- English/Spanish parity for student-facing materials.

### 7.1 Front / back supports model (validated on the Unit 6 pilot)

Every activity is a **clean front** (the task) with its **UDL/MTSS supports on the verso** (back page), so one worksheet serves three print modes:
- **front only** — independent, no scaffold;
- **front + back (duplex)** — scaffolded;
- **back only** — supports as a standalone reference.

Rules:
- Each activity's front is a **fixed page count** (ideally one page) so its support lands on the immediately following page; the support section uses `page-break-before`.
- Support content is **matched to the task** — sentence stems, a worked exemplar, a student-language rubric, cognates / word bank, an annotation guide, or HIPPO guiding questions — never busywork.
- Supports **add access, never lower the goal**, and work **alongside — never in place of** — IEP/504 accommodations.
- The front's goal and rigor are **identical whether or not the back is printed.**
- Feasibility by activity: Vocabulary, Vocab Studio, Practice Quiz, and CER take the model directly (one-page fronts); Cornell Notes, Close Read, and Primary-Source/HIPPO must first be trued to a fixed page count. Reference implementation: **Unit 6, Activity 7 (CER)** — CER front + verso Writing Supports (stems + model + student-language rubric).

### 7.2 Response space (guardrail)

Every box or prompt that asks a student to write **must give them somewhere to write**:
- If the box has room, include **notebook-style writing lines** (faint ruled lines) sized to fill the box.
- If the box has no room, **redirect the response explicitly** — e.g., "Do this in your notebook or on a whiteboard — be ready to share" — rather than leaving a prompt with nowhere to respond.
- A response prompt stranded with no writing space **and** no redirect is a defect.
- For "connect / synthesize / sketch" prompts that need more room than a box allows, make it an active task with a named location (notebook, whiteboard, stand-and-share).
- **Lined notebook paper (multi-line writing areas):** when a prompt gives students several full lines to write on (e.g. the NOTES SUPPORTS "Try it"), the ruled lines must be built as a **borderless table whose rows each carry a bottom border** — **not** stacked bordered paragraphs, which collapse in Word/LibreOffice into a single rule. Each paragraph carries exactly one `w:spacing` element. (Engine: `notebook_table()` in `build_guided_notes.py`.)

### 7.3 Blank-space guardrail (must fit)

Fill meaningful blank space with supports or a context-matched activity (§5) — **but the added content must fit the space it fills; it may never push content onto another page.** If it cannot fit, redirect the response (§7.2) or reflow. A near-empty page is a layout defect: fill it (often best as a **back-page support**, §7.1) or reflow it away. Always render and visually confirm after filling.

### 7.4 CER self-grading rubric (required — College Board AP-aligned; LOCKED Aug 2026, Sean)

Every Constructed Response (CER) includes a **student self-grading rubric modeled on the College
Board AP U.S. History essay rubric** — the **6-point Long-Essay scale**, presented in the AP's own
**A / B / C / D reporting-category** layout so it's familiar to any AP reader. This **supersedes** the
former 1–4 /16 (Claim/Evidence/Reasoning/Conventions) rubric.

| AP category | CER term | Points | Earns the point(s) |
|---|---|---|---|
| **A — Thesis / Claim** | Claim | 0–1 | Defensible claim that answers the prompt + a line of reasoning (not restating the prompt). |
| **B — Contextualization** | Context | 0–1 | Broader historical context (before/during/after) relevant to the prompt. |
| **C — Evidence** | Evidence | 0–2 | +1 two specific accurate facts · +2 *uses* that evidence to support the argument. |
| **D — Analysis & Reasoning** | Reasoning | 0–2 | +1 a reasoning skill (causation / comparison / CCOT) · +2 complex understanding (perspective, qualifier, connection). |

Total **/6**, with a **Reflect & Revise** block (what my score tells me · lowest category · the one
change to earn the next point · recurring weak spot across CERs · re-score line). When the CER is
**document-based**, category **C extends to the AP 7-point Document-Based scale** — the teacher flags
which is in play. Lives on the **CER Writing Supports verso** (§7.1). Reference build: the AP-aligned
`FutureReady_CER_SelfGrade` printable. (The scored self-grade is a self-assessment move — §7.10 — and
teaches against the same criteria the teacher scores.)

### 7.5 QC gate (render + look)

No workbook change ships until it is **rendered to PDF and visually inspected** page by page — writing lines present and legible, no prompt without response space, no bleed/orphan, and every filled space actually fits. (Environment note: LibreOffice `soffice --headless --convert-to pdf` + `pypdfium2` renders faithfully once `libreoffice-writer` is installed.)

### 7.6 Course Standard per-standard anatomy (LOCKED — Unit 6 · US.45 reference)

Every standard runs an identical structure. Front matter opens the unit; each standard then runs an opener + a seven-activity cycle + an exit ticket. Front pages are clean/independent; UDL·MTSS supports live on the **verso** (§7.1).

**Front matter (once):** Cover · Copyright/Framework · **Unit at a Glance** (standards list + 7-activity cycle, *no page numbers* — replaces the Word TOC field) · **TN Standards & SSP Crosswalk** (bottom space filled — Lenses/Dimensions coverage row / "how to read the crosswalk" strip) · **Accessibility/UDL & Accommodations matrix** (bottom space filled — extended rows + the non-replacement guardrail + UDL 3.0/CAST 2024 note) · **How to Use This Workbook** (the **legend** — verified & updated to teach the current systems: **Lenses/Dimensions pills** C/E/G/H/P/T/TCA, the **verso supports** model + three print modes, the **Future Ready** callout, **self-check keys**, **▶ Deck** keying; the fuller legend fills the page — no bottom white space) · **My SMART Goals** (short/mid/long, §7.12) · Before You Begin (goal exemplar). Every front-matter page obeys the §5 white-space bands — no unlabeled blank.

**Per-standard opener (one page):** Learning Targets · **Lenses** (the standard's Dimension pills — C/E/G/H/P/T/TCA; §7.13) · **CORE PATH** (identify the path only — no UDL/MTSS jargon shown to students) · **SET YOUR SMART GOAL** (the guided SMART frame — S·M·A·R·T tagged with **ruled lines to write it**; this is the per-unit **short-term** goal that ladders to *My SMART Goals*, §7.12; fills the opener) · **HOOK** (a strong *read*, not a writing task) · ACTIVATE (think / notebook) · **PREVIEW & PREDICT (ruled** — remaining opener space becomes writing room). Every response box has writing lines or a redirect (§7.2).

**The seven-activity cycle:**
1. **Vocabulary** — word bank + language support + knowledge self-check. *Verso:* Vocabulary Supports (word-attack, quick practice *with space*, cognate practice, study tip). MAKE IT YOURS → notebook/whiteboard redirect.
2. **Vocabulary Studio** (Frayer) — RESPONSE CHOICE. CONNECT THE TERMS → notebook/whiteboard redirect (no stranded box).
3. **Cornell Notes (GUIDED — Direct Teaching)** — the cue column is **pre-seeded** with the standard's direct-instruction (DI) segments **in lecture order**: navy topic · gold `▶ Deck · DI N of M` (maps 1:1 to the teacher deck's on-slide "N of M" DI labels — **every reference populated**, never blank) · italic guiding question. My-notes column (ruled, RESPONSE CHOICE), More Notes/Diagrams, an **expanded DOODLE ZONE** (a labeled sketchnote/dual-coding space with generous room — LOCKED Aug 2026, Sean; reverses the prior "no doodle zone" rule), Key terms, Summary, **Progress Check** (each item carries a **locator cue** — "→ see cue N / your notes"), **Check Yourself** (a rating scale on **every** item, not only item 1), and an **extended-room 12–15 word headline** (ruled). *Verso:* **NOTES SUPPORTS** ladder (§7.9).
4. **Close Read** — key-terms-first *before* the reading; CORE PATH passage with **spaced sub-sections** (visible gap between paragraphs — kills the end-of-passage white space, §7.7); the **academic/tie-together vocabulary words are bolded in-passage**; CLOSE-READ EVIDENCE LAB with ruled answer space; leftover space takes a context-matched text-source fill (§5.5). **Thesis mini-lesson:** "How to Write a Thesis" scaffold introduced here and carried onto the CER Writing Supports verso (§7.6 Act 7) — the thesis is the Close-Read→CER bridge.
5. **Primary Source / HIPPO** — front: source + HIPPO table + confidence check-in. **Every support/response area has real ruled writing room (`notebook_table`) or an explicit redirect** ("write this on your whiteboard / here") — no stranded prompt with nowhere to write (§7.2). *Verso:* HIPPO Supports (guiding questions, sourcing frames, model, try-it).
6. **Practice Quiz** — numbered MC items + **on-page self-check answer key** filling the page (correct letter **+ a one-line rationale** per item: why right / why the tempting distractor is wrong; "commit first, then check"). The rationale key is the Integrity self-grade move and fills the Activity-6 white space. **Rule:** *every* formative MCQ set anywhere in the book ships this self-check key at point of use.
7. **Constructed Response (CER)** — front: big-question organizer, response table, **self-grade rubric** (§7.4), **peer review** (glow/grow/revision). *Verso:* CER Writing Supports (stems, model, student-language rubric, plan-it organizer, word bank).

**Exit Ticket** — closes the standard, kept **whole on its own page** (`cantSplit`), never split across pages.

Reference build: **Unit 6, US.45** (rendered and QC'd page-by-page). Units US.46–US.58 are built by propagating this exact anatomy.

### 7.7 Spacing & separation (LOCKED)

- **Space before every section title** so a title never butts against the block above it.
- **Multi-section readings** (e.g. the CORE PATH passage): add space before each **sub-heading** so sections don't jumble together.
- **Question sets** (Practice Quiz): a clear gap before each question; **questions are numbered**.
- **Standalone boxes never split** across pages — set `cantSplit` on boxes meant to stay whole (Exit Ticket, CONNECT THE TERMS, etc.).
- **No stray empty paragraphs before a forced page break** — they create blank pages. Remove them, and the QC pass (§7.5) must confirm **zero blank/near-empty pages**.
- **Writing lines** are faint ruled lines (`#9AA0AB`), sized to fill their box; response boxes with no room redirect to notebook/whiteboard (§7.2).

### 7.8 Deck ↔ workbook slide-keying (DEFERRED — build decks first)

The workbook will key each writing/response activity to the exact Course Standard deck slide (`▶ Deck slide N`), per `SLIDE_DECK_PLATINUM_STANDARD.md` §1 (shared standard-code spine, workbook→deck keying, deck→workbook cue, same-item checks). **This requires the Course Standard teacher/student decks to be (re)built first.** Until the decks exist, slide-keying is intentionally omitted — never hardcode a slide number. Sequence: build Course Standard decks → then add `▶ Deck slide N` references to the workbook.

### 7.9 Guided notes + NOTES SUPPORTS ladder (LOCKED — Unit 6 · US.45; grounded in CAST UDL 3.0 / 2024 + MTSS)

The workbook, Student deck, and Teacher deck follow **one sequence** so students follow the lecture and take notes in a clear, sequential pattern. **Activity 3 (Direct Teaching Cornell Notes) is the spine.**

**Front — guided Cornell.** The cue column is **pre-seeded** with the standard's direct-instruction (DI) segments in **lecture order**, one cue block per DI slide: **navy topic** · **gold `▶ Deck · DI N of M`** (the guided-notes bridge — it maps 1:1 to the teacher deck's own on-slide "N of M" DI labels; use the *relative* "N of M", never an absolute slide number, so it survives deck renumbering; **every reference must be populated from the deck `_build.json` — a blank `DI _ of _` is a defect**) · **italic guiding question** (what to listen for). The "My notes" column keeps ruled lines + the RESPONSE CHOICE line. Below the notes: an **expanded DOODLE ZONE** — a labeled sketchnote / dual-coding space with generous room (LOCKED Aug 2026, Sean; reverses the earlier "no doodle zone" rule — the sketch space is now a distinct dual-coding move, not a duplicate of More Notes). The **Progress Check** items each carry a **locator cue** ("→ see cue N"), the **Check Yourself** rating scale repeats on **every** item, and the **12–15 word headline** gets extended ruled room.

**Back — NOTES SUPPORTS ("build your notes, your way").** A four-rung support ladder so a high-need student can produce full notes **from the back alone** — the ceiling never drops (UDL 3.0 guideline 5.3 graduated support; MTSS Tier 1 = front, Tier 2/3 = verso):
1. **① Sentence frames — finish the thought** (4 frames).
2. **② Fill-in notes — write just the missing word(s)** (4 cloze bullets + a **word bank**) — the student writes only 1–2 words per line.
3. **③ How to build your answer** — `Name it → Define it in your own words → Give one example` + a **worked model** on a tinted card.
4. **④ Try it — write one full note in your own words** — **lined notebook paper** (5 ruled lines, §7.2) + a **Quick self-check** rubric (`☐ I named the idea ☐ I defined it in my own words ☐ I gave an example ☐ A reader could follow it`).

Intro line (the non-replacement guardrail), verbatim: *"Use one, some, or all — as much support as you need. Works alongside, never in place of, your IEP or 504 plan."*

**Spacing (fixes the "too compact / cognitive overload" note):** generous gaps before each rung heading, loose line spacing inside rungs, word bank and model each on their own tinted line/card. This white space is **intentional labeled workspace** (exempt under §5.1) — do not re-tighten it to reclaim space.

**Propagation & parity.** Every standard is built by `scripts/build_guided_notes.py`: it seeds the cue column from scratch and **clones the US.45 NOTES SUPPORTS block** (preserving every fill/border/font/spacing), swapping only the standard-specific text. This is what guarantees the formatting is identical across all standards. The cue column carries **one row per direct-instruction segment** (4 for most standards, 5 for US.51) — the table auto-expands to fit (`ensure_cue_rows`), keyed to the teacher deck's real `DI N of M` slides.

### 7.9a Activity 3 pagination & white-space guardrail (LOCKED)

The print model only holds if **notes sit on recto (odd) pages and supports on verso (even) pages** — then *print single-sided* = notes only, and *print duplex* = every notes page backed by its own support.

1. **Fits one page** (every Unit 6 standard today, incl. US.51's 5 segments): Cornell notes (front) + NOTES SUPPORTS ladder (back). Clean 2-page duplex.
2. **Needs two note pages** (a long/dense standard): **interleave, never batch** — `Notes-A / Supports-A / Notes-B / Supports-B`. Supports are **page-matched** to the notes page they back (cue-table page → content-note ladder; process/check page → summary + self-check supports). The **Try-it + self-check always lives on the activity's final support page** (never orphaned).
3. **White-space value-question rule:** if a Cornell notes page has real blank space at the bottom (per §5 bands), fill it with one small, valuable thinking move — a **prediction**, a **synthesis** ("connect two cues in one sentence"), a **metacognition** check ("which cue was hardest?"), or a **"3 from before"** spaced-retrieval prompt. Never a filler line, never a note-line duplicate of the My-notes column, and never anything that pushes content to a new page.
4. Respect the ≤120-page cap and the zero-blank-page gate; re-run the QC gate after any Cornell expansion.

### 7.10 Assessment & retrieval cadence (LOCKED — one system woven through the flow)

Assessment is not a single end-of-standard quiz — it is a **cadence** built into the 7-activity flow, so every standard carries all four assessment purposes. This is the "assessment for learning" spine (Black & Wiliam formative feedback; Roediger & Karpicke testing effect; Cepeda spacing). Each purpose has a fixed home in the flow:

| Purpose | Where it lives in the flow | Owner / engine |
|---|---|---|
| **Spaced retrieval** (distributed, interleaved) | Vocabulary spiral (Act. 1), "3 from before" + cumulative timeline stitch on white-space bands (§5.6), two-week callback seed | `spaced-repetition-engine` schedules the intervals; the book **seeds**, the curriculum layer **owns the schedule** (§5.6 honesty guardrail) |
| **Formative** (checks for understanding, low-stakes) | Cornell Progress Check (Act. 3), Close-Read Evidence Lab (Act. 4), HIPPO confidence check-in (Act. 5), Practice Quiz (Act. 6) | `history-hack-unit-content-build`; items bank-sourced + verified |
| **Self-assessment** (metacognition, student-scored) | Vocabulary knowledge self-check (Act. 1), Practice Quiz on-page self-check key (Act. 6, "commit first, then check"), **CER self-grade rubric** /16 + peer glow/grow (Act. 7, §7.4), confidence/muddiest-point/goal-check (§5.6) | student-facing; teaches self-regulation against the same criteria the teacher scores |
| **Summative** (standard/unit mastery, psychometric) | Exit ticket per standard (formative→summative bridge); the **unit test / EOC-style assessment** assembled to blueprint | `tn-assessment-specialist` (DOK/Hess/IRT, TCAP schema) — a separate deliverable the workbook links to, not embedded |

**Rules:** (1) every standard shows spaced retrieval + formative + self-assessment in-book; the summative layer is assembled by `tn-assessment-specialist` and referenced, never hand-authored in the workbook. (2) The self-check answer key sits **on the same page** as the items it checks ("commit first, then check"). (3) Retrieval prompts pull from *earlier* standards (interleaving is what makes it spaced), never this page's own content. (4) Do not overclaim the book as a complete spaced-repetition system — it seeds; `spaced-repetition-engine` owns cross-lesson scheduling.

### 7.12 Future Ready — employability & goals system (LOCKED Aug 2026, Sean; UDL 3.0 / CAST 2024)

Every workbook makes named employability skills **visible and measurable** through a Future Ready system — bookend sheets + a scaffolded SMART-goal ladder + embedded reflective questions + money-math, all rolling up to one measurable spine (the Debrief `/40`). Reference builds: the `FutureReady_*` printables.

**Per-unit bookend.**
- **Launch** (before the unit): Grade & Missing-Items check · **SMART short-term goal** (guided S·M·A·R·T frame, ruled) · **Hireability baseline** — a 10-trait 1–4 rubric (Timeliness · Integrity · Work ethic · Adaptability · Lifelong learning · Organization · Reliability · Civic responsibility · Teamwork · Leadership), each with an observable look-for, scored `/40` · **Voice-to-Email** setup + 5-part email frame.
- **Debrief** (after the unit): Goal check-in (Met/Partly/Not + evidence) · Grade delta · **Timeliness tally** (per-class on-time/late marks → total lates) · **Hireability re-score** `/40` + growth (▲▬▼) · next-unit commitment. The Launch↔Debrief delta **is** the measurement.

**SMART-goal ladder (all goals are SMART).** Students identify & create a **short-, mid-, and long-term** SMART goal, each with a **completed exemplar in a high-schooler's voice** + a blank builder (`My SMART Goals` page) and a **Reflect & Commit** piece (ladder connection · obstacle+plan · accountability partner · first step). A **SMART Support** sheet teaches the frame (what SMART means · worked model · builder · follow-up routine) and prints on the back of Launch. The opener's **SET YOUR SMART GOAL** (§7.6) is the per-unit short-term rung.

**Embedded, high-value only (never forced).** Two in-lesson elements, placed **only** where the content gives a natural hook, max ~2–3 per unit, each rolling up to the Debrief/`My SMART Goals`:
- **Future Ready Questions** — a standard-tied reflective pop-up (path after HS: trade/college/military · free college · scholarships · FAFSA · gap year), hung on the exact standard (e.g., US.05 Gilded Age, US.58 GI Bill, US.68 Space Race). Carries a sources footnote for its historical hooks.
- **Employability micro-moments** — a tiny FR tag where a trait is authentically exercised: Practice-Quiz self-check → **Integrity/Lifelong learning**; Cornell/notes → **Organization**; any collaborative task → **Teamwork/Leadership/Reliability**; Primary Source/CER → **Civic responsibility/Integrity**. Vocabulary & Close Read get **no forced tag**.

**Money-math (where economics fits).** A financial-literacy chart/worksheet (e.g., *The Real Cost of Borrowing* — computed loan amortization) built to the §7.11 data-viz + Sources & Method + **currency-guardrail** rules, tied to a standard (e.g., US.25 · the 1920s). Closed-loop: FAFSA/scholarship guidance points to the counselor / financial-aid office, no web link-outs (CIPA/COPPA/FERPA).

### 7.13 Lenses / Dimensions — disciplinary strand proof-of-coverage (LOCKED Aug 2026, Sean)

Every standard prints its **TDOE disciplinary dimension pills** on the opener (§7.6, labeled **"Lenses"** for students; **"Dimensions"** in formal/adoption contexts) and on the deck's Standard Divider: **C** Culture · **E** Economics · **G** Geography · **H** History · **P** Politics/Government · **T** Tennessee · **TCA** Tennessee Code Annotated. Pill styling: T = gold, TCA = red, others = navy. The dimension tags are sourced **verbatim** from `Live-US-History-Standards-in-order-1-95.docx` (header line only, end-anchored) into a canonical `standard_to_dimensions.json` with a verifier; a course-wide **Dimension Coverage Crosswalk** ships as proof-of-coverage. This gives adoption reviewers explicit, per-standard strand coverage.

---

## 8. Web edition parity

The print PDF is the master; the web edition must render the **same** geometry, palette, and section order:
- Same margins/body proportions expressed responsively (US-Letter body ratio preserved; content column maps to the 7.06 in body).
- Same palette tokens (once §3's canonical navy is settled).
- Same white-space discipline: the web layout must not leave large empty blocks either; the §5 activities render as interactive equivalents.
- Print-to-PDF from the web must reproduce the print book faithfully.

---

## 9. Where each value lives (my encode targets)

When you change something above, here's what I touch:

| You change… | I update… |
|---|---|
| Margins, trim, header/footer offsets | `MARGIN`, `PAGE_W/H`, header/footer draw calls in the ReportLab engine (`build_workbook_template.py`) + web CSS page vars |
| Type sizes / floors | The paragraph styles (`st_body`, `st_h1`, `st_h2`, …) + web CSS type scale |
| Palette / canonical navy | `NAVY/RED/GOLD/CARD/…` constants in the engine + brand tokens in the web edition and the graphic-organizer `toolkit_lib.py` |
| White-space bands / activity library | `white-space-activity-library.md` (the locked reference the skills read) + the render-time white-space gate |
| Section order / anatomy | The build spec + the platinum skills' anatomy sections |
| Cornell doodle zone · populated `DI N of M` · Progress-Check locators · Check-Yourself per-item rating · headline room | `scripts/build_guided_notes.py` (Activity 3 front) |
| Opener SMART goal · Preview & Predict ruled space · Lenses pills | opener builder + `standard_to_dimensions.json` |
| AP-aligned CER self-grade (§7.4) · thesis mini-lesson · HIPPO writing space · MCQ self-check key + rationale | `scripts/build_backpage_supports.py` + quiz builder |
| Future Ready system (§7.12) | `gen_future*` builders + `future_ready_data.json` (SoT) |
| Chart Sources & Method + annual currency guardrail (§7.11) | `future_ready_data.json` · `verify_future_ready_currency.py` · `future-ready-currency.yml` CI |
| Front-matter legend + white-space fills | front-matter builder (How to Use / crosswalk / accessibility matrix) |

The skills I'd sync to this file: `history-hack-unit-content-build` (the unit-workbook builder this standard governs), `history-hack-platinum-unit-builder`, `history-hack-graphic-organizer-workbook`, and `udl-cast-expert`. The standalone DBQ product is governed separately by `history-hack-dbq-workbook`, not by this file.

---

## 10. Open decisions summary (put your call next to each)

1. **Canonical navy + gold** across print/web/deck — §3. ← most important
2. **Margin width** (0.72 in vs. tighter / binding gutter) — §1.
3. **Body font floor** (10.5 pt vs. 11 pt) — §2.
4. ~~One standard for both products, or split student-workbook vs. DBQ~~ — **RESOLVED:** split. This file governs the unit workbook only; the DBQ is a separate product/standard (§4.2).
5. Anything from your **Unit 6** markup that isn't covered here.

---

*Edit freely. The `DECISION NEEDED` flags and §10 are where I most need your call. Hand this back and I'll make the code and skills obey it.*
