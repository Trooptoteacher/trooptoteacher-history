# Pilot Study Design — Protocol Template
## TroopToTeacher Technologies · Education Research Team

**Load when:** Sean is designing a district pilot study, drafting a study protocol for a partner district, preparing IRB or district research approval materials, or describing the planned study in a grant or RFP.

---

## Guiding Principle

The goal of a Year 1 pilot is to generate preliminary evidence, not definitive proof. A well-designed small pilot that reports honest null results is more valuable long-term than a poorly designed study that overstates findings. Design for integrity above all.

---

## Study Design Decision Tree

```
Do you have random assignment to History Hack vs. control?
├─ YES → RCT → targets Tier 1 (requires substantial resources; not recommended Year 1)
└─ NO
   ├─ Do you have a comparison group (matched schools/classrooms)?
   │   ├─ YES → Quasi-Experimental Study (QES) → targets Tier 2
   │   └─ NO
   │       ├─ Do you have pre and post measurements?
   │       │   ├─ YES → Pre-Post Single Group → targets Tier 3
   │       │   └─ NO → Cross-sectional only → supports Tier 4 only
```

**Recommendation for Year 1:** Pre-Post Single Group (Tier 3 attempt). Achievable with 1 partner district. If 2+ districts participate, attempt matched comparison for Tier 2.

---

## Year 1 Pilot Study Protocol Template

### Study Title
*History Hack U.S. History Curriculum Pilot Study: [District Name] [School Year]*

### Study Purpose
To generate preliminary evidence about whether History Hack, a web-based U.S. History curriculum aligned to Tennessee Academic Standards, is associated with measurable gains in student U.S. History knowledge and TCAP EOC performance.

### Design
Single-group pre-post design with historical comparison (prior-year TCAP cohort as reference)
- Study type: Observational / pre-post; not an RCT
- ESSA evidence tier targeted: Tier 3 (Promising Evidence) — pending acceptable effect size and statistical significance

### Participants

**Target:**
- Minimum 60 students (2 classrooms) for 80% power to detect d = 0.5 at alpha = 0.05
- Preferred: 80-120 students (3-4 classrooms) for more stable estimates
- Grade: 8th grade (standard U.S. History year in TN) OR high school U.S. History
- School type: Public district school in Tennessee [specify district]

**Inclusion criteria:**
- Enrolled in U.S. History course for the full academic year
- Participating teacher completes fidelity log
- Parent/guardian consent obtained (if under 18; see consent section)

**Exclusion criteria:**
- Students enrolled for fewer than 60 school days
- Students who switch teacher mid-year

### Intervention (History Hack)

**What teachers will do:**
- Use History Hack as the primary or supplementary curriculum for U.S. History [specify role: primary vs. supplementary — important for fidelity definition]
- Assign platform modules aligned to the unit sequence [list units or confirm with `tn-content-specialist`]
- Complete a brief fidelity log biweekly (estimated 5 min per week)

**Dosage definition:**
- Minimum: 70% of assigned modules completed by the end of the study period
- Measured by: platform completion logs [NEEDS VERIFICATION — confirm this data is accessible from the repo/platform]

**Teacher support:**
- Onboarding session (1-2 hours at start of year)
- Mid-year check-in (30 min, via video call)

### Outcome Measures

**Primary outcome:**
- TCAP U.S. History EOC scale score (state-administered)
- Obtained from: district data-sharing agreement (coordinate with `tt-legal-team` for DPA)
- Comparison: current-year participants vs. prior-year cohort at the same school(s) [specify clearly]

**Secondary outcomes:**
1. In-platform formative quiz scores — unit pre/post scores [NEEDS VERIFICATION — confirm quiz data is logged per student]
2. Module completion rate (% of assigned modules completed)
3. Teacher satisfaction survey (developed by research team, administered end of year)

**Engagement proxy:**
- Average questions answered per student per week
- Session frequency (logins per week)
- Measured by: platform usage logs [NEEDS VERIFICATION]

### Timeline

```
Month 1 (August/September)
  · Finalize data-sharing agreement with district
  · Obtain IRB or district research approval
  · Distribute parent/guardian consent forms
  · Teacher onboarding session
  · Establish baseline (prior TCAP scores pulled from district records)

Months 2-8 (September-April)
  · History Hack used in classrooms per protocol
  · Fidelity logs collected biweekly
  · Platform usage data collected continuously
  · Mid-year check-in (January)

Month 9 (April-May)
  · TCAP EOC administration (state-administered)
  · End-of-year teacher survey administered

Month 10-11 (June-July)
  · TCAP score data received from district
  · Data analysis conducted
  · Preliminary findings report drafted

Month 12 (August)
  · Final report shared with district and made available publicly
  · Findings presented honestly regardless of direction
```

### Data Analysis Plan

