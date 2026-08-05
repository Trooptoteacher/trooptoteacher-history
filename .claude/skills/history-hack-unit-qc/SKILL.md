---
name: history-hack-unit-qc
description: End-to-end QC workflow for History Hack U.S. History units in history-hack-web-app, modeled on the gold-standard Unit 1 pattern (April 2026). Use when the user asks to QC, audit, evaluate, prepare for Schedule F, prepare for TDOE adoption, mirror the Unit 1 pattern, or bring any unit to TDOE Textbook Commission-defensible quality. Runs an 18-item prioritized checklist (Critical/High/Medium/Low) covering standards alignment, five-band differentiation, DOK integrity, Cornell notes, printable graphic organizers, entry-point items, econ/geo reasoning activities, and bilingual content. Produces commit trail, 14-page Standards Alignment Guide PDF, and final scorecard. Trigger phrases include QC unit N, Schedule F review unit N, audit unit N, mirror unit 1 pattern, and TDOE adoption review.
metadata:
  author: Sean Reynolds / TroopToTeacher Technologies
  version: '1.0'
  proven_on: Unit 1 (April 2026) — 18/18 items closed, ~93-95% projected rubric score
  repo: Trooptoteacher/history-hack-web-app
---

> **STOP — PULL THE CURRENT SKILL BEFORE YOU BUILD.** Never build, rebuild, format, render, or QC ANY artifact —
> workbook, teacher/student slide deck, graphic organizer, poster, DBQ, assessment or test, worksheet, comic,
> web page, or anything else — from memory, a cached copy, or a prior session. **Re-read the CURRENT version of
> THIS skill from `main` first** — skills are the single source of truth and change only via skills-only PRs.
> Then **resolve + declare the course** and honor the **Course-Binding Standard**
> (`history-hack-new-course-builder/references/course-binding-and-walls.md`): read only that course's
> standards/content, emit only its prefix, and never read from or write to the protected `us-history` flagship
> on a non-US build. If you cannot confirm you are on the current skill, **STOP and pull it first.**

# History Hack Unit QC — Schedule F Readiness Workflow

## 1. Role and Scope

You are a senior curriculum QC engineer for the History Hack U.S. History platform (TroopToTeacher Technologies). Your job is to take any Unit N of the textbook from its current state to **TDOE Schedule F / Textbook Commission adoption-defensible quality**, matching or exceeding the Unit 1 reference standard.

**Source of truth**: The web app repo (`Trooptoteacher/history-hack-web-app`) is the sole source of truth. The separate `US-History-Hack-Textbook` repo is stale and NOT used. All edits happen in:
- `public/data/textbook/unit-{N}.json` — narrative and differentiation plan
- `public/data/questions/unit-{N}/dok-{1,2,3}.json` — item banks
- `public/data/ican/unit-{N}.json` — I Can statements
- `public/data/pacing-guide.json` — unit pacing
- `data/vocabulary.ts` — cross-unit vocabulary
- `lib/cornell-notes-data.ts` — Cornell notes
- `public/printables/unit-{N}/` — printable graphic organizers
- `docs/adoption/unit-{N}-standards-alignment-guide.pdf` — reviewer-facing PDF

## 1a. Gate orchestration (invoke the standalone gates — never duplicate them)

This skill owns the **end-to-end web-app unit QC workflow** (the 18-item checklist against `history-hack-web-app` JSON). It does **not** re-implement the print/deck release gates — those are standalone, single-owner skills that this workflow **calls** whenever print workbook or deck artifacts are in scope:

- **`history-hack-lesson-flow-qc`** — workbook↔deck exact-slide alignment, DI parity, vocab-first (0 blocker / 0 major).
- **`history-hack-text-integrity-qc`** — no truncated/clipped/placeholder text (0 BLOCKER).
- **`accessibility-qc-agent`** — WCAG 2.2 AA / 508 / ADA Title II final gate.
- **`ell-bilingual-review-specialist`** — English/Spanish + ELL scaffolding QC.
- **`history-hack-print-qc-auditor`** — print-defect / classroom-readiness audit.

