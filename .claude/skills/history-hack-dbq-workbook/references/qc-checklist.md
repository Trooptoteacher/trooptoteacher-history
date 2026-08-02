# QC Checklist — verify independently, never trust self-reports

The defensibility of the whole product rests on this step. A subagent's self-reported page numbers are NOT evidence. Reproduce every claim yourself.

## Render + eyeball
```python
import pypdfium2 as pdfium
pdf = pdfium.PdfDocument('.../MASTER.pdf')
for i in [6, 7]:               # 0-based page indices
    pdf[i].render(scale=1.7).to_pil().save(f'_p{i+1}.png')
```
Read each PNG and check:
- [ ] No text overflow, no mid-word wraps, no truncation.
- [ ] No unintended sparse page with only one or two carryover lines at the top and otherwise blank space.
- [ ] No orphaned heading; each heading stays with at least the first substantive paragraph, table row, prompt, or activity block.
- [ ] Question stems stay with their options; Cornell cue/note pairs stay together; short tables, rubrics, and response frames do not split awkwardly.
- [ ] No invisible / tofu glyphs. Use plain ASCII or HTML entities (`&mdash; &amp; &trade; &ge; &ndash;`), NEVER literal Unicode checkmarks/arrows/bullets — those rendered as tofu in a prior build.
- [ ] Grayscale-legible (row shading + rules do the work, not color).
- [ ] Header text not the same color as its background band.
- [ ] Body ≥ 10.5pt; ™ renders (not ®).

## Verify every page reference against the REAL footer
```python
def U(p): return pdf[p-1].get_textpage().get_text_range().upper()
# For each crosswalk "(p.NN)" claim, confirm the expected anchor keyword is on page NN:
checks = {12:'HOMESTEAD', 14:'PACIFIC RAILWAY', 34:'URBAN SHARE', 35:'MAPPING THE NATION', ...}
bad = sum(0 if kw in U(pg) else 1 for pg,kw in checks.items())
assert bad == 0
```
- [ ] Every content-standard cell page matches its document's real footer.
- [ ] Every SSP cell page matches.
- [ ] Chart/map cells match the ACTUAL page the named artifact renders on (watch the KeepTogether bug — see engine-conventions.md).
- [ ] TOC page numbers match real section-start footers (including any newly inserted section).

## Visual sources (LOCKED rule — check every image)
- [ ] Every visual primary source (cartoon, photograph, poster) is its OWN document with its OWN standalone **OPTIC** box — NOT silently merged into a text document.
- [ ] Render each document page and confirm the image actually depicts what the caption/surrounding text claims. A mismatched image (e.g. wrong subject sitting next to "Doc F") is a **hard fail** — fix before shipping.
- [ ] Text documents use HIPPO; visual-primary documents use OPTIC. No visual-primary source is left without OPTIC analysis.

## Structural
- [ ] Total ≤ 120 pages.
- [ ] Build log says "Converged after N passes."
- [ ] New TOC entry is in correct reading order.

## Sparse-page and pagination gate (MANDATORY)

Run a full-document automated scan that records, for every page:
- extracted word/line count;
- printable-body bounds and occupied content bounds;
- estimated unused printable-body percentage;
- footprint band (`PASS`, `QUARTER`, `HALF`, `THREE_QUARTER`, `REFLOW_FIRST`);
- whether the page is intentionally designed for handwriting, drawing, Cornell notes, DBQ planning, or another student response.

Flag every page at or above 20% unused plus every page with very low text volume or content occupying only a narrow band at the top. Render and visually inspect every flag. Text counts alone can never clear a page.

- [ ] Under 20% unused: `PASS`.
- [ ] 20–40% unused: apply a context-matched quarter-page activity or document why the area is intentional workspace.
- [ ] 40–65% unused: apply a context-matched half-page activity or document why the area is intentional workspace.
- [ ] 65–80% unused: apply a context-matched three-quarter-page activity or document why the area is intentional workspace.
- [ ] Above 80% unused: attempt merge/reflow first; use a full-page lab only when the page is necessary.
- [ ] Every flagged page is classified in the QA log as `INTENTIONAL WORKSPACE`, `ACTIVITY APPLIED`, or `LAYOUT DEFECT`.
- [ ] Every `LAYOUT DEFECT` is fixed by reflowing content, applying the activity library, adjusting spacing, applying keep-with-next/widow-orphan control, or moving the whole logical block.
- [ ] Intentional workspace pages have a visible title, prompt, directions, or response label that makes the blank space purposeful.
- [ ] No page ships with only one or two carryover lines, an orphaned heading, a detached option, or a short table/rubric fragment.
- [ ] Activity choice matches the page purpose and the source's scaffold stage; late sources do not regain early-stage frames.
- [ ] Activity insertion did not create a new page, reduce essential text below 9.5pt, or make response space unusable.
- [ ] The same gate passes for the native PDF and for PDFs rendered from all editable DOCX deliverables.
- [ ] The build/QC report lists every flagged page, unused percentage, footprint band, final disposition, activity type, scaffold stage, minimum font size, and page-count change.

## Final gate (optional but recommended before human review)
Run the `accessibility-qc-agent` skill on the changed pages for a WCAG/508/ADA evidence pass. It stops cleanly at its budget and emits a STATUS block.

## Then and only then
- [ ] Re-share (same asset name, `should_validate=false` for aged images).
- [ ] Update the Google Drive file in place.
- [ ] Re-score Schedule F and update its Drive file.
