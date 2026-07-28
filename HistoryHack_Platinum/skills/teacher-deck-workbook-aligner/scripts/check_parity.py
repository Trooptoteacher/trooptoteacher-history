#!/usr/bin/env python3
"""CONTENT parity gate — the workbook must teach what the deck teaches.

Alignment is not just structural (a map slide). The workbook and deck must carry the
SAME content per standard. This checks the two that drift in practice:
  1. DIRECT INSTRUCTION labels  == workbook Cornell cues (standards[code].criteria)
  2. KEY VOCABULARY Word Wall   == workbook vocab terms (standards[code].vocab)

Reads the deck straight from the .pptx and the unit content JSON. Exit 0 = aligned,
exit 1 = drift (prints every mismatch). Run it after any workbook OR deck change.

Usage:
  python3 check_parity.py TEACHER_DECK.pptx unit<N>_content.json
"""
import sys, zipfile, re, json

def txt(z, n):
    return [t.strip().replace("&quot;", '"').replace("&amp;", "&").replace("&apos;", "'")
            for t in re.findall(r"<a:t>(.*?)</a:t>", z.read(n).decode("utf8", "ignore")) if t.strip()]

def deck_content(deck):
    z = zipfile.ZipFile(deck)
    num = lambda n: int(re.search(r"(\d+)", n).group())
    slides = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)], key=num)
    di, vocab = {}, {}
    cof = lambda j: (re.search(r"US\.\d{2}", j) or [None])[0] if re.search(r"US\.\d{2}", j) else None
    for nm in slides:
        t = txt(z, nm); j = " | ".join(t[:2]); c = cof(j)
        if not c:
            continue
        U = j.upper()
        if "DIRECT INSTRUCTION" in U:
            di.setdefault(c, []).append(t[1] if len(t) > 1 else "")
        elif "KEY VOCABULARY" in U:
            body = [r for r in t[2:] if not r.startswith('"say:"') and "TroopToTeacher" not in r and not r.isdigit()]
            terms = []
            for k, r in enumerate(body):
                if len(r) <= 25:
                    continue
                # a real definition sits right after the term's short initials code
                # (1–4 chars). This guard rejects long Spanish translations, which are
                # NOT preceded by an initials code, from being mistaken for definitions.
                initials = body[k-1] if k >= 1 else ""
                if not (0 < len(initials) <= 4):
                    continue
                term = body[k-5] if k >= 5 and body[k-4].lower() == "say:" else (body[k-3] if k >= 3 else "")
                if term and len(term) <= 44:
                    terms.append(term)
            vocab[c] = terms
    return di, vocab

def main(deck, content):
    di, dvoc = deck_content(deck)
    wb = json.load(open(content)); st = wb["standards"]
    ok = True
    for c in wb["order"]:
        s = st[c]
        crit = s.get("criteria", [])
        dilabels = di.get(c, [])
        di_ok = [d.lower() for d in dilabels[:len(crit)]] == [x.lower() for x in crit]
        wv = [v["term"] for v in s.get("vocab", [])]
        dv = dvoc.get(c, [])
        v_ok = [x.lower() for x in wv] == [x.lower() for x in dv]
        if not (di_ok and v_ok):
            ok = False
            print(f"[{c}] DRIFT")
            if not di_ok:
                print(f"   DI     deck={dilabels}")
                print(f"   cues   wb  ={crit}")
            if not v_ok:
                print(f"   vocab  deck={dv}")
                print(f"   vocab  wb  ={wv}")
        else:
            print(f"[{c}] aligned  (DI {len(dilabels)}↔cues {len(crit)} · vocab {len(dv)})")
    print("\nPARITY:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
