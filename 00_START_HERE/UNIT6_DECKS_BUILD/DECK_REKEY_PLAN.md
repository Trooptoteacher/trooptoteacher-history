# Unit 6 Deck Re-Key Plan — student review deck ↔ workbook ↔ teacher lecture

**Status:** ✅ **EXECUTED (2026-08-01)** — student-deck re-key done and QC-verified to
**0 blocker / 0 major / 0 minor**. Target 3 (dropping the 21 visual assets into slides) remains.
Original plan (approved by Sean) retained below for the record.

## Execution record — student deck re-key (Target 2)

- **DI parity:** each standard's "combined" review slide was split so student DI count == teacher DI
  count (4 per standard; US.51 = 5). Every DI slide is captioned **"US.xx · DI k of M · <segment>"**,
  which resolves the workbook's guided-Cornell cue "▶ Deck · DI k of M" to an exact slide.
- **Vocab-first:** KEY VOCABULARY moved to immediately after each standard's TITLE (before instruction).
- **Image-safe:** every segment-matched photo stayed on its original slide; only text-only slides were
  duplicated (zero picture surgery). Visual QA confirmed each kept image matches its assigned segment
  (Quarantine=FDR broadcast, Pearl Harbor=attack photo, Tuskegee=airmen, atomic=mushroom cloud, UN=signing).
- **Deck:** 113 → 128 slides; page numbers renumbered; `validate.py` PASSED; branding/template untouched.
- **Builder:** `scratchpad/rekey_student_deck.py` (per-standard segment plan).
- **Verification:** `build_alignment_maps.py` → 0/0/0; no blank slides; cover intact.

## Execution record — teacher deck alignment (2026-08-01)

The teacher deck's DI segmentation already matched the workbook (4/standard, US.51=5 — it is the
reference the workbook was keyed to), so **no re-segmentation**. Three workbook-alignment fixes:

- **Vocab-first:** each standard's teaching KEY VOCABULARY moved before its first DIRECT INSTRUCTION,
  mirroring the workbook (Vocabulary = Act 1–2, before Cornell notes). Verified vocab-before-DI in all 14.
- **Workbook write-cues:** added a gold "✍ In your workbook · <activity>" caption (113 slides) to every
  slide where students write — Vocabulary (Act 1–2), each DI (Cornell & Close Read, Act 3–4), Primary
  Source (Act 5), Practice Quiz (Act 6, on CHECK FOR UNDERSTANDING), CER (Act 7, on STUDENT ACTIVITY).
- **Ordering defect fixed:** each standard's VOCAB_REVIEW + PROGRESS CHECK had been stranded *after*
  the next boundary slide; every block is now contiguous
  [DIVIDER → QUICK REVIEW → CONFIDENCE → HOOK → VOCAB → DI×M → PEOPLE → PRIMARY SOURCE → GUIDED
  PRACTICE → STUDENT ACTIVITY → CHECK → ANSWER REVEAL → WRAP-UP → VOCAB REVIEW → PROGRESS CHECK].
  Front matter first; "Unit 6 Complete" last. Footer page numbers renumbered sequentially.
- **Verification:** pure reorder (258 slides, none added/dropped) + additive cues; `validate.py` PASSED;
  lesson-flow QC agent **0/0/0**; visual QA clean (cues collision-free, boundary fixed, pages sequential).
  Builder: `scratchpad/rekey_teacher_deck.py`.
- **Pre-existing item (not caused by this pass):** the CHECK-FOR-UNDERSTANDING title renders with an
  overlapping element in LibreOffice on all 14 CHECK slides — present in the original deck; flagged for
  a separate print-QC pass.

**Still open — Target 3:** place the 21 QA'd visual assets (`UNIT6_VISUAL_ASSETS/`) onto Data-Analysis /
geographic slides, with the two mandatory caption caveats (US.57, US.58). Placement table below.

---

## Original plan (as approved)

**Status:** ACTIONABLE PLAN — flagged for Sean's sign-off before execution.
**Why a plan and not a done rebuild:** the student deck is a *strong, branded, committed asset*. The
fix requires **re-segmenting direct-instruction content and adding review slides** (design/authoring,
not a mechanical move). Per house rule ("assess before recreating — don't rebuild strong decks") and
the honesty doctrine, this is specified precisely so execution on sign-off is deterministic and low-risk.

## What the QC agent found (mechanical pass, committed decks + workbook)

`build_alignment_maps.py Teacher Student Workbook` → **0 blocker · 28 major · 0 minor.**
All 28 are deck-side, two patterns, one per standard ×14:

1. **DI under-coverage / non-parity (14).** Teacher teaches **4 DI segments** (US.51 = 5); the student
   review deck condenses them into fewer labeled slides (e.g., US.45: one "KEY POINT" slide carries
   DI 1+2, then two "DIRECT INSTRUCTION" slides). After Target 1a keyed the workbook's guided Cornell
   to the teacher's **"DI N of M"** segments, a student reviewing at home cannot cleanly resolve
   "DI 1 of 4 / DI 2 of 4" — both land on the same condensed slide.
