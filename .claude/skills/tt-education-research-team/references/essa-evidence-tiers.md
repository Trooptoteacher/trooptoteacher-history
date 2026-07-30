# ESSA Evidence Tiers — Reference Guide
## TroopToTeacher Technologies · Education Research Team

**Load when:** Sean asks about ESSA tiers, a district RFP requires an evidence statement, or a grant application asks for the level of evidence supporting History Hack.

---

## Statutory Basis

The Every Student Succeeds Act (ESSA, 2015), Section 8101(21), defines four tiers of evidence for educational interventions. These tiers govern which programs can receive Title I, Title II, and Title IV funding, and are frequently required in district vendor RFPs and state adoption processes.

---

## Tier Definitions

### Tier 1 — Strong Evidence

**Statutory requirement:**
- At least one well-designed and well-implemented **randomized controlled trial (RCT)**
- Study must demonstrate a statistically significant positive effect on student outcomes
- Study must have been conducted in a setting relevant to the proposed use

**Practical implication for edtech:**
- Requires an RCT with random assignment of students or classrooms to treatment vs. control
- Sample must be large enough for adequate statistical power
- Effect must be significant at p < 0.05 and preferably show practical significance (e.g., effect size d > 0.2)

**History Hack status: NOT MET — no outcome study of any type has been conducted.**

---

### Tier 2 — Moderate Evidence

**Statutory requirement:**
- At least one well-designed and well-implemented **quasi-experimental study (QES)**
- Must demonstrate a statistically significant positive effect on student outcomes
- Study must use a comparison group (matched schools, matched students, or difference-in-differences design)

**Practical implication for edtech:**
- No random assignment required, but must have a credible counterfactual
- Acceptable designs: propensity-score matching, regression discontinuity, difference-in-differences
- Common district-friendly design: matched prior-year comparison cohort using school-level TCAP data

**History Hack status: NOT MET.**

**Roadmap to Tier 2:**
1. Identify 2+ partner districts willing to share TCAP score data
2. Design matched comparison: classrooms using History Hack vs. demographically similar classrooms not using it
3. Control for prior achievement, SES, teacher experience
4. Run for one full TCAP EOC cycle (one academic year)
5. Analyze with regression controlling for covariates
6. Report effect size and confidence intervals honestly regardless of direction

---

### Tier 3 — Promising Evidence

**Statutory requirement:**
- At least one well-designed and well-implemented **correlational study with statistical controls**
- OR a pre-post study with a single group demonstrating significant gains
- Must demonstrate a statistically significant positive effect

**Practical implication for edtech:**
- Single-group pre-post design is the most accessible starting point for a solo founder
- Requires: baseline measure (pre-test or prior-year TCAP), post measure (post-test or current-year TCAP), statistical test showing significant gain
- No comparison group required, but conclusions are weaker
- Effect size must be reported

**History Hack status: NOT MET — but achievable in Year 1 with a single pilot cohort.**

**Minimum viable Tier 3 design:**
- 1 partner district, 2-4 classrooms, ~60-80 students
- Pre: start-of-year History Hack diagnostic or prior year TCAP score
- Post: TCAP U.S. History EOC score at end of year
- Analysis: paired t-test or regression; report Cohen's d
- Timeline: one academic year aligned to TCAP administration

---

### Tier 4 — Demonstrates a Rationale

**Statutory requirement:**
- A well-specified **logic model** based on high-quality research findings or positive evaluation findings
- Includes an **ongoing study** to produce Tier 1, 2, or 3 evidence (the ongoing study requirement is not enforced for every use case — check specific program requirements)

**Practical implication for edtech:**
- No outcome study required
- Requires: (a) a written logic model connecting activities to outcomes, and (b) citations to peer-reviewed research that supports the theoretical rationale
- This is the starting point for virtually every new edtech product

**History Hack status: CURRENT STATUS — Tier 4.**

