---
name: history-hack-dbq-workbook
description: "Build a standalone History Hack **DBQ / primary-source investigation** package (a Document-Based-Question SKU) to the Platinum quality bar. This is the DBQ product ONLY — it is a different product from the unit (Course Standard) student workbook. Use when Sean/TroopToTeacher asks for a DBQ workbook, primary-source packet, document investigation, HIPPO/OPTIC analysis, DBQ language-access companion, DBQ teacher guide, or Schedule F self-score for a standalone DBQ SKU. Do NOT use for the unit student workbook, Course Standard student workbooks, Cornell-note lesson workbooks, the 7-activity lesson spine, canonical assessment integration, or Base/Support/EL edition consolidation — for the unit workbook / four-piece unit set use `history-hack-unit-content-build` instead."
license: MIT
metadata:
  author: TroopToTeacher Technologies LLC
  version: '1.4'
  canonical_template: Unit 4 DBQ Workbook
  source_of_truth_repo: https://github.com/Trooptoteacher/History-Hack-US-History-Workbooks
---

# History Hack DBQ Workbook Builder (standalone DBQ SKU)

The repeatable, integrity-first process for producing a commercial-grade **standalone
primary-source / DBQ package**. Unit 4 is the Platinum reference implementation.

> **Vernacular — this is not the unit workbook.** A **DBQ workbook** is a standalone
> Document-Based-Question SKU (one investigation question, a curated document set, HIPPO/OPTIC
> analysis, an essay + rubric). The **unit (Course Standard) student workbook** is a different
> product — the lesson-by-lesson book with the 7-activity cycle, guided Cornell notes, and the
> deck-aligned spine — built by `history-hack-unit-content-build`. They are two separate items;
> never conflate the two or let one absorb the other's architecture (see the Product Boundary
> Gate below).

## When to Use This Skill

- Building a standalone DBQ or primary-source investigation for a U.S. History, Government, World History, or Tennessee History unit.
- Creating a DBQ student workbook, optional faded language-access companion, and English teacher guide.
- Extending or re-scoring an existing DBQ package with a crosswalk, accommodations matrix, geography/data sections, or stronger source analysis.
- Extending or re-scoring an existing workbook (add crosswalk, accommodations matrix, geography/data sections).
- Running or updating a Schedule F self-score for a workbook.
- Re-templating the whole line when the Tennessee standards change (2027-28).

## Product Boundary Gate (LOCKED)

This skill owns only the standalone DBQ product. It must never absorb the Course Standard student-workbook architecture.

- **DBQ responsibilities:** one investigation question; curated document set; standalone visual documents; HIPPO/OPTIC; data, map, and Tennessee reasoning; evidence planning; essay and rubric; optional faded language-access companion; English teacher scoring guide.
- **Excluded responsibilities:** lesson-by-lesson course instruction; universal Cornell notes; Lean-deck slide alignment; Base/Support/EL edition consolidation; canonical web-app assessment integration; modified assessment forms; full Course Standard UDL/MTSS student-workbook sequence; DOCX-first course-book production.
- UDL, MTSS, accessibility, and bilingual principles may inform optional access supports inside the DBQ. They may not turn the DBQ into the separate Course Standard workbook SKU.
- If the user requests Cornell notes, a full standards-based **unit student workbook**, lesson sequences, the 7-activity cycle, assessment-bank integration, or legacy-edition consolidation, stop — that is the unit workbook, a different product. Load `history-hack-unit-content-build` instead.
- A Course Standard workbook may link to a standalone DBQ, but neither product may silently embed or duplicate the other's architecture.

## DBQ Package Model (LOCKED)

The standard package has three files:

1. English Student DBQ Workbook.
2. Optional bilingual Language-Access Companion used alongside the English workbook and faded over time.
3. English Teacher Guide with implementation, source notes, scoring guidance, rubric, and model responses.

Do not create a Spanish teacher guide or a full Spanish duplicate workbook unless Sean explicitly changes the product model.

## ⛔ STEP 0 — SOURCE FROM GOOGLE DRIVE FIRST (HARD GATE — do this before anything else)