If a check here overlaps one of those, defer to the standalone skill and record its result — do not fork a second copy of the logic (that is the drift this canonical set exists to prevent). Sibling lane: `wcs-app-approval-qc` owns district-submission readiness.

## 2. Credit-Conscious Execution

**User priority**: "Save credits as much as possible." Follow this hierarchy:

1. **Audit first** — most items are often already done. Run the audit script before spawning subagents or doing expensive work.
2. **Local edits over subagents** — do JSON edits, Python scripts, and git operations locally. Never spawn a subagent for work you can do in ~5 tool calls.
3. **Spawn subagents ONLY for genuinely expensive work** — Spanish translation of full narratives (~12K words) is the canonical case. Small translations or single-item writes → do locally.
4. **No browsing** unless the user explicitly asks for external research.
5. **Batch git operations** — commit after each priority band (Critical, High, Medium, Low), not after every file edit.
6. **No `confirm_action` for internal code edits** — the user has standing authorization.

## 3. The 18-Item Prioritized Checklist

Every unit QC runs this exact checklist. Items map 1:1 to the Unit 1 reference. Load `references/18-item-checklist.md` for the full spec of each item with code patterns and verification rules.

### Critical (3 items) — must pass before district submission
1. **Compile Standards Alignment Guide PDF** — 14-page reviewer doc at `docs/adoption/unit-{N}-standards-alignment-guide.pdf` (use `scripts/build_alignment_guide.py`)
2. **Fix vocabulary boundary leaks** — audit `data/vocabulary.ts` for mistagged unit assignments
3. **Link I Can statements ↔ textbook sections** — bidirectional `sectionId` / `icanStatementIds` keys

### High (5 items) — differentiation depth (the headline)
4. **Per-statement WIDA sentence frames** on I Can — L1L2 / L3L4 / L5L6 bands
5. **4 printable graphic organizers** as HTML at `public/printables/unit-{N}/` — cause-effect, SAPA, timeline, Venn (or unit-appropriate variants)
6. **IEP/504 accommodations crosswalk** — 10-entry `tier3Intensive.accommodationsCrosswalk.accommodations`
7. **504 band** between Tier 2 and Tier 3 — `section504Accommodations` with 6+ strategies + `keyDistinction` field
8. **C3 Dimension 4 civic-action extension** — `extensionsAdvanced.strategies[N]` with `c3Dimension: "D4"`, `ssp`, `standards` keys

### Medium (5 items) — quality and coverage
9. **Spanish `readingContentEs` on all I Can statements**
10. **Stimulus field on every document-based DOK-3 item** — `{type, citation, text}` block
11. **Retag mistagged D2→D3/D4** DOK-3 items
12. **Cornell notes covering all unit standards** in `lib/cornell-notes-data.ts`
13. **Honors acceleration track** — `honorsAcceleration` with 5 strategies + `distinctionFromExtensions`
**13b. Spanish `narrativeEs` on all textbook sections** — use a translation subagent (see Section 6)

### Low (5 items) — polish and TDOE Table 3 coverage
14. **`ellSupportNote` on boundary vocabulary** (words that could span units)
15. **3-4 DOK-1 "Tier 2/3 entry-point" items** per unit — simplified language, chunked stems, WIDA L1-L3, `tier2Entry: true`, `tier3Entry: true`, `scaffolds` block
16. **SSP codes on all extension strategies**
17. **Standalone economic + geographic reasoning activities** — `differentiationPlan.standaloneReasoningActivities` with 2 econ + 2 geo (TDOE Table 3 Indicators 3.6, 3.7)
18. **Pacing guide audit** — all unit standards covered with per-day breakdowns

### Scaffolding (6 items, v2.5+) — in-text differentiation within `narrative` and `narrativeEs`

Applies to every unit once the 18-item base is complete. Load `references/scaffolding-schema.md` for full spec. All six marker types use bracketed inline syntax that strips cleanly to the original narrative (verify with `reconstruct4.py`).

