#!/usr/bin/env python3
"""Render a workbook docx and flag under-filled / near-blank pages (needs libreoffice-writer + poppler + pillow).
Usage: python3 check_fill.py <workbook.docx>"""
import sys, os, subprocess, glob, tempfile
from PIL import Image
docx=sys.argv[1]; d=tempfile.mkdtemp()
subprocess.run(['env','-u','JAVA_TOOL_OPTIONS',f'HOME={d}','soffice','--headless','--convert-to','pdf','--outdir',d,docx],check=True,capture_output=True)
pdf=glob.glob(os.path.join(d,'*.pdf'))[0]
subprocess.run(['pdftoppm','-png','-r','50',pdf,os.path.join(d,'p')],check=True)
files=sorted(glob.glob(os.path.join(d,'p-*.png'))); wasted=[]
for f in files:
    im=Image.open(f).convert('L'); W,H=im.size; px=im.load()
    top=int(H*0.075); foot=int(H*0.885); last=top
    for y in range(top,foot):
        c=0
        for x in range(2,W-2,2):
            if px[x,y]<200: c+=1
            if c>5: break
        if c>5: last=y
    fill=(last-top)/(foot-top); pg=int(os.path.basename(f).split('-')[1].split('.')[0])
    if fill<0.5: wasted.append((pg,round(fill*100)))
print(f"pages={len(files)}  under-half-filled={len(wasted)}: {[f'p{p}:{fl}%' for p,fl in wasted]}")
