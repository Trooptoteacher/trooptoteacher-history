#!/usr/bin/env python3
# Approximate page-fill estimator for docx-js workbooks (no renderer available).
# Segments the body by pageBreakBefore and estimates each segment's height in twips,
# so we can flag activities that overflow one page (bleed) vs fill cleanly.
import sys, zipfile, re

USABLE = 13100  # body height per page minus footer allowance (page 15840 - 1152 - 1152 ~= 13536, less footer)

def paras_and_tables(xml):
    # top-level block children of <w:body>: w:p and w:tbl, in order
    body = re.search(r'<w:body>(.*)</w:body>', xml, re.S).group(1)
    return re.findall(r'<w:p\b.*?</w:p>|<w:tbl>.*?</w:tbl>', body, re.S)

def sp(pr, name, default=0):
    m = re.search(rf'<w:spacing[^>]*w:{name}="(\d+)"', pr)
    return int(m.group(1)) if m else default

def max_font(block):
    szs = [int(s) for s in re.findall(r'<w:sz w:val="(\d+)"', block)]
    return max(szs) if szs else 22

def text_len(block):
    return sum(len(t) for t in re.findall(r'<w:t[^>]*>(.*?)</w:t>', block, re.S))

def para_height(p):
    pr = re.search(r'<w:pPr>(.*?)</w:pPr>', p, re.S)
    pr = pr.group(1) if pr else ''
    before, after = sp(pr,'before',0), sp(pr,'after',100)
    if '<w:pBdr>' in pr and text_len(p) <= 1:      # ruled writing line
        return before + after + 200
    hp = max_font(p) or 22
    cpl = max(20, int(9792 / (hp * 4.7)))
    lines = max(1, -(-text_len(p)//cpl))           # ceil
    lh = int(hp * 11)                              # ~line height in twips
    return before + after + lines*lh

def table_height(t):
    h = 0
    for tr in re.findall(r'<w:tr\b.*?</w:tr>', t, re.S):
        m = re.search(r'<w:trHeight w:val="(\d+)"', tr)
        trmin = int(m.group(1)) if m else 0
        # tallest cell = stacked paragraph heights
        cellmax = 0
        for tc in re.findall(r'<w:tc>.*?</w:tc>', tr, re.S):
            ch = sum(para_height(p) for p in re.findall(r'<w:p\b.*?</w:p>', tc, re.S))
            cellmax = max(cellmax, ch)
        h += max(trmin, cellmax) + 60   # cell padding
    return h

def heading_text(block):
    t = ' '.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', block, re.S))
    return re.sub(r'\s+',' ',t).strip()[:60]

xml = zipfile.ZipFile(sys.argv[1]).read('word/document.xml').decode()
blocks = paras_and_tables(xml)
segs=[]; cur={'label':'(front)','h':0}
for b in blocks:
    is_p = b.startswith('<w:p')
    if is_p and 'w:pageBreakBefore' in b:
        segs.append(cur); cur={'label':heading_text(b) or '(section)','h':0}
    cur['h'] += para_height(b) if is_p else table_height(b)
segs.append(cur)

# report activity/standard segments
print(f"{'segment':52} {'est.twips':>9} {'pages':>6} {'lastpage fill':>13}")
for s in segs:
    if s['h']<200: continue
    pages = max(1, -(-s['h']//USABLE))
    last = s['h'] - (pages-1)*USABLE
    fill = int(100*last/USABLE)
    flag = ''
    if pages>1 and fill<45: flag=' <-- BLEED (last page mostly empty)'
    print(f"{s['label'][:52]:52} {s['h']:9d} {pages:6d} {fill:11d}%{flag}")
