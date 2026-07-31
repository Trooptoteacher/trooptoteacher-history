# U.S. History Hack — Student Workbook Platinum Standard

**Version:** 1.0 — DRAFT for Sean's review
**Owner:** TroopToTeacher Technologies LLC
**Status:** Working master. Edit this file, hand it back, and it becomes the source of truth I encode into the build engine (print PDFs) and the web edition.

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
| Margins (all four sides) | **0.72 in, uniform** | Single constant `MARGIN`. Change once, everything reflows. |
| Printable body width | **7.06 in** | = 8.5 − (2 × 0.72). All content boxes size to this. |
| Running header rule | **0.55 in from top** | Thin rule; caps label above it at 0.50 in. |
| Header content | Left: `U.S. HISTORY HACK · <SECTION>` · Right: `<UNIT> · <section>` | |
| Running footer rule | **0.60 in from bottom** | |
| Footer content | Left: copyright line at 0.44 in · Right: **dynamic page number** at 0.44 in | Page numbers are never hardcoded. |
| Printable **body** (for white-space math) | Everything **between the header rule and the footer rule**, inside the side margins | This is the area §5 measures. Header, footer, and margins are excluded. |

> `DECISION NEEDED — margins`: 0.72 in is generous and reads clean, but costs page count. If you want tighter (e.g. 0.6 in) or a wider inside gutter for binding, set it here.

---

## 2. Typography

Two type families, used consistently:

- **Headline / display:** Georgia (serif).
- **Body / UI:** Helvetica / Arial (DM Sans in the engine when the font is embedded).
- **Primary-source excerpts:** serif, justified, slightly larger for readability.

| Element | Size / leading | Color role |
|---|---|---|
| H1 section head | 17 pt / 21 | Navy |
| H2 sub-head | 12.5 pt / 16 | Red |
| Small label (caps) | 9 pt / 12 | Navy |
| **Body text** | **10.5 pt / 15** | Ink |
| Primary-source excerpt | 11 pt / 16.5 serif, justified | Ink |
| Citation | 8.5 pt italic | Muted |
| Image caption | 8 pt | Muted |
| Source credit | 7 pt | Muted grey |

**Font floors (hard rules):**

- Essential student-facing instructional text: **≥ 10.5 pt** whenever practical.
- Never below **9.5 pt** in compact activity furniture (table cells, response frames).
- Fine print (captions, credits, footers): 7–9 pt is acceptable.
- **Never shrink essential instructional text just to make an activity fit.** If it won't fit at size, use a smaller activity or reflow (see §5).

> `DECISION NEEDED — body size`: 10.5 pt is the current floor for body copy. If your Unit 6 review says the reading feels dense, we can raise the floor to 11 pt (fewer words per page, more pages).

---

## 3. Brand palette

Light writable surfaces are intentionally pale so students can write on them and everything stays grayscale-legible.

| Token | Hex | Use |
|---|---|---|
| Navy | `#1B2A4A` | Headers, bands, rules |
| Red | `#B22234` | H2, accents, emphasis |
| Gold | `#C89B3C` | Kickers, badges, Tennessee accent |
| Card / cream | `#F7F5EF` | Callout and content-box fill |
| Navy 2 (secondary) | `#2C3E63` | Panels |
| Light | `#EEF2F8` | Tints |
| Border | `#C9C2B4` | Box rules |
| Writing-line | `#C4CCDA` | Faint response guide-lines |

> `DECISION NEEDED — one canonical navy (IMPORTANT)`: three different navies are in play across the assets today, and they should be reconciled to one:
> - Print workbook + graphic organizers: **`#1B2A4A`**
> - Web edition / unit-builder brand system: **`#0A1F3C`** (with secondary `#143159`)
> - Teacher slide deck: **`#1A2332`**
>
> Pick one navy (and confirm gold — the deck uses `#C9A84C`, print uses `#C89B3C`) and I'll make print, web, and deck match it everywhere.

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

> `DECISION NEEDED — student workbook vs. DBQ`: the anatomy above is the shared spine. The standalone DBQ product adds HIPPO/OPTIC document analysis; the course student workbook adds Cornell notes, guided notes, and the lesson spine. Tell me if you want this document to govern **both** or if you want me to split it into two standards after your Unit 6 pass.

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

## 6. Print & production rules

- **300 DPI**; grayscale-legible (see §3 grayscale rule).
- Workbook **≤ 120 pages**.
- Two-pass build so the TOC and crosswalk page references reconverge after any white-space insert (never hardcode a page number).
- **Keep-with-next / widow-orphan control:** headings stay with their first block; question stems stay with their options; short tables, rubrics, prompts, and response frames never split across pages.
- Every image is verified against its own caption *and* the surrounding tasks before shipping (medium labeled honestly — engraving ≠ photograph).
- Least-cost build: programmatic (ReportLab) PDF, not hand-layout.

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

### 7.3 Blank-space guardrail (must fit)

Fill meaningful blank space with supports or a context-matched activity (§5) — **but the added content must fit the space it fills; it may never push content onto another page.** If it cannot fit, redirect the response (§7.2) or reflow. A near-empty page is a layout defect: fill it (often best as a **back-page support**, §7.1) or reflow it away. Always render and visually confirm after filling.

### 7.4 CER self-grading rubric (required)

Every Constructed Response (CER) includes a **student self-grading rubric**, not just a yes/no checklist: a scored table rating **Claim, Evidence, Reasoning, and Conventions** on a **1–4** scale, with a **total (/16)** and a "one thing I'll improve next time" line. It replaces the checklist (which it subsumes) to save space and teach self-assessment against the same criteria the teacher scores. Reference: Unit 6, US.45 Activity 7.

### 7.5 QC gate (render + look)

No workbook change ships until it is **rendered to PDF and visually inspected** page by page — writing lines present and legible, no prompt without response space, no bleed/orphan, and every filled space actually fits. (Environment note: LibreOffice `soffice --headless --convert-to pdf` + `pypdfium2` renders faithfully once `libreoffice-writer` is installed.)

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

The skills I'd sync to this file: `history-hack-platinum-workbook`, `history-hack-platinum-unit-builder`, `history-hack-graphic-organizer-workbook`, and `udl-cast-expert`.

---

## 10. Open decisions summary (put your call next to each)

1. **Canonical navy + gold** across print/web/deck — §3. ← most important
2. **Margin width** (0.72 in vs. tighter / binding gutter) — §1.
3. **Body font floor** (10.5 pt vs. 11 pt) — §2.
4. **One standard for both products, or split** student-workbook vs. DBQ — §4.2.
5. Anything from your **Unit 6** markup that isn't covered here.

---

*Edit freely. The `DECISION NEEDED` flags and §10 are where I most need your call. Hand this back and I'll make the code and skills obey it.*
