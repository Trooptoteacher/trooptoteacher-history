#!/usr/bin/env python3
"""Reconcile a unit's workbook vocabulary to its teacher deck's KEY VOCABULARY Word Wall.

Deck = source of truth. Overwrites, per standard:
  standards[code].vocab      = the deck's Word Wall terms (term / say / es / def, verbatim)
  standards[code].auth.frayer = the first two deck terms (so Activity 2 uses real deck vocab)

Writes the content JSON in place (make a .bak first if you want one). After running, rebuild
the workbook and run check_parity.py — it should PASS.

Usage:
  python3 reconcile_vocab.py TEACHER_DECK.pptx unit<N>_content.json
"""
import sys, zipfile, re, json

def txt(z, n):
    return [t.strip().replace("&quot;", '"').replace("&amp;", "&").replace("&apos;", "'")
            for t in re.findall(r"<a:t>(.*?)</a:t>", z.read(n).decode("utf8", "ignore")) if t.strip()]

def word_wall(z, slides):
    """Return {code: [{term,say,es,def}]} from every KEY VOCABULARY slide.
    Robust to both Word Wall layouts (with or without a 'say:' pronunciation run):
    each entry ends in a long definition, preceded by a short (<=4 char) initials code."""
    out = {}
    cof = lambda j: (re.search(r"US\.\d{2}", j) or [None])[0] if re.search(r"US\.\d{2}", j) else None
    for nm in slides:
        t = txt(z, nm); j = " | ".join(t[:2]); c = cof(j)
        if not c or "KEY VOCABULARY" not in j.upper():
            continue
        body = [r for r in t[2:] if not r.startswith('"say:"') and "TroopToTeacher" not in r and not r.isdigit()]
        vocab = []
        for k, r in enumerate(body):
            if len(r) <= 25:
                continue
            initials = body[k-1] if k >= 1 else ""
            if not (0 < len(initials) <= 4):      # rejects long Spanish translations
                continue
            if k >= 5 and body[k-4].lower() == "say:":
                term, say, es = body[k-5], body[k-3], body[k-2]
            else:
                term, say, es = (body[k-3] if k >= 3 else ""), "", (body[k-2] if k >= 2 else "")
            if term and len(term) <= 44:
                vocab.append({"term": term, "say": say, "es": es, "def": r})
        out[c] = vocab
    return out

def main(deck, content):
    z = zipfile.ZipFile(deck)
    num = lambda n: int(re.search(r"(\d+)", n).group())
    slides = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)], key=num)
    wall = word_wall(z, slides)
    c = json.load(open(content)); st = c["standards"]
    changed = 0
    for code in c["order"]:
        dv = wall.get(code, [])
        if not dv:
            print(f"  {code}: deck Word Wall empty — kept workbook vocab (INVESTIGATE)")
            continue
        st[code]["vocab"] = [{"term": v["term"], "say": v["say"], "es": v["es"], "def": v["def"]} for v in dv]
        st[code].setdefault("auth", {})["frayer"] = [v["term"] for v in dv][:2]
        changed += 1
        print(f"  {code}: {len(dv)} deck terms → {', '.join(v['term'] for v in dv)}")
    json.dump(c, open(content, "w"), ensure_ascii=False, indent=1)
    print(f"\nreconciled {changed}/{len(c['order'])} standards; wrote {content}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
