#!/usr/bin/env python3
"""Build the combined Unit 1 Lean Teacher Answer Key (markdown -> PDF) for US.01-US.07.
Pulls Three Perspectives model answers, primary-source excerpts + sourcing (WHO/WHEN/WHY),
and the We Do / Tennessee model from the locked _build.json (summary-labels only)."""
import json, subprocess, os
from collections import OrderedDict

BASE = "/home/user/workspace"
D = json.load(open(f"{BASE}/unit1-lean-full/_build.json"))
OUTDIR = f"{BASE}/hh-web/public/downloads/tcap-decks/unit-1-lean"
MD = f"{BASE}/Unit1_Lean_Teacher_Answer_Key.md"
PDF_OUT = f"{OUTDIR}/Unit1_Lean_Teacher_Answer_Key.pdf"

STD_TITLE = {
    "US.01": "Homestead Act & Transcontinental Railroad",
    "US.02": "Federal Policies Toward American Indians",
    "US.03": "Compromise of 1877, Jim Crow & Plessy v. Ferguson",
    "US.04": "Gilded Age Politics & Economics",
    "US.05": "Inventions & Business Leaders",
    "US.06": "Industrial Centers & Urbanization",
    "US.07": "Immigration: Old vs. New",
}

by_std = OrderedDict()
for s in D["slides"]:
    by_std.setdefault(s["standard"], []).append(s)

def pval(p):
    return p.get("answer") or p.get("us01") or ""

lines = []
lines.append("# U.S. History Hack — Unit 1 Lean Student Deck")
lines.append("## Teacher Answer Key · Standards US.01–US.07")
lines.append("")
lines.append("**Product:** Unit 1 Lean Student Deck · 48 slides · 16:9  ")
lines.append("**Publisher:** TroopToTeacher Technologies LLC · U.S. History Hack  ")
lines.append("**Aligned to:** TN Academic Standards & TCAP EOC · Unit 1 (US.01–US.07)  ")
lines.append("**Version:** 2.0 · Last updated 2026-07-01")
lines.append("")
lines.append("This key gives model answers for the **Three Perspectives synthesis** and **Source It First** "
             "prompts on every standard, plus the We Do and Tennessee Connection models for US.01. Narrative "
             "content is a summary-label of the locked v3.2 / v2.9 curriculum; all Spanish scaffolding, DOK-tiered "
             "checks, and full teacher notes live in the full Unit 1 TCAP lecture deck and teacher's guide.")
lines.append("")
lines.append("The **Three Perspectives** framework is fixed wording used across the whole app: "
             "*Who benefited? · Who bore the costs? · Who decided?* Return to these three questions to analyze "
             "any event, policy, or decision.")
lines.append("")

