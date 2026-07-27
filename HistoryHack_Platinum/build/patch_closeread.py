#!/usr/bin/env python3
"""Replace the Close-Read block in a workbook builder with an adaptive version:
passage + Evidence Lab stay on ONE page (no front-to-back split, no orphan row)
by scaling rows / writing-lines / passage font to the passage length."""
import re, sys

CANON = r'''const _secs=(a.close_sections&&a.close_sections.length)?a.close_sections:[['',a.close]];
  const _cl=(a.close||'').length;
  const _long=_cl>1350;
  const _pf=_cl>2000?18:(_cl>1500?19:21);
  const _rows=_cl>1900?2:3;
  const _wl=_cl>1900?1:2;
  const _chunks=[];
  _secs.forEach(([h,c])=>{ if(h) _chunks.push(R(h,{s:_pf,b:true,c:NAVY})); _chunks.push(R(c,{s:_pf})); });
  out.push(callout('CORE PATH — read one chunk at a time',_chunks));
  if(!_long) out.push(callout('LANGUAGE SUPPORT',['Key terms to know first: '+s.vocab.slice(0,2).map(v=>v.term).join(', ')+'. Read once for the gist, then again for evidence.']));
  else out.push(P([R('Key terms first: ',{s:19,b:true,c:NAVY}),R(s.vocab.slice(0,2).map(v=>v.term).join(', ')+'. Read once for the gist, then again for evidence.',{s:19,c:GREY})],{spacing:{after:30}}));
  out.push(P([R('CLOSE-READ EVIDENCE LAB — ',{s:21,b:true,c:NAVY}),R('for each question: quote the EVIDENCE from the passage above, then write YOUR ANSWER (or answer aloud / diagram it).',{s:20})],{spacing:{after:20}}));
  const _tdq=a.tdq.slice(0,_rows);
  out.push(writeTable(['Text-dependent question','Evidence from the passage','Your answer (what it shows)'],_tdq.map(q=>[q,'','']),[3248,2900,3500],{lines:_wl,noSplit:true}));'''

def patch(path):
    s = open(path).read()
    pat = re.compile(
        r"const _secs=\(a\.close_sections.*?writeTable\(\['Text-dependent question'.*?\{lines:[^}]*\}\)\);",
        re.DOTALL)
    m = pat.search(s)
    if not m:
        print(f"  {path}: close-read anchor NOT FOUND"); return False
    s = s[:m.start()] + CANON + s[m.end():]
    open(path, "w").write(s)
    print(f"  patched {path}")
    return True

if __name__ == "__main__":
    patch(sys.argv[1])