19. **`[[Vocab]]` or `[[narrative|canonical]]` pipe-alias vocab wraps** — first-occurrence-per-section wrap of every Unit N vocab term. Use pipe-alias when narrative text differs from canonical vocab key (e.g. `[[Jim Crow|Jim Crow Laws]]`, `[[Ellis Island|Isla Ellis]]`, `[[ethnic neighborhoods|Ethnic Clusters]]`). Renderer parses both syntaxes; text before pipe is display, text after pipe is the vocabulary.ts lookup key.
20. **`[SSP: N,M]` Social Studies Practice tags** — 3-10 per section, placed immediately after the clause that demonstrates the practice. EN and ES markers must be identical in number and position.
21. **`[CHUNK: Quick Check — question]` retrieval prompts** — 2-4 per section at sub-topic boundaries, on their own line, 10-20 word DOK 1-2 question answerable from preceding paragraphs.
22. **`[SUMMARY-L1L3: ...]` + `[SUMMARY-L4L6: ...]` tiered WIDA summary pairs** — 2-5 pairs per section at end of sub-topic clusters. L1L3: 15-25 words, simple SVO. L4L6: 25-40 words, academic vocab. Always appear as a pair.
23. **`[PROMPT: ...]` metacognitive reflections** — 1-2 per section after ethically/analytically weighty passages. Open-ended, 10-25 words.
24. **`[CONTEXT: ...]` primary source pre-reading** — before every quoted primary source, 2-3 sentences (30-60 words) giving author background + date + why it matters.

**CRITICAL rule for scaffolding**: narrative text must be UNCHANGED byte-for-byte before and after scaffolding. Only markers are added. Verify with `reconstruct4.py` (in `/home/user/workspace/hh-eval/scaffolding-work/`) which strips all markers with bracket-depth-aware extraction and compares to the original.

**Scaffolding commit message**: `Unit {N} QC v2.5: add in-text scaffolding markers (SSP, vocab, chunk, tiered summaries, prompts, context)`. Bump version by 0.1 (e.g., v2.4 → v2.5).

## 4. Workflow — Step by Step

### Step 1: Audit
Run the audit script to get current state:
```bash
cd /home/user/workspace/hh-eval
python3 scripts/audit_unit.py {N}
```
(Script is included; if not present, replicate the audit logic from `references/audit-script-template.py`.)

Output: a per-item status table showing `DONE`, `PARTIAL`, or `TODO` for all 18 items.

### Step 2: Plan
Create a todo list with only the items that are `PARTIAL` or `TODO`. Skip `DONE` items — don't redo work.

### Step 3: Execute in priority bands
- Complete all Critical items, commit, push.
- Complete all High items, commit, push.
- Complete all Medium items, commit, push.
- Complete all Low items, commit, push.

For each item, follow the exact code pattern in `references/18-item-checklist.md`. Reuse the reference data structures — don't invent new schemas.

### Step 4: Rebuild alignment PDF
After each band, rebuild:
```bash
cd /home/user/workspace/hh-eval
python3 scripts/build_alignment_guide.py {N}
```

### Step 5: Final verification
Run the audit again. All 18 items must show `DONE`. Bump `textbook/unit-{N}.json` version (+0.1 per band) and `lastUpdated` to today.

### Step 6: Deliver
Share the final PDF via `share_file`, produce a scorecard matching the Unit 1 report format (Critical X/3, High X/5, Medium X/5-6, Low X/5, Total X/18-19).

## 5. Git Operations (CRITICAL pattern)

`git config --global` does NOT persist in the sandbox. Use `-c` flags on every commit:
```bash
git -c user.name="Sean Reynolds" -c user.email="trooptoteacher31@gmail.com" commit -m "Unit N QC {band}: ..."
```

For pushes, use `api_credentials=["github"]` on the bash call. Proxy: `git-agent-proxy.perplexity.ai`.

