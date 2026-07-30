#!/usr/bin/env python3
"""Replace vocab_for() in every unit's derive script so the Word Bank is sourced
from terms that actually appear in the standard's OWN reading content — fixing
both under-tagging (borrowed wrong-topic terms) and source mis-tagging
(e.g. "Dawes Act" tagged to the Inventions standard)."""
import re, glob, os

OLD = '''def vocab_for(code, n=3):
    out = []
    for v in vocab:
        if code in (v.get("relatedStandards") or []) and v.get("term"):
            out.append({"term": v["term"], "say": "", "es": v.get("termEs", ""),
                        "def": v.get("definition", "")})
        if len(out) >= n:
            break
    # Fallback: a debate/perspective standard (e.g. US.20) may have no tagged
    # terms. Borrow from the rest of the unit's vocab so the Word Bank + Cornell
    # supports are never empty (all unit terms are same-era, so on-topic enough).
    if len(out) < 3:
        have = {o["term"] for o in out}
        for v in vocab:
            if v.get("term") and v["term"] not in have:
                out.append({"term": v["term"], "say": "", "es": v.get("termEs", ""),
                            "def": v.get("definition", "")})
                have.add(v["term"])
            if len(out) >= max(3, n):
                break
    return out'''

NEW = '''def vocab_for(code, n=3):
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

scripts = []
for u in range(1, 11):
    ws = f"/home/user/Unit{u}_Claude_Core/analysis"
    for name in (f"derive_unit{u}.py", "derive_unit1_v2.py"):
        p = os.path.join(ws, name)
        if os.path.exists(p):
            scripts.append(p)

for p in scripts:
    s = open(p).read()
    if "def vocab_for" not in s:
        continue
    if OLD in s:
        s = s.replace(OLD, NEW)
        open(p, "w").write(s)
        print(f"patched {p}")
    elif "appears in THIS standard" in s:
        print(f"already patched {p}")
    else:
        print(f"!! vocab_for shape differs, NOT patched: {p}")
