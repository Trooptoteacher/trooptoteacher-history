# WCS 2026–2027 — Schedule & Assessment Facts (for lesson-plan + pacing features)

**Source docs (saved alongside this file):**
- `WCS_Student_School_Calendar_2026-2027.pdf` (approved Nov 17, 2025)
- `WCS_District_Assessment_Calendar_2026-2027.pdf` (updated Jun 15, 2026, 8 pp.)

District: **Williamson County Schools (WCS)**. Product context: **grades 9–12 U.S. History**, so the **6–12** rows govern (K–5 / K–8 rows are not relevant to this product).

---

## 1. Class-time / late-start facts (drives the lesson-plan schedule picker)

> ⚠️ **Bell schedules are per-school.** The exact numbers below are **Franklin High School (FHS) 2026–27** (`FHS_Bell_Schedule_2026-27.pdf`, saved alongside). WCS has several high schools; other schools may differ, so treat the schedule set as school-scoped and default to the teacher's school (FHS for the pilot).

**FHS 2026–27 bell schedules (period length):**

| Schedule | Period length | First bell | Notes |
|---|---|---|---|
| **Regular** (default) | **47 min** | 7:40 (1st) | 7 periods + SAIL/FN5 advisory 10:14–10:42 + A/B/C lunch waves |
| **Activities** | **43 min** | 7:40 (1st) | includes a 45-min "Activity" block 9:20–10:05 |
| **Late Start** | **41 min** | 8:25 (1st) | PLC meetings 7:25–8:10 first; used on the 27 late-start dates |

- **App correction needed:** the app currently models `min-46 / min-43 / min-41`. The **43** (Activities) and **41** (Late Start) match FHS exactly, but **`min-46` should be `min-47`** for FHS Regular. Rename/add `min-47` as the FHS Regular default.
- **Late-start days (grades 6–12):** school starts 45 minutes late; **FHS late-start period = 41 min**. **27 late-start dates**, almost all **Mondays** (list below). Auto-detect these dates → default to the 41-min Late Start schedule.
- **6–12 Late Start dates (27):**
  - **Sem 1:** Aug 18, Aug 24, Aug 31, Sep 8, Sep 14, Sep 21, Sep 28, Oct 5, Oct 19, Oct 26, Nov 2, Nov 9, Nov 16, Nov 30, Dec 7
  - **Sem 2:** Jan 5, Jan 11, Jan 19, Jan 25, Feb 1, Feb 8, Feb 22, Mar 1, Mar 8, Mar 22, Mar 29, Apr 5
- **K–5 Early Release:** 11 dates, 113 min — *not relevant to the HS product.*

### Lesson-plan schedule picker (design)
- **Default = FHS Regular (47 min).** Options: **Regular (47)** · **Activities (43)** · **Late-Start / Monday (41)** · **Custom minutes** (e.g., teacher enters 50) · **Block schedule** (e.g., 90 min).
- **Auto-detect:** if the teacher picks a date that is one of the 27 late-start dates below, default the picker to the **41-min Late Start** schedule (teacher can override).
- **Bell-schedule minutes are now known (FHS):** 47 / 43 / 41 — no open gap for FHS. Other WCS high schools would need their own bell-schedule PDFs to populate school-specific numbers.

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
