# BUILD PREFLIGHT — LOCKED (run BEFORE any build; no exceptions)

**Why this exists.** A Unit 1 workbook shipped built from *memory* and from an *outdated* skill
(v1.0) while `main` already carried **v1.2** with new LOCKED gates. That must never happen again.
Every build — workbook, deck, DBQ, organizer, packet, crosswalk — starts here.

> **Rule 0 — never build from memory.** You must have the actual skill file open in front of you,
> pulled from the most-updated source, and you must check the delivered artifact against a complete
> checklist of that skill's LOCKED gates before delivering.

## The five preflight steps (do all, in order)

1. **Identify the owning skill.** Look up the job in `.claude/skills/SKILLS.md` (one job, one owner).
   Do not guess the skill from the task name.

2. **Pull the MOST-UPDATED skill — from `main`, not the work branch.**
   ```
   git fetch origin main
   git show origin/main:.claude/skills/<skill>/SKILL.md      # read THIS, not the local copy
   ```
   - Read the `version` + `changelog_*`. The work branch copy may be stale (it was, at v1.0 vs main v1.2).
   - If assets/files referenced by the skill seem missing or moved, they were likely relocated by a
     recent update — **look on `main`, in `courses/world-history/`, in `courses/_playbooks/`, and in
     `history-hack-new-course-builder/references/`** before concluding anything is gone. Skills get
     restructured (e.g., course-parameterization moved the future-ready/dimensions assets).
   - If the local branch is behind, either rebase the skill from `main` or read every gate from `main`
     and build to it. Never build to the older local copy.

3. **Extract the LOCKED gates into a checklist.** Copy every "(LOCKED)" gate and every "must ship"
   requirement from the `main` SKILL.md + its `references/` into an explicit checklist for this build.

4. **Build to meet EVERY gate.** Not most — every. If a gate cannot be met this pass, say so
   explicitly in the report (held, with the reason) — never silently skip it.

5. **Verify before delivery.** Run the skill's QC + the guardrail validator; it must exit 0. For unit
   workbooks: `python3 print-pipeline/verify_workbook_platinum.py <unit.json>`. Report the pass and any
   held gates honestly.

## Current LOCKED gates — `history-hack-unit-content-build` v1.2 (unit student workbook)

Re-read from `main` each build (this list is a convenience copy, not the source of truth):

- [ ] **Front matter:** Cover · My SMART Goals · Unit at a Glance · How-to-Use legend
- [ ] **Standards Alignment / Adoption Crosswalk** (front-matter + reviewer artifact): per standard
      the **verbatim TDOE standard**, **SSP.01–06**, cross-curricular **TDOE ELA**, DOK; **reviewer
      assurances** block (accuracy/Policy 2.600, bias, PD-source citations, WCAG 2.2 AA / tagged PDF-UA)
- [ ] **Per-standard opener:** Learning Targets · Lenses (C/E/G/H/P/T/TCA) · SET YOUR SMART GOAL · Hook · Preview
- [ ] **The 7 activities, in order:** 1 Vocabulary · 2 Vocabulary Studio (Frayer) · 3 **Guided Cornell
      (Direct Teaching = spine)** · 4 Close Read · 5 Primary Source/HIPPO · 6 Practice Quiz · 7 CER
- [ ] **Exit Ticket** per standard (whole on its page)
- [ ] **Guided Cornell:** DI segments pre-seeded in lecture order, `▶ Deck · DI N of M` keyed, Doodle Zone,
      Progress Check + Check-Yourself; **NOTES SUPPORTS ladder on the verso**
- [ ] **Generous notebook-lined writing space (LOCKED):** every write-in area has real ruled lines
- [ ] **Practice Quiz:** items **bank-sourced from the authoritative `assessmentSource`** (US flagship =
      web-app `public/data/us-history/questions/unit-N/dok-{1,2,3}.json`; match by content — its codes are
      older), **content-verified keys**, on-page self-check key (correct **bold letter, indented** + rationale)
- [ ] **UDL 3.0 (CAST 2024) back page (LOCKED):** dedicated verso three-principle crosswalk + citation
- [ ] **Future Ready embedded (never forced):** SMART ladder · employability micro-moments · a
      standard-tied Future Ready Question · SPEAK IT Mission Brief · money-math from the currency SoT
- [ ] **Differentiation visible:** ★ Entry / ● On-Level / ▲ Extension
- [ ] **America 250 brand tokens** (Heritage Blue #1F3A5F · Patriot Red #B22234 · Muted Gold #C9A227 · Founders Cream #F8F5EF)
- [ ] **Zero blank/near-empty pages**
- [ ] **Bidirectional deck↔workbook slide-keying** (after the Course-Standard decks are (re)built)
- [ ] **Accessibility / Rubric F:** delivered PDF is a **tagged PDF/UA** export; `accessibility-qc-agent` terminal gate
- [ ] **Course-parameterized:** resolve `courses/<id>/course.json`; never hardcode US.01–US.95 / TCAP EOC on a non-US build

> Format note: the user's directive on this project is **print-first via the WeasyPrint print-pipeline
> (no `.docx`)**. The skill's own text still says "DOCX-native"; when they conflict, the user's no-docx
> directive wins for delivery, but **every LOCKED content gate above still applies**. Flag the conflict
> so the skill can be reconciled via a skills-only PR to `main`.
