# Skills Reconciliation — locked decisions + execution blueprint

**Why:** `.claude/skills/` had drifted into contradictory per-branch versions, so every content build
loaded a different toolbox → inconsistent output. This reconciles to ONE canonical, non-contradictory
skill set on `main`. Decisions below were set by Sean and confirmed by a 4-lens mission panel
(UDL/learning-science · TDOE Schedule F/adoption · teacher usability · skills architecture) — the
panel was **unanimous** on the substantive calls.

## Locked decisions

1. **Single unit builder = `history-hack-platinum-unit-builder`** (Sean). Strip the INLINED gates from
   the pilot version; it **references** the standalone skills instead. Absorbs the standalone print
   `course-standard-builder`'s Unit 6 print/format spec (→ `references/course-standard-format.md`).
2. **QC + Platinum-standard + content engine = STANDALONE skills, referenced as MANDATORY ship-blocking gates**
   (unanimous panel): `history-hack-lesson-flow-qc`, `history-hack-text-integrity-qc`,
   `history-hack-platinum-standard`, `history-hack-unit-content-build` (owns `build_guided_notes.py` etc.).
   Not inlined — they are runnable checks reused across every product and already caught real bugs.
3. **NOTES SUPPORTS stay on the verso, in the student book, default-included** (unanimous panel; wins
   Schedule F Table 4 visibility + UDL self-access). Reject the "gate into teacher pack" model.
   - "Lighter book" is delivered as a **PRINT FLAG**, not gating: *Duplex = notes + supports
     (scaffolded); Single-sided = notes only (lighter/independent)* — one book-level choice.
   - Adopt the one good idea from the other branch — **scaffold fading** — as a *content property*
     inside the verso across standards (full frames → how-to+try-it → self-check), not by relocation.
   - "Crammed/overload" is a **spacing/layout problem**, fixed by the §5 white-space banded rule +
     print-QC, never by removing supports.
4. **Retire `tcap-item-writer-v2`** → absorbed into `tn-assessment-specialist` (migrate full
   psychometric schema: IRT 3PL, Hess CRM, DOK/Bloom's, distractor codes, field-test flag).
5. **DBQ skill = `history-hack-dbq-workbook`** (retire the `platinum-workbook` name; fix stale pointers).
6. **Rename the new-course orchestrator** currently colliding on "course-standard" (the cradle-to-grave
   NEW-COURSE-EDITION pipeline) so it no longer clashes with the unit builder's print spec. It CALLS
   the unit builder; it does not re-implement it.
7. **Brand = America 250 palette** (Sean) — see `BRAND_PALETTE.md`. Retire `#1B2A4A` / `#0A1F3C` /
   `#C89B3C`.

## Anti-drift rule (the root-cause fix)

- `.claude/skills/` is **main-owned and read-only on work branches.**
- Skills change **only** via a dedicated **skills-only PR** merged to `main` first; content/unit
  branches then rebase and consume skills read-only. No feature branch carries its own skill variant.
- Add a one-owner **skill registry** (`.claude/skills/SKILLS.md`: one job + one owner per skill) and a
  CI lint: fail on (a) two skills with overlapping jobs, (b) a builder inlining a gate/engine instead
  of referencing its standalone skill, (c) references to retired names.

## Execution (skills-only PR → `main`, review-first)

1. Branch `skill/reconcile-canonical-set` off `origin/main`.
2. Bring in the standalone engine + QC + platinum-standard skills; set `platinum-unit-builder` to reference
   them (strip inlined gates); absorb print spec; apply America 250 tokens in skill brand rules.
3. Retire `tcap-item-writer-v2`; rename DBQ + new-course collision; repoint all references.
4. Add `SKILLS.md` registry + the CI lint.
5. Open the PR for Sean's review — nothing merges to `main` without sign-off. Then all branches rebase.

## Separate follow-on (content, not skills)

Unit 6 brand re-skin to America 250 + the readability pass (Activity 4 own page, ruled write-space,
chunked CER, spread HIPPO, white-space banded rule) — runs on the Unit 6 content branch after the
canonical skills land.
