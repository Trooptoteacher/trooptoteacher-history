#!/usr/bin/env python3
"""Approximate pagination estimator for the workbook docx (no LibreOffice needed).
Walks word/document.xml top-level paragraphs + tables, estimates twip heights, segments by
Activity/section heading, and reports pages-per-section + trailing white space on the last page.
Heights are heuristic (±~15%) — use for RELATIVE bleed detection + before/after checks, not exact layout.
Usage: python3 paginate_estimate.py <workbook.docx>"""
import sys, zipfile, re, html
PAGE=15840-1152-1152     # usable height between top/bottom margins (twips)
TW=9792                  # text width
def clean(t): return html.unescape(re.sub(r'<[^>]+>','',t))

def run_text(p): return clean(''.join(re.findall(r'<w:t[ >].*?</w:t>', p, re.S)))
def sz_of(p):
    m=re.search(r'<w:sz w:val="(\d+)"', p); return int(m.group(1)) if m else 22
def para_h(p, width=TW):
    """height of a single <w:p> in twips"""
    txt=run_text(p); s=sz_of(p)
    # line height ~ pt*20*1.18 ; pt = s/2
    lh=int((s/2)*20*1.18)+6
    # chars per line at this size across width
    cpl=max(8,int(width/ (s/2*11.0)))   # ~ avg char advance ≈ pt*11 twips
    ruled = 'C9C2B4' in p
    if ruled: nlines=1
    else:
        nlines=max(1, -(-len(txt)//cpl)) if txt else 1
    # spacing before/after
    sb=int(re.search(r'w:before="(\d+)"',p).group(1)) if re.search(r'w:before="(\d+)"',p) else 0
    sa=int(re.search(r'w:after="(\d+)"',p).group(1)) if re.search(r'w:after="(\d+)"',p) else 100
    base = nlines*lh + sb + sa
    if ruled: base = lh + sb + sa   # ruled line ~ one line + its spacing
    return base

def cell_h(tc):
    ps=re.findall(r'<w:p[ >].*?</w:p>', tc, re.S)
    w=int(re.search(r'<w:tcW w:type="dxa" w:w="(\d+)"',tc).group(1)) if re.search(r'<w:tcW',tc) else TW
    h=sum(para_h(p,max(400,w-220)) for p in ps) if ps else 220
    return h+130   # cell top/bottom margins

def row_h(tr):
    cells=re.findall(r'<w:tc>.*?</w:tc>', tr, re.S)
    ch=max([cell_h(c) for c in cells], default=240)
    m=re.search(r'<w:trHeight w:val="(\d+)"', tr)
    atleast=int(m.group(1)) if m and 'atLeast' in tr else 0
    return max(ch, atleast)

def tbl_h(t): return sum(row_h(tr) for tr in re.findall(r'<w:tr>.*?</w:tr>', t, re.S))+40

def main(path):
    x=zipfile.ZipFile(path).read('word/document.xml').decode('utf-8','ignore')
    body=re.search(r'<w:body>(.*)</w:body>', x, re.S).group(1)
    # sequence of top-level blocks (p or tbl) in order
    blocks=re.findall(r'(<w:p[ >].*?</w:p>|<w:tbl>.*?</w:tbl>)', body, re.S)
    segs=[]; cur={"name":"(front matter)","page":1,"used":0,"pages":1}
    page_used=0; page=1
    def newseg(name):
        nonlocal cur; segs.append(cur); cur={"name":name,"start_page":page,"used":0,"pages":1,"trailing":0}
    def brk():
        nonlocal page,page_used; page+=1; page_used=0; cur["pages"]=cur.get("pages",1)+1
    cur={"name":"(opening)","start_page":1,"used":0,"pages":1}
    for b in blocks:
        is_tbl=b.startswith('<w:tbl')
        pbb = (not is_tbl) and 'w:pageBreakBefore' in b
        pagebr = '<w:br w:type="page"' in b or 'w:type="page"' in b
        head = None
        if not is_tbl and ('w:pStyle w:val="Heading' in b):
            ht=run_text(b)
            if re.match(r'(Standard |Activity |Cornell Notes|Guided Support|Light Support|Geographer)', ht):
                head=ht[:60]
        if pbb or head:
            # start a new page + possibly new segment
            if head:
                segs.append(cur); cur={"name":head,"start_page":page+1 if page_used>0 else page,"used":0,"pages":1}
            if page_used>0: brk()
        h = tbl_h(b) if is_tbl else para_h(b)
        # place on page(s)
        if page_used + h > PAGE:
            # overflow to next page(s)
            remain = PAGE - page_used
            over = h - remain
            brk()
            while over > PAGE:
                brk(); over-=PAGE
            page_used = over
        else:
            page_used += h
        cur["used"]=cur.get("used",0)+h
        cur["end_page"]=page
    segs.append(cur)
    # report
    print(f"{'SECTION':42} {'pages':>5} {'fill last pg':>12}")
    print("-"*64)
    for s in segs:
        if s['name'].startswith('(') and s.get('used',0)==0: continue
        pages=max(1, -(-s.get('used',0)//PAGE))
        last_fill = s.get('used',0) - (pages-1)*PAGE
        pct=int(100*last_fill/PAGE)
        flag = '  <-- BLEEDS (2nd pg nearly empty)' if pages>=2 and pct<45 else ('  <-- tight' if pages==1 and pct>92 else '')
        print(f"{s['name'][:42]:42} {pages:>5} {pct:>10}%{flag}")

if __name__=='__main__':
    main(sys.argv[1])
