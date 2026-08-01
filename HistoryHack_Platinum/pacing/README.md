# US History Pacing — 2026–27 (WCS)

The pacing foundation for History Hack US History, built from the Williamson
County Schools calendars.

## Files
| File | What it is |
|---|---|
| `HH_US_History_Pacing_Guide_2026-27.pdf` | The teacher-facing pacing guide (9 pp). US.01→US.95 consecutively, 1/day, re-dated to 2026–27. |
| `calendar_2026_27.json` | Structured, machine-readable calendar: school year, grading periods, breaks, half-days, 6–12 late-start dates, and every assessment window. The "source of truth" the app + regenerations read from. |
| `pacing_2026_27.json` | The generated day-by-day schedule (177 rows: date, quarter, standard/activity, unit, late-start flag, testing overlay). |
| `source_calendars/` | The original WCS PDFs: student school calendar, district assessment calendar, late-start/early-release schedule. |

## How the guide was built
- **Standards:** US.01 → US.95 in order, **one standard per instructional day** (per request).
- **Buffers:** each unit closes with a clean Review / Flex / CSA rhythm (~4–5 days/unit).
- **Calendar:** 177 instructional days, **Aug 10, 2026 → May 27, 2027**, skipping every WCS break/holiday.
- **Late starts:** the 27 WCS 6–12 late-start (45-min) days are flagged ⏰ so teachers plan lighter.
- **Testing overlay:** benchmark windows, Civics Test, fall semester exams, and the **US History EOC (Apr 19 – May 6, 2027)** as the hard stop.
- **Fit:** the last standard (US.95) lands **Apr 8, 2027**; content wraps **Apr 14**, five days before the EOC — the remaining ~6 weeks are EOC review, Civics Test completion, and special projects (mirrors last year's shape).

## Regenerating (next year)
The annual reminder ("Annual: refresh WCS calendars + US History pacing guide")
fires each June 12. Replace the three `source_calendars/` PDFs, update
`calendar_2026_27.json` dates, and re-run the generator to preserve the same
per-standard timing on the new calendar.
