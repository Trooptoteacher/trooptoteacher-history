---
name: wcs-technology-use-compliance
description: Proves that the WCS Technology Use Guidance (2026) — its Educator Blueprint, Areas of Focus 1-4, Appendix exceptions, and every law, board policy, SOP, and research framework it cites — is embedded across the U.S. History Hack product and curriculum, that no requirement is in breach, and makes where we MEET or EXCEED the law visible to any skeptic. Owns the machine-checkable compliance registry (requirements.json), the guardrail (verify_wcs_compliance.py), and the printable skeptic-facing matrix (build_wcs_matrix.py). Use when the user asks to prove WCS technology/tech-use compliance, embed or verify the WCS Technology Use Guidance, show we meet or exceed the WCS/TN laws, run the tech-use compliance guardrail, update the compliance matrix, or answer a board/parent/reviewer skeptic on policy or legal exposure. Sibling to wcs-app-approval-qc (submission packet) and copyright-integrity-accreditation (IP/FERPA-COPPA) — this skill owns the WCS Technology Use Guidance embedding + no-breach proof.
license: MIT
metadata:
  author: TroopToTeacher Technologies
  version: '1.0'
  home: 06_COMPLIANCE_INTERNAL/wcs-technology-use/
  sources_of_truth:
    - WCS Technology Use Guidance (2026) — Educator Blueprint, Areas of Focus 1-4, Appendix, References
    - WCS/TN classroom-law table (No. 660, 939, 330, 442, 279, TCA 2-2-111, No. 493)
    - WCS Board Policies & SOPs (4.201, 4.209, 4.215, 4.401, 4.406) + Acceptable Use Guidelines
    - TN statutes (SB0514/HB0531, Public Chapter 808, Public Chapter 744 of 2022)
    - Federal privacy & accessibility (FERPA, COPPA, CIPA, ADA Title II / WCAG 2.2 AA, Section 508)
    - Research frameworks (Bold School, PICRAT, Hattie Visible Learning, Marano handwriting study, NETP 2024)
---

# WCS Technology Use Guidance — Compliance (embedding + no-breach proof)

This skill is the single owner of one job: **prove, with resolvable evidence, that every
requirement of the WCS Technology Use Guidance and the laws/policies/frameworks it cites is embedded
in History Hack — and make where we meet or exceed the law visible to a skeptic.** It exists because
"we comply" is worthless as an assertion; it must be *checkable*, and it must *fail loudly* the moment
a claim loses its evidence.

## When to Use This Skill

- **Prove WCS technology-use compliance** / **show we meet the law** / **embed the WCS Technology Use Guidance**
- **Run the tech-use compliance guardrail** before a submission, board meeting, or adoption review
- **Update the compliance matrix** after a product/curriculum change
- **Answer a skeptic** (board member, parent, principal, reviewer) who questions the content or legal posture
- **Add a new requirement** when WCS/TN issues new guidance or a new law takes effect
- **Quarterly Administrative Review** of the tech-use posture (Aug/Nov/Feb/May; May catches July-1 TN laws)

## What This Skill Does NOT Own

- **WCS App Approval submission packet** (the 34-item response document) → `wcs-app-approval-qc`
- **IP / copyright / FERPA-COPPA legal review** of content and features → `copyright-integrity-accreditation`
- **WCAG 2.2 AA / 508 accessibility testing** of live URLs → `accessibility-qc-agent`
- **TDOE Schedule F / state adoption** panel review → `tn-textbook-adoption-agent`
- **Historical fact accuracy** (Policy 2.600) → `historian-factcheck-agent`

Those skills run separately; their artifacts are cited as *evidence* in this skill's registry, but this
skill never re-implements their gates.

## The three artifacts (in `06_COMPLIANCE_INTERNAL/wcs-technology-use/`)

1. **`requirements.json` — the single source of truth.** Every WCS requirement as a row: `id`, `group`,
   `source` (the citation), `requirement`, `hh_response` (how we meet it), `posture` (`meets` | `exceeds`),
   `evidence[]`, `status`. Nothing else may claim WCS compliance; if it is not in this file, it is not proven.
2. **`verify_wcs_compliance.py` — the guardrail.** Reads the registry and exits non-zero on any breach:
   a requirement with `status: gap`, a `doctrine`/`repo` evidence path that does not resolve, a `webapp`
   path that is missing when the web app is co-located, a requirement with no resolvable evidence, or a
   malformed row. Run authoritatively with the web app co-located and `--require-webapp` (CI mode).
