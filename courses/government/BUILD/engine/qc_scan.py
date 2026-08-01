#!/usr/bin/env python3
"""Print-QC scanner for the Government Hack package.

Scans every PDF deliverable and reports, per file: page count, file size, and —
for content documents (workbooks, assessment books, teacher guides, organizer
toolkits) — activities that BLEED across a page boundary (a real classroom
copy-defect: an organizer that spills onto a second, nearly-empty page wastes
paper and confuses students). Also flags the 4 known primary-source images that
need >10MB re-export or are on a placeholder. Emits JSON + a human summary.
"""
import os, sys, json, re, glob
from pdfminer.pdfpage import PDFPage
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTImage, LTFigure

ROOT = "/home/user/trooptoteacher-history/courses/foundations-constitutional-government"
CONTENT = ("Student_Workbook", "Assessment_Book", "Teacher_HowToUse",
           "Graphic_Organizer_Toolkit", "graphic-organizers")
FLAGGED_IMAGES = {  # from MASTER_DELIVERABLES_INDEX.md §4
    "GC.04_looking-glass-1787": ">10MB re-export pending",
    "GC.32_nast-third-term-panic": ">10MB re-export pending",
    "GC.33_yellow-press-cartoon": ">10MB re-export pending",
    "GC.28_tennessee-state-capitol": "corrupt in transit; on placeholder",
}

def page_count(pdf):
    with open(pdf, "rb") as fh:
        return sum(1 for _ in PDFPage.get_pages(fh))

def bleed_scan(pdf):
    pages = []
    for layout in extract_pages(pdf):
        txt = "".join(el.get_text() for el in layout if isinstance(el, LTTextContainer))
        pages.append(txt)
    n = len(pages)
    hdr = re.compile(r'(Activity\s+\d+[^\n]{0,55}|Standard\s+GC\.\d+[^\n]{0,55})')
    seq = []
    for pi, txt in enumerate(pages):
        for m in hdr.finditer(txt):
            seq.append((pi, re.sub(r'\s+', ' ', m.group(1)).strip()))
    bleeds = []
    for i, (pi, h) in enumerate(seq):
        nxt = seq[i+1][0] if i+1 < len(seq) else n
        if nxt - pi > 1 and h.startswith("Activity"):
            bleeds.append({"header": h, "start_page": pi+1, "next_header_page": nxt+1})
    # near-empty trailing page: last page with <120 chars of text = likely a widow/orphan page
    tail_light = len(pages[-1].strip()) < 120 if pages else False
    return {"pages": n, "headers": len(seq), "bleeds": bleeds, "last_page_sparse": tail_light}

def main():
    out = sys.argv[1]
    pdfs = sorted(p for p in glob.glob(f"{ROOT}/**/*.pdf", recursive=True)
                  if "node_modules" not in p)
    results = []
    for pdf in pdfs:
        rec = {"pdf": os.path.relpath(pdf, ROOT), "bytes": os.path.getsize(pdf)}
        try:
            base = os.path.basename(pdf)
            if any(m in base for m in CONTENT):
                rec.update(bleed_scan(pdf))
            else:
                rec["pages"] = page_count(pdf)
            rec["status"] = "ok"
        except Exception as e:
            rec["status"] = "ERROR"; rec["error"] = str(e)
        results.append(rec)

    # flagged image check
    img_report = []
    for stem, note in FLAGGED_IMAGES.items():
        hits = glob.glob(f"{ROOT}/**/{stem}.*", recursive=True)
        for h in hits:
            img_report.append({"image": os.path.relpath(h, ROOT),
                               "bytes": os.path.getsize(h), "note": note})
        if not hits:
            img_report.append({"image": stem, "bytes": 0, "note": note + " (NOT FOUND)"})

    manifest = {"pdfs": results, "flagged_images": img_report}
    with open(out, "w") as fh:
        json.dump(manifest, fh, indent=2)

    # summary
    ok = [r for r in results if r["status"] == "ok"]
    err = [r for r in results if r["status"] != "ok"]
    bleeders = [r for r in ok if r.get("bleeds")]
    sparse = [r for r in ok if r.get("last_page_sparse")]
    print(f"PDFs scanned: {len(results)}  ok={len(ok)}  errors={len(err)}")
    print(f"total size: {sum(r['bytes'] for r in results)/1e6:.1f} MB")
    print(f"content docs with BLEEDING activities: {len(bleeders)}")
    for r in bleeders:
        print(f"  {r['pdf']}  ({len(r['bleeds'])} bleed)")
        for b in r["bleeds"][:6]:
            print(f"     - {b['header']}  p{b['start_page']}->{b['next_header_page']}")
    print(f"docs with sparse last page (possible widow page): {len(sparse)}")
    for r in sparse:
        print(f"  {r['pdf']}  ({r['pages']}p)")
    if err:
        print("ERRORS:")
        for r in err: print(f"  {r['pdf']}: {r.get('error')}")
    print("FLAGGED IMAGES:")
    for i in img_report:
        print(f"  {i['image']}  {i['bytes']//1024}KB — {i['note']}")

if __name__ == "__main__":
    main()
