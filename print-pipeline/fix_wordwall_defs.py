#!/usr/bin/env python3
"""
Word Wall definition QC for the teacher deck:
  (1) Run-over fix: each definition box (cx=5239512, cy=420624 = 5.73x0.46in)
      is moved up 0.07in and grown to 0.63in, filling the reserved white-card
      space (card 1.38in - header 0.74in). 3-line definitions now fit inside
      the box instead of spilling past it. Uniform, targeted only at def boxes.
  (2) Content QC: three definitions truncated mid-sentence with a trailing
      ellipsis are completed with accurate, sourced text.
"""
import sys, re, zipfile, shutil, os

DEF_EXT = 'cx="5239512" cy="420624"'          # unique to Word Wall definition boxes
NEW_CY  = 576072                               # 0.63in
DY      = 64008                                # move up 0.07in
WW = {13,27,43,58,73,88,104}

# content completions: exact truncated phrase -> accurate completion
COMPLETIONS = {
    27: ("mainstream American culture. It resulted in…",
         "mainstream American culture. It caused the loss of about 90 million acres of tribal land."),
    43: ("removing federal troops from the South, effectively ending…",
         "removing federal troops from the South, effectively ending Reconstruction."),
    58: ("a thin layer of prosperity covered deep social…",
         "a thin layer of prosperity covered deep social problems and inequality."),
}

OFF_DEF_RE = re.compile(
    r'<a:off x="(\d+)" y="(\d+)"/><a:ext ' + re.escape(DEF_EXT) + r'/>')

def fix_slide(idx, xml):
    changed = 0
    def repl(m):
        nonlocal changed
        x, y = m.group(1), int(m.group(2))
        changed += 1
        return f'<a:off x="{x}" y="{y-DY}"/><a:ext cx="5239512" cy="{NEW_CY}"/>'
    xml2 = OFF_DEF_RE.sub(repl, xml)
    ctext = 0
    if idx in COMPLETIONS:
        old, new = COMPLETIONS[idx]
        if old in xml2:
            xml2 = xml2.replace(old, new); ctext = 1
        else:
            print(f"  !! slide {idx}: truncated phrase not found (already fixed?)")
    return xml2, changed, ctext

def main(src, dst):
    zin = zipfile.ZipFile(src)
    tmp = dst + ".tmp"
    zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    tot_boxes = tot_text = 0
    for it in zin.infolist():
        data = zin.read(it.filename)
        m = re.match(r"ppt/slides/slide(\d+)\.xml$", it.filename)
        if m and int(m.group(1)) in WW:
            idx = int(m.group(1))
            xml2, nb, nt = fix_slide(idx, data.decode("utf-8"))
            tot_boxes += nb; tot_text += nt
            data = xml2.encode("utf-8")
        zout.writestr(it, data)
    zout.close(); zin.close()
    shutil.move(tmp, dst)
    print(f"{os.path.basename(dst)}: {tot_boxes} def boxes grown, "
          f"{tot_text} truncated definitions completed")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
