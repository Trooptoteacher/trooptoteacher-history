# Platinum Workbook — Full Build Process

The end-to-end loop, as validated on the Unit 1 DBQ Workbook. Follow in order.

## 1. FIRST check Google Drive for already-sourced material (HARD GATE — do this BEFORE web sourcing AND before workspace scaffolding)
- Sean maintains pre-vetted, publisher-quality primary-source and image libraries in Google Drive, organized per unit. **Always check Drive before sourcing anything new** — web-sourcing first is a process failure that wastes effort and risks lower-provenance duplicates.
- Search Drive with the `gws` CLI (`api_credentials=["gws"]`, required or you get 401): look for the unit folder (e.g. `name contains 'Unit 2' or name contains 'Progressive'`) and its `images/` subfolder.
- If found, download and REUSE them: `PRIMARY_SOURCE_CITATIONS.md`, `IMAGE_CITATIONS.md`, `standards-crosswalk`, `TABLE_OF_CONTENTS.md`, and the standard-code-named `images/` library. The citation files carry MLA/APA + archive links + rights + pull-ready excerpts; images are named by standard code (e.g. `US.14_ida-tarbell.jpg`).
- Only source NEW material from the web for genuine gaps not already covered — and note explicitly which items were gap-filled.
- Commands: search with `gws drive files list --params '{"q":"...","fields":"files(id,name,mimeType)"}' --format json`. Download regular files (md/csv/jpg/pdf) with `gws drive files get --params '{"fileId":"...","alt":"media"}' -o <path>`. Google Docs/Sheets/Slides need `files.export` instead.
- **Verify each downloaded image against its citation** — the citation's described medium/subject must match what the image actually shows (a Drive file can be mislabeled, e.g. an illustrated program cover filed as a "photograph"). Correct the caption to the truth.

## 2. Set up the unit workspace
- Create a dedicated folder, e.g. `/home/user/workspace/<subject>_unit<N>_workbook/`.
- Copy in the template engine `assets/build_workbook_template.py` (or clone the latest from the `History-Hack-US-History-Workbooks` repo if it is the source of truth for this build).

## 3. Gather standards VERBATIM
- Fetch the authoritative TDOE standards document (U.S. History: `https://www.tn.gov/content/dam/tn/education/standards/ss/Social_Studies_Standards.pdf`). For other subjects, locate that subject's official TDOE Social Studies standards.
- Extract the verbatim text of every content standard in the unit and all SSP practices.
- **Save to memory** under `projects.history_hack.textbook.<unit>.verbatim_standards`.
- Never paraphrase a standard in the crosswalk — use exact wording + content strands (C,E,G,H,P,T,TCA, etc.).

## 4. Map standards -> real content (honest Full vs. Context)
- For each content standard, decide: does the workbook carry a dedicated primary source + task for it (**Full**), or is it only present as framing/theme (**Context**)?
- The way to know: grep the built body text for the standard's key nouns. No dedicated document/task hit = Context. Disclose Context in a crosswalk footnote.
- Flag which standards need a geography (SSP `G`) treatment.

## 5. Write the build spec
- Write a markdown build spec in the unit folder (e.g. `BUILD_SPEC_<section>.md`) BEFORE delegating. Include: placement, exact text for any intro/guardrail/callout, table columns + verbatim rows, visual language, dynamic-page-number requirement, and a VERIFY list.

## 6. Build in ReportLab (delegate ONE subagent)
- Spawn ONE `general_purpose` subagent:
  - `preload_skills: ["office/pdf", "design-foundations", "accessibility-qc-agent"]`
  - Repository setup: use existing workspace at the unit folder; do NOT clone.
  - Objective: read the build spec IN FULL; read the engine fully to learn helpers, palette, styles, and the two-pass marker mechanism; implement per spec reusing the keyed-marker pattern (NEVER hardcode page numbers); run the two-pass build; verify; report back page counts and reconvergence examples.
  - **Visual-source handling (LOCKED):** a cartoon/photograph/poster that is a primary source in its own right is its OWN document (its own Doc letter) with its OWN standalone **OPTIC** box via the `VISUAL_IS_PRIMARY` set + `optic_box(...)` mechanism (see engine-conventions.md). NEVER merge a visual primary source into a text document, and NEVER attach an image to a document it does not genuinely depict. Text = HIPPO, visual = OPTIC.
- Keep the objective under ~2000 chars; reference file paths, don't inline large content.

## 7. Two-pass (iterate-until-stable) rebuild
- Any inserted section shifts all downstream pages. The engine's `make_pdf()` iterates builds until the `TOC_PAGES` and `XW` dicts stabilize (converges in ~2 passes). Confirm you see "Converged after N passes."

## 8. Run the rendered white-space activity gate
- Read `white-space-activity-library.md` in full.
- Measure unused printable-body area after rendering. Do not infer visual fullness from extracted character counts alone.
- Apply the locked bands: under 20% passes; 20–40% quarter-page; 40–65% half-page; 65–80% three-quarter-page; above 80% merge/reflow first.
- Match the activity to the page purpose and scaffold stage. Use fixed-height engine components so the activity cannot create a spill page.
- Rebuild and reconverge after each insertion set.

## 9. Verify independently (see qc-checklist.md)
- Render changed pages to PNG and read them. Extract page text and confirm every page reference matches the real footer. Do NOT trust the subagent's self-report.

## 10. Ship
- Re-share the workbook PDF with the SAME shared-asset name for version history and `should_validate=false`.
- Update the existing Google Drive file in place with `gws drive files update --params '{"fileId":"..."}' --upload <file> --upload-content-type application/pdf --format json` (`api_credentials=["gws"]`).

## 11. Re-score Schedule F (see schedule-f-scoring.md)
- Update the self-score markdown to reflect the package as built. Re-share (same asset name) + update its Drive file.

## Integrity guardrails baked into every build
- Only claim supports/standards actually present.
- Frame teacher-applied accommodations as guidance; never claim the workbook "provides an IEP" or replaces mandated accommodations.
- Public-domain / open-license sources only; honest provenance; ™ not ®; no fabricated ISBN.
