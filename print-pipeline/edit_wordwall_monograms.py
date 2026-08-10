#!/usr/bin/env python3
"""
Remove the initials-monogram chips from Word Wall slides in a deck (.pptx),
and reclaim their width for the definition text.

Per Sean: the per-term initials squares ("RS", "DA", ...) add cognitive load
and aren't needed on the Word Wall. This deletes, ONLY on slides titled
"Word Wall", each monogram square (solid fill F3EAD0, ~0.5x0.5in) and its
1-3 char initials text, then shifts each definition box left to the monogram's
left edge and widens it to the same right edge (fewer wrapped lines, no gap).

Surgical string edits on the slide XML (shapes are flat, never nested), so the
package is preserved byte-for-byte except the targeted shapes. No other slide
type is touched.
"""
import sys, re, zipfile, shutil, os
import xml.etree.ElementTree as ET

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NSDECL = f'xmlns:a="{A}" xmlns:p="{P}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
NS = {"a": A, "p": P}
EMU = 914400.0
MONO_FILL = "F3EAD0"
SP_RE = re.compile(r"<p:sp\b.*?</p:sp>", re.DOTALL)

def box(sp):
    xf = sp.find("p:spPr/a:xfrm", NS)
    if xf is None: return None
    off, ext = xf.find("a:off", NS), xf.find("a:ext", NS)
    if off is None or ext is None: return None
    return (int(off.get("x")), int(off.get("y")),
            int(ext.get("cx")), int(ext.get("cy")))

def fill_hex(sp):
    f = sp.find("p:spPr/a:solidFill/a:srgbClr", NS)
    return f.get("val") if f is not None else None

def text_of(sp):
    return "".join((t.text or "") for t in sp.findall(".//a:t", NS))

def parse(span):
    return ET.fromstring(f"<root {NSDECL}>{span}</root>").find("p:sp", NS)

def is_mono_square(sp, b):
    if fill_hex(sp) != MONO_FILL: return False
    _, _, w, h = b
    return 0.4*EMU <= w <= 0.62*EMU and 0.4*EMU <= h <= 0.62*EMU

def is_initials(sp, b):
    if fill_hex(sp) is not None: return False
    _, _, w, h = b
    if not (0.4*EMU <= w <= 0.62*EMU and 0.4*EMU <= h <= 0.62*EMU): return False
    t = text_of(sp).strip()
    return 1 <= len(t) <= 3 and t.isupper()

def process_slide(xml):
    if "Word Wall" not in xml:
        return xml, 0, 0
    spans = list(SP_RE.finditer(xml))
    # pass 1: monogram square positions (x,y)
    monos = []
    for m in spans:
        sp = parse(m.group(0)); b = box(sp)
        if b and is_mono_square(sp, b):
            monos.append((b[0], b[1]))
    if not monos:
        return xml, 0, 0
    # pass 2: build edited string
    out = []
    last = 0
    removed = widened = 0
    for m in spans:
        out.append(xml[last:m.start()])
        span = m.group(0); sp = parse(span); b = box(sp)
        drop = False; new = span
        if b:
            if is_mono_square(sp, b) or is_initials(sp, b):
                drop = True
            else:
                # definition box? the monogram IMMEDIATELY to its left, same cell
                # (same row, gap < 1in) — not just any same-row monogram, or a
                # right-column def would snap onto the left column.
                x, y, w, h = b
                if w >= 4.3*EMU and text_of(sp).strip():
                    cands = [(mx, my) for mx, my in monos
                             if abs(y - my) <= 0.18*EMU and 0 < (x - mx) <= 1.0*EMU]
                    if cands:
                        mx, my = max(cands, key=lambda c: c[0])   # nearest on the left
                        newx = mx
                        neww = (x + w) - mx
                        span2 = span.replace(f'<a:off x="{x}" y="{y}"/>',
                                             f'<a:off x="{newx}" y="{y}"/>')
                        span2 = span2.replace(f'<a:ext cx="{w}" cy="{h}"/>',
                                              f'<a:ext cx="{neww}" cy="{h}"/>')
                        if span2 != span:
                            new = span2; widened += 1
        if drop:
            removed += 1
        else:
            out.append(new)
        last = m.end()
    out.append(xml[last:])
    return "".join(out), removed, widened

def process_deck(src, dst):
    zin = zipfile.ZipFile(src)
    tmp = dst + ".tmp"
    zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    tot_r = tot_w = tot_s = 0
    for item in zin.infolist():
        data = zin.read(item.filename)
        if re.match(r"ppt/slides/slide\d+\.xml$", item.filename):
            xml = data.decode("utf-8")
            new, r, w = process_slide(xml)
            if r or w:
                tot_s += 1; tot_r += r; tot_w += w
                data = new.encode("utf-8")
        zout.writestr(item, data)
    zout.close(); zin.close()
    shutil.move(tmp, dst)
    print(f"{os.path.basename(dst)}: {tot_s} Word Wall slides edited, "
          f"{tot_r} monogram shapes removed, {tot_w} definitions widened")

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    process_deck(src, dst)