for std, ss in by_std.items():
    lines.append("---")
    lines.append("")
    lines.append(f"## {std} — {STD_TITLE.get(std, '')}")
    lines.append("")
    ps = next((s for s in ss if s["kind"] == "Primary Source Analysis"), None)
    tp = next((s for s in ss if s["kind"] == "Three Perspectives Synthesis"), None)

    # US.01 opens the whole unit with the Hook question — answer it here.
    if std == "US.01":
        hook = next((s for s in ss if s["kind"] == "Hook"), None)
        if hook:
            lines.append("### Unit Hook (Slide 1)")
            lines.append(f"**Question:** *{hook.get('assertion','')}*")
            lines.append("")
            lines.append("**Exemplar answer:** Settling the continent required the federal government to give away "
                         "land and resources it treated as \u201cempty\u201d \u2014 through the Homestead Act (160-acre grants) and "
                         "the Pacific Railway Act (alternate-section grants and subsidies to the railroads). Those who "
                         "benefited were settlers, railroad corporations, and eastern markets. The price was paid by the "
                         "people already there: Plains Indian nations lost land, treaty rights, and the buffalo herds their "
                         "economies depended on, and Chinese laborers did the most dangerous railroad work for low pay while "
                         "facing discrimination. **A strong answer names both a beneficiary and someone who bore the cost, "
                         "and cites specific evidence** (a law, a group, or a consequence). This is the thread the unit "
                         "returns to across all seven standards.")
            lines.append("")
            lines.append("*Facilitation:* 10-sec silent think \u2192 60-sec Turn & Talk \u2192 cold-call 2\u20133 pairs. Accept a range "
                         "of responses on the opening pass; students refine the answer with evidence as the unit unfolds.")
            lines.append("")

    if ps:
        lines.append("### Source It First")
        sif = ps.get("sourceItFirst", {})
        if sif:
            lines.append(f"- **WHO:** {sif.get('who','')}")
            lines.append(f"- **WHEN:** {sif.get('when','')}")
            lines.append(f"- **WHY it matters:** {sif.get('why','')}")
            lines.append("")
        for src in ps.get("sources", []):
            lines.append(f"**{src.get('title','')}** — {src.get('author','')}, {src.get('date','')}")
            lines.append(f"> {src.get('excerpt','')}")
            lines.append(f"Source: [{src.get('archiveName','')}]({src.get('url','')})")
            lines.append("")
        assertion = ps.get("assertion", "")
        if assertion:
            lines.append(f"**Analyze prompt (summary-label):** {assertion}")
            lines.append("")

    if tp:
        lines.append("### Three Perspectives — model answers")
        for p in tp.get("perspectives", []):
            lines.append(f"**{p.get('lens','')}** — *{p.get('prompt','')}*")
            lines.append(f"{pval(p)}")
            lines.append("")

    # US.01 extras: We Do + Tennessee
    if std == "US.01":
        wd = next((s for s in ss if s["kind"] == "We Do"), None)
        if wd:
            lines.append("### We Do (model chain)")
            chain = wd.get("chain") or wd.get("model") or ""
            if isinstance(chain, list):
                chain = " → ".join(chain)
            lines.append(f"Cause → effect → consequence: **{chain if chain else 'railroad → collapse of the buffalo herds → forced relocation of Plains nations.'}**")
            lines.append("Model one link aloud, then students complete two more (e.g. free land → rapid settlement → treaty violations; new rail markets → cash-crop farming → farmer debt).")
            lines.append("")
        tn = next((s for s in ss if s["kind"] == "Tennessee Connection"), None)
        if tn:
            lines.append("### Tennessee Connection")
            lines.append("**George Jordan of Triune, Williamson County** — the only Medal of Honor recipient from "
                         "Williamson County. A formerly enslaved man who served with the 9th Cavalry (Buffalo Soldiers), "
                         "he earned the Medal of Honor for defending Fort Tularosa (1880). Locate Triune on the 1878 county map.")
            lines.append("")

lines.append("---")
lines.append("")
lines.append("## Sourcing & verification")
lines.append("")
lines.append("All imagery and quoted documents are public-domain, drawn from the Library of Congress, National "
             "Archives, National Park Service, Internet Archive, Wikimedia Commons, and the Tennessee State Library "
             "& Archives — captioned on-slide and cited in the History Hack primary-source catalog. Narrative content "
             "is locked at v3.2 (US.01) / repo v2.9 (US.02–US.07), expert-panel reviewed.")
lines.append("")
lines.append("© 2026 TroopToTeacher Technologies LLC. Proprietary. All rights reserved.")
lines.append("")

open(MD, "w").write("\n".join(lines))
print("Wrote markdown:", MD, "(", len(lines), "lines )")

# Render PDF via the deck-builder's make_key_pdf.py if present, else fallback to a simple reportlab render
KEY_SCRIPT = f"{BASE}/skills/user/history-hack-tcap-deck-builder/scripts/make_key_pdf.py"
print("make_key_pdf exists:", os.path.exists(KEY_SCRIPT))
