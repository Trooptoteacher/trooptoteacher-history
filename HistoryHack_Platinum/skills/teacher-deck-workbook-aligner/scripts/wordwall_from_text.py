#!/usr/bin/env python3
"""Extract the KEY VOCABULARY Word Wall from a teacher deck's TEXT.

Use this when the teacher deck exceeds the Drive connector's 10 MB binary-download cap
(reconcile_vocab.py needs the .pptx). The connector's read_file_content returns the deck's
full slide TEXT at ANY size — save that JSON ({"fileContent": "..."}), point this at it, and
you get the same {code: [{term,say,es,def}]} that reconcile_vocab.py produces from the binary.

Each Word Wall entry in the flattened text is: term / [say: pron] / Spanish / initials(<=4) /
definition. Blocks are bounded by the next "US.NN ·" slide title so definitions containing
words like "progressive" don't get mistaken for a section break.

Usage:
  python3 wordwall_from_text.py read_file_content.json out_deck_vocab.json
  # then feed out_deck_vocab.json into the same reconcile step reconcile_vocab.py uses.
"""
import json, sys, re

def main(textjson, out):
    raw = json.load(open(textjson))
    t = raw.get("fileContent", raw) if isinstance(raw, dict) else raw
    lines = [l.strip() for l in t.split("\n")]
    heads = [i for i, l in enumerate(lines) if l.endswith("KEY VOCABULARY")]
    SLIDE = re.compile(r"^US\.\d{2}\s*[·•]")       # next slide title = block boundary
    codes = []
    for i in heads:
        m = re.search(r"US\.\d{2}", lines[i])
        if m:
            codes.append((m.group(), i))

    def parse(h):
        body = []
        for l in lines[h+1:]:
            if SLIDE.match(l):
                break
            if l in ("Word Wall", "") or "TroopToTeacher" in l or l.isdigit() or l.startswith('"say:"'):
                continue
            body.append(l)
        out = []
        for k, l in enumerate(body):
            if len(l) <= 25:
                continue
            ini = body[k-1] if k >= 1 else ""
            if not (0 < len(ini) <= 4):
                continue
            if k >= 4 and body[k-3].lower().startswith("say:"):
                term, say, es = body[k-4], body[k-3][4:].strip(), body[k-2]
            else:
                term, say, es = (body[k-3] if k >= 3 else ""), "", (body[k-2] if k >= 2 else "")
            if term and len(term) <= 44 and not term.lower().startswith("say:"):
                out.append({"term": term, "say": say, "es": es, "def": l})
        return out

    res = {c: parse(h) for c, h in codes}
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    for c in sorted(res):
        print(f"{c}: {len(res[c])} -> {', '.join(v['term'] for v in res[c])}")
    counts = {c: len(v) for c, v in res.items()}
    odd = [c for c, n in counts.items() if not (4 <= n <= 8)]
    print("\nreview these (unexpected term count):", odd if odd else "none")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
