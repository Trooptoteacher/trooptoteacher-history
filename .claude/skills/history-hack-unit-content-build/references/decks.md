# Decks — finalize (assess → keep → retune)

The Course Standard decks usually already exist and are strong. **Assess before recreating.**
Unit 6's decks (Student 113 slides, Teacher 258) were complete, on-brand, and content-aligned —
the right move was palette unification + targeted fixes, NOT rebuilding.

## Structure (title-labeled blocks)
- **Student (Lean):** slide 1 = "How This Deck Works" legend; then per standard an 8-slide block
  starting at `base = 2 + 8·k` (k=0 for the first standard): title, 3 content/DIRECT INSTRUCTION,
  `SOURCE IT FIRST` (base+4), `THREE PERSPECTIVES` (base+5), `KEY VOCABULARY` (base+6),
  `PROGRESS CHECK` (base+7).
- **Teacher (Full):** ~18-slide block per standard; every slide title is labeled
  (`US.xx · KEY VOCABULARY`, `US.xx · DIRECT INSTRUCTION`, `US.xx · PRIMARY SOURCE ANALYSIS`,
  `US.xx · CHECK FOR UNDERSTANDING`, `US.xx · STUDENT ACTIVITY`, …) — **map by title, not position.**
- All slides are navy full-bleed, so gold text is readable anywhere on the canvas.

## Palette unification (LOCKED canonical)
Migrate deck tokens → canonical by rewriting `srgbClr val` in every `ppt/**/*.xml`:
`1A2332→1B2A4A` (navy), `C9A84C→C89B3C` (gold), `C62828→B22234` (teacher red),
`F9A825→C89B3C` (teacher amber). Do it by unzip→regex-replace→rezip (preserve all other parts):
```python
import zipfile, re, os
def migrate(src,out,mp):
    zi=zipfile.ZipFile(src); zo=zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED)
    for it in zi.infolist():
        data=zi.read(it.filename)
        if it.filename.startswith('ppt/') and it.filename.endswith('.xml'):
            t=data.decode('utf8','replace')
            for a,b in mp.items(): t=re.sub(r'(srgbClr val=")('+a+r')(")',lambda m:m.group(1)+b+m.group(3),t,flags=re.I)
            data=t.encode('utf8')
        zo.writestr(it,data)
    zi.close(); zo.close()
```
Validate: `validate.py OUT.pptx --original SRC.pptx` → "All validations PASSED". Re-render to confirm.

## Known layout fix — DIRECT INSTRUCTION long titles (Student deck)
Student DI content slides put full sentences at 23pt in a ~0.95" band above a gold divider at
T≈1.9"; 4-line titles clip the divider. Fix: for DI content-title boxes at 23pt with long text,
set runs to 19pt, set box top≈0.82"/height≈1.02", and enable shrink-to-fit
(`MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE`). Longest titles then wrap to 3 lines above the divider.
Teacher DI titles are short headings (30pt) and already fit — don't touch them. Verify by render.

## Adding cues — see slide-keying.md
The `✍ In your workbook` cue is part of finalization but documented with the keying it mirrors.

## Deliver
Both decks 16:9 (13.33×7.5). Commit to `00_START_HERE/UNITn_DECKS_BUILD/` with STATUS.md. Optional
export to PDF/PNages for review; the .pptx is the editable authoritative file.
