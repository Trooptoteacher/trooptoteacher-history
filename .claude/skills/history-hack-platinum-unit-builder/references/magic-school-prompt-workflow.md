# MagicSchool Worksheet Prompt Workflow

## Purpose

Let the user generate first-draft worksheets independently while preserving the History Hack standards spine and reducing rework.

## Sequence

1. Audit the target unit and identify genuine worksheet gaps.
2. Read the verified standards source directly.
3. Select the Social Studies Practice(s) that the worksheet actually measures.
4. Define the learning target, success criteria, assessment evidence, and worksheet purpose.
5. Select UDL options that remove barriers without lowering rigor.
6. Assign the MTSS purpose:
   - Tier 1: universal core access for all students
   - Tier 2: targeted scaffold or supplemental practice
   - Tier 3: intensive, explicit, highly scaffolded support
7. Add WIDA L1–2, L3–4, and L5–6 supports.
8. Add accessibility, bilingual parity, citation, and copyright requirements.
9. Produce one self-contained, copy-ready prompt per missing asset.
10. When the user uploads the result, classify it as keep, revise, reject, or merge.
11. Fact-check, correct, brand, format, create/verify the teacher key, export PDF, and connect the physical file.

## Required Prompt Header

Every prompt begins with:

```text
HISTORY HACK WORKSHEET DRAFT REQUEST

UNIT:
[Prepopulated unit number and title]

STANDARD:
[Prepopulated standard ID]
[Exact verified standard wording]

SOCIAL STUDIES PRACTICE(S):
[Prepopulated SSP code, official skill label, and how students will use it]

LEARNING TARGET:
[Prepopulated student-facing target]

SUCCESS CRITERIA:
[Prepopulated observable evidence]

WORKSHEET TYPE AND PURPOSE:
[Prepopulated asset type and instructional role]
```

## Required Design Block

```text
INSTRUCTIONAL DESIGN REQUIREMENTS

UDL 3.0:
- Engagement: [specific option appropriate to this lesson]
- Representation: [specific option appropriate to this content]
- Action and expression: [specific response choices appropriate to the target]

MTSS:
- Primary tier: [Tier 1, Tier 2, or Tier 3]
- Universal core expectation: [what remains rigorous for everyone]
- Targeted scaffolds: [specific supports]
- Scaffold-fading plan: [how support is reduced]

WIDA:
- L1–2: [word bank, visuals, chunking, and structured frame]
- L3–4: [partially structured academic frame]
- L5–6: [independent academic language demand]

ACCESSIBILITY:
- Descriptive headings and logical reading order
- Simple tables with header rows
- No color-only meaning
- Adequate contrast and writing space
- Alt-text recommendations for any necessary image
- Screen-reader-friendly directions

BILINGUAL PARITY:
- Produce equivalent English and Spanish student editions.
- Do not shorten, simplify away, or omit assessed content in Spanish.
```

## Required Output Block

```text
OUTPUTS

1. Editable student worksheet in English
2. Equivalent editable student worksheet in Spanish
3. Separate teacher answer key
4. Brief teacher implementation note
5. Source/citation list for any quotation, image recommendation, statistic, or primary source

CONTENT GUARDRAILS

- Do not invent or paraphrase the standard.
- Do not invent quotations, statistics, citations, historical documents, or image sources.
- Do not use proprietary commercial curriculum text.
- Mark any uncertain claim as [VERIFY] rather than guessing.
- Use HIPP for lesson-level source analysis. Use HIPPO only for a complete DBQ.
- Preserve the historical-thinking demand across all tiers and WIDA bands.
- Do not include student names, records, or personally identifiable information.
- Do not mention external curriculum marketplaces.
```

## Delivery Format

Provide prompts in a table or packet with:

- Prompt ID
- Unit and standard
- Asset name
- Audience
- MTSS tier
- SSP code(s)
- Existing asset being supplemented, if any
- Copy-ready prompt
- Expected upload filename

The expected filename must follow the district file architecture, for example:

`US.08 - Labor Cause and Effect Organizer - Student.docx`

## Returned-Draft Review

When a MagicSchool draft is uploaded:

- Verify the standard and SSP alignment.
- Check factual claims and citations.
- Check that the teacher key answers the actual student version.
- Compare English and Spanish content for parity.
- Confirm UDL choices are actionable.
- Confirm MTSS supports are specific and do not reduce rigor.
- Rebuild inaccessible tables or layouts.
- Apply approved History Hack branding.
- Preserve the editable Word original.
- Export and inspect the PDF.
- Add the file to the manifest and generator only after it passes.
