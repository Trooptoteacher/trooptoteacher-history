#!/usr/bin/env python3
"""Batch DOCX -> PDF renderer for the Government Hack print package.

Keeps ONE soffice UNO session open and renders every deliverable docx to a PDF
sitting next to it. Captures a per-file manifest (page count, bytes, status) and
a bleed report for content documents (workbooks / assessment books / guides) so
the print-QC pass has hard data instead of guesses.

Usage: python3 batch_render.py <glob-root> <manifest.json>
"""
import sys, os, glob, json, subprocess, time, traceback
import uno
from com.sun.star.beans import PropertyValue

PORT = 2003

def url(p): return uno.systemPathToFileUrl(os.path.abspath(p))
def prop(n, v):
    pv = PropertyValue(); pv.Name = n; pv.Value = v; return pv

def start_soffice():
    env = dict(os.environ); env.pop("JAVA_TOOL_OPTIONS", None)  # hang fix
    prof = f"file:///tmp/uno_profile_{PORT}"
    subprocess.run("pkill -9 soffice 2>/dev/null", shell=True); time.sleep(1)
    subprocess.Popen(['soffice','--headless','--invisible','--norestore','--nologo',
        '--nofirststartwizard', f'-env:UserInstallation={prof}',
        f'--accept=socket,host=localhost,port={PORT};urp;StarOffice.ComponentContext'], env=env)
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
    for _ in range(90):
        try:
            ctx = resolver.resolve(f'uno:socket,host=localhost,port={PORT};urp;StarOffice.ComponentContext')
            return ctx
        except Exception: time.sleep(0.5)
    sys.exit("ERROR: could not connect to soffice UNO socket")

def pdf_page_count(pdf):
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfpage import PDFPage
    with open(pdf, 'rb') as fh:
        return sum(1 for _ in PDFPage.get_pages(fh))

def bleed_report(pdf):
    """Return (headers, bleeding_activities[]) — activities whose content spills >1 page."""
    from pdfminer.high_level import extract_pages
    from pdfminer.layout import LTTextContainer
    import re
    pages_text = []
    for layout in extract_pages(pdf):
        buf = [el.get_text() for el in layout if isinstance(el, LTTextContainer)]
        pages_text.append("".join(buf))
    n = len(pages_text)
    hdr = re.compile(r'(Activity \d+[^\n]*|Standard GC\.\d+[^\n]*)')
    seq = []
    for pi, txt in enumerate(pages_text):
        for m in hdr.finditer(txt):
            seq.append((pi, m.group(1).strip()[:60]))
    bleeds = []
    for i, (pi, h) in enumerate(seq):
        nxt = seq[i+1][0] if i+1 < len(seq) else n
        if nxt - pi > 1 and h.startswith("Activity"):
            bleeds.append({"header": h, "start_page": pi+1, "next_header_page": nxt+1})
    return len(seq), bleeds

CONTENT_MARKERS = ("Student_Workbook", "Assessment_Book", "Teacher_HowToUse", "Graphic_Organizer_Toolkit")

def main():
    root, manifest_path = sys.argv[1], sys.argv[2]
    docs = sorted(glob.glob(os.path.join(root, "**", "*.docx"), recursive=True))
    docs = [d for d in docs if "node_modules" not in d]
    ctx = start_soffice()
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
    results = []
    for i, docx in enumerate(docs, 1):
        pdf = os.path.splitext(docx)[0] + ".pdf"
        rec = {"docx": docx, "pdf": pdf}
        t0 = time.time()
        try:
            doc = desktop.loadComponentFromURL(url(docx), '_blank', 0, (prop('Hidden', True),))
            try:
                idxs = doc.getDocumentIndexes()
                for k in range(idxs.getCount()): idxs.getByIndex(k).update()
            except Exception: pass
            try: doc.refresh()
            except Exception: pass
            doc.storeToURL(url(pdf), (prop('FilterName', 'writer_pdf_Export'),))
            doc.close(False)
            rec["pages"] = pdf_page_count(pdf)
            rec["bytes"] = os.path.getsize(pdf)
            rec["status"] = "ok"
            if any(m in os.path.basename(docx) for m in CONTENT_MARKERS):
                try:
                    hdrs, bleeds = bleed_report(pdf)
                    rec["headers"] = hdrs
                    rec["bleeds"] = bleeds
                except Exception as e:
                    rec["bleed_error"] = str(e)
        except Exception as e:
            rec["status"] = "FAIL"
            rec["error"] = str(e)
            traceback.print_exc()
        rec["seconds"] = round(time.time() - t0, 1)
        results.append(rec)
        b = rec.get("bleeds", [])
        print(f"[{i}/{len(docs)}] {rec['status']:4} {os.path.basename(docx)} "
              f"-> {rec.get('pages','?')}p {rec.get('bytes',0)//1024}KB {rec['seconds']}s"
              + (f"  !!{len(b)} BLEED" if b else ""), flush=True)
        with open(manifest_path, "w") as fh:
            json.dump(results, fh, indent=2)
    try: desktop.terminate()
    except Exception: pass
    subprocess.run("pkill -9 soffice 2>/dev/null", shell=True)
    ok = sum(1 for r in results if r.get("status") == "ok")
    print(f"\nDONE: {ok}/{len(results)} rendered OK", flush=True)

if __name__ == "__main__":
    main()
