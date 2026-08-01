# Schedule F self-score — grounding rubric for EVERY section (LOCKED practice)

**Standing rule (Sean):** the TDOE High School Social Studies **Schedule F** rubric grounds
everything we build. **Every section we complete ships with its own Schedule F self-score.** Not a
final gate — a running, per-section discipline that keeps the whole unit academically defensible.

- **Instrument:** TDOE High School Social Studies Instructional Materials Scoring Rubric (Schedule F /
  TN Textbook & Instructional Materials Quality Commission). Rubric PDF:
  https://www.tn.gov/content/dam/tn/textbook-commission/documents/schedule-f/High_School_Social_Studies_Rubric.pdf
- **Scale:** 0 = not present · 1 = present but intent/frequency not fully met · 2 = present and fully met.
- **Structure:** Gateway/Table 1 (Alignment) · Table 2 Instructional Focus (9 indicators, /18) ·
  Table 3 Social Studies Practices/SSPs (7 indicators, /14) · Table 4 Accessibility (2, /4).
  **Total = Tables 2–4, max 36.** Statutory bar: ≥80% AND Gateway satisfied.
- **Standing:** History Hack is **supplemental** (T.C.A. §49-6-2202(a)(3)) — no Commission approval
  required; the self-score is a defensibility artifact, disclosed as a publisher self-assessment.
  Author = TroopToTeacher Technologies LLC.

## The honesty doctrine (what makes a self-score defensible)
1. **Score as-built, never as-planned.** Every indicator note states the evidence + any gap plainly.
2. **Hold indicators low on principle** when that's the honest answer (e.g., "Review Opportunities held
   at 1 — spaced review is a curriculum-layer responsibility"). A principled non-claim beats an
   inflated 2. State the intended ceiling explicitly.
3. **Accuracy is foundational** (TDOE Policy 2.600). A known factual error (wrong date, erroneous map,
   bad figure) is a deficiency that blocks "fully met" until fixed — regardless of how good the rest is.
4. Mark contextual standards **Context**, not Full, with a footnote.
5. Common Core RH/WHST codes are internal cross-subject proof ONLY — never marketed as Common
   Core-aligned (T.C.A. §49-6-2202).

## Per-section vs. unit-level
- **Unit deliverables** (Student Workbook, Teacher Guide, each Deck) get a full Tables 2–4 (/36) score.
- **Sub-sections** (e.g., a visual-asset layer, an assessment set) score only the indicators they
  touch — say so explicitly and don't fabricate a /36. A visual-asset layer, for instance, touches
  Content Accuracy, SSP.06 (geographic awareness), Disciplinary Literacy, Multiple Perspectives, and
  Accessibility (alt text/print+digital). Reference: `00_START_HERE/UNIT6_VISUAL_ASSETS/SCHEDULE_F_SELF_SCORE.md`.

## File convention
Each completed section commits a `SCHEDULE_F_SELF_SCORE.md` in its build folder:
- indicator table (indicator · score · as-built evidence/gap),
- deficiencies with severity (critical/major/minor) + remediation,
- an honest section verdict (approvable / not yet, and why),
- subtotal/total + % for full unit deliverables (with the "what changed" delta on re-score).
Re-score after any change that touches an indicator; verify page refs (they shift on insert).

## Workflow
1. When a section is complete, write/refresh its `SCHEDULE_F_SELF_SCORE.md` against the as-built material.
2. Resolve **critical/major** deficiencies before calling the section done (accuracy defects especially).
3. Roll section scores up into the unit deliverable's Tables 2–4 total at unit close.
4. The `tn-textbook-adoption-agent` skill runs the formal panel-style review; this doc is the
   lightweight running discipline that keeps us ready for it.
