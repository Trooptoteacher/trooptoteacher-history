---
name: magic-school-created-worksheets
description: "Create fully populated, copy-ready MagicSchool prompts for History Hack worksheets and review the returned files. Use when the user asks for Magic School Created Worksheets, MagicSchool worksheet prompts, independently generated worksheets, or a prompt packet for missing unit materials. Imports exact verified standards, Social Studies Practices, UDL 3.0, MTSS, WIDA, accessibility, bilingual parity, citations, teacher-key requirements, filenames, and post-upload Platinum QA."
license: Proprietary
compatibility: "Designed for History Hack U.S. History curriculum workflows by TroopToTeacher Technologies LLC."
metadata:
  author: "TroopToTeacher Technologies LLC"
  version: "1.0"
---

# Magic School Created Worksheets

## Purpose

Help the user create first-draft History Hack worksheets independently in MagicSchool without requiring the user to locate, paste, or interpret standards and instructional frameworks.

The agent supplies complete, copy-ready prompts. MagicSchool supplies a draft. The returned file does not become an approved History Hack asset until it passes review, correction, formatting, and connection QA.

## When to Use

Use this skill when the user asks to:

- Create MagicSchool prompts for History Hack worksheets
- Build “Magic School Created Worksheets”
- Generate missing worksheets independently and upload them later
- Produce prompts for guided notes, Cornell notes, HIPP organizers, Venn diagrams, compare/contrast work, cause-and-effect organizers, primary-source activities, formative assessments, exit tickets, or similar materials
- Review a worksheet generated from one of these prompts

## Required Inputs

Before generating prompts, establish:

- Unit number and title
- Standard ID
- Verified exact standard wording
- Applicable Social Studies Practice(s)
- Existing materials and genuine gap
- Intended worksheet type
- Intended MTSS tier
- Student audience and language requirements

If the verified standards source or unit audit is unavailable, do not invent the missing information. Retrieve the source or clearly identify the blocker.

## Non-Negotiable Rules

- Never give the user a blank prompt asking them to paste the standard.
- Never leave MagicSchool to ask the user which worksheet type, learning target, primary source, content focus, or perspective to use.
- Import the exact verified standard wording into every prompt.
- Include only Social Studies Practices the worksheet genuinely teaches or measures.
- Create prompts only for genuine gaps identified through an asset audit.
- MagicSchool output is a draft, not a factual, standards, citation, or formatting authority.
- Preserve the rigor of the historical-thinking target across all tiers and language levels.
- Use HIPP for lesson-level source analysis. Use HIPPO only for a complete DBQ.
- Require equivalent English and Spanish student content; do not shorten the Spanish edition.
- Teacher-facing materials remain English unless a bilingual teacher edition is specifically requested.
- Do not include student names, records, or personally identifiable information in prompts.
- Do not request proprietary commercial curriculum text or unlicensed content.
- Do not mention external curriculum marketplaces.
- Begin every prompt with an execution directive: all required decisions are supplied; do not ask follow-up questions; create the requested package now.

## Framework Composition

Each prompt must contain:

### Standards and Practices

- Unit and lesson context
- Standard ID and exact official wording
- Applicable SSP code(s), skill label, and student action
- Student-facing learning target
- Observable success criteria
- Assessment evidence
- One explicitly selected worksheet type
- One explicitly stated instructional focus
- A balanced perspective plan appropriate to the standard
- Preselected content and primary sources, or an explicit statement that no primary source is required

### UDL 3.0

- Multiple means of engagement
- Multiple means of representation
- Multiple means of action and expression
- Specific options appropriate to the worksheet, not generic labels

### MTSS

- Primary tier: Tier 1, Tier 2, or Tier 3
- Universal core expectation
- Targeted scaffolds
- Scaffold-fading plan
- Progress-monitoring evidence when applicable

### WIDA

- L1–2: visuals, word bank, chunking, and highly structured frames
- L3–4: partially structured academic-language frames
- L5–6: independent academic-language demand

### Accessibility and Language

- Logical heading hierarchy and reading order
- Simple tables with headers
- No color-only instructions
- Adequate contrast and writing space
- Alt-text recommendations
- Screen-reader-friendly directions
- English/Spanish student-edition parity

### Required Outputs

- Editable English student worksheet
- Equivalent editable Spanish student worksheet
- Separate teacher answer key
- Brief teacher implementation note
- Source and citation list
- Expected upload filename

## Prompt Creation Workflow

1. Audit the unit and confirm the worksheet is genuinely missing.
2. Read the verified standard directly from the standards source of truth.
3. Select the SSP(s) the worksheet will teach or assess.
4. Define the learning target, success criteria, and evidence of mastery.
5. Choose the worksheet type because it fits the target, not merely to fill a category.
6. Select the historical content focus and perspective balance.
7. Preselect any primary source, including creator, title, date, repository URL, rights status, and exact excerpt when permitted.
8. Select actionable UDL options.
9. Assign an MTSS tier and scaffold-fading plan.
10. Add WIDA supports for all three bands.
11. Add accessibility and bilingual requirements.
12. Add factual, citation, copyright, and no-invention guardrails.
13. Produce one self-contained prompt per worksheet.
14. Provide the expected Word filename and upload instructions.

Read `references/prompt-template.md` before creating the prompt packet.

## Prompt Packet Output

For each worksheet, provide:

- Prompt ID
- Unit and standard
- Worksheet name
- Student/teacher audience
- SSP code(s)
- MTSS tier
- Reason the asset is needed
- Copy-ready MagicSchool prompt
- Expected upload filename

Do not make the user combine fragments from several places. Each prompt must stand alone.

## Returned Worksheet Workflow

When the user uploads MagicSchool-created files:

1. Inventory the upload and match it to the prompt ID.
2. Confirm the file is editable Word when required.
3. Verify standards and SSP alignment.
4. Fact-check claims, quotations, dates, statistics, and source attributions.
5. Check copyright and licensing.
6. Compare English and Spanish editions for parity.
7. Confirm the teacher key answers the actual student edition.
8. Evaluate UDL, MTSS, WIDA, and accessibility implementation.
9. Correct layout, History Hack branding, filenames, headings, tables, and writing space.
10. Preserve one authoritative editable Word original.
11. Export and visually inspect the print-ready PDF.
12. Add it to the unit manifest and generator only after it passes.

Read `references/returned-file-review.md` during review.

## Completion Standard

A MagicSchool-created worksheet is complete only when:

- The physical Word file exists and opens
- Standard and SSP alignment are correct
- Historical content and citations pass review
- UDL, MTSS, WIDA, bilingual, and accessibility requirements are functional
- Student and teacher versions correspond
- History Hack formatting and naming are correct
- PDF export passes visual inspection
- The file is connected to the correct unit and standard
