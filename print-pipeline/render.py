#!/usr/bin/env python3
"""
History Hack print pipeline — structured content JSON -> semantic HTML ->
WeasyPrint -> print-ready PDF.

Layout is governed ENTIRELY by the shared contract (contract/print-contract.css)
plus a per-course brand token file (contract/tokens/<course>.css). This renderer
turns structured content into semantic HTML and makes NO per-document layout
decisions, so every product (textbook, student workbook, DBQ workbook, graphic
organizer) across every course paginates by the same deterministic rules.
Re-running on edited content re-flows correctly — no manual realignment, ever.

Usage:
    python3 render.py CONTENT.json OUT.pdf [--tokens us-history] [--print-shop]
"""
import argparse
import html
import json
import sys
from pathlib import Path

from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
CONTRACT = ROOT / "contract"


def esc(s) -> str:
    return html.escape(str(s), quote=False)


def rich(s) -> str:
    # Content may carry a trusted, small set of inline tags (<strong>, <em>).
    return str(s)


# ---- block renderers -------------------------------------------------------
def render_blocks(blocks) -> str:
    return "".join(BLOCKS[b["type"]](b) for b in blocks)


def b_heading(b) -> str:
    lvl = int(b.get("level", 2))
    return f"<h{lvl}>{rich(b['text'])}</h{lvl}>"


def b_para(b) -> str:
    return f"<p>{rich(b.get('text', b.get('html', '')))}</p>"


def b_html(b) -> str:
    return str(b["html"])


def b_box(b) -> str:
    ps = "".join(f"<p>{rich(p)}</p>" for p in b["paras"])
    return f'<div class="box"><div class="k">{esc(b["label"])}</div>{ps}</div>'


def b_table(b) -> str:
    cls = f' class="{esc(b["class"])}"' if b.get("class") else ""
    head = "".join(f"<th>{esc(h)}</th>" for h in b["head"])
    write = b.get("class") == "write"
    tr_open = '<tr class="write">' if write else "<tr>"
    rows = ""
    for r in b["rows"]:
        tds = ""
        for i, c in enumerate(r):
            qcls = ' class="q"' if (write and i == 0) else ""
            tds += f"<td{qcls}>{rich(c)}</td>"
        rows += f"{tr_open}{tds}</tr>"
    return f"<table{cls}><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>"


def b_cornell(b) -> str:
    rows = "".join(
        f'<tr><td class="cue">{esc(c)}</td><td>{rich(n)}</td></tr>' for c, n in b["rows"]
    )
    return f'<h3>{esc(b["heading"])}</h3><table class="cornell"><tbody>{rows}</tbody></table>'


def b_cornellnotes(b) -> str:
    rows = "".join(
        f'<tr><td class="cue">{esc(c)}</td><td class="note"></td></tr>' for c in b["cues"]
    )
    return f'<h3>{esc(b["heading"])}</h3><table class="cornell"><tbody>{rows}</tbody></table>'


def b_activity(b) -> str:
    out = (f'<div class="activity-title">Activity {esc(b["num"])} — {esc(b["name"])}'
           f' <span class="time">⏱ {esc(b["time"])}</span></div>')
    if b.get("lead"):
        out += f'<div class="activity-lead">{esc(b["lead"])}</div>'
    return out + render_blocks(b["blocks"])


# textbook
def b_chapter(b) -> str:
    k = f'<div class="chapter-kicker">{esc(b["kicker"])}</div>' if b.get("kicker") else ""
    return (f'<div class="chapter">{k}'
            f'<div class="chapter-title">{rich(b["title"])}</div>'
            f'{render_blocks(b.get("blocks", []))}</div>')


def b_section(b) -> str:
    out = f'<div class="section">{rich(b["title"])}</div>'
    return out + render_blocks(b.get("blocks", []))


def b_figure(b) -> str:
    cap = f'<figcaption>{rich(b["caption"])}</figcaption>' if b.get("caption") else ""
    return f'<figure class="figure"><img src="{esc(b["img"])}">{cap}</figure>'


def b_sidebar(b) -> str:
    ps = "".join(f"<p>{rich(p)}</p>" for p in b["paras"])
    lbl = f'<div class="k">{esc(b["label"])}</div>' if b.get("label") else ""
    return f'<aside class="sidebar">{lbl}{ps}</aside>'


def b_pullquote(b) -> str:
    return f'<div class="pullquote">{rich(b["text"])}</div>'


# DBQ
def b_source(b) -> str:
    img = f'<img src="{esc(b["img"])}">' if b.get("img") else ""
    cite = f'<div class="cite">{rich(b["cite"])}</div>' if b.get("cite") else ""
    body = render_blocks(b.get("blocks", []))
    return (f'<div class="source"><div class="source-head">{esc(b["head"])}</div>'
            f'<div class="source-body">{img}{body}{cite}</div></div>')


