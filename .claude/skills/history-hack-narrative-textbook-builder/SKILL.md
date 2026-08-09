---
name: history-hack-narrative-textbook-builder
description: "Builds and edits the History Hack **narrative illustrated textbook** — the story-driven, primary-source-illustrated student *reader* (reference edition: **\"To Form a More Perfect Union\"**, U.S. History, released in 5 parts across Units 1–10) — via the WeasyPrint print path (content JSON → HTML → the locked B&W-safe print contract → PDF). This is a DISTINCT product from the 7-activity Course Standard unit workbook (that is `history-hack-unit-content-build`) and from the DBQ SKU (`history-hack-dbq-workbook`); it is the illustrated narrative course a student reads. **Course-parameterized** via `courses/<id>/course.json` (U.S. History is the reference/default; also builds World History, Government, Grade 6/7/8, Tennessee editions with identical structure and gates). Owns: the full-bleed cover, the founder's foreword, the one-page Flight-Crew spread, per-standard **\"stops\"** (hook → primary-source image + a two-tier right column of a Source-It-First WHO/WHEN/WHY sourcing band and an **HVT \"High-Value Target\" must-know box** → EN/ES Word Wall → Tennessee Connection → Flight-Log cue), **CER writing pages** (claim + evidence + self-grade rubric + \"Writing Lab\" workbook⇄app handoff), the **Arc-of-the-Union coordinate-plot section** (students score each milestone −3…+3, plot the points, connect the arc, then read it cross-curricular with math (slope/mean/extrapolate) and science (pattern/turning point)), the **B&W-safe print contract**, per-page copyright footer + page numbers, the LOCKED **white-space ≥90% value rule** enforced by a build-time page-fill QC gate, and the matching **Flight Log companion** (write-in student log with a brand cover and a bidirectional Textbook-Stop-N ⇄ Flight-Log-Entry-N cross-reference generated from the same stop data so it can't drift). Use when asked to build, edit, reformat, fill white space in, re-cover, add a foreword to, add the Arc plot to, or reprint the narrative textbook / the 'To Form a More Perfect Union' PDFs for any unit or course; and to edit the existing Part 1–5 PDFs in code instead of by hand."
license: Proprietary
metadata:
  author: "Sean Reynolds / TroopToTeacher Technologies LLC"
  version: "1.1"
  reference_implementation: "To Form a More Perfect Union — U.S. History, Part 1 (Units 1–3). Unit 1 (US.01–US.07) is the CERTIFIED PLATINUM reference — a COMPLETE unit, not a Stop-1 proof: 51pp tagged PDF/UA reader + Flight Log (student + teacher-key), dedicated Geography section, dimension chips on every stop, ≥9pt a11y floor, Arc-of-the-Union plot. Cleared the Grade-A release gate 2026-08-08: build/print QC PASS, accessibility Grade A (0 Critical/0 High), TDOE Schedule F 35/36 = 97.2% with Gateway MET, content accuracy PASS, SF-7 7/7 verbatim, NIMAS + AT-log closed. Units 2–7 replicate it feature-for-feature and gate-for-gate."
  product: "Narrative illustrated textbook (student reader) — NOT the unit workbook, DBQ packet, decks, or organizer toolkit"
  render_path: "content → HTML → WeasyPrint → PDF, governed entirely by references/print-contract.css"
  platinum_gate_evidence: "history-hack-web-app: scripts/print-book/qc/2026-08-08_Unit1_Release_Gate_Certification.md (+ the accessibility, Schedule-F, historian, AT-log and NIMAS artifacts it cites in scripts/print-book/qc/ and scripts/print-book/nimas/)"
---

> **STOP — PULL THE CURRENT SKILL BEFORE YOU BUILD.** Never build, rebuild, format, render, edit, or QC ANY
> artifact — including this narrative textbook — from memory, a cached copy, or a prior session. **Re-read the
> CURRENT version of THIS skill from `main` first** — skills are the single source of truth and change only via
> skills-only PRs. Then **resolve + declare the course** and honor the **Course-Binding Standard**
> (`history-hack-new-course-builder/references/course-binding-and-walls.md`): read only that course's
> standards/content, emit only its prefix (US/GC/W/TN/…), and **never** read from or write to the protected
> `us-history` flagship on a non-US build. If you cannot confirm you are on the current skill, STOP and pull it.

