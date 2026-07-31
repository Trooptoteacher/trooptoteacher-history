#!/usr/bin/env python3
"""Corrected print-QC scan.

Per page: text length + whether it carries an image. Flags what is actually a
classroom copy-defect:
  * BLANK INTERIOR PAGE — an interior page with ~no text and no image (wastes a
    sheet, confuses collation). Multi-page activities are NOT flagged; only truly
    empty pages are.
  * COVER PAGE COUNT — covers should be 1 (or 2) pages.
Reports total page count per deliverable. Emits JSON + summary.
"""
import os, sys, json, glob
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTImage, LTFigure

ROOT = "/home/user/trooptoteacher-history/courses/foundations-constitutional-government"

def page_profiles(pdf):
    profs = []
    for layout in extract_pages(pdf):
        text = "".join(el.get_text() for el in layout if isinstance(el, LTTextContainer))
        has_img = False
        stack = list(layout)
        while stack:
            el = stack.pop()
            if isinstance(el, LTImage): has_img = True; break
            if isinstance(el, LTFigure): stack.extend(list(el))
        profs.append((len((text or "").strip()), has_img))
    return profs

def main():
    out = sys.argv[1]
    pdfs = sorted(p for p in glob.glob(f"{ROOT}/**/*.pdf", recursive=True) if "node_modules" not in p)
    results = []
    for pdf in pdfs:
        rel = os.path.relpath(pdf, ROOT)
        rec = {"pdf": rel, "bytes": os.path.getsize(pdf)}
        try:
            profs = page_profiles(pdf)
            n = len(profs)
            rec["pages"] = n
            blanks = [i+1 for i,(t,img) in enumerate(profs)
                      if 0 < i < n-1 and t < 30 and not img]   # interior only
            rec["blank_interior_pages"] = blanks
            results.append(rec); rec["status"]="ok"
        except Exception as e:
            rec["status"]="ERROR"; rec["error"]=str(e); results.append(rec)
    with open(out,"w") as fh: json.dump(results, fh, indent=2)

    ok=[r for r in results if r["status"]=="ok"]
    blankers=[r for r in ok if r.get("blank_interior_pages")]
    covers=[r for r in ok if "Cover" in os.path.basename(r["pdf"])]
    bigcovers=[r for r in covers if r["pages"]>2]
    print(f"PDFs: {len(results)}  ok={len(ok)}  total={sum(r['bytes'] for r in results)/1e6:.1f}MB")
    print(f"\nBLANK INTERIOR PAGES (real defect): {len(blankers)} files")
    for r in blankers:
        print(f"  {r['pdf']}  pages={r['pages']}  blank={r['blank_interior_pages']}")
    print(f"\nCOVERS >2 pages (check): {len(bigcovers)}")
    for r in bigcovers: print(f"  {r['pdf']}  pages={r['pages']}")
    print(f"\nPAGE COUNTS (workbooks & books):")
    for r in ok:
        b=os.path.basename(r['pdf'])
        if any(k in b for k in ("Student_Workbook","Assessment_Book","Teacher_HowToUse","Organizer_Toolkit","graphic-organizers")):
            print(f"  {r['pages']:>3}p  {r['pdf']}")

if __name__=="__main__": main()
