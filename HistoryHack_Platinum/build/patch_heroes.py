#!/usr/bin/env python3
"""Add the unit hero image to cover wraps and workbook cover pages.
Covers (uniform _uN scripts): U2,3,4,7,8,9.  Workbooks: U1,2,3,4,7,8,9.
Unit 1 cover already has its own hero; Unit 6 skipped (AP-copyrighted Iwo Jima)."""
import re, sys

# unit -> (w, h, cover_credit_oneline, wb_caption, wb_credit)
META = {
 1: (1200, 957, None,
     "The Golden Spike ceremony completing the Transcontinental Railroad, Promontory Summit, Utah, May 10, 1869.",
     "Andrew J. Russell / U.S. National Archives. Public domain."),
 2: (1536,1204, "Pennsylvania Avenue, Washington, D.C., early 1900s · Library of Congress · Public domain",
     "Crowds fill Pennsylvania Avenue in Washington, D.C., during the Progressive Era.",
     "Library of Congress. Public domain."),
 3: (1200, 967, "Col. Theodore Roosevelt and the Rough Riders, San Juan Heights, 1898 · Library of Congress · Public domain",
     "Colonel Theodore Roosevelt and the Rough Riders atop San Juan Heights, Cuba, 1898.",
     "William Dinwiddie / Library of Congress. Public domain."),
 4: (1021, 689, "A Ford assembly line in the era of mass production, early 1900s · Public domain",
     "Automobiles on a Ford assembly line during the era of mass production, early twentieth century.",
     "Public domain."),
 7: (1200, 937, "Construction of the Berlin Wall, 1961 · U.S. National Archives · Public domain",
     "East German workers construct the Berlin Wall, 1961.",
     "U.S. National Archives. Public domain."),
 8: (1200,1212, "Astronaut Buzz Aldrin on the Moon, Apollo 11, 1969 · NASA · Public domain",
     "Astronaut Buzz Aldrin walks on the Moon during Apollo 11, July 20, 1969.",
     "Neil Armstrong / NASA. Public domain."),
 9: ( 588, 458, "March on Washington for Jobs and Freedom, 1963 · U.S. National Archives · Public domain",
     "The March on Washington for Jobs and Freedom, August 28, 1963.",
     "U.S. National Archives. Public domain."),
}

COVER_UNITS = [2,3,4,7,8,9]
WB_UNITS    = [1,2,3,4,7,8,9]

def patch_cover(u):
    w,h,cred,_,_ = META[u]
    p=f"/home/user/Unit{u}_Claude_Core/analysis/build_cover_u{u}.js"
    s=open(p).read(); orig=s
    # 1) HERO consts
    s=s.replace("const HERO='';",
        f"const HERO='analysis/assets/hero.jpg'; const HERO_W={w}, HERO_H={h};\n"
        f"const HERO_CRED={cred!r};")
    # 2) heroImg block -> aspect-fit array + credit
    old_block=("  const heroImg=(HERO && fs.existsSync(HERO))\n"
      "    ? new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:120,after:120},children:[new ImageRun({data:fs.readFileSync(HERO),transformation:{width:560,height:400},altText:{title:'Cover',description:'Cover',name:'cover'}})]})\n"
      "    : new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:120,after:120},border:{top:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:10},bottom:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:10}},children:[R('SEMIQUINCENTENNIAL  ·  1776–2026',{s:22,b:true,c:GOLD,caps:true})]});")
    new_block=("  let _hw=600, _hh=Math.round(HERO_H*(_hw/HERO_W)); if(_hh>470){_hh=470;_hw=Math.round(HERO_W*(_hh/HERO_H));}\n"
      "  const heroImg=(HERO && fs.existsSync(HERO))\n"
      "    ? [new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:120,after:30},\n"
      "        border:{top:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:8},bottom:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:8}},\n"
      "        children:[new ImageRun({data:fs.readFileSync(HERO),transformation:{width:_hw,height:_hh},altText:{title:'Cover image',description:HERO_CRED,name:'cover-hero'}})]}),\n"
      "       P(R(HERO_CRED,{s:14,i:true,c:WHITE}),{align:AlignmentType.CENTER,spacing:{after:120}})]\n"
      "    : [new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:120,after:120},border:{top:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:10},bottom:{style:BorderStyle.SINGLE,size:18,color:GOLD,space:10}},children:[R('SEMIQUINCENTENNIAL  ·  1776–2026',{s:22,b:true,c:GOLD,caps:true})]})];")
    if old_block not in s:
        print(f"  U{u} COVER: heroImg block anchor NOT FOUND"); return False
    s=s.replace(old_block,new_block)
    # 3) spread
    s=s.replace("\n    heroImg,\n","\n    ...heroImg,\n")
    if s==orig: print(f"  U{u} COVER: no change"); return False
    open(p,"w").write(s); print(f"  U{u} COVER patched"); return True