# History Hack — Narrative Illustrated Textbook Builder

Load `history-hack-platinum-standard` first (mission, decision rule, tier convention). This skill owns **one
job**: the illustrated narrative *reader* a student reads cover-to-cover — the "To Form a More Perfect Union"
product line. It does not build the unit workbook, the decks, the DBQ packet, the organizer toolkit, or the
assessment bank; those have their own owners (see `SKILLS.md`).

## What this product is (and is not)

- **IS:** a story-driven, primary-source-illustrated textbook, written in the voice of the house author
  ("Sam Calloway"), with a recurring **Flight Crew** (Archive/J. Troop, Spark, Co-Pilot, Navigator, Notetaker,
  Sam Calloway, MSgt "Muck") who *guide*, and composite **era-friends** who lived the year. One **stop per
  standard**. Released per course in **parts** (US History = 5 parts, Units 1–10).
- **IS NOT:** the 7-activity Cornell unit workbook (`history-hack-unit-content-build`), the DBQ SKU
  (`history-hack-dbq-workbook`), the decks (`history-hack-tcap-deck-builder` / `-lean-deck-builder`), or the
  organizer toolkit (`history-hack-graphic-organizer-workbook`).

## Reference implementation

`references/render_textbook.py` + `references/print-contract.css` render the **certified** reference — Unit 1
(US.01–US.07), the complete platinum build (not just a Stop-1 proof). `references/build-and-edit-conventions.md`
is the LOCKED spec: page order, the stop template, the value-block menu, the Arc-of-the-Union plot spec, the
**Geography section** + **dimension chips**, the crew/cover/foreword conventions, the edit-in-code workflow, and
the build gates. Build to that spec; do not re-derive it from a rendered PDF.

## Platinum reference — Unit 1 (certified); what every unit replicates

Unit 1 is the **locked exemplar**: the bar Units 2–7 (and every course edition) match feature-for-feature and
gate-for-gate. Do not ship a unit below it. **Certification evidence:** `history-hack-web-app`
`scripts/print-book/qc/2026-08-08_Unit1_Release_Gate_Certification.md`.

**Structure a certified unit carries (beyond the base stop template):**
- **Dedicated Geography section** in the reader (locate/interpret the unit's places — e.g. Unit 1's industrial
  centers), with a matching **Geography Waypoints** section + a **blank U.S.-outline plot box** in the Flight Log.
- **Dimension chips on every stop** (reader *and* Flight Log) — the standard's content-dimension tag, visible
  and consistent across both surfaces.
- **Verbatim "I can" learning target on every stop** (SF-7) — from the course's `ican` bank, verbatim, or
  clearly labeled authored; never paraphrased silently.
- **Arc-of-the-Union** milestones wired to **real primary-source citations** (`arcPoints` → bank sourceIds),
  never invented.

**The Grade-A gate bar Unit 1 cleared (the pass line, not a target):**
- **Build/print QC** — clean render, **≤10% white** on every content page (documented section-break exceptions
  only), text-integrity clean, workbook⇄deck⇄Flight-Log lesson-flow mapped.
- **Accessibility = Grade A** — 0 Critical / 0 High; **tagged PDF/UA** (one single tagged render, no baked
  untagged front matter), **≥9pt everywhere** (only decorative glyphs below, exposed as artifacts), and a
  clean **ordered heading walk H1→H2→H3 with no skips** (Unit 1: H1×6 → H2×33 → H3×41).
- **TDOE Schedule F ≥90%** (≥33/36, Tables 2–4) **AND Gateway MET** — a bound standards crosswalk with
  independently verified page refs, all unit standards addressed. Unit 1 scored **35/36 = 97.2%**.
- **Content accuracy (Policy 2.600)** — `historian-factcheck-agent` PASS, 0 Critical/0 High; no known error ships.
- **Adoption packet** — NIMAS-conformant accessible-source fileset + an assistive-tech (AT) test log
  (`scripts/print-book/nimas/unit-N/` + the AT-log QC artifact).

