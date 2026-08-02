# Workbook docx methods (python-docx / OOXML)

The workbook is edited as OOXML via `python-docx`. Standards/activities are found by paragraph
text; boxes are single-row shaded tables; writing lines are empty paragraphs with a bottom border.

## Finding structure
```python
from docx import Document
from docx.oxml.ns import qn
doc=Document('workbook.docx'); body=doc.element.body
def ptext(el): return ''.join(n.text or '' for n in el.iter(qn('w:t'))).strip()
def has_pbb(p):
    ppr=p.find(qn('w:pPr')); return ppr is not None and ppr.find(qn('w:pageBreakBefore')) is not None
```
- Standard region: paragraphs whose text starts with `Standard US.xx` … up to the next one.
- Activity headers: text starts with `Activity N —`. Each activity begins with `pageBreakBefore`,
  so a section is the span between two PBB markers — **shrinking inside a section can't create a new
  spill elsewhere.**
- A "box" is a `w:tbl` whose first cell text is the label (e.g., `HOOK — …`, `SET YOUR GOAL`).
- A "writing line" is a `w:p` with a `w:pBdr/w:bottom` and no text.

## Writing-line paragraph (house style)
```python
def wline(color='9AA0AB', h=460):   # h = exact line height in twips
    p=OxmlElement('w:p'); pPr=OxmlElement('w:pPr'); sp=OxmlElement('w:spacing')
    for k,v in (('w:before','0'),('w:after','0'),('w:line',str(h)),('w:lineRule','exact')): sp.set(qn(k),v)
    pPr.append(sp); b=OxmlElement('w:pBdr'); bot=OxmlElement('w:bottom')
    for k,v in (('w:val','single'),('w:sz','8'),('w:space','1'),('w:color',color)): bot.set(qn(k),v)
    b.append(bot); pPr.append(b); p.append(pPr); return p
```

## Reclaiming vertical space (to kill orphan pages)
- Convert empty `w:br`-page-break carrier paragraphs → `pageBreakBefore` on the next heading, then
  delete the carrier.
- Remove on-page writing lines from **notebook-redirect** boxes (HOOK, ACTIVATE, MAKE IT YOURS).
- Reduce writing-line `w:line` on rating grids / HIPPO cells (255 auto → ~200 exact). Cells that
  only need a mark (knowledge-rating) don't need full-height lines.
- Reduce word-bank cell line spacing (~216 auto) for verbose definitions.
- Shrink an oversized inline image: scale **both** `wp:extent` and the `a:ext` in `a:xfrm`
  (LibreOffice lays out from `wp:extent`; scaling only `a:ext` does nothing visible).

## Cloning a reference block and editing runs (for back-page supports)
Deep-copy the reference elements (preserves all formatting), then edit text. **Never collapse a
multi-run paragraph into one run** — that loses inline bold (e.g., the `H:`/`Claim:` labels).
Rebuild model paragraphs as alternating bold-label + regular-body runs:
```python
import copy
def rebuild_model(p, segments):        # segments = [("H: ", "body…"), ...]
    runs=p.findall(qn('w:r')); base=runs[0].find(qn('w:rPr')) if runs else None
    for r in runs: p.remove(r)
    for label, bodytext in segments:
        for text,bold in ((label,True),(bodytext,False)):
            r=p.makeelement(qn('w:r'),{}); rp=copy.deepcopy(base) if base is not None else p.makeelement(qn('w:rPr'),{})
            b=rp.find(qn('w:b'))
            if bold and b is None: rp.append(p.makeelement(qn('w:b'),{}))
            if not bold and b is not None: rp.remove(b)
            r.append(rp); t=p.makeelement(qn('w:t'),{}); t.set(qn('xml:space'),'preserve'); t.text=text; r.append(t); p.append(r)
```

## Inserting a cloned block at an anchor
Capture the anchor **element** (not an index) before inserting. Two equivalent idioms:
- `anchor.addnext(el)` in **reverse** order (each new el goes right after the anchor), or
- `anchor.addprevious(el)` in **forward** order (each new el goes right before the anchor) — this
  is what `clone_notes_supports` uses to drop a whole cloned page in reading order before the next
  Activity header.

Indices shift after inserts; element refs don't.

## Notebook paper (multi-line ruled writing area) — use a TABLE, not stacked paragraphs
Stacked empty paragraphs that each carry only a `w:bottom` border **collapse**: Word/LibreOffice
merge adjacent identical paragraph borders and render **one** rule (a single line above the next
block) instead of N ruled lines. Build ruled notebook paper as a **borderless table whose rows
each carry a bottom border** — row/cell borders never collapse. Also give each paragraph **exactly
one** `w:spacing` element: setting `space_before/after` via python-docx *and* appending your own
`w:spacing` creates two siblings and the exact line height is silently dropped. See
`notebook_table()` in `scripts/build_guided_notes.py` (5 rows, `trHeight` 460 exact, cell
`w:bottom single sz 8 color 9AA0AB`). A single isolated ruled line at body level is fine as a
bordered paragraph; two or more adjacent ones must be a table.

## Guided Cornell cue seeding
Activity 3's cue column ships empty (or with stale auto-questions). Seed it with the standard's
direct-instruction segments in lecture order — navy topic / gold `▶ Deck · DI N of M` / italic
guiding question — via `seed_guided_cornell()`. See `references/guided-notes-and-supports.md`.

## Working scripts
- `scripts/build_backpage_supports.py` — VOCAB/HIPPO/WRITING back-page supports, exit-ticket
  consolidation, per-standard model content.
- `scripts/build_guided_notes.py` — guided Cornell cue seeding + the NOTES SUPPORTS ladder
  (frames → cloze → how-to → try-it notebook lines + self-check); clones the US.45 reference for
  formatting parity.
