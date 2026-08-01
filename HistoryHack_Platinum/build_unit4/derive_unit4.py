#!/usr/bin/env python3
"""Derive analysis/unit4_content.json (+ exit tickets + images) for the Unit 2
Course Standard workbook, grounded entirely in the History Hack web app's
canonical data (ican reading content, vocabulary, primary-source bank, and the
DOK question bank). No facts are invented: passages come from the vetted
authored-synthesis reading content, assessment items come from the question
bank, TN connections come from the app's tennesseeConnection field.

Outputs match the schema build_workbook.js expects (see unit1_content.json)."""
import json, os, re

WEB = "/workspace/history-hack-web-app/public/data/us-history"
OUT = "/home/user/Unit4_Claude_Core/analysis"

ican = json.load(open(f"{WEB}/ican/unit-4.json"))
vocab = json.load(open(f"{WEB}/vocabulary/unit-4.json"))
psrc = json.load(open(f"{WEB}/primary-sources/unit-4.json"))
dok = {}
for lvl in (1, 2, 3, 4):
    raw = json.load(open(f"{WEB}/questions/unit-4/dok-{lvl}.json"))
    dok[lvl] = raw["questions"] if isinstance(raw, dict) else raw

ORDER = [s["standardCode"] for s in ican]           # US.08 … US.18
ICAN = {s["standardCode"]: s for s in ican}

# Per-standard factcards — a topic-guaranteed fallback source for the Word Bank
# when the vocabulary bank under-covers a standard.
try:
    _factcards = json.load(open(f"{WEB}/factcards/unit-4.json"))
except Exception:
    _factcards = []
FC_BY_STD = {}
for _f in _factcards:
    _sid = _f.get("standardId")
    if _sid:
        FC_BY_STD.setdefault(_sid, []).append(_f)

# ---- helpers ---------------------------------------------------------------

DIM_NAME = {"C": "Culture", "E": "Economics", "G": "Geography",
            "H": "History", "P": "Politics/Government", "T": "Tennessee Connection",
            "TCA": "Tennessee Connection"}

def move(lst, frm, to):
    c = list(lst)
    it = c.pop(frm)
    c.insert(to, it)
    return c

def debias_idx(options_list, correct_idx, target_idx):
    """Move the correct option (by index) to target_idx; reletter A..D in new
    order. Returns (options_dict, key_letter)."""
    n = len(options_list)
    if not (0 <= correct_idx < n):
        correct_idx = 0
    target_idx = max(0, min(target_idx, n - 1))
    order = move(list(range(n)), correct_idx, target_idx)
    newopts, newkey = {}, None
    for i, oi in enumerate(order):
        L = chr(ord("A") + i)
        newopts[L] = options_list[oi]
        if oi == correct_idx:
            newkey = L
    return newopts, newkey

def ican_questions(code, dok_level=None):
    """The ican file's OWN questions for a standard (topic-aligned with its
    reading content). The separate DOK bank is NOT used: its standard tagging
    disagrees with the ican file for several standards, which would pair (e.g.)
    a Social Darwinism reading with a Boss Tweed quiz."""
    qs = ICAN[code].get("questions", [])
    out = []
    for q in qs:
        opts = q.get("options")
        ca = q.get("correctAnswer")
        if not (isinstance(opts, list) and len(opts) >= 3 and isinstance(ca, int) and 0 <= ca < len(opts)):
            continue
        if dok_level is not None and q.get("dokLevel") != dok_level:
            continue
        out.append(q)
    return out

