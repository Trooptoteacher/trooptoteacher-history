#!/usr/bin/env python3
"""
History Hack print pipeline — content JSON -> HTML -> WeasyPrint -> print-ready PDF.

Layout is governed ENTIRELY by print-pipeline/styles/workbook.css (the layout
contract). This renderer only turns structured content into semantic HTML; it
makes NO per-document layout decisions, so every unit paginates by the same
deterministic rules. Re-running on edited content re-flows correctly — no manual
realignment, ever.

Usage:
    python3 render.py content/us-history/unit-01.json out/Unit1_Student_Workbook.pdf
"""
import html
import json
import sys
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent


def esc(s: str) -> str:
    return html.escape(str(s), quote=False)


def rich(s: str) -> str:
    # Content may carry a small, trusted set of inline tags (<strong>, <em>).
    return str(s)


def render_table(block) -> str:
    cls = f' class="{esc(block["class"])}"' if block.get("class") else ""
    head = "".join(f"<th>{esc(h)}</th>" for h in block["head"])
    rows = ""
    write = block.get("class") == "write"
    tr_open = '<tr class="write">' if write else "<tr>"
    for r in block["rows"]:
        tds = ""
        for i, cell in enumerate(r):
            qcls = ' class="q"' if (write and i == 0) else ""
            tds += f"<td{qcls}>{rich(cell)}</td>"
        rows += f"{tr_open}{tds}</tr>"
    return f"<table{cls}><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>"


def render_box(block) -> str:
    ps = "".join(f"<p>{rich(p)}</p>" for p in block["paras"])
    return f'<div class="box"><div class="k">{esc(block["label"])}</div>{ps}</div>'


def render_cornell(block) -> str:
    rows = "".join(
        f'<tr><td class="cue">{rich(c)}</td><td class="note">{rich(n)}</td></tr>'
        for c, n in block["rows"]
    )
    return (f'<h3>{esc(block["heading"])}</h3>'
            f'<table class="cornell"><tbody>{rows}</tbody></table>')


def render_cornellnotes(block) -> str:
    rows = "".join(
        f'<tr><td class="cue">{esc(c)}</td><td class="note"></td></tr>'
        for c in block["cues"]
    )
    return (f'<h3>{esc(block["heading"])}</h3>'
            f'<table class="cornell"><tbody>{rows}</tbody></table>')


def render_activity(block) -> str:
    out = (f'<div class="activity-title">Activity {block["num"]} — '
           f'{esc(block["name"])} <span class="time">⏱ {esc(block["time"])}</span></div>')
    if block.get("lead"):
        out += f'<div class="activity-lead">{esc(block["lead"])}</div>'
    out += render_blocks(block["blocks"])
    return out


def render_head(block):
    sub = (f'<span style="color:#C9A227;font-weight:700;font-size:9pt"> &middot; '
           f'{esc(block["sub"])}</span>') if block.get("sub") else ""
    return (f'<h2 style="color:#1F3A5F;border-bottom:2px solid #C9A227;padding-bottom:2pt;'
            f'margin:13pt 0 5pt;font-size:14pt;break-after:avoid">{esc(block["text"])}{sub}</h2>')


def render_lines(block):
    n = block.get("n", 3)
    return "".join('<div style="border-bottom:0.5pt solid #9AA0AB;height:19pt"></div>'
                   for _ in range(n))


def render_image(block):
    cap = f'<div style="font-size:8pt;color:#5C6470;font-style:italic;margin-top:2pt">{rich(block["caption"])}</div>' if block.get("caption") else ""
    return (f'<div style="text-align:center;margin:6pt 0"><img src="{block["src"]}" '
            f'style="max-width:{block.get("w","100%")};max-height:{block.get("h","3in")};'
            f'border:1px solid #C9C2B4;border-radius:4px">{cap}</div>')


