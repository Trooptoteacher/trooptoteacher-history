# Adoption crosswalk + Social Studies Practices (SSP) — required per unit

Every unit ships a **Standards Alignment / Adoption Crosswalk** (a reviewer-facing document) and
surfaces the same alignment in the workbook's front-matter. This is what a TN Textbook &
Instructional Materials Quality Commission (Schedule F / Policy 2.600) reviewer expects to see.

## What the crosswalk must contain
1. **Standards coverage** — per standard: the **verbatim TDOE standard** (code + full text),
   the **Social Studies Practices** it exercises (SSP.01–SSP.06), cross-curricular **TDOE ELA**
   link(s) for the grade band, and DOK coverage.
2. **SSP crosswalk** — each SSP.01–SSP.06 → its description → which activities/items exercise it.
3. **Reviewer assurances checklist** — standards alignment (100%), SSP, cognitive rigor (DOK/Hess),
   content accuracy (Policy 2.600 — no known factual error ships), bias/sensitivity, copyright /
   public-domain sources with citations, accessibility (WCAG 2.2 AA / tagged PDF/UA), item-writing
   conventions (for embedded assessments), and interoperability (machine-readable export).

Assessment items in the workbook come from the authoritative bank via `tn-assessment-specialist`,
which already carries DOK/Hess/IRT/SSP metadata — mirror that into the crosswalk; do not re-derive.

## TN Social Studies Practices (verbatim TDOE — shared across all TN social studies courses)

| Code | Short | Full text |
|---|---|---|
| **SSP.01** | Collect from sources | Collect data and information from a variety of primary and secondary sources: printed materials (texts, newspapers, autobiographies, speeches, interviews, letters, journals); graphic representations (maps, timelines, charts, political cartoons, photographs, artwork); field observations/landscape analysis; artifacts; media and technology sources. |
| **SSP.02** | Examine a source | Critically examine a primary or secondary source to extract and paraphrase ideas; discern evidence from assertion; draw inferences and conclusions; recognize author's purpose, point of view, and potential bias; assess strengths and limitations of arguments. |
| **SSP.03** | Synthesize / compare | Synthesize data from a variety of sources: establish accuracy and validity by comparing sources; recognize disparities among accounts; frame appropriate questions for further investigation. |
| **SSP.04** | Construct arguments | Construct and communicate arguments citing supporting evidence: demonstrate and defend ideas; compare and contrast viewpoints; illustrate cause and effect; predict outcomes; devise new outcomes/solutions. |
| **SSP.05** | Historical awareness | Develop historical awareness: recognize how/why accounts change over time; present the past with historical empathy; evaluate how time and place create context; identify continuity and change over time and connect to the present. |
| **SSP.06** | Geographic awareness | Develop geographic awareness: analyze relationships, patterns, and diffusion across scales; analyze map types by origin/authority/structure/context/validity; analyze locations, conditions, and connections of places; examine regions; analyze human–environment interaction. |

## Which practice an activity exercises (signal guide)
- Source / cartoon / map / chart used → **SSP.01** (+ **SSP.02** if analyzed for bias/POV)
- Author purpose, POV, bias, evidence-vs-assertion → **SSP.02**
- Compare/contrast documents, thinkers, accounts; corroboration → **SSP.03**
- Claim + evidence, evaluate, cause/effect argument (CER) → **SSP.04**
- Change/continuity over time, sequencing, context, historical empathy → **SSP.05**
- Place, region, spatial pattern, human–environment, map reasoning → **SSP.06**

Tag the PRIMARY practice first; add secondary practices where genuinely exercised. Recall-only
tasks map weakly — still tag the closest practice (often SSP.05, situating a fact in context).

## Where SSP shows up in the workbook
- The 7-activity spine already exercises SSPs (source read → SSP.01/02; CER → SSP.04; compare →
  SSP.03; primary-source/data → SSP.01/06). Label each activity's SSP in the teacher guide and the
  crosswalk so the alignment is visible before the work.

The formal adoption panel is run by `tn-textbook-adoption-agent`; the accessibility terminal gate by
`accessibility-qc-agent`. This reference defines the crosswalk artifact those gates expect.