def _vf_clean(t):
    t = (t or "").strip()
    t = t.split(":")[0].strip()   # drop subtitles like "Tet Offensive: Psychological Victory"
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
        key = re.sub(r"\s*\([^)]*\)", "", term).strip().lower()
        if term and key and key not in have:
            out.append({"term": term, "say": "", "es": es or "", "def": defn or ""})
            have.add(key)
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
    # 3) the standard's OWN factcards. Keep a factcard only if it is really about
    #    THIS standard (a distinctive word from its title/summary appears in the
    #    passage) — drops mis-tagged factcards — then use its title + chunk
    #    headings, skipping generic sub-headings.
    _GEN = {"crisis", "success", "growth", "impact", "limitations", "culture",
            "rebellion", "benefits", "harm", "scale", "origins", "legacy",
            "background", "controversy", "revelations", "shooting", "structure",
            "overview", "vaccine", "highways", "development", "results",
            "requirements", "conditions", "decision", "leaders", "accusations",
            "revolution", "attacks", "causes", "economic power", "historic election",
            "push factors", "core philosophy", "social impact", "reasons for founding",
            "before the war", "use against japan", "lasting impact", "requirements",
            "workforce entry", "military service", "surprise attack", "the leak"}
    _CW = {"victory", "america", "american", "transform", "national", "three",
           "world", "first", "other", "great", "modern", "impact", "history",
           "people", "states", "united", "century", "における"}
    def _fc_relevant(fc):
        words = re.findall(r"[a-z]{5,}", (fc.get("title", "") + " " + fc.get("shortSummary", "")).lower())
        return any(w not in _CW and w in hay for w in words)
    for fc in FC_BY_STD.get(code, []):
        if not _fc_relevant(fc):
            continue
        _chunks = fc.get("chunks", [])
        cands = []
        for ch in _chunks:
            cands.append((_vf_clean(ch.get("heading", "")), ch.get("headingEs", ""),
                          ch.get("content", "") or fc.get("shortSummary", "")))
        if not _chunks:
            cands.append((_vf_clean(fc.get("title", "")), fc.get("titleEs", ""), fc.get("shortSummary", "")))
        for term, es, defn in cands:
            if len(out) >= n:
                break
            if term and term.lower() not in _GEN:
                add(term, es, defn)
        if len(out) >= n:
            break
    # 4) only if still almost empty, pad from the bank (prefer 2 correct terms
    #    over adding a wrong 3rd) so the Word Bank / Cornell is never empty
    if len(out) < 2:
        for v in vocab:
            if len(out) >= 2:
                break
            if v.get("term"):
                add(v["term"], v.get("termEs", ""), v.get("definition", ""))
    return out[:n]

def sources_for(code, n=2):
    out = []
    for p in psrc:
        if p.get("standardId") != code:
            continue
        cite = p.get("citation") or {}
        repo = ""
        if isinstance(cite, dict):
            repo = cite.get("repository") or cite.get("mlaCitation", "")
        out.append({
            "title": p.get("documentTitle", "Primary source"),
            "who": p.get("author") or "Unknown",
            "date": str(p.get("date") or ""),
            "quote": (p.get("excerpt") or "")[:240],
            "repo": (repo or "Public domain")[:160],
            "url": p.get("sourceUrl") or "",
        })
        if len(out) >= n:
            break
    return out

def close_passage(s):
    secs = s.get("readingContent", {}).get("sections", [])
    return " ".join(x.get("content", "").strip() for x in secs).strip()

def close_sections(s):
    """The authored reading kept as titled chunks (heading + paragraph) so the
    Close Read renders in readable sections, not one wall of text."""
    out = []
    for sec in s.get("readingContent", {}).get("sections", []):
        h = (sec.get("heading") or "").strip()
        c = (sec.get("content") or "").strip()
        if c:
            out.append([h, c])
    return out

def tdqs(s):
    secs = s.get("readingContent", {}).get("sections", [])
    q = []
    for sec in secs[:3]:
        h = (sec.get("heading") or "").strip().rstrip(".")
        if h:
            q.append(f"What is the main idea of the “{h}” section, and what evidence supports it?")
    q.append("Whose perspective benefits in this passage, and whose is harmed or left out?")
    return q[:4]

def cues_from(s):
    secs = s.get("readingContent", {}).get("sections", [])
    cues = []
    for sec in secs[:3]:
        h = sec.get("heading", "").strip().rstrip(".")
        if h:
            cues.append(f"What does the passage say about {h[0].lower() + h[1:]}?")
    cues.append("Key terms →")
    return cues

def lenses_str(tags):
    dims = [DIM_NAME[t] for t in tags if t in DIM_NAME]
    # dedupe preserve order
    seen, out = set(), []
    for d in dims:
        if d not in seen:
            seen.add(d); out.append(d)
    return " · ".join(out) if out else "History (H)"

# ---- de-bias target positions: balanced A,B,C,D across the 11 CFUs ---------
targets = [i % 4 for i in range(len(ORDER))]   # 0,1,2,3,0,1,2,3,0,1,2

content = {
    "unit": {
        "code": "Unit 4",
        "title": "The 1920s (1920–1929)",
        "standards_range": "US.28–US.38",
        "publisher": "TroopToTeacher Technologies LLC",
        "footer": "U.S. History Hack · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards & TCAP EOC",
    },
    "standards": {},
    "order": ORDER,
}
exit_tickets = {}
used_item_ids = {}

