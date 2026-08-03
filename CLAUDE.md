# TroopToTeacher Technologies — U.S. History Hack

> **Don't just learn history. Hack it.**
> _The curriculum that was built to make a difference, not to make money._
> **Mission over margin.**

**Mission (the Platinum Standard):** Pearson and McGraw-Hill were built to make money. TroopToTeacher
Technologies and History Hack were built to make a difference. Every deliverable is measured
against what actually teaches — and it must be *better and more effective for students* than
anything on the market. The bar is better, not parity.

## Standing decision rule

When a scope/design/trade-off question has a right answer, choose whatever maximizes, in order:
**(1) 100% alignment · (2) TDOE Schedule F Social Studies Rubric · (3) best path to state adoption —
highest integrity, highest quality.** Default to the adoption-grade choice; do not ask the user to
arbitrate these. Only surface a question for a genuine fork Schedule F/alignment doesn't settle —
and lead with the recommendation. Content accuracy (TDOE Policy 2.600) is foundational; no known
error ships. Report honestly — done, held, and every gap.

Full doctrine: `00_START_HERE/ADOPTION_STANDARD.md` · invoke the `history-hack-platinum-standard` skill.

## Product model (print-first; the web platform amplifies)

The product is **print-first**: the student workbook is the spine, and technology enters the flow
**only when it enhances** — justified on the SAMR ladder, **within the workbook flow**. The web
platform's value is five pieces paper can't do — **parallel test-data analytics · real-time standard
mastery · reteaching · lesson-plan builder · gamification + read-aloud** — and the lesson hands off
**workbook ⇄ app** several times (e.g., write a CER on paper → self-grade on the rubric → input to
the app for real-time feedback → revise). The page must stand alone; the app raises the ceiling,
never lowers the floor. Full doctrine: `00_START_HERE/PRODUCT_MODEL_DOCTRINE.md`.

## Canonical set (one job, one owner)

`.claude/skills/` is **main-owned and read-only on work branches.** Skills change only via a
skills-only PR to `main`; content branches rebase and consume them read-only. The registry
`.claude/skills/SKILLS.md` names one owner per job; `lint_skills.py` + the `skills-lint` CI workflow
fail any PR that reintroduces a name collision, a retired name, a dangling reference, or a builder
that inlines a gate. Front door: `00_START_HERE/BUILD_STANDARD.md`. Brand: `00_START_HERE/BRAND_PALETTE.md`
(**America 250**).

## Production guardrails — print-first platform (LOCKED)

**Documents (workbooks, teacher guides, answer keys, organizers) — DOCX-native → PDF.**
Author natively in `.docx` (the docx engine / `engine.js` / `python-docx` — `build_guided_notes.py`,
`build_teacher_guide.py`), then convert to PDF with LibreOffice
(`HOME=/root/lohome soffice --headless --convert-to pdf FILE`). **Never author the document as HTML
or markdown and render it to PDF** — HTML→PDF mangles page breaks, running headers/footers, and page
numbers; native `.docx` paginates correctly. The **editable `.docx` is the author's archive / master**
(TroopToTeacher's source of truth for future edits); the **PDF is the distribution artifact teachers
receive and print** — a faithful convert, not teacher-edited. Detail: `00_START_HERE/BUILD_STANDARD.md`
§4. (24×36 vector wall posters are the only direct-vector exception — they are not documents.)

**Slide decks — .pptx-native → PDF.**
Generate `.pptx` natively via **pptxgenjs**, then convert to PDF via **LibreOffice**. **Never HTML or
markdown → slides.** **Set `pres.layout` BEFORE adding any slides** (e.g. 16:9 `13.333"×7.5"`) — the
layout can't be changed after slides exist. Required QA gates, **in order**:

1. **markitdown content dump** — `python -m markitdown deck.pptx`: verify slide count, order, names,
   and no placeholder/lorem/truncated text.
2. **`validate.py` file check** — the `pptx` skill's `scripts/office/validate.py` (package integrity;
   no orphan/duplicate parts) + a python-pptx load→save round-trip dup check.
3. **Render to images and visually inspect EVERY slide for overflow/clipping** —
   `soffice --headless --convert-to pdf deck.pptx` then `pdftoppm`/pypdfium2 to images; read them.

**Gate 3 is MANDATORY — clipped/overflowing text passes gates 1 and 2 silently** (markitdown reads
the text that exists; validate.py checks the package, not the layout). Pixels are authoritative for
what a student sees. Owners: `history-hack-tcap-deck-builder` (teacher deck), `history-hack-lean-deck-builder`
(student deck); deck standard: `00_START_HERE/SLIDE_DECK_PLATINUM_STANDARD.md`.

> Engineering note: duplicate `.pptx` slides only with the `pptx` skill's `add_slide.py` — **never**
> python-pptx's `add_slide` (it can orphan a slide part and corrupt the package on re-save).