**What Tier 4 gives you:**
- Eligible for some Title IV (ESEA) funding streams that accept Tier 4
- Honest basis for district conversations
- Foundation for an evidence roadmap

**What Tier 4 does NOT give you:**
- "Research-proven" language — prohibited
- Claims of efficacy — prohibited
- Eligibility for programs that require Tier 1-3

---

## RFP Language Templates

### If asked "What ESSA evidence tier does History Hack meet?"

> History Hack currently meets **ESSA Tier 4 (Demonstrates a Rationale)** as defined under ESSA Section 8101(21)(D). The product design is grounded in peer-reviewed research on retrieval practice (Dunlosky et al., 2013), spaced repetition (Cepeda et al., 2006), and Rosenshine's Principles of Instruction (2012). A logic model documenting the connection between these research bases and anticipated student outcomes is available upon request.
>
> We are transparent that no outcome study has been completed. A district pilot study is in planning for [year] to generate Tier 3 evidence. TroopToTeacher Technologies is committed to building an honest, rigorous evidence base and will not claim a tier we have not earned through completed research.

### If an RFP asks for a Tier 1 or Tier 2 study

> At this time, History Hack has not been the subject of a randomized controlled trial or quasi-experimental study. We are not able to make a Tier 1 or Tier 2 claim. We welcome the opportunity to discuss a collaborative pilot study with [district name] that could generate the evidence base required for future consideration under these higher tiers.

---

## ESSA Tier Evidence-Building Roadmap for History Hack

```
YEAR 0 (Now) ─────────────────────────────────────────────────────
  Tier 4: Logic model + research alignment document complete
  Action: Finalize logic model, write Research Foundations white paper

YEAR 1 ───────────────────────────────────────────────────────────
  Target: Tier 3 (Promising Evidence)
  Design: Single-group pre-post with TCAP EOC outcome
  Required: 1 partner district, data-sharing agreement, IRB/district approval
  Action: Run pilot, analyze, publish honest findings (positive OR null)

YEAR 2-3 ─────────────────────────────────────────────────────────
  Target: Tier 2 (Moderate Evidence)
  Design: Matched quasi-experimental with comparison cohort
  Required: 2+ districts, larger sample, matched controls
  Action: Extend pilot, add comparison group, replicate findings

YEAR 4+ ──────────────────────────────────────────────────────────
  Target: Tier 1 (Strong Evidence) — aspirational
  Design: RCT (requires university partner, external IRB, significant resources)
  Note: Tier 2 is sufficient for most district adoption decisions
```

---

## Common ESSA Tier Misconceptions to Correct

| Misconception | Correction |
|---|---|
| "Research-based design = Tier 1" | No. Research-based design = Tier 4. The research cited must be ABOUT the product, not the underlying theory. |
| "We align to Rosenshine's Principles, so we're evidence-based" | You are Tier 4. Alignment to principles is rationale, not evidence of the product's efficacy. |
| "A pre-post improvement in our users' scores proves it works" | Without a comparison group and controls, this is observational, not causal. It can support Tier 3 if properly designed. |
| "Testimonials from teachers count" | They do not count as ESSA evidence. They are valuable for marketing but not for tier claims. |
| "We can say Tier 3 because we have a logic model" | No. Tier 3 requires a completed study with statistical results. A logic model is Tier 4. |

---

## Key Citations for ESSA Evidence Framework

- U.S. Department of Education. (2016). *Non-regulatory guidance: Using evidence to strengthen education investments.* https://www2.ed.gov/policy/elsec/leg/essa/guidanceuseseinvestment.pdf
- Coalition for Evidence-Based Policy. (Various). Evidence summary standards aligned to ESSA tiers.
- What Works Clearinghouse (WWC) Review Standards — referenced by ESSA as a credible source for Tier 1/2 findings: https://ies.ed.gov/ncee/wwc/

---
*Research Team · TroopToTeacher Technologies LLC · Integrity-first, always.*