**Before sourcing ANY document, image, or citation from the web, you MUST first check Sean's Google Drive for already-sourced material.** Sean maintains pre-vetted, publisher-quality libraries per unit. Web-sourcing before checking Drive is a process failure — it wastes effort and risks lower-provenance duplicates.

1. Search Drive via the `gws` CLI (`api_credentials=["gws"]`, required or you get 401). Find the unit folder (`name contains '<Unit N>' or name contains '<theme>'`) and its `images/` subfolder.
2. Download and REUSE what exists: `PRIMARY_SOURCE_CITATIONS.md` (MLA/APA + archive links + rights + pull-ready excerpts), `IMAGE_CITATIONS.md`, `standards-crosswalk`, `TABLE_OF_CONTENTS.md`, and the standard-code-named `images/` library.
3. Only source NEW material from the web for genuine gaps the Drive library does not already cover — and note explicitly which items were gap-filled.

Full commands and file IDs pattern: `references/build-process.md` Step 1. Do not skip this gate even when you think you already know the sources.

## Non-Negotiable Standing Rules (LOCKED)

These are Sean's permanent constraints. Never violate them.

**Branding**
- Product name is **"U.S. History Hack"** (WITH "U.S.") for the U.S. History line. For other subjects use the parallel name (e.g. "Government Hack", "World History Hack", "Tennessee History Hack") — confirm the exact name with Sean before first use of a new subject.
- Palette: **NAVY `#1B2A4A`, RED `#B22234`, GOLD `#C89B3C`, CARD `#F7F5EF`** (secondary NAVY2 `#2C3E63`, LIGHT `#EEF2F8`, BORDER `#C9C2B4`). See `references/engine-conventions.md`.
- Trademarks use **™ NOT ®**.
- ISBN → literal **"[to be assigned]"** placeholder. **Never fabricate an ISBN or any identifier number.**

**Copyright / integrity (this is a district/school-board adoption artifact — be honest, never defensive)**
- Public-domain and openly-licensed sources ONLY. Honest provenance on every asset.
- **Google Drive is the FIRST source, always** — see the STEP 0 hard gate at the top of this skill. Never web-source before checking Drive.
- Pearson / McGraw Hill / Savvas are **category references ONLY** — never copy their content.
- **Never overclaim.** If a standard is only contextually present, label it **Context**, not **Full**. If a support isn't actually in the book, don't list it. Follow the `copyright-integrity-accreditation` skill for asset classification and fair-use.
- Accommodations language must state supports work **alongside — never in place of** — a student's legally required IEP/504 accommodations.

**Visual sources are standalone documents (LOCKED — validated on Unit 1, do NOT regress)**
- A political cartoon, photograph, poster, or any image that is a **primary source in its own right IS its own document** (its own Doc letter) and gets its **own standalone OPTIC analysis box** (Overview, Parts, Title/Text, Interrelationships, Conclusion). The College Board scores cartoons and photographs as full documents — so do we. Text documents get HIPPO; visual-primary documents get OPTIC.
- **NEVER silently merge a visual primary source into a text document** as decorative art, and **NEVER attach an image to a text document it is not genuinely about.** If an image only illustrates a text act (e.g. a labor photo beside a labor law), it may accompany that document ONLY when it truly depicts that document's subject — but a source that carries its own argument must stand alone with OPTIC.
- **Every image must be verified to match the document it sits with.** During QC, render each document page and confirm the image actually depicts what the surrounding text/caption claims. A mismatched image (wrong subject next to "Doc F") is a hard QC failure — fix before shipping.
- The engine encodes this with a `VISUAL_IS_PRIMARY` set + a standalone `optic_box(...)`; see `references/engine-conventions.md`. Do not remove or bypass this mechanism when templating a new unit.

**Competitive differentiator**
- The **Tennessee Connection** is the core differentiator vs. Pearson/McGraw Hill/Savvas. It must be prominent AND on the cover.

**Framework stack (ONE attributed sentence, in this order)**
TN-first anchor → Common Core RH/WHST literacy (cross-subject proof ONLY, **never** marketed as Common Core-aligned per T.C.A. §49-6-2202) → AP USH → C3 → IDM.