Report every held gate honestly; "close" is not Grade A (release rule in `CLAUDE.md`).

## Course parameterization

Resolve the course from `courses/<id>/course.json` (`id`, `displayName`, `standardsPrefix`, `standardsFile`).
Derive every label, standard code, footer, and "Tennessee/State Connection" from it — never hardcode
U.S. History / US.01 / TCAP. Defaults to the U.S. History flagship. Narrative + illustrated text is sourced
from the canonical banks in `history-hack-web-app` (primary-sources/images/questions) and the per-course
`content-build/<course>/narrative/unit-NN.json` — **never invent a citation or a source** (Policy 2.600).

## LOCKED gates (run before any part ships)

1. **Page-fill ≥ 90% (build gate).** The renderer measures every page's fill below the running footer and
   FAILS the build if any non-exempt page is < 90%. Exempt: the full-bleed **cover** and the **foreword**
   (fills once personalized). When a page is short, add **value, not filler** — see the value-block menu.
2. **B&W-safe.** Interior prints in black-and-white: dark ink on white/light tints, never white-on-navy or
   gold-on-navy for reading-critical content; color-encoding maps flagged `colorKey` with a "see the deck"
   note. (Guardrail #6.)
3. **Per-page © footer + page number**, running head/foot owned by the print contract.
4. **No internal pages in a distributed file** — strip the "Permissions & Publishing Checklist" and
   print-production/spine notes from any teacher/student-facing download.
5. **Invoke** — do not re-implement — the shared release gates: `history-hack-print-qc-auditor` (print
   defects), `history-hack-text-integrity-qc` (no clipped/placeholder text), `accessibility-qc-agent`
   (WCAG/UA), `historian-factcheck-agent` (Policy 2.600), `tn-textbook-adoption-agent` (Schedule F),
   `ell-bilingual-review-specialist` (EN/ES + ELL), `copyright-integrity-accreditation` (IP/FERPA/COPPA).
6. **Accessibility build gate (tagged/UA · ≥9pt · heading order).** The whole unit is ONE tagged **PDF/UA**
   render — never a merge of a baked, untagged front-matter PDF (that reintroduces the A11Y-01 Critical);
   verify `StructTreeRoot` is present on the served file. **≥9pt everywhere** (body 10–11pt); only decorative
   glyphs render smaller and only as AT artifacts. The heading tree is an **ordered walk H1→H2→H3 with no
   skips** — promote stop/phase titles to the tier that keeps it unbroken. These are the build-side inputs to
   the Grade-A accessibility gate; see "Platinum reference — Unit 1" for the full pass bar.
7. **Adoption gate (Grade A before served/submitted).** No unit reaches the served path or a district/TDOE
   packet below a straight **Grade A** on all three release gates (build/print QC · accessibility Grade A ·
   Schedule F ≥90% + Gateway MET + content accuracy), plus the NIMAS fileset + AT test log for the adoption
   packet. Report held gates honestly.

## The white-space value rule (LOCKED)

Meaningful white space is a missed teaching moment. Any short page earns a **value block** — a check-in,
self-assessment, prediction/anticipation guide, reflection, plot/data activity, or Future-Ready/ACT-Ready
tie — chosen for high-impact pedagogy (Hattie ≥ 0.40), never filler. The `.value` component and the block
menu live in `references/build-and-edit-conventions.md`.

## Editing the existing PDFs

The already-shipped Part 1–5 PDFs were authored ad hoc and have **no code source**; do not hand-edit the
flattened PDF. Bring the target part into this pipeline (extract images to `references/assets`, capture text
into the course narrative JSON), apply edits in the content + contract, re-render, pass the QC gate, then
replace the served PDF in `history-hack-web-app/public/textbook-pdf/`. See the edit workflow in the
conventions reference.

## Serving

Rendered PDFs are served from `history-hack-web-app/public/textbook-pdf/` (full-book parts + per-unit splits)
and surfaced on the `/textbook` reader. Per-unit split = cover + How-This-Book-Works + that unit + image
credits; the full part is the complete volume. Register new parts in `app/textbook/page.tsx`.
