#!/usr/bin/env python3
"""
Faithful pptx -> HTML -> (WeasyPrint) PDF renderer, for the visual overflow gate
when no working LibreOffice is available.

Rebuilds each slide as an EMU-exact HTML page: every shape an absolutely
positioned box at its true size, with real fills, borders, fonts (Calibri ->
Carlito, metric-identical), font sizes, alignment, bodyPr insets, and embedded
pictures. WeasyPrint lays out text with real Pango/HarfBuzz metrics, so text
that overflows its box overflows visibly in the render — the exact thing gate 3
looks for. Text boxes are drawn with a faint frame and any overflow is tinted,
so clips are obvious on inspection.

Usage: deck_render_weasy.py deck.pptx out.pdf [slideNum ...]
"""
import sys, zipfile, re, base64, math
import xml.etree.ElementTree as ET
from weasyprint import HTML

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"a": A, "p": P, "r": R}
EMU_PX = 9525.0           # EMU per CSS px at 96dpi
PGW, PGH = 12191695, 6858000

FONT_MAP = {
    "Calibri": "Carlito", "Calibri Light": "Carlito", "Calibri Body": "Carlito",
    "Georgia": "Liberation Serif", "Times New Roman": "Liberation Serif",
    "Trebuchet MS": "DejaVu Sans", "Arial": "Liberation Sans",
}
def font_css(name):
    return FONT_MAP.get(name, "Carlito")

def px(emu): return f"{float(emu)/EMU_PX:.2f}"

def esc(s):
    return (s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))