def b_hippo(b) -> str:
    lines = int(b.get("lines", 2))
    return (f'<div class="hippo"><div class="k">{esc(b["label"])}</div>'
            f'<div class="writelines" style="height:{lines*21}pt"></div></div>')


def b_writelines(b) -> str:
    lines = int(b.get("lines", 3))
    return f'<div class="writelines" style="height:{lines*21}pt"></div>'


# organizer
def b_grid(b) -> str:
    cells = "".join(f"<div>{render_blocks([c]) if isinstance(c, dict) else rich(c)}</div>"
                    for c in b["cells"])
    return f'<div class="grid" style="--cols:{int(b.get("cols",2))}">{cells}</div>'


def b_frame(b) -> str:
    title = f'<div class="frame-title">{esc(b["title"])}</div>' if b.get("title") else ""
    plain = " plain" if b.get("plain") else ""
    inner = "".join(f"<p>{rich(p)}</p>" for p in b.get("paras", []))
    style = f' style="min-height:{int(b["lines"])*21}pt"' if b.get("lines") else ""
    return f'<div class="frame">{title}<div class="frame-body{plain}"{style}>{inner}</div></div>'


def b_tchart(b) -> str:
    lh = f' style="min-height:{int(b["lines"])*21}pt"' if b.get("lines") else ""
    return (f'<div class="tchart">'
            f'<div class="col"><div class="col-head">{esc(b["left"])}</div><div class="col-body"{lh}></div></div>'
            f'<div class="col"><div class="col-head">{esc(b["right"])}</div><div class="col-body"{lh}></div></div>'
            f'</div>')


def b_frayer(b) -> str:
    q = b["quads"]
    cells = [f'<td><div class="k">{esc(x)}</div></td>' for x in q]
    grid = (f'<table class="frayer-grid"><tr>{cells[0]}{cells[1]}</tr>'
            f'<tr>{cells[2]}{cells[3]}</tr></table>')
    return f'<div class="frayer">{grid}<div class="term">{esc(b["term"])}</div></div>'


def b_venn(b) -> str:
    return (f'<div class="venn">'
            f'<div class="circle left"></div><div class="circle right"></div>'
            f'<div class="label left">{esc(b["left"])}</div>'
            f'<div class="label both">{esc(b.get("both","Both"))}</div>'
            f'<div class="label right">{esc(b["right"])}</div></div>')


def b_standard(b) -> str:
    return f'<div class="standard">{esc(b.get("code",""))} — {esc(b.get("title",""))}</div>' + \
        render_blocks(b.get("blocks", []))


BLOCKS = {
    "heading": b_heading, "para": b_para, "html": b_html, "box": b_box, "table": b_table,
    "cornell": b_cornell, "cornellnotes": b_cornellnotes, "activity": b_activity,
    "chapter": b_chapter, "section": b_section, "figure": b_figure, "sidebar": b_sidebar,
    "pullquote": b_pullquote, "source": b_source, "hippo": b_hippo, "writelines": b_writelines,
    "grid": b_grid, "frame": b_frame, "tchart": b_tchart, "frayer": b_frayer, "venn": b_venn,
    "standard": b_standard,
}


def render_doc(data, tokens: str, print_shop: bool) -> str:
    body = f'<span class="runhead">{esc(data.get("runhead",""))}</span>'
    body += f'<span class="runfoot">{esc(data.get("runfoot",""))}</span>'
    if data.get("standards"):          # legacy workbook shape: standards -> blocks
        for std in data["standards"]:
            body += b_standard({**std, "blocks": std.get("blocks", [])})
    body += render_blocks(data.get("blocks", []))

    token_uri = (CONTRACT / "tokens" / f"{tokens}.css").as_uri()
    contract_uri = (CONTRACT / "print-contract.css").as_uri()
    links = f'<link rel="stylesheet" href="{token_uri}">' \
            f'<link rel="stylesheet" href="{contract_uri}">'
    if print_shop:
        links += f'<link rel="stylesheet" href="{(CONTRACT / "print-shop.css").as_uri()}">'
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">{links}</head>'
            f'<body>{body}</body></html>')


def main() -> int:
    ap = argparse.ArgumentParser(description="History Hack shared print renderer")
    ap.add_argument("content")
    ap.add_argument("out")
    ap.add_argument("--tokens", default="us-history", help="brand token file (contract/tokens/<name>.css)")
    ap.add_argument("--print-shop", action="store_true", help="add crop marks + bleed for a print vendor")
    args = ap.parse_args()

    src = Path(args.content)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    data = json.loads(src.read_text(encoding="utf-8"))
    html_str = render_doc(data, args.tokens, args.print_shop)
    # base_url = content dir so figures/sources may reference local images.
    HTML(string=html_str, base_url=str(src.resolve().parent)).write_pdf(str(out))
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
