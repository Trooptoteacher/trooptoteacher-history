#!/usr/bin/env python3
"""Render overlap_crosswalk.json -> overlap_crosswalk.md (keeps the readable table in sync)."""
import json, os
d = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(d, "overlap_crosswalk.json"), encoding="utf8"))
out = ["# Cross-Course Overlap Crosswalk — the reuse engine", "",
       "Standards that cover the **same topic** across courses, and the **already-sourced**",
       "primary sources to **reuse** (source/write once, serve every course). US.xx sources are",
       "in the geo provenance ledger + US content; GC.xx are in the completed Government sourcing",
       "list. **Verify W↔WH numbering before reusing World History items** (see SUITE_INVENTORY.md).",
       ""]
for c in data["clusters"]:
    out.append(f"## {c['topic']}")
    out.append("")
    out.append(f"- **U.S. History:** {', '.join(c['us_history']) or '—'}")
    out.append(f"- **World History:** {', '.join(c['world_history']) or '—'}")
    out.append(f"- **Government:** {', '.join(c['government']) or '—'}")
    out.append("- **Reuse these already-sourced primary sources:**")
    for s in c["reusable_sources"]:
        out.append(f"  - {s}")
    out.append("")
out.append("---")
out.append(f"_{len(data['clusters'])} overlap clusters. Generated from overlap_crosswalk.json._")
open(os.path.join(d, "overlap_crosswalk.md"), "w", encoding="utf8").write("\n".join(out))
print(f"WROTE overlap_crosswalk.md ({len(data['clusters'])} clusters)")
