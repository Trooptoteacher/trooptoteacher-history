#!/usr/bin/env python3
"""Render a DOCX -> PDF via the LibreOffice python-UNO bridge, updating the TOC/indexes first.
Robust in this container: launches soffice with JAVA_TOOL_OPTIONS UNSET (the proxy JVM options make
headless soffice hang), a private profile, and a socket bridge. This is the reliable PDF path the
platinum system expects (soffice --convert-to CLI hangs here).

Usage:  python3 render_pdf.py <in.docx> <out.pdf> [--pages]
        --pages also prints a pagination report (page count + which page each 'Activity'/'Standard'
        header lands on) so print-preflight can flag activities that bleed across pages.
"""
import sys, os, subprocess, time, argparse
import uno
from com.sun.star.beans import PropertyValue

def url(p): return uno.systemPathToFileUrl(os.path.abspath(p))
def prop(n, v):
    pv = PropertyValue(); pv.Name = n; pv.Value = v; return pv

def render(inp, outp, port=2003):
    env = dict(os.environ); env.pop("JAVA_TOOL_OPTIONS", None)  # <-- the hang fix
    prof = f"file:///tmp/uno_profile_{port}"
    subprocess.run("pkill -9 soffice 2>/dev/null", shell=True); time.sleep(1)
    subprocess.Popen(['soffice','--headless','--invisible','--norestore','--nologo','--nofirststartwizard',
        f'-env:UserInstallation={prof}',
        f'--accept=socket,host=localhost,port={port};urp;StarOffice.ComponentContext'], env=env)
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
    ctx = None
    for _ in range(60):
        try:
            ctx = resolver.resolve(f'uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext'); break
        except Exception: time.sleep(0.5)
    if ctx is None: sys.exit("ERROR: could not connect to soffice UNO socket")
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
    doc = desktop.loadComponentFromURL(url(inp), '_blank', 0, (prop('Hidden', True),))
    try:
        idxs = doc.getDocumentIndexes()
        for i in range(idxs.getCount()): idxs.getByIndex(i).update()
    except Exception as e: print("index update warn:", e)
    try: doc.refresh()
    except Exception as e: print("refresh warn:", e)
    doc.storeToURL(url(outp), (prop('FilterName', 'writer_pdf_Export'),))
    doc.close(False)
    try: desktop.terminate()
    except Exception: pass
    subprocess.run("pkill -9 soffice 2>/dev/null", shell=True)
    print("rendered", outp)

def pagination_report(pdf):
    """Print page count and the page each Activity/Standard header lands on; flag activities that
    span more than one page (bleed)."""
    from pdfminer.high_level import extract_pages
    from pdfminer.layout import LTTextContainer
    import re
    pages_text = []
    for layout in extract_pages(pdf):
        buf = []
        for el in layout:
            if isinstance(el, LTTextContainer): buf.append(el.get_text())
        pages_text.append("".join(buf))
    n = len(pages_text)
    print(f"PAGES: {n}")
    # locate headers and their start page
    hdr = re.compile(r'(Activity \d+ —[^\n]*|Standard GC\.\d+ —[^\n]*)')
    seq = []  # (page_index, header)
    for pi, txt in enumerate(pages_text):
        for m in hdr.finditer(txt):
            seq.append((pi, m.group(1).strip()[:60]))
    # an activity "bleeds" if the next header starts >1 page later (content spilled)
    bleeds = []
    for i, (pi, h) in enumerate(seq):
        nxt = seq[i+1][0] if i+1 < len(seq) else n
        if nxt - pi > 1 and h.startswith("Activity"):
            bleeds.append((h, pi+1, nxt+1))
    print(f"HEADERS: {len(seq)}  BLEEDING ACTIVITIES (span >1 page): {len(bleeds)}")
    for h, p0, p1 in bleeds:
        print(f"   BLEED: '{h}' starts p{p0}, next header p{p1}")
    if not bleeds: print("   ✓ no activity spans more than one page")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("inp"); ap.add_argument("outp"); ap.add_argument("--pages", action="store_true")
    a = ap.parse_args()
    render(a.inp, a.outp)
    if a.pages: pagination_report(a.outp)