WB_HELPER = (
 "\n// Cover hero image — the unit's curated public-domain photograph (app hero art).\n"
 "const HERO={{file:'analysis/assets/hero.jpg', w:{w}, h:{h},\n"
 "  cap:{cap!r},\n"
 "  cred:{cred!r}}};\n"
 "function coverHero(rec,{{maxW=380,maxH=290}}={{}}){{\n"
 "  let w=Math.min(rec.w,maxW), h=Math.round(rec.h*(w/rec.w));\n"
 "  if(h>maxH){{ h=maxH; w=Math.round(rec.w*(h/rec.h)); }}\n"
 "  const out=[new Paragraph({{alignment:AlignmentType.CENTER,spacing:{{before:40,after:30}},\n"
 "    border:{{top:{{style:BorderStyle.SINGLE,size:14,color:GOLD,space:8}},bottom:{{style:BorderStyle.SINGLE,size:14,color:GOLD,space:8}}}},\n"
 "    children:[new ImageRun({{data:fs.readFileSync(rec.file),transformation:{{width:w,height:h}},\n"
 "      altText:{{title:'Unit cover image',description:rec.cap,name:'cover-hero'}}}})]}})];\n"
 "  out.push(P(R(rec.cap,{{s:16,i:true,c:GREY}}),{{align:AlignmentType.CENTER,spacing:{{after:8}}}}));\n"
 "  out.push(P(R('Source: '+rec.cred,{{s:14,c:GREY}}),{{align:AlignmentType.CENTER,spacing:{{after:110}}}}));\n"
 "  return out;\n"
 "}}\n")

def patch_wb(u):
    w,h,_,cap,cred = META[u]
    p=f"/home/user/Unit{u}_Claude_Core/analysis/build_workbook_u{u}.js" if u!=1 else "/home/user/Unit1_Claude_Core/analysis/build_workbook.js"
    s=open(p).read(); orig=s
    if "function coverHero(" in s:
        print(f"  U{u} WB: already has coverHero"); return False
    # 1) inject helper after the SAMPLE/ORDER line
    m=re.search(r"const SAMPLE=process\.env\.SAMPLE\?Number\(process\.env\.SAMPLE\):0; const ORDER=[^\n]*\n", s)
    if not m: print(f"  U{u} WB: SAMPLE anchor not found"); return False
    helper=WB_HELPER.format(w=w,h=h,cap=cap,cred=cred)
    s=s[:m.end()]+helper+s[m.end():]
    # 2) reduce standards-line spacing (uniform tail)
    s=s.replace("Grades 9–12',{s:22,c:INK}),{align:AlignmentType.CENTER,spacing:{after:300}})",
                "Grades 9–12',{s:22,c:INK}),{align:AlignmentType.CENTER,spacing:{after:140}})")
    # reduce the big statement paragraph spacing if present
    s=s.replace("{align:AlignmentType.CENTER,spacing:{before:280,after:180}}",
                "{align:AlignmentType.CENTER,spacing:{before:150,after:110}}")
    # 3) insert ...coverHero(HERO), before the FIRST cover TENNESSEE CONNECTION callout
    idx=s.find("callout('TENNESSEE CONNECTION")
    if idx<0: print(f"  U{u} WB: TN callout anchor not found"); return False
    line_start=s.rfind("\n",0,idx)+1
    s=s[:line_start]+"  ...coverHero(HERO),\n"+s[line_start:]
    if s==orig: print(f"  U{u} WB: no change"); return False
    open(p,"w").write(s); print(f"  U{u} WB patched"); return True

print("== COVERS ==")
for u in COVER_UNITS: patch_cover(u)
print("== WORKBOOKS ==")
for u in WB_UNITS: patch_wb(u)
print("done")