3. **`build_wcs_matrix.py` — the skeptic-facing artifact.** Renders the registry to a print-first HTML
   matrix (`wcs-technology-use-matrix.html`) — law → requirement → where we meet it → MEETS/EXCEEDS →
   evidence — in the America 250 palette. Print-first (CLAUDE.md): hand it to any skeptic; every claim is cited.

```
python3 06_COMPLIANCE_INTERNAL/wcs-technology-use/verify_wcs_compliance.py --require-webapp   # guardrail
python3 06_COMPLIANCE_INTERNAL/wcs-technology-use/build_wcs_matrix.py                          # (re)build matrix
```

## Working Rules (non-negotiable)

1. **Evidence-only.** Never set `posture` to `meets`/`exceeds` without at least one *resolvable* evidence
   pointer. A claim you cannot resolve on disk is a `gap`, and a `gap` fails the guardrail. "Planned" is not "met."
2. **No fabrication.** Do not invent routes, files, policy numbers, citations, effect sizes, or dates. If the
   product does not have it, the honest state is `gap` — surface it, do not paper over it. (CLAUDE.md content-accuracy rule.)
3. **Meets vs. Exceeds is earned.** Use `exceeds` only where History Hack genuinely goes beyond the requirement
   (the Platinum bar: better, not parity) — e.g. print-first vs. "prioritize non-digital," a closed-loop no-link-out
   environment vs. "filtered internet," a built Celebrate Freedom Week program vs. "observe the week." Never inflate.
4. **Every requirement carries a content-repo anchor where one truthfully exists.** Product-only features are
   proven by `webapp` evidence and verified when the web app is co-located; the authoritative run (CI) co-locates it.
5. **The matrix is generated, never hand-edited.** Edit `requirements.json`, then regenerate. A hand-edited matrix
   can drift from the guardrail and is not trustworthy.
6. **Run the guardrail before you claim compliance.** If it does not exit 0, you are in breach — fix the evidence
   or the product, not the registry.

## Adding or updating a requirement

1. Add/adjust the row in `requirements.json` with a real `source` citation and a precise `hh_response`.
2. Point `evidence[]` at real artifacts: `doctrine`/`repo` (this repo), `webapp`/`webapp_route` (the app),
   `external` (the statute/framework). Confirm each path resolves.
3. Set `posture` honestly (`meets` unless you can defend `exceeds`).
4. Run `verify_wcs_compliance.py --require-webapp` → must exit 0.
5. Regenerate the matrix with `build_wcs_matrix.py`.
6. Log it in `06_COMPLIANCE_INTERNAL/ADMINISTRATIVE_REVIEW.md` if it changes the standing posture.

## Coverage (what the registry proves)

- **Educator Blueprint** — Plan with Purpose · Teach with Intention · Reflect & Respond
- **Area 1** — Safety, Privacy & Application Vetting (AUG, FERPA/COPPA/CIPA, LearnPlatform vetting, family portal)
- **Area 2** — Instructional Technology Best Practices (Bold School + PICRAT, pedagogy-first, print-first, defined duration, paper during digital assessments)
- **Area 3** — Intentional Student Technology Use (active > passive, IEP/504 exceptions, evidence of efficacy, screen minimization, PLC data + ClassLink analytics)
- **Area 4** — Training & Support (professional learning, proactive monitoring, digital/AI literacy, district website, families)
- **Appendix** — uninterrupted-access exceptions (health/IEP/504/ILP/assistive tech)
- **TN classroom laws** — No. 660 (syllabus/religion), No. 939 (founding documents), No. 330 (Civics Seal), No. 442 (Civics Test), No. 279 (Celebrate Freedom Week), TCA 2-2-111 (voter drive), No. 493 (prohibited concepts)
- **WCS policies & SOPs** — 4.406 Internet, 4.215 AI (board), 4.201 AI (SOP), 4.209 Chromebook, 4.401 Textbooks
- **TN statutes & state guidance** — SB0514/HB0531 AI, Public Chapter 808, Age-Appropriate Materials Act, TDOE CS standards, teen social-media guidance
- **Federal** — accessibility (ADA Title II / WCAG 2.2 AA / 508; IDEA/504/ADA rights)
- **Research frameworks cited** — Hattie effect sizes (Educational-Impact Gate), Marano handwriting neuroscience (print-first), NETP 2024
- **Graphic organizers** — the workbook toolkit meets/exceeds the district-supplied examples
