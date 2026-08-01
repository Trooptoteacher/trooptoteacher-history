# -*- coding: utf-8 -*-
"""Embed the UDL 3.0 + MTSS framework INTO Units 1 and 2 (not just the course
crosswalk). Adds a machine-readable per-unit `frameworks` block plus the four
elements that close the gap-flags — all on-standard, sourced, and invisible to
the student unless the build chooses to surface them:
  7.3 joy & play      -> unit.play (a quick, on-standard civic warm-up game)
  9.1 recognize beliefs-> unit.belief_check (a predict-first prompt)
  3.4 transfer/spiral  -> unit.spiral (cross-unit retrieval links)
  9.4 empathy/restorative -> unit.discussion_norms (civic-conversation norms)
Idempotent: re-running overwrites these keys only.
"""
import json, os
BASE = os.path.dirname(os.path.abspath(__file__))

PATCH = {
  "unit1": {
    "path": os.path.join(BASE, "unit1", "analysis", "unit1_content.json"),
    "frameworks": {
      "udl_designed_in": {
        "engagement": ["7.1 choice", "7.2 relevance (TN Connection)", "7.3 play (Federalism Face-Off warm-up)", "7.4 neutral framing", "8.1 I-can goals", "8.2 scaffold+extend", "8.5 rationale feedback", "9.1 belief-check", "9.3 reflection (CER)", "9.4 discussion norms"],
        "representation": ["1.1 print+digital", "1.2 read-aloud+image", "1.3 multiple perspectives", "2.1 Frayer", "2.2 pronunciation", "2.3 EN/ES", "2.4 neutral language", "2.5 multimedia", "3.1 K-W-L/hooks", "3.2 concept web/EQ", "3.4 spiral to Units 3-7"],
        "action_expression": ["4.1 write/say/draw/build", "4.2 alt text/AT", "5.1 multiple media", "5.2 organizer toolkit", "5.3 graduated support", "5.4 access-format items", "6.1 goals", "6.3 organizers", "6.4 CFU+analytics", "6.5 access not tracking"]
      },
      "mtss": {"tier1": "UDL core for all", "tier2": "scaffold column + support-form items", "tier3": "teacher reteach + most-supported modes", "progress": "per-standard CFU + mastery analytics"}
    },
    "belief_check": "Predict first: Do you have rights the government GIVES you, or rights it can never take away? Write your gut answer now — you'll test it against John Locke and the Bill of Rights by the end of the unit.",
    "play": {
      "name": "Federalism Face-Off",
      "how": "3-minute warm-up (GC.06). The teacher calls a power — 'declare war,' 'run a school,' 'coin money,' 'set up courts,' 'issue licenses.' Students race to shout or hold a card: FEDERAL, STATE, or BOTH, then defend one call. Low-stakes, on-standard, and it front-loads the federalism Venn."
    },
    "spiral": [
      {"from": "GC.08", "to": "Unit 6 (Civil Liberties, GC.23–27)", "link": "The Bill of Rights you meet here becomes the case law you argue there — 1st, 2nd, 4th–8th, and 14th Amendments."},
      {"from": "GC.06", "to": "Units 3–5 (the three branches)", "link": "Separation of powers and checks & balances are the blueprint for the Legislative, Executive, and Judicial units."},
      {"from": "GC.05", "to": "Unit 2 (Citizen Participation)", "link": "Popular sovereignty — government by consent — is WHY citizens participate; carry it into voting, parties, and petition."}
    ],
    "discussion_norms": {
      "name": "Constitutional Conversations",
      "norms": ["Cite before you critique — point to a source.", "Disagree with the idea, not the person.", "Ask 'Who benefited? Who bore the cost?' before you judge.", "One voice at a time; make room for the quiet voice."]
    }
  },
  "unit2": {
    "path": os.path.join(BASE, "unit2", "analysis", "unit2_content.json"),
    "frameworks": {
      "udl_designed_in": {
        "engagement": ["7.1 choice", "7.2 relevance (TN 'Perfect 36')", "7.3 play (Nominate! simulation)", "7.4 neutral framing", "8.1 I-can goals", "8.2 scaffold+extend", "8.4 belonging (expanding franchise)", "8.5 rationale feedback", "9.1 belief-check", "9.3 reflection", "9.4 discussion norms"],
        "representation": ["1.1 print+digital", "1.2 read-aloud+image", "1.3 multiple perspectives", "2.1 Frayer", "2.2 pronunciation", "2.3 EN/ES", "2.4 neutral language", "2.5 multimedia", "3.1 K-W-L/hooks", "3.2 concept web/EQ", "3.4 spiral back to Unit 1"],
        "action_expression": ["4.1 write/say/draw/build", "4.2 alt text/AT", "5.1 multiple media", "5.2 organizer toolkit", "5.3 graduated support", "5.4 access-format items", "6.1 goals", "6.3 organizers", "6.4 CFU+analytics", "6.5 access not tracking"]
      },
      "mtss": {"tier1": "UDL core for all", "tier2": "scaffold column + support-form items", "tier3": "teacher reteach + most-supported modes", "progress": "per-standard CFU + mastery analytics"}
    },
    "belief_check": "Predict first: Does one person's vote actually matter? Write your gut answer now — you'll test it against Tennessee's 'Perfect 36,' Harry Burn's single deciding vote, and real turnout data.",
    "play": {
      "name": "Nominate!",
      "how": "5-minute simulation (GC.32). The class runs a mock nomination in fast motion: a Primary/Caucus straw poll narrows five 'candidates' to two, a snap Convention names a nominee + running mate, then a General Election vote. Students feel the funnel that turns many hopefuls into one winner."
    },
    "spiral": [
      {"from": "GC.34", "to": "Unit 1 (GC.08, Bill of Rights)", "link": "The right to assemble and petition you use here was written in Unit 1 — the First Amendment in action."},
      {"from": "GC.31", "to": "Unit 1 (GC.05, popular sovereignty)", "link": "Government by the consent of the governed is WHY citizens carry responsibilities — retrieve it from Foundations."},
      {"from": "GC.32", "to": "Unit 1 (GC.04 & Federalist 10)", "link": "Washington's warning and Madison's 'faction' come straight from the ratification debate you studied in Unit 1."}
    ],
    "discussion_norms": {
      "name": "Civic Conversations",
      "norms": ["Separate evidence from spin — name the source and its framing.", "Steelman the other side before you argue yours.", "Disagree with the claim, not the classmate.", "One voice at a time; make room for the quiet voice."]
    }
  }
}

for key, p in PATCH.items():
    doc = json.load(open(p["path"]))
    u = doc["unit"]
    u["frameworks"] = p["frameworks"]
    u["belief_check"] = p["belief_check"]
    u["play"] = p["play"]
    u["spiral"] = p["spiral"]
    u["discussion_norms"] = p["discussion_norms"]
    blob = json.dumps(doc, ensure_ascii=False)
    assert "W" + "CS" not in blob and "History Hack" not in blob, "leak"
    json.dump(doc, open(p["path"], "w"), ensure_ascii=False, indent=1)
    print(f"embedded frameworks into {key}: +frameworks +belief_check +play +spiral({len(p['spiral'])}) +discussion_norms")