**Print-first production**
- 300 DPI; grayscale-legible (NO color-only encoding — use shading + rules + labels).
- Workbook ≤ 120 pages; body ≥ 10.5pt (table cells ~9.5-10pt OK; fine print ~9pt OK).
- **No unintended sparse pages:** a page with only one or two carryover lines, an orphaned heading, a detached question option, or a short table/rubric fragment is a release blocker. Intentional writing/workspace pages may remain spacious only when their purpose is visibly labeled.
- **White-space activity gate (LOCKED — Unit 4 Platinum standard):** after rendering, measure unused printable-body area and apply the fixed-footprint activity library in `references/white-space-activity-library.md`. Under 20% unused passes; 20–40% unused receives a quarter-page activity; 40–65% receives a half-page activity; 65–80% receives a three-quarter-page activity; over 80% triggers merge/reflow first, then a full-page lab only when the page is necessary. Intentional labeled writing, drawing, mapping, and planning space is exempt.
- Activities must be context-matched, standards-aligned, and produce observable student thinking. Never add filler prose, decorative art, repetitive busywork, or an activity that forces another page.
- Preserve scaffold fading: early sources may use explicit prompts, word banks, and frames; middle sources use reduced cues and optional supports; later sources require independent analysis and self-monitoring. Available space never justifies restoring an earlier scaffold on a later source.
- Essential student-facing instructional text remains ≥ 10.5pt when practical and never below 9.5pt in compact activity furniture. Never shrink essential text to make an activity fit.
- Apply keep-with-next and widow/orphan controls. Keep headings with the first substantive block; keep question stems with their options; and avoid splitting short tables, prompts, rubrics, and response frames.
- **Least-cost AI/ML**: programmatic ReportLab, no premium model. Build the PDF in code, not by hand.

**Two-tier book model**
- Each unit sold separately gets its OWN cover / copyright / TOC.
- The future course book gets a course title + front TOC + end matter (a separate build).

**Aged primary-source images** fail the automated quality-check — after visual inspection, share them with `should_validate=false`.

## The Platinum Workbook Anatomy (section order)

A Platinum unit workbook, in reading order:

1. **Cover** — unit title, DBQ/investigation title, product name ™, Tennessee Connection line, "[to be assigned]" ISBN.
2. **Copyright page** — TroopToTeacher Technologies LLC as author/producer; public-domain rights statement; single-classroom license; framework-stack sentence.
3. **Table of Contents** — page numbers captured dynamically (never hardcoded).
4. **Tennessee Standards Alignment crosswalk** — 2 tables: content standards (e.g. US.01-US.07) with verbatim standard text + strands → exact page(s); AND all Social Studies Practices (SSP.01-SSP.06) → page(s). Label each **Full** or **Context** honestly.
5. **Accessibility & Accommodations matrix** — see below.
6. **How to Use This Workbook.**
7. **Document set** (DBQ documents A-F etc.) — each is a primary source with sourcing analysis: **HIPPO for text documents, OPTIC for visual documents.** A cartoon/photograph/poster that carries its own argument is its OWN document (its own Doc letter) with its OWN standalone OPTIC box — never merged into a text document or paired with unrelated text. See the LOCKED "Visual sources are standalone documents" rule above.
8. **Additional standard document sets** as needed.
9. **Reading the Data** — secondary-source charts (built from public-domain Census/INS data).
10. **Mapping the Nation** — national primary-source map (SSP.06 geographic reasoning).
11. **Tennessee Connection** — TN primary-source map / local reasoning (the differentiator).
12. **Reusable graphic organizer** — works on any source.

The **Accessibility & Accommodations matrix** (2 pages) maps learner needs (SWD, 504/IEP, EL/WIDA, low-vision) → the specific built-in support → where/how → teacher action. Only itemize supports genuinely present. Include the IEP/504 non-replacement guardrail in the intro AND a footnote. Add two callout boxes: "Digital & Printable Use" (the print-ready PDF is inherently digital and LMS-uploadable) and "Review & Reinforcement" (spaced review lives at the curriculum layer, not in a single DBQ book).

