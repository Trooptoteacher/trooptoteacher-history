#!/usr/bin/env python3
"""Extract the deck<->workbook alignment data for one unit.

Reads the AUTHENTIC teacher deck (.pptx) and the unit content JSON, and emits an
align.json the layer builder consumes. Detects, per standard:
  - the STANDARD divider slide number
  - the DIRECT INSTRUCTION slide numbers + their labels (verbatim)
and pairs them against the workbook's Cornell cues (standards[code].criteria).

Convention it relies on (all History Hack teacher decks follow it):
  divider slide text starts with "STANDARD" and contains a US.NN code;
  DI slide text contains "DIRECT INSTRUCTION" and the US.NN code, with the
  concept label as the slide's second text run.

Usage:
  python3 extract_align.py TEACHER_DECK.pptx unit<N>_content.json align.json
"""
import sys, zipfile, re, json

def texts(z, n):
    x = z.read(n).decode("utf8", "ignore")
    return [t.strip() for t in re.findall(r"<a:t>(.*?)</a:t>", x) if t.strip()]

def main(deck, content, out):
    z = zipfile.ZipFile(deck)
    num = lambda n: int(re.search(r"(\d+)", n).group())
    slides = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)], key=num)
    code_re = re.compile(r"US\.\d{2}")
    std_div, di = {}, {}
    for i, n in enumerate(slides, 1):
        t = texts(z, n)
        joined = " | ".join(t[:2])
        m = code_re.search(joined)
        if not m:
            continue
        code = m.group()
        if joined.upper().startswith("STANDARD"):
            std_div[code] = i
            di.setdefault(code, [])
        elif "DIRECT INSTRUCTION" in joined.upper():
            label = t[1] if len(t) > 1 else t[0]
            di.setdefault(code, []).append({"n": i, "label": label})

    wb = json.load(open(content))
    st = wb["standards"]
    order = wb["order"]
    recs = []
    for c in order:
        s = st[c]
        tn = (s.get("tn_connection", "") or "").split(". ")[0]
        recs.append({
            "code": c,
            "title": s.get("title", ""),
            "ican": s.get("ican", ""),
            "criteria": s.get("criteria", [])[:4],       # workbook Cornell cues
            "di_slides": di.get(c, []),                    # deck DI slides (verbatim)
            "divider_slide": std_div.get(c),
            "vocab_n": len(s.get("vocab", [])),
            "source": (s.get("sources") or [{}])[0].get("title", ""),
            "tn": tn if len(tn) <= 150 else tn[:150],
        })
    json.dump({"unit": wb["unit"], "order": order, "recs": recs}, open(out, "w"), indent=1)

    # console verification of the DI <-> Cornell parity (the hard requirement)
    print("STD    divider  #DI  DI labels  vs  Cornell criteria")
    for r in recs:
        dl = [d["label"] for d in r["di_slides"]]
        exact = [d.lower() for d in dl[:len(r["criteria"])]] == [c.lower() for c in r["criteria"]]
        flag = "EXACT" if exact else f"{len(dl)} DI / {len(r['criteria'])} cues — review"
        print(f"{r['code']}  s{r['divider_slide']}  {len(dl)}   {flag}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
