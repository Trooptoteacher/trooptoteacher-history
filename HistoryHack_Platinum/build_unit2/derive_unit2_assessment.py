#!/usr/bin/env python3
"""Derive analysis/unit2_assessment.json (Formative + Summative Form A/B) for the
Unit 2 Assessment Book. Items are drawn from a COHERENCE-FILTERED pool per
standard: the ican file's own on-topic questions, plus DOK-bank items whose stem
matches that standard's distinctive terms (the raw bank standard-tags are loose
and mix topics, so filtering by distinctive keyword keeps every item on-standard).
All correct-answer positions are de-biased."""
import json, re
WEB = "/workspace/history-hack-web-app/public/data/us-history"
OUT = "/home/user/Unit2_Claude_Core/analysis"

ican = {s["standardCode"]: s for s in json.load(open(f"{WEB}/ican/unit-2.json"))}
ORDER = list(ican.keys())
dok = {}
for l in (1, 2, 3, 4):
    raw = json.load(open(f"{WEB}/questions/unit-2/dok-{l}.json"))
    dok[l] = raw["questions"] if isinstance(raw, dict) else raw

# Distinctive terms per standard (proper nouns + specific concepts). A bank item
# counts as on-standard only if its stem contains one of these.
DISTINCT = {
 "US.08": ["darwin", "social gospel", "gospel of wealth", "spencer", "rauschenbusch", "survival of the fittest", "fittest"],
 "US.09": ["booker", "washington", "du bois", "dubois", "atlanta compromise", "niagara", "naacp", "tuskegee"],
 "US.10": ["populis", "granger", "grange", "kelley", "free silver", "bryan", "farmers' alliance", "farmers alliance"],
 "US.11": ["labor union", "labor movement", "knights of labor", "afl", "gompers", "haymarket", "pullman", "homestead strike", "strike", "collective bargaining"],
 "US.12": ["trust", "monopol", "rockefeller", "standard oil", "sherman antitrust", "robber baron", "vertical integration", "horizontal integration"],
 "US.13": ["working condition", "child labor", "triangle shirtwaist", "sweatshop", "tenement", "women work", "factory condition"],
 "US.14": ["muckrak", "tarbell", "sinclair", "the jungle", "jacob riis", " riis", "la follette", "lincoln steffens", "ida "],
 "US.15": ["initiative", "referendum", "recall", "direct primary", "seventeenth amendment", "sixteenth amendment", "17th amendment", "16th amendment", "secret ballot"],
 "US.16": ["square deal", "trust-bust", "trustbust", "conservation", "national park", "meat inspection", "pure food", "roosevelt"],
 "US.17": ["new freedom", "federal reserve", "clayton antitrust", "underwood tariff", "federal trade commission", "wilson"],
 "US.18": ["suffrag", "nineteenth amendment", "19th amendment", "susan b. anthony", "stanton", "seneca falls", "carrie chapman catt", "harry burn", "perfect 36"],
}

def move(l, a, b):
    c = list(l); it = c.pop(a); c.insert(b, it); return c

def debias(options, ci, ti):
    n = len(options); ci = ci if 0 <= ci < n else 0; ti = max(0, min(ti, n - 1))
    order = move(list(range(n)), ci, ti)
    choices, key = [], None
    for i, oi in enumerate(order):
        L = chr(65 + i); choices.append({"id": L, "text": options[oi]})
        if oi == ci: key = L
    return choices, key

def norm_ican(q, std):
    return {"_id": q["id"], "std": std, "dok": q.get("dokLevel", 2),
            "stem": q["question"], "options": list(q["options"]),
            "ci": q["correctAnswer"], "why": q.get("explanation", ""), "rc": "History"}

def norm_bank(q, std):
    ch = q.get("choices") or []
    opts = [c.get("text", "") for c in ch]
    ids = [c.get("id") for c in ch]
    ca = q.get("correctAnswer")
    if ca not in ids:
        return None
    return {"_id": q["id"], "std": std, "dok": q.get("dokLevel", 2),
            "stem": q.get("stem", ""), "options": opts, "ci": ids.index(ca),
            "why": q.get("explanation", ""), "rc": q.get("reportingCategory", "History")}

def on_topic(stem, std):
    s = stem.lower()
    return any(k in s for k in DISTINCT[std])

def pool_for(std):
    seen, pool = set(), []
    for q in ican[std].get("questions", []):
        opts, ca = q.get("options"), q.get("correctAnswer")
        if isinstance(opts, list) and len(opts) == 4 and isinstance(ca, int):
            pool.append(norm_ican(q, std)); seen.add(q["question"].strip().lower())
    for l in (2, 3, 1, 4):
        for q in dok[l]:
            if std not in (q.get("standardCodes") or []):
                continue
            if q.get("itemType") != "mcq":
                continue
            if not on_topic(q.get("stem", ""), std):
                continue
            n = norm_bank(q, std)
            if not n or len(n["options"]) != 4:
                continue
            k = n["stem"].strip().lower()
            if k in seen:
                continue
            seen.add(k); pool.append(n)
    return pool

def emit(item, ti):
    choices, key = debias(item["options"], item["ci"], ti)
    dist = {}
    for c in choices:
        dist[c["id"]] = (item["why"] if c["id"] == key else "Common misconception — recheck the evidence.")
    sid = re.sub(r"[^A-Za-z0-9]", "", item["_id"])[-4:].upper()
    return {"id": f"{item['std']}-{sid}", "std": item["std"], "dok": item["dok"],
            "stem": item["stem"], "choices": choices, "key": key, "rc": item["rc"], "distract": dist}

formative, formA, formB = {}, [], []
report = []
for idx, std in enumerate(ORDER):
    pool = pool_for(std)
    # order: DOK-2 first for forms, keep a DOK-3 for form challenge
    pool.sort(key=lambda x: (x["dok"] != 2, x["dok"]))
    # formative: 2 items ; formA: next 3 ; formB: next 3 (distinct); wrap if short
    def take(seq, k, start):
        return [seq[(start + j) % len(seq)] for j in range(k)] if seq else []
    formative[std] = [emit(it, (i) % 4) for i, it in enumerate(take(pool, 2, 0))]
    formA += [emit(it, (idx + j) % 4) for j, it in enumerate(take(pool, 3, 2))]
    formB += [emit(it, (idx + j + 2) % 4) for j, it in enumerate(take(pool, 3, 5))]
    report.append((std, len(pool)))

out = {"unit": "Unit 2", "formative": formative, "formA": formA, "formB": formB,
       "disclosure": "Classroom-formative · pre-field-test (pre-calibration) — not a secure TCAP form. First administration is what calibrates these items."}
json.dump(out, open(f"{OUT}/unit2_assessment.json", "w"), ensure_ascii=False, indent=1)

print("pool sizes per standard:")
for std, n in report:
    print(f"  {std}: {n} on-topic items")
print(f"formative items: {sum(len(v) for v in formative.values())} | formA: {len(formA)} | formB: {len(formB)}")
from collections import Counter
print("formA key dist:", dict(Counter(i['key'] for i in formA)))
print("formB key dist:", dict(Counter(i['key'] for i in formB)))
