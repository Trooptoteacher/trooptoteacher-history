#!/usr/bin/env python3
"""Derive analysis/unit1_assessment.json (Formative + Summative Form A/B) for the
Unit 2 Assessment Book. Items are drawn from a COHERENCE-FILTERED pool per
standard: the ican file's own on-topic questions, plus DOK-bank items whose stem
matches that standard's distinctive terms (the raw bank standard-tags are loose
and mix topics, so filtering by distinctive keyword keeps every item on-standard).
All correct-answer positions are de-biased."""
import json, re
WEB = "/workspace/history-hack-web-app/public/data/us-history"
OUT = "/home/user/Unit1_Claude_Core/analysis"

ican = {s["standardCode"]: s for s in json.load(open(f"{WEB}/ican/unit-1.json"))}
ORDER = list(ican.keys())
dok = {}
for l in (1, 2, 3, 4):
    raw = json.load(open(f"{WEB}/questions/unit-1/dok-{l}.json"))
    dok[l] = raw["questions"] if isinstance(raw, dict) else raw

# Distinctive terms per standard (proper nouns + specific concepts). A bank item
# counts as on-standard only if its stem contains one of these.
DISTINCT = {
 "US.01": ["homestead act", "transcontinental railroad", "golden spike", "promontory", "westward expansion", "great plains", "homesteader", "land grant", "pacific railway"],
 "US.02": ["dawes act", "reservation", "wounded knee", "sitting bull", "sand creek", "assimilation", "boarding school", "plains indian", "little bighorn", "ghost dance", "buffalo"],
 "US.03": ["compromise of 1877", "jim crow", "plessy", "separate but equal", "poll tax", "literacy test", "sharecrop", "disenfranchise", "grandfather clause", "redeemers"],
 "US.04": ["gilded age", "political machine", "boss tweed", "tammany", "patronage", "spoils system", "civil service", "pendleton", "robber baron", "laissez-faire", "monopoly", "trust"],
 "US.05": ["edison", "light bulb", "telephone", "bell", "bessemer", "steel", "carnegie", "rockefeller", "standard oil", "vertical integration", "horizontal integration"],
 "US.06": ["urbanization", "tenement", "ellis island", "slum", "jacob riis", "settlement house", "hull house", "skyscraper", "how the other half lives", "streetcar"],
 "US.07": ["old immigrant", "new immigrant", "angel island", "nativism", "chinese exclusion", "southern and eastern europe", "melting pot", "steerage", "assimilat"],
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

out = {"unit": "Unit 4", "formative": formative, "formA": formA, "formB": formB,
       "disclosure": "Classroom-formative · pre-field-test (pre-calibration) — not a secure TCAP form. First administration is what calibrates these items."}
json.dump(out, open(f"{OUT}/unit1_assessment.json", "w"), ensure_ascii=False, indent=1)

print("pool sizes per standard:")
for std, n in report:
    print(f"  {std}: {n} on-topic items")
print(f"formative items: {sum(len(v) for v in formative.values())} | formA: {len(formA)} | formB: {len(formB)}")
from collections import Counter
print("formA key dist:", dict(Counter(i['key'] for i in formA)))
print("formB key dist:", dict(Counter(i['key'] for i in formB)))
