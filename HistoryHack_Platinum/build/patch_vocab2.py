#!/usr/bin/env python3
"""Upgrade vocab_for(): when the vocab bank has too few in-passage terms, fill the
Word Bank from the standard's own FACTCARD concepts (topic-guaranteed) instead of
borrowing unit-wide terms. Also drops the tagged-but-not-in-passage tier that was
still injecting mis-tagged terms (e.g. 'Reservation System' onto the Inventions
standard). Applies to every unit's derive script."""
import re, os

OLD = '''def vocab_for(code, n=3):
    # Source the Word Bank from terms that actually appear in THIS standard's own
    # reading content, so the vocabulary always matches the standard's topic
    # (fixes under-tagging AND source mis-tagging like "Dawes Act" -> Inventions).
    s = ICAN[code]
    parts = [s.get("title", ""), s.get("iCanText", "")]
    for sec in s.get("readingContent", {}).get("sections", []):
        parts.append(sec.get("heading", "")); parts.append(sec.get("content", ""))
    hay = " ".join(parts).lower()
    def mk(v):
        return {"term": v["term"], "say": "", "es": v.get("termEs", ""),
                "def": v.get("definition", "")}
    tagged = [v for v in vocab if v.get("term") and code in (v.get("relatedStandards") or [])]
    out, have = [], set()
    def add(v):
        if v["term"] not in have:
            out.append(mk(v)); have.add(v["term"])
    # 1) tagged to THIS standard AND the term appears in its reading content (best)
    for v in tagged:
        if v["term"].lower() in hay:
            add(v)
        if len(out) >= n:
            return out[:n]
    # 2) ANY unit term that appears in this standard's reading content (topic-relevant
    #    by construction — excludes mis-tagged terms that never appear in the passage)
    for v in vocab:
        if len(out) >= n:
            break
        if v.get("term") and v["term"].lower() in hay:
            add(v)
    if len(out) >= n:
        return out[:n]
    # 3) tagged to this standard even if not literally in the passage (bank mapping)
    for v in tagged:
        if len(out) >= n:
            break
        add(v)
    if len(out) >= n:
        return out[:n]
    # 4) last resort so the Word Bank / Cornell supports are never empty
    for v in vocab:
        if len(out) >= n:
            break
        if v.get("term"):
            add(v)
    return out[:n]'''

NEW = '''def _vf_clean(t):
    t = (t or "").strip()
    for pre in ("The ", "Rise of ", "Impact of ", "Emergence of ", "Growth of ",
                "Role of ", "Effects of ", "Expansion of "):
        if t.startswith(pre):
            t = t[len(pre):]
    return t.strip()

def vocab_for(code, n=3):
    # Word Bank must match the standard's TOPIC. Prefer bank terms that actually
    # appear in this standard's own reading content; if the bank under-covers the
    # standard, fill from its own FACTCARD concepts (topic-guaranteed) rather than
    # borrowing unrelated unit-wide terms.
    s = ICAN[code]
    parts = [s.get("title", ""), s.get("iCanText", "")]
    for sec in s.get("readingContent", {}).get("sections", []):
        parts.append(sec.get("heading", "")); parts.append(sec.get("content", ""))
    hay = " ".join(parts).lower()
    out, have = [], set()
    def add(term, es="", defn=""):
        term = (term or "").strip()
        if term and term not in have:
            out.append({"term": term, "say": "", "es": es or "", "def": defn or ""})
            have.add(term)
    tagged = [v for v in vocab if v.get("term") and code in (v.get("relatedStandards") or [])]
    # 1) tagged to THIS standard AND appears in its reading content (best)
    for v in tagged:
        if v["term"].lower() in hay:
            add(v["term"], v.get("termEs", ""), v.get("definition", ""))
        if len(out) >= n:
            return out[:n]
    # 2) ANY bank term that appears in this standard's reading content
    for v in vocab:
        if len(out) >= n:
            break
        if v.get("term") and v["term"].lower() in hay:
            add(v["term"], v.get("termEs", ""), v.get("definition", ""))
    if len(out) >= n:
        return out[:n]
    # 3) the standard's OWN factcard concepts (topic-guaranteed)
    for fc in FC_BY_STD.get(code, []):
        for ch in fc.get("chunks", []):
            if len(out) >= n:
                break
            add(_vf_clean(ch.get("heading", "")),
                ch.get("headingEs", ""),
                ch.get("content", "") or fc.get("shortSummary", ""))
        if len(out) >= n:
            break
        add(_vf_clean(fc.get("title", "")), fc.get("titleEs", ""), fc.get("shortSummary", ""))
    if len(out) >= n:
        return out[:n]
    # 4) last resort so the Word Bank / Cornell supports are never empty
    for v in vocab:
        if len(out) >= n:
            break
        if v.get("term"):
            add(v["term"], v.get("termEs", ""), v.get("definition", ""))
    return out[:n]'''

FC_INJECT = '''ICAN = {s["standardCode"]: s for s in ican}

# Per-standard factcards — a topic-guaranteed fallback source for the Word Bank
# when the vocabulary bank under-covers a standard.
try:
    _factcards = json.load(open(f"{WEB}/factcards/unit-%d.json"))
except Exception:
    _factcards = []
FC_BY_STD = {}
for _f in _factcards:
    _m = re.match(r"fact-us(\\d+)", _f.get("id", ""))
    if _m:
        FC_BY_STD.setdefault("US.%%02d" %% int(_m.group(1)), []).append(_f)'''

for u in range(1, 11):
    ws = f"/home/user/Unit{u}_Claude_Core/analysis"
    p = os.path.join(ws, "derive_unit1_v2.py" if u == 1 else f"derive_unit{u}.py")
    if not os.path.exists(p):
        print(f"MISSING {p}"); continue
    s = open(p).read()
    if OLD not in s:
        print(f"!! vocab_for(current) not found in {p}"); continue
    s = s.replace(OLD, NEW)
    # inject factcard loader right after the ICAN line (once)
    if "FC_BY_STD" not in s.split("def _vf_clean")[0]:
        s = s.replace('ICAN = {s["standardCode"]: s for s in ican}',
                      FC_INJECT % u, 1)
    open(p, "w").write(s)
    print(f"patched {p}")
