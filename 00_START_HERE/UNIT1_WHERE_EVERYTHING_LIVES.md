# History Hack — Unit 1: Where Everything Lives
**As of 2026-08-10** · single source-of-truth map for the U.S. History Unit 1 rebuild

---

## The two working repos (edit here)

### 1. `trooptoteacher-history` — skills, decks, deliverables, standards
**Branch:** `claude/skill-narrative-textbook-platinum-unit1` → **PR #32 (open)** · last commit **2026-08-10**

| What | Path | Current version / date | Status |
|---|---|---|---|
| **Skills (canonical, 32)** | `.claude/skills/` (+ `SKILLS.md`, `lint_skills.py`) | synced **FL-2026.08.10** | ✅ edit source of truth |
| **Teacher deck** | `HistoryHack_Platinum/deliverables_unit1/Unit1_Teacher_Deck_America250.pptx` | America 250 · 2026-08-10 | ✅ monograms removed, defs fixed, FOLLOW-ALONG + Cornell/write cues |
| **Student deck** | `…/Unit1_Student_Deck_America250.pptx` | America 250 · 2026-08-10 | ✅ **Accessibility Grade A** |
| **Graphic Organizer Toolkit** | `…/Unit1_Teacher_Graphic_Organizer_Toolkit.pdf` | Course-Standard brand | ✅ canonical (35 pp) |
| **DBQ / Primary-Source Workbook** | `HistoryHack_Platinum/dbq_replacement/HH_US_History_DBQ_Workbook*.pdf` (+ Teacher Answer Key) | America 250 · Units 1–10 | ✅ canonical |
| **Day-One deck** | `HistoryHack_Platinum/day_one/Day1_Welcome_Respect_Deck.pptx` (+ .pdf) | 2026-08-10 | ✅ editable |
| **Lesson-flow map** | `HistoryHack_Platinum/deliverables_unit1/LESSON_FLOW_MAP_Unit1.md` | 2026-08-10 | ✅ deck⇄book⇄log |
| **A11y QC report** | `HistoryHack_Platinum/qc_reports/2026-08-10_slide-deck_QC_Report.md` | 2026-08-10 | ✅ Grade A (re-audit) |

### 2. `history-hack-web-app` — the print pipeline (mission book + flight logs)
**Branch:** `claude/us01-flightlog-handoff-qc` → **PR #669 (open, NEW)** · last commit **2026-08-10**
*(supersedes stale PR #659 — this branch already contains #659's commits)*

| What | Path | Current version / date | Status |
|---|---|---|---|
| **Standard (codified)** | `scripts/print-book/FLIGHT_LOG_STANDARD.md` | **FL-2026.08.10** | ✅ G11 handoff + G12 per-Stop merge locked |
| **Build stamp** | `scripts/print-book/bookmeta.py` | **FL-2026.08.10** | ✅ |
| **Mission Book (reader)** | `public/textbook-pdf/unit-1.pdf` | America 250 · 74 pp | ✅ crew "Open your Flight Log to Entry N" cues |
| **Student Flight Log** | `public/flight-logs/unit-1/unit-1-flight-log-student.pdf` | 23 pp · 2026-08-10 | ✅ **Cornell + Entry merged per Stop** |
| **Teacher Flight Log (key)** | `…/unit-1-flight-log-teacher-key.pdf` | 24 pp · 2026-08-10 | ✅ merged per Stop |
| **Builders** | `scripts/print-book/build_flightlog.py`, `render_proof.py` | 2026-08-10 | ✅ |

**Cross-reference rule (locked):** Stop N = Entry N = US.0N across reader ⇄ deck ⇄ Flight Log.

---

## Reference / export repos (do NOT edit here)

| Repo | What it is | Version / date | Action |
|---|---|---|---|
| `history-hack-skill-library` | Portable `.zip` skill bundle for other platforms | **v1.4.0 · 2026-08-02 (STALE)** | Re-export from `trooptoteacher-history/.claude/skills` after PRs merge; still ships retired `tcap-item-writer-v2` |
| `TroopToTeacher-Course-Build` | (Your "course builder" repo) | **last push 2026-07-31 (STALE)** | Got none of today's work; not where the pipeline lives — leave or re-sync later |

---

## To finish consolidation
1. **Merge PR #669** (history-hack-web-app) → main — reader + flight logs + standard.
2. **Merge PR #32** (trooptoteacher-history) → main — decks + skills + deliverables. *(Skills = skills-only PR governance.)*
3. **Close PR #659** (superseded by #669).
4. After merge: **re-export the skill `.zip` bundle** to `history-hack-skill-library` (bump from v1.4.0).
5. Courses rebuild from the two mains.

## Known follow-ups (not blockers)
- Verify the reader renders the crew "turn to Entry N" cue on **all 7 stops** (confirmed in code; render-check pending).
- Deck `.pptx` visual QA gate can't run here (LibreOffice broken) — open decks once in PowerPoint to confirm.
- `history-hack-skill-library` bundle is stale — refresh post-merge.

_Session: https://claude.ai/code/session_01DzJ9Kwmjezv58fBz9hBhC7_