class Deck:
    def __init__(self, path):
        self.z = zipfile.ZipFile(path)
        self.theme = self._scheme()
    def _scheme(self):
        m = {}
        try:
            t = ET.fromstring(self.z.read("ppt/theme/theme1.xml"))
            cs = t.find(".//a:clrScheme", NS)
            for c in cs:
                tag = c.tag.split("}")[1]
                srgb = c.find("a:srgbClr", NS); sysc = c.find("a:sysClr", NS)
                if srgb is not None: m[tag] = srgb.get("val")
                elif sysc is not None: m[tag] = sysc.get("lastClr", "000000")
        except Exception: pass
        return m
    def rels(self, slide_name):
        rp = f"ppt/slides/_rels/{slide_name.split('/')[-1]}.rels"
        d = {}
        try:
            r = ET.fromstring(self.z.read(rp))
            for rel in r:
                d[rel.get("Id")] = rel.get("Target")
        except Exception: pass
        return d

    def color(self, node):
        """node = a fill/color parent; return #hex or None."""
        if node is None: return None
        s = node.find("a:solidFill", NS)
        if s is None: return None
        srgb = s.find("a:srgbClr", NS)
        if srgb is not None: return "#" + srgb.get("val")
        sc = s.find("a:schemeClr", NS)
        if sc is not None:
            key = sc.get("val")
            key = {"bg1":"lt1","tx1":"dk1","bg2":"lt2","tx2":"dk2"}.get(key, key)
            v = self.theme.get(key)
            if v: return "#" + v
        return None

    def emu_box(self, sp):
        xf = sp.find("p:spPr/a:xfrm", NS) or sp.find("p:grpSpPr/a:xfrm", NS)
        if xf is None: return None
        off = xf.find("a:off", NS); ext = xf.find("a:ext", NS)
        if off is None or ext is None: return None
        return (int(off.get("x")), int(off.get("y")),
                int(ext.get("cx")), int(ext.get("cy")))

    def render_sp(self, sp, out):
        box = self.emu_box(sp)
        if box is None: return
        x, y, w, h = box
        if w <= 0 or h <= 0: return
        spPr = sp.find("p:spPr", NS)
        fill = self.color(spPr)
        # border
        bd = ""
        ln = spPr.find("a:ln", NS) if spPr is not None else None
        if ln is not None:
            lc = self.color(ln)
            lw = ln.get("w")
            if lc: bd = f"border:{max(1,int(lw or 9525)/EMU_PX):.0f}px solid {lc};"
        tx = sp.find("p:txBody", NS)
        style = (f"position:absolute;left:{px(x)}px;top:{px(y)}px;"
                 f"width:{px(w)}px;height:{px(h)}px;"
                 f"{'background:'+fill+';' if fill else ''}{bd}"
                 "box-sizing:border-box;")
        if tx is None:
            out.append(f'<div style="{style}"></div>'); return
        bp = tx.find("a:bodyPr", NS)
        def ins(a, d): return (int(bp.get(a)) if (bp is not None and bp.get(a)) else d)
        pl, pt = ins("lIns", 91440), ins("tIns", 45720)
        pr, pb = ins("rIns", 91440), ins("bIns", 45720)
        anchor = (bp.get("anchor") if bp is not None else None) or "t"
        just = {"t":"flex-start","ctr":"center","b":"flex-end"}.get(anchor,"flex-start")
        # a text frame: faint outline + overflow tint so clips are visible
        style += ("outline:0.6px dashed rgba(120,120,120,.45);"
                  "display:flex;flex-direction:column;"
                  f"justify-content:{just};"
                  f"padding:{px(pt)}px {px(pr)}px {px(pb)}px {px(pl)}px;")
        # overflow container: we DON'T clip, so spillover shows; mark it
        inner = []
        for para in tx.findall("a:p", NS):
            pPr = para.find("a:pPr", NS)
            algn = {"ctr":"center","r":"right","just":"justify","l":"left"}.get(
                pPr.get("algn") if pPr is not None else None, "left")
            runs_html = []
            para_txt = ""
            for run in para.findall("a:r", NS):
                rPr = run.find("a:rPr", NS)
                t = run.find("a:t", NS)
                s = (t.text or "") if t is not None else ""
                para_txt += s
                sz = 18.0
                fam = "Carlito"; b = False; i = False; col = "#111111"
                if rPr is not None:
                    if rPr.get("sz"): sz = int(rPr.get("sz"))/100.0
                    b = rPr.get("b") == "1"; i = rPr.get("i") == "1"
                    lat = rPr.find("a:latin", NS)
                    if lat is not None and lat.get("typeface"):
                        fam = font_css(lat.get("typeface"))
                    c = self.color(rPr)
                    if c: col = c
                rs = (f"font-family:'{fam}';font-size:{sz:.1f}pt;color:{col};"
                      f"{'font-weight:bold;' if b else ''}{'font-style:italic;' if i else ''}")
                runs_html.append(f'<span style="{rs}">{esc(s)}</span>')
            if not runs_html:
                inner.append('<div style="height:1em;">&nbsp;</div>')
            else:
                inner.append(f'<div style="text-align:{algn};margin:0;line-height:1.2;">'
                             + "".join(runs_html) + "</div>")
        out.append(f'<div style="{style}"><div style="width:100%;">'
                   + "".join(inner) + "</div></div>")

    def render_pic(self, pic, rels, out):
        box = self.emu_box(pic)
        if box is None: return
        x, y, w, h = box
        blip = pic.find(".//a:blip", NS)
        src = ""
        if blip is not None:
            rid = blip.get(f"{{{R}}}embed")
            tgt = rels.get(rid)
            if tgt:
                mp = "ppt/" + tgt.replace("../", "")
                try:
                    data = self.z.read(mp)
                    ext = mp.rsplit(".",1)[-1].lower()
                    mime = {"jpg":"jpeg","jpeg":"jpeg","png":"png","gif":"gif"}.get(ext,"jpeg")
                    src = f"data:image/{mime};base64," + base64.b64encode(data).decode()
                except Exception: pass
        style = (f"position:absolute;left:{px(x)}px;top:{px(y)}px;"
                 f"width:{px(w)}px;height:{px(h)}px;object-fit:cover;")
        if src: out.append(f'<img src="{src}" style="{style}"/>')
        else: out.append(f'<div style="{style}background:#ccc;"></div>')

    def slide_html(self, slide_name):
        root = ET.fromstring(self.z.read(slide_name))
        rels = self.rels(slide_name)
        tree = root.find(".//p:cSld/p:spTree", NS)
        out = []
        for el in tree:
            tag = el.tag.split("}")[1]
            if tag == "sp": self.render_sp(el, out)
            elif tag == "pic": self.render_pic(el, rels, out)
            elif tag == "grpSp":
                for sub in el:
                    st = sub.tag.split("}")[1]
                    if st == "sp": self.render_sp(sub, out)
                    elif st == "pic": self.render_pic(sub, rels, out)
        return ('<div class="slide">' + "".join(out) + "</div>")

    def slide_names(self):
        return sorted([n for n in self.z.namelist()
                       if re.match(r"ppt/slides/slide\d+\.xml$", n)],
                      key=lambda n: int(re.search(r"(\d+)", n).group()))

def main():
    src, outpdf = sys.argv[1], sys.argv[2]
    only = set(int(x) for x in sys.argv[3:]) if len(sys.argv) > 3 else None
    d = Deck(src)
    names = d.slide_names()
    W, H = PGW/EMU_PX, PGH/EMU_PX
    css = (f"@page{{size:{W:.1f}px {H:.1f}px;margin:0;}}"
           f".slide{{position:relative;width:{W:.1f}px;height:{H:.1f}px;"
           "overflow:hidden;background:#fff;page-break-after:always;}}"
           "*{margin:0;padding:0;}")
    body = []
    for n in names:
        idx = int(re.search(r"(\d+)", n).group())
        if only and idx not in only: continue
        body.append(d.slide_html(n))
    html = f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(body)}</body></html>"
    HTML(string=html).write_pdf(outpdf)
    print(f"WROTE {outpdf}  ({len(body)} slides)")

if __name__ == "__main__":
    main()
