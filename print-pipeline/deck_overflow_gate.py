#!/usr/bin/env python3
"""
Deck visual-overflow gate (geometry proxy).

The pixel-render gate (soffice -> PDF -> images) is the gold standard, but when
no working LibreOffice is available this estimates text overflow straight off
the OOXML: for every text shape, compare the box (a:ext, minus a:bodyPr insets)
to an estimate of the rendered text extent (per-run font size x char count,
wrapped to the box width, x line height). Decks here use NO autofit, so text
that exceeds its box is a real clip on screen.

Heuristic, deliberately conservative to avoid false alarms:
  char width  = 0.50 em    line height = 1.22 x font size
  WARN   when estimated text height / available height  > 1.10
  CLIP   (likely visible overflow)                      > 1.25
Also flags a single unbreakable run wider than the box (horizontal clip).
"""
import sys, zipfile, math, re
import xml.etree.ElementTree as ET

EMU_IN = 914400
EMU_PT = 12700
NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}
CHAR_W = 0.50      # avg glyph advance as fraction of em
LINE_H = 1.22      # line box as multiple of font size
WARN, CLIP = 1.10, 1.25
DEFAULT_SZ = 1800  # hundredths pt, used only if a run/para has no sz

def _ins(bodyPr, attr, default):
    if bodyPr is None: return default
    v = bodyPr.get(attr)
    return int(v) if v is not None else default

def shape_overflow(sp):
    """Return (ratio, box_wh_in, worst_kind, text_snip) or None if no text."""
    xfrm = sp.find("p:spPr/a:xfrm", NS)
    ext = xfrm.find("a:ext", NS) if xfrm is not None else None
    tx = sp.find("p:txBody", NS)
    if ext is None or tx is None:
        return None
    W, H = int(ext.get("cx")), int(ext.get("cy"))
    if W <= 0 or H <= 0:
        return None
    bodyPr = tx.find("a:bodyPr", NS)
    if bodyPr is not None and bodyPr.get("wrap") == "none":
        wrap = False
    else:
        wrap = True
    lIns = _ins(bodyPr, "lIns", 91440); rIns = _ins(bodyPr, "rIns", 91440)
    tIns = _ins(bodyPr, "tIns", 45720); bIns = _ins(bodyPr, "bIns", 45720)
    availW = max(1, W - lIns - rIns)
    availH = max(1, H - tIns - bIns)

    total_h = 0.0
    all_text = []
    worst_w_run = 0
    paras = tx.findall("a:p", NS)
    if not paras:
        return None
    for p in paras:
        runs = p.findall("a:r", NS)
        # paragraph default size from pPr/defRPr or endParaRPr
        pPr = p.find("a:pPr", NS)
        def_sz = None
        if pPr is not None:
            d = pPr.find("a:defRPr", NS)
            if d is not None and d.get("sz"): def_sz = int(d.get("sz"))
        para_text = ""
        line_max_sz = def_sz or 0
        width_emu = 0.0
        for r in runs:
            rPr = r.find("a:rPr", NS)
            sz = int(rPr.get("sz")) if (rPr is not None and rPr.get("sz")) else (def_sz or DEFAULT_SZ)
            bold = rPr is not None and rPr.get("b") == "1"
            t = r.find("a:t", NS)
            s = t.text or "" if t is not None else ""
            para_text += s
            line_max_sz = max(line_max_sz, sz)
            cw = CHAR_W * (1.06 if bold else 1.0) * (sz/100.0) * EMU_PT
            width_emu += len(s) * cw
            # longest unbreakable token (for horizontal clip when wrap off / one long word)
            for tok in re.split(r"\s+", s):
                worst_w_run = max(worst_w_run, len(tok) * cw)
        if line_max_sz == 0:
            line_max_sz = DEFAULT_SZ
        if wrap:
            lines = max(1, math.ceil(width_emu / availW)) if para_text.strip() else 1
        else:
            lines = 1
        line_box = (line_max_sz/100.0) * LINE_H * EMU_PT
        # paragraph spacing before/after (spcPts val is hundredths pt)
        spc = 0
        if pPr is not None:
            for tag in ("a:spcBef", "a:spcAft"):
                node = pPr.find(f"{tag}/a:spcPts", NS)
                if node is not None and node.get("val"):
                    spc += int(node.get("val"))/100.0 * EMU_PT
        total_h += lines * line_box + spc
        if para_text.strip():
            all_text.append(para_text.strip())

    if not all_text:            # decorative/empty shape — nothing can visibly clip
        return None
    ratio_v = total_h / availH
    kind = None
    if ratio_v > WARN:
        kind = "V-CLIP" if ratio_v > CLIP else "V-warn"
    ratio = ratio_v
    if worst_w_run > availW * 1.02:  # a token wider than the box
        rw = worst_w_run / availW
        if rw > ratio:
            ratio = rw; kind = "H-CLIP" if rw > CLIP else "H-warn"
    if kind is None:
        return None
    snip = (" / ".join(all_text))[:70]
    return (ratio, (W/EMU_IN, H/EMU_IN), kind, snip)

def analyze(path):
    z = zipfile.ZipFile(path)
    slides = sorted([n for n in z.namelist()
                     if re.match(r"ppt/slides/slide\d+\.xml$", n)],
                    key=lambda n: int(re.search(r"(\d+)", n).group()))
    findings = []
    for n in slides:
        idx = int(re.search(r"slide(\d+)\.xml", n).group(1))
        root = ET.fromstring(z.read(n))
        for sp in root.iter("{%s}sp" % NS["p"]):
            r = shape_overflow(sp)
            if r:
                findings.append((idx, *r))
    return len(slides), findings

def main():
    for path in sys.argv[1:]:
        nslides, f = analyze(path)
        clips = [x for x in f if "CLIP" in x[3]]
        warns = [x for x in f if "warn" in x[3]]
        print("=" * 78)
        print(f"{path}")
        print(f"  slides: {nslides}   CLIP (likely visible overflow): {len(clips)}"
              f"   warn (borderline): {len(warns)}")
        for idx, ratio, (w, h), kind, snip in sorted(f, key=lambda x: -x[1]):
            print(f"   slide {idx:>3}  {kind:<7} est {ratio*100:4.0f}% of box "
                  f"({w:.1f}x{h:.1f}in)  “{snip}”")
        print(f"  GATE: {'FAIL' if clips else 'PASS (no likely clips)'}"
              f"  ({len(warns)} borderline to eyeball)")

if __name__ == "__main__":
    main()