def render_cover(block):
    NAVY, RED, GOLD, CREAM, INK = "#1F3A5F", "#B22234", "#C9A227", "#F8F5EF", "#20262E"
    img = (f'<img src="{block["image"]}" style="width:100%;height:2.9in;object-fit:cover;'
           f'border-radius:6px;border:1px solid #C9C2B4">') if block.get("image") else ""
    stds = "".join(f'<li style="margin-bottom:1pt">{rich(s)}</li>' for s in block.get("standards", []))
    return f'''<div style="page-break-after:always;font-family:'DejaVu Sans',Arial,sans-serif;color:{INK}">
      <div style="background:{NAVY};color:#fff;border-left:12px solid {RED};padding:14pt 16pt;border-radius:6px 6px 0 0">
        <div style="color:{GOLD};font-weight:700;letter-spacing:1pt;font-size:11pt">U.S. HISTORY HACK&trade; &middot; AMERICA 250</div>
        <div style="font-size:23pt;font-weight:700;margin:4pt 0 2pt">{rich(block["title"])}</div>
        <div style="color:#DCE6F1;font-size:12pt">{rich(block.get("subtitle",""))}</div>
      </div>
      <div style="margin:8pt 0">{img}</div>
      <table style="width:100%;border-collapse:collapse"><tr>
        <td style="width:48%;vertical-align:top;padding-right:10pt">
          <div style="color:{NAVY};font-weight:700;font-size:9.5pt;text-transform:uppercase;letter-spacing:.4pt;margin-bottom:2pt">Standards covered</div>
          <ul style="margin:0 0 8pt 16pt;font-size:9.5pt">{stds}</ul>
        </td>
        <td style="width:52%;vertical-align:top">
          <div style="color:{NAVY};font-weight:700;font-size:9.5pt;text-transform:uppercase;letter-spacing:.4pt;margin-bottom:2pt">Unit summary</div>
          <div style="font-size:9.7pt;line-height:1.4">{rich(block.get("summary",""))}</div>
        </td></tr></table>
      <div style="background:{GOLD};color:{NAVY};border-radius:5px;padding:9pt 12pt;margin:8pt 0">
        <div style="font-weight:700;font-size:9.5pt;letter-spacing:.4pt">&#9733; TENNESSEE CONNECTION</div>
        <div style="font-size:9.7pt;line-height:1.4;margin-top:2pt">{rich(block.get("tn",""))}</div>
      </div>
      <div style="background:{CREAM};border:1px solid #C9C2B4;border-radius:5px;padding:9pt 12pt;margin:8pt 0">
        <div style="color:{NAVY};font-weight:700;font-size:9.5pt;text-transform:uppercase;letter-spacing:.4pt">What students &amp; families can expect</div>
        <div style="font-size:9.6pt;line-height:1.4;margin-top:2pt">{rich(block.get("expect",""))}</div>
      </div>
      <div style="font-size:8pt;color:#5C6470;border-top:1px solid #C9C2B4;margin-top:10pt;padding-top:6pt;line-height:1.4">
        {rich(block.get("copyright",""))}</div>
    </div>'''


def render_tag(block):
    # small Future-Ready / ACT connection chip
    color = block.get("color", "#1F3A5F")
    return (f'<div style="font-family:Arial;font-size:8pt;color:{color};font-weight:700;'
            f'background:#EEF2F8;border-left:3px solid {color};padding:3pt 8pt;margin:4pt 0;'
            f'border-radius:3px">{rich(block["text"])}</div>')


BLOCKS = {
    "box": render_box,
    "table": render_table,
    "cornell": render_cornell,
    "cornellnotes": render_cornellnotes,
    "activity": render_activity,
    "head": render_head,
    "lines": render_lines,
    "tag": render_tag,
    "image": render_image,
    "cover": render_cover,
}


def render_blocks(blocks) -> str:
    return "".join(BLOCKS[b["type"]](b) for b in blocks)


def render_unit(data) -> str:
    body = f'<span class="runhead">{esc(data["runhead"])}</span>'
    body += f'<span class="runfoot">{esc(data["runfoot"])}</span>'
    if data.get("front"):
        body += render_blocks(data["front"])
        body += '<div style="break-after:page"></div>'
    for std in data["standards"]:
        body += f'<div class="standard">{esc(std["code"])} — {esc(std["title"])}</div>'
        body += render_blocks(std["blocks"])
    if data.get("back"):
        body += '<div style="break-before:page"></div>'
        body += render_blocks(data["back"])
    css = (ROOT / "styles" / "workbook.css").as_uri()
    return (f'<!doctype html><html><head><meta charset="utf-8">'
            f'<link rel="stylesheet" href="{css}"></head><body>{body}</body></html>')


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "content/us-history/unit-01.json"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "out/Unit1_Student_Workbook.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    data = json.loads(src.read_text())
    HTML(string=render_unit(data), base_url=str(ROOT)).write_pdf(str(out))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