## Build Process (the repeatable loop)

Read `references/build-process.md` for the full step-by-step. The short version:

1. **Gather standards verbatim.** Fetch the authoritative TDOE standards PDF; save verbatim text to memory under `projects.history_hack.textbook.<unit>.verbatim_standards`. Never paraphrase a standard in the crosswalk.
2. **Map standards → real content.** Determine which standards get a dedicated source (**Full**) vs. only framing (**Context**). Be honest.
3. **Write a build spec** as a markdown file in the unit's workspace folder before delegating.
4. **Build in ReportLab** using the canonical engine (`assets/build_workbook_template.py`) — reuse the **two-pass marker mechanism**; NEVER hardcode a page number. See `references/engine-conventions.md`.
5. **Run the rendered white-space gate.** Measure each page's unused printable-body area, classify it, and insert the smallest context-matched fixed-footprint activity required by `references/white-space-activity-library.md`. Reflow/merge pages above 80% unused before adding content.
6. **Two-pass (iterate-until-stable) rebuild** so all TOC and crosswalk page references reconverge after any insert.
7. **Verify independently** (see QC below) — never trust a subagent self-report.
8. **Re-share** the workbook (reuse the SAME shared-asset name for version history, `should_validate=false`) and **update the Google Drive file** in place.
9. **Re-score Schedule F** (see below), re-share + update Drive.

**Delegation:** for the actual build, spawn ONE `general_purpose` subagent with `preload_skills: ["office/pdf", "design-foundations", "accessibility-qc-agent"]`, repository setup = use existing workspace (do NOT clone), pointed at the unit's workspace folder and the build spec. Save findings to workspace files.

## Quality Control (MANDATORY — this is what makes it defensible)

Never trust a subagent's self-reported page numbers. Verify every claim independently:

- Render new/changed pages to PNG with `pypdfium2` and read the image yourself for overflow, mid-word wraps, illegible cells, invisible/tofu glyphs, and grayscale legibility.
- Run a full-document white-space scan using printable-body geometry, not text counts alone. Record unused-area percentage, footprint band, activity selected, scaffold stage, minimum font size, and pagination change. Visually inspect every page at or above 20% unused and classify it as `INTENTIONAL WORKSPACE`, `ACTIVITY APPLIED`, or `LAYOUT DEFECT`; no unresolved layout defect may ship.
- Inspect both the native PDF and any PDF rendered from an editable DOCX. A clean native PDF does not prove the DOCX pagination is clean.
- Extract page text with `get_textpage().get_text_range()` and confirm each crosswalk "Where in this workbook" page reference matches the real footer on that page.
- **The classic bug:** a zero-height marker placed before a `KeepTogether` image block stays on the prior page while the image flows to the next — the reference ends up one page off. Fix by gluing the marker INSIDE the `KeepTogether` with the image. See `references/engine-conventions.md` and `references/qc-checklist.md`.
- Confirm total ≤ 120 pages and body ≥ 10.5pt.

### MANDATORY image-content verification gate (NEVER skip, NEVER spot-check)

Every image in the build MUST be verified by looking at the rendered image itself — not the filename, not the caption, not the subagent's word. Drive/app assets have been found MISLABELED more than once (a "corset" diagram filed as "The Awakening"; a "View of Washington City" cityscape filed as `US.15_us_territorial_map_1900.jpg`; an 1892 wood ENGRAVING filed as an Underwood "photograph"). Filename and citation are UNTRUSTED until the pixels confirm them.

For EVERY page that contains an image, do all four — no exceptions, no sampling:
1. **Render and READ the actual image** (`pdfium ... .render(scale~1.7).to_pil()` → `read` the PNG). Do not rely on OCR/text extraction for this step — you must look.
2. **Does the picture match its own caption/title/alt-text?** A map caption must show a map; a "photograph" must be a photograph (not an engraving/lithograph/cartoon); the depicted subject, era, and people must match. If not → STOP and fix the file or the label before shipping.
3. **Does the picture match the surrounding tasks?** e.g. an "identify two overseas territories on this map" task REQUIRES a territorial map actually showing those territories. Cross-check the image against every question that references it.
4. **Is the medium label honest?** Engraving ≠ photograph ≠ lithograph ≠ cartoon. Relabel to what the pixels actually show; never inherit a medium claim from a citation the image doesn't support. Remove any source URL that points to a different item than the one pictured.

