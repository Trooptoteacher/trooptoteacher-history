# WCS 2026–2027 — Schedule & Assessment Facts (for lesson-plan + pacing features)

**Source docs (saved alongside this file):**
- `WCS_Student_School_Calendar_2026-2027.pdf` (approved Nov 17, 2025)
- `WCS_District_Assessment_Calendar_2026-2027.pdf` (updated Jun 15, 2026, 8 pp.)

District: **Williamson County Schools (WCS)**. Product context: **grades 9–12 U.S. History**, so the **6–12** rows govern (K–5 / K–8 rows are not relevant to this product).

---

## 1. Class-time / late-start facts (drives the lesson-plan schedule picker)

- **Regular days:** WCS bell schedule. The app already models three WCS period lengths — **46 / 43 / 41 min** (`ScheduleId = "min-46" | "min-43" | "min-41"`). Which one is "most days" vs. special-schedule days still needs confirming against the school's actual bell schedule.
- **Late-start days (grades 6–12):** school starts **45 minutes late → shortened periods**. **27 late-start dates**, mostly **Mondays**. The per-period minutes on a late-start day are NOT in the calendar; they come from the school bell schedule (⚠️ still needed to set exact defaults).
- **6–12 Late Start dates (27):**
  - **Sem 1:** Aug 18, Aug 24, Aug 31, Sep 8, Sep 14, Sep 21, Sep 28, Oct 5, Oct 19, Oct 26, Nov 2, Nov 9, Nov 16, Nov 30, Dec 7
  - **Sem 2:** Jan 5, Jan 11, Jan 19, Jan 25, Feb 1, Feb 8, Feb 22, Mar 1, Mar 8, Mar 22, Mar 29, Apr 5
- **K–5 Early Release:** 11 dates, 113 min — *not relevant to the HS product.*

### Lesson-plan schedule picker (design)
- **Default = WCS schedule.** Options: **Regular (WCS)** · **Late-Start / Monday (short)** · **Custom minutes** (e.g., teacher enters 50) · **Block schedule** (e.g., 90 min).
- **Auto-detect:** if the teacher picks a date that is one of the 27 late-start dates above, default the picker to the Late-Start schedule (teacher can override).
- ⚠️ **Still needed from the school:** the actual bell-schedule minute values — regular period length AND late-start period length — to set the true numeric defaults. (46/43/41 are in code but not yet mapped to "regular vs. late-start.")

---

## 2. Instructional-days / grading calendar (drives pacing)

- **1st Semester = 83 instructional days · 2nd Semester = 94 instructional days.**
- Start **Aug 10, 2026** (½ day); first full day **Aug 11**.
- **Q1 ends Oct 9** (44 grading days) · Fall Break **Oct 12–16** · **1st Semester ends Dec 18** (½ day; 39 grading days).
- **2nd semester begins Jan 5, 2027** · **Q3 ends Mar 12** (46 grading days) · Spring Break **Mar 15–19** · **Last day May 27** (½ day; 48 grading days) · Graduation window **May 27–30**.
- Closures: Labor Day Sep 7 · Thanksgiving Nov 23–27 · Winter Break Dec 21–Jan 4 · MLK Jan 18 · Mid-Winter/Presidents Feb 12–15 · Spring Holiday Mar 26.

### Pacing connection (design)
- **Default:** auto-distribute the US History units/standards across the real instructional days above (Aug 11 → May 27), respecting closures + the half-days + late-start days.
- **Override:** teachers can set their own pacing (drag a standard's target date, compress/expand a unit). Default is WCS calendar; custom is opt-in.

---

## 3. Assessment windows (U.S.-History-relevant rows; drives pacing + remediation timing)

- **Civics Test — Grades 11–12** — window **Aug 10, 2026 – May 27, 2027**, ~30 min, **administered in U.S. History classes** (state-mandated, graduation requirement). *Surface this to US History teachers.*
- **1st-Quarter Beginning-Year Assessment (Performance Matters), Gr 6–12** — Aug 11 – Sept 11 (~40 min/test).
- **1st-Quarter Benchmark (Performance Matters), Gr 2–12 select core** — **Oct 2–26, 2026**.
- **2nd-Quarter Benchmark** — **Dec 4, 2026 – Jan 12, 2027**.
- **Fall Semester Exams (Midterms), Gr 7–12** — **Dec 15–18, 2026** (15% of HS fall final).
- (Later pages of the assessment PDF cover spring benchmarks, winter/spring screenings, and TCAP/EOC windows — see the saved PDF for full detail; the U.S. History **EOC/TCAP** window sits in the spring.)

### Remediation-timing connection
- Benchmark windows (Oct 2–26, Dec 4–Jan 12) are the natural trigger points for the **"Remediate this standard"** feature — flag low standards right after each benchmark and offer reteach packs before the next summative.

---

*This file is a distilled reference for the lesson-plan generator, pacing, and remediation features. Numbers taken verbatim from the two saved WCS PDFs; the one open gap is the school's exact bell-schedule minutes (regular + late-start).*
