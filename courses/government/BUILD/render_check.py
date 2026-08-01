#!/usr/bin/env python3
"""Render a workbook docx to PDF (Spire.Doc) + PNGs (PyMuPDF) and report per-page fill,
so layout/bleed can be VISUALLY verified in this sandbox (LibreOffice's Word filter is broken).
Deps: pip install spire.doc PyMuPDF pikepdf.  Usage: python3 render_check.py <in.docx> [outdir]
Note: Spire free renders the first ~10 pages with a watermark — build SAMPLE=N docs to inspect later pages."""
import sys, os
from spire.doc import Document, FileFormat
import fitz
inp=sys.argv[1]; out=sys.argv[2] if len(sys.argv)>2 else "/tmp/render_check"
os.makedirs(out, exist_ok=True)
pdf=os.path.join(out,"doc.pdf")
d=Document(); d.LoadFromFile(inp); d.SaveToFile(pdf, FileFormat.PDF); d.Close()
doc=fitz.open(pdf)
for i,p in enumerate(doc):
    words=p.get_text('words'); maxy=max((w[3] for w in words), default=0)
    h=p.rect.height; fill=int(100*maxy/h)
    t=p.get_text().strip().splitlines(); head=(t[0][:55] if t else '(blank)')
    p.get_pixmap(dpi=100).save(os.path.join(out,f"pg{i+1:02d}.png"))
    print(f"pg{i+1:2d}: fill={fill:3d}%  {head}")
