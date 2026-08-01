#!/usr/bin/env python3
# QC render helper: for a unit, render (a) the FIRST standard in full (architecture check),
# (b) the FULLEST close-read standard from Activity 4 onward (bleed check for A4-A7),
# (c) the LAST standard from Activity 4 onward (CER-back / back-matter check).
# Usage: python3 qc_render.py <unitN> <outdir>
import sys, os, subprocess, json, re, shutil
BUILD=os.path.dirname(os.path.abspath(__file__))
unit=sys.argv[1]                       # e.g. "unit7"
outdir=sys.argv[2]
os.makedirs(outdir, exist_ok=True)
udir=os.path.join(BUILD,unit)
c=json.load(open(os.path.join(udir,f"analysis/{unit}_content.json")))
order=c['order']; stds=c['standards']
def clen(code):
    a=stds[code].get('auth',{}) or {}
    return len((a.get('close') or '')) + sum(len(q) for q in (a.get('tdq') or []))
first=order[0]; last=order[-1]; fullest=max(order,key=clen)
env=dict(os.environ, NODE_PATH="../unit1/node_modules")

def build(script, code):
    e=dict(env, ONLYSTD=code)
    r=subprocess.run(["node",script], cwd=udir, env=e, capture_output=True, text=True)
    if r.returncode!=0:
        print("BUILD FAIL", script, code, r.stderr[-400:]); return None
    return os.path.join(udir,"deliverables",f"{unit.capitalize()}_PREVIEW_{code}.docx")

def render(docx, tag):
    if not docx or not os.path.exists(docx): print("NO DOCX", tag); return
    d=os.path.join(outdir,tag); os.makedirs(d, exist_ok=True)
    r=subprocess.run(["python3","render_check.py",docx,d], cwd=BUILD, capture_output=True, text=True)
    print(f"--- {tag} ({os.path.basename(docx)}) ---")
    print(r.stdout.strip() or r.stderr[-300:])

# (a) first standard, full
render(build("build_workbook.js", first), f"first_{first}")

# deep slice: start block() at Activity 4 so A4..A7 land on early pages
src=open(os.path.join(udir,"build_workbook.js")).read()
i=src.index("  out.push(H(`Standard ${code}")
j=src.index("  // Activity 4 — Close Read")
tmp=src[:i]+"  out.push(H(`Standard ${code} — ${s.title}`,1,{brk:true}));\n"+src[j:]
open(os.path.join(udir,"build_workbook_TMP.js"),"w").write(tmp)
render(build("build_workbook_TMP.js", fullest), f"fullest_{fullest}_A4on")
if last!=fullest:
    render(build("build_workbook_TMP.js", last), f"last_{last}_A4on")
os.remove(os.path.join(udir,"build_workbook_TMP.js"))
# clean preview docx so we don't commit them
for f in os.listdir(os.path.join(udir,"deliverables")):
    if "PREVIEW" in f: os.remove(os.path.join(udir,"deliverables",f))
print(f"\nCHOSEN {unit}: first={first} fullest_closeread={fullest} last={last}")
print(f"PNGs under: {outdir}/(first_*|fullest_*|last_*)/pgNN.png")