2. **Vocabulary sequenced after direct instruction (14).** Student deck places KEY VOCABULARY last
   in each standard block; the workbook does Vocabulary as Activities 1–2 (first). Student is sent
   backward.

## The re-key (per standard, ×14) — deterministic operations

For each standard block in the **student** deck:

1. **Move KEY VOCABULARY** to immediately after the standard TITLE slide (before any DI/KEY-POINT
   content). → fixes pattern 2. *Pure slide reorder; no content change; fully reversible.*
2. **Re-segment direct instruction to one review slide per teacher DI segment**, same order and titles
   as the teacher deck's DI slides (US.xx · DIRECT INSTRUCTION 1..M). Split the current condensed
   "KEY POINT / DIRECT INSTRUCTION" slides so **M student DI slides == M teacher DI slides == M
   workbook Cornell cues**. → fixes pattern 1. *Content authoring — reuse the teacher slide's body
   text verbatim so wording parity holds; keep the student-deck template/branding.*
3. **Keep** SOURCE IT FIRST, THREE PERSPECTIVES, PROGRESS CHECK; **confirm** PROGRESS CHECK is the
   last slide of the block (US.58 must retain its final Progress Check — the scratchpad copy was short
   one slide; the committed deck is correct, keep it).
4. **Do not** reintroduce teacher-only slides (QUICK REVIEW, CONFIDENCE CHECK, PEOPLE WHO SHAPED,
   CHECK FOR UNDERSTANDING, ANSWER REVEAL) into the student deck — their removal is correct.
5. Target counts after re-key: student DI = 4 for every standard **except US.51 = 5**.

## "How This Deck Works" legend (Sean's note)

The UDL/MTSS "How This Deck Works" slide currently sits as student slide 1. Per Sean, it must **not**
read as a mid-standard lecture slide. It is at the very front (acceptable), but move it to an
**appendix** or mark it clearly as front-matter so it never falls between a task cue and its activity.

## Target 3 — visual asset placement (drop the QA'd package into the decks)

All assets live in `00_START_HERE/UNIT6_VISUAL_ASSETS/US.xx/` (21 files, each with a `.citation.md`).
Place each on its standard's slide during the re-key. **Data graphic → Data Analysis slide;
map → SOURCE IT FIRST or a dedicated geographic slide (fixes SSP.06).** Caption must carry the
sidecar attribution; two maps carry a **mandatory caption caveat**.

| Std | Data graphic (→ Data Analysis) | Map (→ geographic/source slide) | Caption caveat |
|---|---|---|---|
| US.45 | us_unemployment_great_depression | — (map optional, not built) | NICB series ≠ modern BLS |
| US.46 | lend_lease_by_country | — (map not used) | don't mix later cumulative totals |
| US.47 | holocaust_deaths_by_country | holocaust_camps_europe_map | CC BY 3.0 attribution required |
| US.48 | pearl_harbor_losses | pearl_harbor_attack_map (NHHC) | — |
| US.49 | — | — (map optional, not built) | — |
| US.50 | wwii_battle_casualties | dday_normandy_map **+** pacific_island_hopping_map | casualty defs not comparable |
| US.51 | — | — | (Tuskegee/442nd/Navajo/101st — photos, if added, PD only) |
| US.52 | women_workforce_1940_45 | — | labor-force vs employed share |
| US.53 | black_migration_employment | great_migration_map (schematic) | label "schematic" |
| US.54 | incarceration_by_camp | wra_camps_map (schematic) | markers approximate |
| US.55 | us_war_production_1941_1945 | — | 1940/1945 partial periods |
| US.56 | hiroshima_nagasaki_casualties | manhattan_project_sites_map | 1946 MED estimates; 3 NPS sites only |
| US.57 | — | germany_occupation_zones_map | **MANDATORY:** modified/derivative map, anachronistic boundaries, state the date |
| US.58 | un_founding_members_timeline | un_51_member_states_map | **MANDATORY:** Newsmap dating error — caption the correct 10 Jan 1946 opening |

## Execution & verification (on sign-off)

1. Re-key the student deck per the ops above (reorder + re-segment), branding unchanged.
2. Place visuals with cited captions + the two mandatory caveats.
3. Re-key the workbook's remaining absolute `▶ Deck slide N` references (Activities 1,2,5,6,7) to the
   new shared sequence (guided Cornell already uses deck-agnostic "DI N of M").
4. Re-run `build_alignment_maps.py` → **must return 0 blocker / 0 major**; then the visual pass on the
   ~5 changed slides per standard. Ship only at 100% Workbook→Exact-Slide resolution.

**Estimated scope:** ~14 blocks × (1 reorder + 1–2 new DI slides + 1–2 asset drops). Mechanical once
approved; the risk being managed by holding for sign-off is *content re-segmentation on a strong deck*.