**Primary analysis:**
- Paired t-test (if using same students' prior TCAP vs. current TCAP) OR
- Independent samples t-test (if comparing prior-year cohort to current-year cohort)
- Report: mean difference, standard deviation, 95% confidence interval, Cohen's d
- If d >= 0.2 and p < 0.05: describes a small positive effect
- If d >= 0.5: describes a medium positive effect (the threshold for educationally meaningful)

**Secondary analysis:**
- Correlation between platform usage (dosage) and TCAP score change
- Subgroup analysis by prior achievement quartile [only if sample is large enough — n >= 30 per subgroup]

**What to report regardless of findings:**
- Full results including null or negative results
- Sample attrition and reasons for exclusion
- Effect size with confidence intervals
- Fidelity data (did teachers actually use the platform as intended?)
- Study limitations section (see below)

### Limitations to Pre-Register and Report

The study team will acknowledge the following limitations in any report:

1. **No random assignment** — cannot establish causal attribution; observed gains may reflect teacher effects, school environment, or other factors
2. **Single cohort / single school** — results may not generalize to other districts or student populations
3. **Historical comparison confound** — prior-year and current-year cohorts may differ on unmeasured characteristics; prior-year students did not have access to History Hack but also did not have the same teacher in the same year
4. **Selection bias** — districts that volunteer for a pilot may be above average in implementation capacity and teacher buy-in
5. **Dosage confound** — students who complete more modules may be higher-motivation students who would perform better regardless
6. **Short-term measurement** — TCAP EOC is assessed once at end of year; long-term retention beyond the study year is not measured

---

## IRB and Consent Framework

**IMPORTANT: This is a framework, not legal advice. Defer all specific IRB submission decisions to `tt-legal-team` and the relevant university or district IRB office.**

### When IRB review is required:
- Any time a university partner is involved in data collection or analysis
- Any time results will be published in an academic journal or conference
- Any time student data is collected beyond what the district routinely collects for educational purposes

### When district research approval (not full IRB) may suffice:
- District-internal evaluation with no university involvement
- Data limited to district-held records (TCAP scores, attendance)
- Results used for internal improvement only (not publication)
- Check each district's specific research approval policy — they vary

### Consent document checklist:
- [ ] Study purpose described in plain language (8th-grade reading level)
- [ ] What data will be collected (platform logs, TCAP scores, survey responses)
- [ ] How data will be stored and for how long
- [ ] Who will have access to data (named: Sean Reynolds, [university partner if applicable])
- [ ] Student data will not be sold or shared with third parties
- [ ] Participation is voluntary; withdrawal does not affect grades
- [ ] Contact information for questions
- [ ] Parent/guardian signature line (for students under 18)
- [ ] Student assent form (for students 13 and older — recommended)

### Data storage requirements:
- De-identified data only after linking TCAP scores to platform usage
- Student ID numbers, not names, in analysis files
- Password-protected, encrypted storage (not shared Google Docs)
- Retention period: [NEEDS VERIFICATION — confirm with `tt-legal-team`; typical is 3-5 years]

---

## Fidelity of Implementation Log Template

Distribute biweekly to participating teachers:

```
Teacher Fidelity Log — History Hack Pilot
Week of: ___________  Teacher: ___________  School: ___________

1. How many class periods used History Hack this week?  __ out of __ total periods
2. Which modules/units were assigned this week? [list]
3. Approximately what % of students completed the assigned module? ___%
4. Did you encounter any technical issues? [ ] No  [ ] Yes — describe briefly: ___
5. Did you supplement History Hack with other materials this week? [ ] No  [ ] Yes — describe: ___
6. Any other notes:
```

---

## Sample Size Reference Table

| Students (n) | Design | Detectable effect (d) at 80% power, alpha = 0.05 |
|---|---|---|
| 30 | Pre-post | d = 0.70 (large; will miss smaller effects) |
| 60 | Pre-post | d = 0.50 (medium; recommended minimum) |
| 100 | Pre-post | d = 0.40 |
| 200 | Pre-post | d = 0.28 |
| 400 | QES with matched comparison | d = 0.20 (small; educationally meaningful) |

**Honest expectation-setting with districts:**
> "A Year 1 pilot with 60-120 students will give us enough sensitivity to detect a meaningful effect if one exists, but it will not have the statistical power to rule out small effects. We are transparent that this is preliminary evidence, and we will design a larger study in Year 2 if the pilot shows promise."

---

## Report Template — Findings Summary

```
HISTORY HACK PILOT STUDY — PRELIMINARY FINDINGS
[District Name] · [School Year]
TroopToTeacher Technologies LLC

STUDY DESIGN: [Pre-post / Quasi-experimental]
SAMPLE: [n] students, [n] classrooms, [n] schools
OUTCOME MEASURED: TCAP U.S. History EOC scale score

RESULTS:
  Mean TCAP score, pilot cohort:         [X.X] (SD = [X.X])
  Mean TCAP score, comparison/prior yr:  [X.X] (SD = [X.X])
  Mean difference:                       [+/- X.X points]
  Effect size (Cohen's d):               [X.XX]
  Statistical test:                      [t(df) = X.XX, p = X.XX]
  95% Confidence Interval:               [lower, upper]

INTERPRETATION:
  [Accurate, honest interpretation. Do not overstate. If p > 0.05, state the
   result did not reach statistical significance. If d < 0.2, state the effect
   was not educationally meaningful by conventional standards.]

DOSAGE ANALYSIS:
  Average module completion rate:        [X]%
  Average sessions per student:          [X]
  Correlation with TCAP change:          [r = X.XX, p = X.XX]

LIMITATIONS:
  [List all pre-registered limitations]

ESSA TIER CLAIM (post-study):
  [If significant positive effect with acceptable design: Tier 3 — Promising Evidence]
  [If null result: Tier 4 — Demonstrates a Rationale (study did not yield positive effect)]

NEXT STEPS:
  [Honest recommendation: expand, redesign, or pause based on findings]
```

---

## Key Statistical References

- Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum. — defines d = 0.2 small, 0.5 medium, 0.8 large
- Bloom, H. S., et al. (2008). Performance trajectories and performance gaps as achievement effect-size benchmarks for educational interventions. *Journal of Research on Educational Effectiveness, 1*(4), 289-328. — contextualizes effect sizes in K-12 education (typically d = 0.1 to 0.3 for well-designed interventions)
- What Works Clearinghouse Procedures Handbook — free at https://ies.ed.gov/ncee/wwc/ — the gold standard for study quality criteria districts recognize

---
*Research Team · TroopToTeacher Technologies LLC · Integrity-first, always.*