Commit message format:
- Critical: `Unit {N} QC critical batch: standards alignment guide, vocab fixes, I Can linking`
- High: `Unit {N} QC high batch: sentence frames, graphic organizers, 504 band, C3 D4 extension`
- Medium: `Unit {N} QC medium batch: stimulus extraction, C3 retag, Cornell notes`
- Low: `Unit {N} QC low batch: entry-point items, reasoning activities`
- Spanish: `Unit {N} QC 6d: add Spanish narrativeEs to all {X} textbook sections`

## 6. Spanish Translation Subagent Pattern

For full narrative translation (only genuine credit-expensive step), use this pattern.

Load `references/translation-subagent-brief.md` for the complete subagent prompt template. Key elements:
- Preload `ell-bilingual-review-specialist` skill
- Target Grade 10-11 Latin American Spanish (Lexile 1000-1100 equivalent)
- Preserve `[Strand: ...]` markers verbatim — count before and after
- Standardized historical terminology glossary (locked terms)
- One Spanish file per section in `/home/user/workspace/hh-eval/translation-work/`
- Parallel injection script pulls translations into JSON

## 7. Deliverables Checklist

Every unit QC must produce:
- [ ] Commits in `main` branch covering all 18 items
- [ ] Version-bumped `textbook/unit-{N}.json` (e.g., v2.4 when fully done)
- [ ] `docs/adoption/unit-{N}-standards-alignment-guide.pdf` (14 pages, ~94KB)
- [ ] Final completion report to user in the Unit 1 format (priority scorecard + what-this-means-for-Schedule-F paragraph)

## 8. Reference Files

Load these from `references/` as needed during execution:
- **`18-item-checklist.md`** — the full spec for each of the 18 items: JSON patterns, code templates, verification rules, file paths. Read before executing any band.
- **`tdoe-table-3-mapping.md`** — how each QC item maps to TDOE Textbook Commission Scoring Rubric Table 3 indicators. Read before writing the final report.
- **`translation-subagent-brief.md`** — ready-to-paste subagent objective template for Spanish translations.
- **`unit-1-reference-state.md`** — the exact final state of Unit 1 (v2.5) as the gold standard. Reference when uncertain about a data structure.
- **`git-identity-workaround.md`** — sandbox git config quirks and push proxy setup.
- **`scaffolding-schema.md`** — the 6-marker in-text scaffolding schema (v1.1) with pipe-alias vocab syntax, placement rules, and renderer parsing pseudocode. Read before executing scaffolding items 19-24.

## 9. Related Skills

- **`ell-bilingual-review-specialist`** — pass as preloaded skill to the translation subagent
- **`tn-assessment-specialist`** (supersedes the retired `tcap-item-writer-v2`) — use when writing new DOK-1 entry-point items or DOK-3 stimulus-based items
- **`tn-textbook-adoption-agent`** — use for final TDOE rubric scoring projection
- **`instructional-design-specialist`** — use when writing Cornell notes or graphic organizers from scratch
- **`tn-content-specialist`** — use when any unit standard lacks a textbook section and must be drafted

## 10. When NOT to Use This Skill

Do not use this skill for:
- Writing new textbook narratives from scratch (use `tn-content-specialist`)
- Single-item edits (just do the edit; no need to run the full workflow)
- Cross-unit architectural decisions (e.g., vocabulary refactor) — flag for user decision
- Marketing, sales, or adoption-packaging materials (those live outside the repo)

## 11. Success Criteria

A unit passes QC when:
- All 18 base checklist items are `DONE`
- All 6 scaffolding items (19-24) are `DONE` for v2.5+ readiness
- Standards Alignment Guide PDF builds cleanly
- All JSON files parse valid
- All strand markers (`[Strand: ...]`, `[TCA: ...]`) are preserved across EN and ES
- Narrative text strips byte-equal to pre-scaffolding original (verify with `reconstruct4.py`)
- Projected TDOE rubric score ≥ 90%
- Commit log shows one commit per priority band + one scaffolding commit
