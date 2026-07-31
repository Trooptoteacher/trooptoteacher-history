# Rendering & the QC gate

## Convert to PDF (docx or pptx)
LibreOffice needs the matching module: `libreoffice-writer` (docx), `libreoffice-impress` (pptx).
If a file "could not be loaded" but `python-docx`/`python-pptx` open it fine, the module is
missing — `apt-get install -y libreoffice-impress` (or `-writer`), don't assume corruption.

```bash
export HOME=/root/lohome
soffice --headless --convert-to pdf FILE.docx   # run with sandbox disabled
```

## Blank / near-empty page detection (the gate)
```python
import pypdfium2 as pdf, numpy as np
d = pdf.PdfDocument('FILE.pdf')
blanks=[]
for i in range(len(d)):
    arr=np.asarray(d[i].render(scale=0.3).to_pil().convert('L'))
    ink=(arr<200).mean()          # fraction of dark pixels
    if ink<0.020: blanks.append((i+1, round(ink*100,2)))
print(len(d),'pages; near-blank:',blanks)
```
- `< ~0.4%` = truly blank (header/footer only). `~0.4–1.3%` = an orphaned box header/writing
  lines that tipped over. Writing-heavy pages read low-ink but are legitimate — confirm visually.
- **The gate:** zero pages under ~2% ink. Re-run after every phase.

## Locate a defect page in the source
Map a blank page back to content by reading adjacent pages' text:
```python
t = d[i].get_textpage().get_text_range()   # per-page text
```
Then find the offending element in the docx/pptx and reflow/tighten.

## Contact sheet (full page-by-page review)
```python
import pypdfium2 as pdf, math
from PIL import Image, ImageDraw
d=pdf.PdfDocument('FILE.pdf'); n=len(d)
th=[d[i].render(scale=0.2).to_pil().convert('RGB') for i in range(n)]
tw,H=th[0].size; cols=12; rows=math.ceil(n/cols)
sheet=Image.new('RGB',(cols*(tw+5)+5, rows*(H+5)+5),'white'); dr=ImageDraw.Draw(sheet)
for i,im in enumerate(th):
    r,c=divmod(i,cols); x=5+c*(tw+5); y=5+r*(H+5)
    sheet.paste(im,(x,y)); dr.text((x+2,y+2),str(i+1),fill='red')
sheet.save('contact.png')
```
Open the contact sheet and inspect fresh (a subagent works well): real visual structure, writable
areas light, nothing clipped at a boundary, footers present, no dead space.

## Content-extent measurement (for fit decisions, excluding footer)
```python
arr=np.asarray(d[i].render(scale=2.0).to_pil().convert('L')); Hh=arr.shape[0]
rows=np.where((arr[:int(Hh*0.90)]<180).any(axis=1))[0]
bottom_pct = rows.max()/Hh*100    # where body content ends, ignoring the footer band
```
Use this to decide how much to reclaim when pulling an orphan back onto its page.

## Deck validation (pptx skill)
```bash
python /root/.claude/skills/pptx/scripts/office/validate.py OUT.pptx --original SRC.pptx
```
Always pass `--original` for template-derived decks so inherited XSD quirks don't read as yours.