for idx, code in enumerate(ORDER):
    s = ICAN[code]
    tags = s.get("strands") or []
    tn_raw = s.get("tnStandard", "")
    tn_text = re.sub(r"^US\.\d+\s*[–\-:]\s*", "", tn_raw).strip()
    ic = s.get("iCanText", "")
    ic_body = re.sub(r"^I can\s*", "", ic).strip().rstrip(".")

    used = set()
    dok3 = ican_questions(code, 3)
    dok2 = ican_questions(code, 2)

    # CFU = the DOK-3 item (fallback DOK-2), de-biased to its balanced position.
    cfu = None
    cfu_src = (dok3 or dok2)
    if cfu_src:
        q = cfu_src[0]; used.add(q["id"])
        opts, key = debias_idx(q["options"], q["correctAnswer"], targets[idx])
        cfu = {"dok": q.get("dokLevel", 3), "stem": q["question"], "options": opts,
               "key": key, "why": q.get("explanation", "")}

    # Exit ticket = a distinct DOK-2 item (fallback DOK-3), de-biased.
    et_src = [q for q in dok2 + dok3 if q["id"] not in used]
    if et_src:
        q = et_src[0]; used.add(q["id"])
        opts, key = debias_idx(q["options"], q["correctAnswer"], (targets[idx] + 2) % 4)
        exit_tickets[code] = {"id": q["id"], "stem": q["question"], "dok": q.get("dokLevel", 2),
                              "choices": [{"id": k, "text": v} for k, v in opts.items()],
                              "correct": key, "reportingCategory": "History"}

    # Quiz = remaining DOK-2 items, de-biased individually.
    quiz = []
    for j, q in enumerate([x for x in dok2 if x["id"] not in used][:3]):
        opts, key = debias_idx(q["options"], q["correctAnswer"], j % 4)
        quiz.append({"id": q["id"], "dok": q.get("dokLevel", 2), "stem": q["question"],
                     "opts": opts, "key": key})
    # LEVELING: guarantee >=2 quiz items so every Practice Quiz is a consistent
    # length. Thin standards are supplemented from the question bank, filtered to
    # the standard's distinctive TITLE terms so supplements stay on-topic.
    if len(quiz) < 2:
        stop = {"their","this","that","from","with","into","over","american","history",
                "united","states","movement","policies","developments","reasons","causes",
                "impact","society","early","during","other","between","people","world"}
        kw = {w for w in re.findall(r"[a-z]{4,}", ICAN[code].get("title","").lower()) if w not in stop}
        qids = {x["id"] for x in quiz} | set(used)
        for lvl in (2, 1):
            for q in dok.get(lvl, []):
                if len(quiz) >= 2:
                    break
                if q.get("itemType") != "mcq" or q.get("id") in qids:
                    continue
                ch = q.get("choices"); ca = q.get("correctAnswer")
                if not (isinstance(ca, str) and len(ca) == 1 and isinstance(ch, list) and len(ch) >= 3):
                    continue
                if not any(k in q.get("stem", "").lower() for k in kw):
                    continue
                ids = [c.get("id") for c in ch]
                if ca not in ids:
                    continue
                opts, key = debias_idx([c.get("text", "") for c in ch], ids.index(ca), len(quiz) % 4)
                quiz.append({"id": q["id"], "dok": q.get("dokLevel", 2), "stem": q["stem"],
                             "opts": opts, "key": key})
                qids.add(q["id"])

    voc = vocab_for(code, 3)
    frayer = [v["term"] for v in voc[:2]] or [s.get("title", code)]

    tnc = s.get("tennesseeConnection") or {}
    tn_conn = tnc.get("text", "").strip() if tnc.get("hasTennesseeConnection") else ""

    # Geographic tasks where a standard has a real spatial dimension (the
    # Progressive-era standards aren't map-heavy like Unit 1's westward
    # expansion, so we add them only where they're grounded and meaningful).
    GEO_TASKS = {
        "US.28": "The Great Migration moved millions of Black Americans out of the rural South to Northern and Midwestern cities. Use the list below to map where people left and where they went, then explain the pattern.",
    }
    GEO_PLACES = {
        "US.28": [
            ["Rural South (Mississippi, Alabama, Georgia)", "The South", "origin — sharecropping, Jim Crow, and racial violence"],
            ["Chicago", "Illinois", "destination — meatpacking and factory jobs"],
            ["Detroit", "Michigan", "destination — automobile-industry jobs"],
            ["Harlem / New York City", "New York", "destination — center of the Harlem Renaissance"],
            ["Cleveland", "Ohio", "destination — industrial jobs"],
        ],
        "US.30": [
            ["Nashville, Tennessee", "Middle Tennessee", "WSM Radio’s barn-dance program began here in Dec 1925 and was named the Grand Ole Opry in 1927 — radio made it a national institution"],
            ["Memphis, Tennessee", "West TN (Mississippi River)", "Beale Street blues district; W.C. Handy, “Father of the Blues,” published “The Memphis Blues” (1912) here"],
            ["Chattanooga, Tennessee", "Southeast Tennessee", "Birthplace (1894) of Bessie Smith, the “Empress of the Blues”"],
            ["Bristol, Tennessee/Virginia", "Northeast TN (Appalachia)", "The July 1927 Bristol Sessions — the “big bang” of country music (Carter Family, Jimmie Rodgers)"],
            ["Mississippi Delta", "Lower Mississippi River", "Rural roots of the blues that traveled up the river to Memphis, onto records and radio"],
        ],
    }
    GEO_SOURCES = {
        "US.30": [
            "Grand Ole Opry / WSM — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/grand-ole-opry/",
            "William Christopher “W.C.” Handy — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/william-christopher-handy/",
            "Bessie Smith — Encyclopædia Britannica: https://www.britannica.com/biography/Bessie-Smith",
            "Bristol Sessions — Tennessee Encyclopedia: https://tennesseeencyclopedia.net/entries/bristol-sessions/",
        ],
    }
    geo = GEO_TASKS.get(code, "")
    geo_places = GEO_PLACES.get(code, [])
    geo_sources = GEO_SOURCES.get(code, [])
    geo_review = ({"status": "drafted", "by": "", "date": "",
                   "note": "Places drafted from the standard's official TN text and criteria; anchor facts verified against the cited sources. Pending SME sign-off."}
                  if geo_sources else {"status": "n/a", "by": "", "date": "", "note": ""})
    if not geo and "G" in tags:
        geo = f"On a map, locate the places named in this standard ({s.get('title','')}) and mark where the key events happened."

    dim_map = {}
    for t in tags:
        if t in DIM_NAME and DIM_NAME[t] not in ("Tennessee Connection",):
            secs = s.get("readingContent", {}).get("sections", [])
            dim_map[t] = f"{DIM_NAME[t]} lens on {s.get('title','this standard')}: " + \
                (secs[0]["content"][:110] + "…" if secs else "")

    content["standards"][code] = {
        "title": s.get("title", code),
        "tn": tn_text,
        "ican": ic,
        "ref": {"range": "—", "dt": "—", "vocab": "—", "source": "—",
                "persp": "—", "progress": "—"},
        "vocab": voc,
        "sources": sources_for(code, 2),
        "cfu": cfu or {"dok": 3, "stem": f"Which statement best explains {s.get('title','this standard')}?",
                       "options": {"A": "", "B": "", "C": "", "D": ""}, "key": "A", "why": ""},
        "auth": {
            "close": close_passage(s),
            "close_sections": close_sections(s),
            "tdq": tdqs(s),
            "frayer": frayer,
            "quiz": quiz,
            "cer": f"Claim + Evidence + Reasoning: Using this standard, take a position on the central question — {ic_body}? Support your claim with two pieces of evidence from the passage and explain your reasoning.",
        },
        "std_source": "Tennessee U.S. History Academic Standards (aligned)",
        "target": ic_body,
        "targets": [ic_body],
        "criteria": [sec.get("heading", "") for sec in s.get("readingContent", {}).get("sections", [])[:3]],
        "cues": cues_from(s),
        "lenses": lenses_str(tags),
        "dim_map": dim_map,
        "geo": geo,
        "geo_places": geo_places,
        "geo_sources": geo_sources,
        "geo_review": geo_review,
        "tn_connection": tn_conn,
        "hook": f"{s.get('title','This standard')}: {tn_text.rstrip('.')}. Who gained, who was left out — and why does it still matter?",
    }

json.dump(content, open(f"{OUT}/unit4_content.json", "w"), ensure_ascii=False, indent=1)
json.dump(exit_tickets, open(f"{OUT}/unit4_exit_tickets.json", "w"), ensure_ascii=False, indent=1)
# NOTE: unit4_images.json is produced by build_unit2_images.py — do NOT clobber it here.

# ---- report ----------------------------------------------------------------
print(f"standards: {len(content['standards'])}")
for code in ORDER:
    st = content["standards"][code]
    q = len(st["auth"]["quiz"]); v = len(st["vocab"]); src = len(st["sources"])
    cfu_ok = "Y" if st["cfu"].get("stem") and st["cfu"]["options"].get("A") else "n"
    et = "Y" if code in exit_tickets else "n"
    cl = len(st["auth"]["close"])
    print(f"  {code} {st['title'][:34]:34} vocab={v} quiz={q} src={src} cfu={cfu_ok} exit={et} close={cl}c tn={'Y' if st['tn_connection'] else 'n'}")
# de-bias distribution of CFU keys
from collections import Counter
print("CFU key positions:", dict(Counter(content['standards'][c]['cfu']['key'] for c in ORDER)))
