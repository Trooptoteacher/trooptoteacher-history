import json, os, re
ROOT="/home/user/trooptoteacher-history"
OUT=os.path.join(ROOT,"standards-2026-27")
os.makedirs(os.path.join(OUT,"standards"),exist_ok=True)

# (out_name, level, source_path, provenance, verified)
LIST_SRC=[
 ("grade-06-world-history-geography","Grade 6","courses/world-history-grade6/standards/world-history-grade6-standards.json","GitHub mirror (moreproblems/moreproblems G6-SS.json) + WebSearch cross-check",False),
 ("grade-07-world-history-geography","Grade 7","courses/world-history-grade7/standards/world-history-grade7-standards.json","GitHub mirror + WebSearch cross-check; exemplar lists omitted",False),
 ("grade-08-us-history-geography","Grade 8","courses/us-history-grade8/standards/us-history-grade8-standards.json","GitHub mirror + WebSearch cross-check",False),
 ("hs-world-history","High School","courses/world-history/standards/world-history-standards.json","Repo-verified (ingested from official TDOE PDF)",True),
 ("hs-government-civics","High School","courses/government/standards/government-standards.json","Repo-verified",True),
 ("tennessee-history","High School / Elective","courses/tennessee-history/standards/tennessee-history-standards.json","Repo-verified (ingested from official TDOE PDF)",True),
]

index={"title":"2026-27 Tennessee Social Studies Academic Standards","note":"Canonical machine-readable source of truth. Valid year: 2026-27 (last year of the current standards before the 2024-adopted revisions take effect 2027-28).","courses":[]}

def summarize(course, level, prefix, standards, practices, provenance, verified, extra_note=""):
    geo=sum(1 for s in standards if s.get("geo"))
    return {"file":f"standards/{course}.json","course":course,"level":level,"standardsPrefix":prefix,
            "standards_count":len(standards),"geo_flagged":geo,"practices_count":len(practices),
            "provenance":provenance,"verified":verified,"caveat":("" if verified else "VERIFY verbatim text vs official TDOE PDF")+extra_note}

for out_name, level, path, prov, verified in LIST_SRC:
    d=json.load(open(os.path.join(ROOT,path)))
    st=d.get("standards",[]); pr=d.get("practices",[])
    obj={"course":out_name,"level":level,"standardsPrefix":d.get("standardsPrefix"),
         "title":d.get("course"),"source":d.get("source"),"provenance":prov,"verified":verified,
         "practices":pr,"standards":st}
    json.dump(obj,open(os.path.join(OUT,"standards",out_name+".json"),"w"),indent=2,ensure_ascii=False)
    index["courses"].append(summarize(out_name,level,d.get("standardsPrefix"),st,pr,prov,verified))
    print(f"{len(st):4d}  {out_name}")

# HS US History from dict-form tn_standards_source.json
us=json.load(open(os.path.join(ROOT,"HistoryHack_Platinum/build/tn_standards_source.json")))
us_std=[]
for k,v in us.items():
    if re.match(r"^US\.\d+", k):
        text = v.get("text") or v.get("standard") or (v if isinstance(v,str) else "")
        geo = bool(v.get("geo")) if isinstance(v,dict) else False
        cluster = v.get("cluster") or v.get("unit") or "" if isinstance(v,dict) else ""
        us_std.append({"code":k,"text":text,"strand":[],"geo":geo,"cluster":cluster})
us_std.sort(key=lambda s:[int(x) for x in re.findall(r"\d+",s["code"])])
obj={"course":"hs-us-history","level":"High School","standardsPrefix":"US","title":"United States History and Geography (HS)",
     "source":us.get("_source"),"provenance":"Repo product source-of-truth (HistoryHack_Platinum/build/tn_standards_source.json)","verified":True,
     "practices":[],"standards":us_std}
json.dump(obj,open(os.path.join(OUT,"standards","hs-us-history.json"),"w"),indent=2,ensure_ascii=False)
index["courses"].append(summarize("hs-us-history","High School","US",us_std,[],obj["provenance"],True))
print(f"{len(us_std):4d}  hs-us-history")

# order index by level then course
index["courses"].sort(key=lambda c:(c["level"],c["file"]))
index["total_standards"]=sum(c["standards_count"] for c in index["courses"])
index["total_courses"]=len(index["courses"])
json.dump(index,open(os.path.join(OUT,"index.json"),"w"),indent=2,ensure_ascii=False)
print("\nTOTAL:",index["total_standards"],"standards across",index["total_courses"],"courses")
