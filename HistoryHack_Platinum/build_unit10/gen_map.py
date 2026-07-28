import json,re,sys,glob,zipfile,os
unit=sys.argv[1]; content=sys.argv[2]; teacher_deck=sys.argv[3]; out=sys.argv[4]
c=json.load(open(content)); st=c.get("standards",c)
# extract DI subtitles per standard from teacher deck (verbatim cornell cues)
tmp=f"/tmp/ded_{unit}"; os.system(f"rm -rf {tmp}; mkdir -p {tmp}")
zipfile.ZipFile(teacher_deck).extractall(tmp)
di={}
for f in sorted(glob.glob(f"{tmp}/ppt/slides/slide*.xml"),key=lambda x:int(re.search(r'\d+',os.path.basename(x)).group())):
    x=open(f,encoding="utf-8").read()
    m=re.search(r'(US\.\d+)\s*[·•]\s*DIRECT INSTRUCTION',x)
    if m:
        ts=re.findall(r'<a:t>([^<]+)</a:t>',x)
        sub=ts[1].strip() if len(ts)>1 else ""
        if sub and 'DIRECT INSTRUCTION' not in sub: di.setdefault(m.group(1),[]).append(sub)
M={}
for code in st:
    s=st[code]; cfu=s.get("cfu",{}); opts=cfu.get("options",{})
    choices=[opts.get(k,"") for k in ("A","B","C","D")]; key=cfu.get("key","A")
    voc=s.get("vocab",[])[:3]
    M[code]={
      "cornell_cues": di.get(code, s.get("cues",[]))[:4],
      "vocab":[{"term":v["term"],"es":v.get("es",""),"def":v.get("def","")} for v in voc],
      "progress":{"stem":cfu.get("stem",""),"choices":choices,"correct_idx":"ABCD".index(key) if key in "ABCD" else 0}
    }
json.dump(M,open(out,"w"),ensure_ascii=False,indent=1)
print(f"map: {len(M)} standards, DI-cues for {len(di)} standards")
