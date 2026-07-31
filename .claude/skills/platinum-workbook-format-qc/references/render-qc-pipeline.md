# Render-QC Pipeline — see the pages before you send them

**The single most important discipline in this skill.** A workbook that "builds" can still have
invisible writing lines, merged lines, or a page that bleeds. You cannot catch these from the code or
the estimator — you must **rasterize the docx and look at it.**

## Why not LibreOffice
LibreOffice's Word *import* filter is broken in this sandbox: it converts `.txt`→pdf fine but returns
"source file could not be loaded" for any `.docx`. Do not rely on it. The working path is Spire.Doc.

## Install
```
pip install spire.doc PyMuPDF
```
- **Spire.Doc** renders `.docx`→PDF (free tier: a red "Evaluation Warning" watermark, and it only
  converts the **first ~10 pages**; content past a per-page limit on the last converted page can be
  truncated — this is a renderer artifact, not a bug in your doc).
- **PyMuPDF (`fitz`)** rasterizes the PDF→PNG so you (Claude) can Read the image.

## `assets/render_check.py` — the tool
```
python3 render_check.py <in.docx> [outdir]
```
Prints per-page `fill=NN%` + the page's first text line, and writes `pg01.png … pg10.png` into
`outdir`. **Then Read the PNGs.** `fill%` = the y of the lowest text word ÷ page height.

### Reading the fill number (calibration — learned empirically)
- **Text-heavy pages:** fill% is fairly accurate (e.g. Frayer front rendered 82% vs estimate 84%).
- **Open-box pages:** fill% *under*-reports, because empty draw boxes and ruled lines carry no text
  words — a Sketch Studio that looks 64% "full" of boxes reads low. Judge those by eye.
- **Footer pollution:** on a temp slice the footer text can dominate `maxy`, pinning every page near
  95%. Ignore the number there and look at the images.
- **Light line colors read faint in Spire.** `8892A0` is chosen so lines are clearly visible; the old
  `C9C2B4` renders almost invisibly in Spire (and on screen) — that's exactly why it was abandoned.

## `assets/pagefit.py` — the bleed estimator (fast, whole-doc)
```
python3 pagefit.py <in.docx>
```
Segments the body at `pageBreakBefore` and estimates each segment's height in twips → pages →
last-page fill%. Flags `<-- BLEED (last page mostly empty)` when a segment spans >1 page and the last
page is <45% full.
- **It runs HIGH on open boxes** (counts full box height) and can't see **run-level page breaks**
  (`new PageBreak()` inside a paragraph) — so the aggregated **`(front)` matter segment is a false
  positive; ignore it.** Trust it for *activity* segments (those start with an `H {brk:true}` =
  `pageBreakBefore`).
- Use it as a scan: any activity segment flagged BLEED, or sitting at 95%+ est, go render that page.

## The two calibration facts that drive anti-bleed
1. **Word renders TALLER than Spire.** A page that is at the very bottom edge in the Spire PNG will
   bleed in real Word/print. Leave headroom: aim for a comfortable ~65–90% in Spire.
2. **Standards vary in length.** Close-read passages and TDQ counts differ. The *first* standard is not
   the worst case. Find the fullest (longest `close` text / most TDQs) and render **that** page.

## Deep-page trick — render a page past Spire's 10-page cap
Spire only converts ~10 pages, so Activity 4+ of a single standard fall off the end. To see them,
build a **temp slice** that makes `block()` start at the activity you need:
```js
// scratch: rewrite unit1/build_workbook.js -> build_workbook_TMP.js
// replace everything between the standard-heading push and "  // Activity 4 — Close Read"
// with just: out.push(H(`Standard ${code} — ${s.title}`,1,{brk:true}));
```
Then `ONLYSTD=<worst-std> node build_workbook_TMP.js` and `render_check.py` it — the target activity
now lands on page ~3. Delete the TMP file when done. (This is exactly how the Close-Read self-check
was verified against the longest Government standard.)

## Standard render-QC loop
1. `ONLYSTD=<worst-standard> node build_workbook.js` → small preview docx in `deliverables/`.
2. `render_check.py preview.docx outdir` → **open pg02…pg08 and actually look**: lines visible? boxes
   present? nothing at the very bottom edge? labels bold where they should be?
3. `pagefit.py full.docx` → scan for BLEED on activity segments.
4. For any suspect activity past page 10, use the deep-page slice.
5. Fix → rebuild → re-render. Do not stop at "it builds."
6. When correct, rebuild ALL units, standard + `LARGEPRINT=1.5`, and clean up preview/TMP files.