Record an explicit per-image PASS line in the build/QC log: `p<N> — <doc> — image shows <what you saw> — matches caption? Y/N — matches tasks? Y/N — medium correct? Y/N`. A build is not shippable until every image line reads Y/Y/Y. This gate applies equally to the workbook AND the Teacher's Guide (and any reused image, e.g. a doc image reused on the Tennessee Connection page — verify it in BOTH locations).

Optionally run the `accessibility-qc-agent` skill as the final gate before Sean's human review.

## Schedule F Self-Score

Read `references/schedule-f-scoring.md`. Score honestly against the TDOE HS Social Studies rubric (Gateway + Tables 2-4, max 36). Rules:
- Score the package **as built**, not as planned. Mark gaps plainly.
- Hold an indicator LOW when the honest answer is low, even if a point is "available" — a principled non-claim (e.g. "Review Opportunities held at 1 because spaced review is a curriculum-layer responsibility") is more defensible to a committee than an inflated card.
- Note History Hack is **supplemental** under T.C.A. §49-6-2202(a)(3) (no Commission approval required); the self-score is a defensibility artifact.
- Author = TroopToTeacher Technologies LLC; disclose Perplexity Computer only as a drafting tool.

## Templating to Other Units & Subjects

- **Units 2-10 (U.S. History):** swap the standard set (US.xx), the DBQ investigation, the documents, the TN Connection map/source. Keep the engine, section anatomy, QC loop, and scoring identical.
- **Other subjects (Government / World / Tennessee):** confirm the parallel product name and the correct TDOE standards framework for that subject; the SSP practices and section anatomy carry over. Update the framework-stack sentence's subject-specific anchors (e.g. AP Gov / AP World instead of AP USH).
- **2027-28 standards refresh:** re-fetch the new verbatim standards, re-map Full/Context, rebuild the crosswalk; the engine and process are unchanged. This is the primary reason the process is templated.

## Pricing & Packaging (standalone DBQ SKU)

Each unit's DBQ workbook is sold on Teachers Pay Teachers as a **standalone entry-point SKU** = one product / two files (student workbook + complete teacher guide). It sits BENEATH the fuller Unit Platinum bundle (~$80.99) and must not undercut it.

- **Teacher license: $14.99 sale / $18.00 list (anchor).** Display $18 as original; sell at $14.99.
- **Teacher key ALWAYS included** — never sell the answer key/rubric as a separate add-on for this SKU. The included key is what justifies pricing above the ~$4 bare-DBQ-prompt tier.
- **District / multi-classroom: $49 per unit.**
- **10-unit standalone-DBQ bundle:** $119 sale / $149 list (teacher), $349 (district); sold as a growing bundle (raise price as units ship).
- Market anchors: bare DBQ prompts ~$4; single units ~$9-16; The DBQ Project district binders ~$27/unit; full-year bundles $150-310.
- Every unit build must also produce a matching **Teacher's Guide** (AP-aligned rubric + two annotated model essays + scoring guidance + honest "author-generated, not externally graded" disclosure) so the SKU always ships with its key. Listing-copy template: see the Unit 1 example at `dbq_workbook/TpT_Listing_Unit1_DBQ.md`.

## Canonical Artifacts (reference implementation)

- Template engine: `assets/build_workbook_template.py` (generalized from the Unit 1 build).
- Living source of truth: the `History-Hack-US-History-Workbooks` GitHub repo (see frontmatter). Bundled template is a starting point; the repo is canonical when they diverge.
- Reference docs in `references/`: `build-process.md`, `engine-conventions.md`, `qc-checklist.md`, `white-space-activity-library.md`, `schedule-f-scoring.md`.
