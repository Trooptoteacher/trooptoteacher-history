#!/usr/bin/env python3
"""
Build the Day One deck as an EDITABLE .pptx (native text boxes + shapes).

No python-pptx/pptxgenjs here, so we assemble OOXML directly: reuse a known-good
package skeleton (master / layout / theme / presProps) from an existing America
250 deck so PowerPoint opens it cleanly, drop that deck's slides, and write 11
fresh Day-One slides as real, editable shapes.

Usage: build_day1_pptx.py BASE_DECK.pptx OUT.pptx
"""
import sys, re, zipfile, html

PX = 9525            # EMU per px @96dpi  (matches the PDF's 1280x720 layout)
NAVY="1F3A5F"; RED="B22234"; GOLD="C9A227"; GOLDINK="846009"
CREAM="F8F5EF"; TINT="F3ECD6"; INK="1F2430"; COOL="EAF0F7"; PINK="F4ECEC"
GREY="8A94A3"; CARDBD="E4DCC6"; LINEG="B9C2CF"

def esc(s): return html.escape(s, quote=False)

class Slide:
    def __init__(self): self.sid=1; self.body=[]
    def _id(self):
        self.sid+=1; return self.sid
    def rect(self, x,y,w,h, fill=None, line=None, lw=9525, dash=None, prst="rect"):
        sid=self._id()
        f = f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>' if fill else '<a:noFill/>'
        ln=""
        if line:
            d=f'<a:prstDash val="{dash}"/>' if dash else ''
            ln=f'<a:ln w="{lw}"><a:solidFill><a:srgbClr val="{line}"/></a:solidFill>{d}</a:ln>'
        self.body.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{sid}" name="r{sid}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{int(x*PX)}" y="{int(y*PX)}"/>'
            f'<a:ext cx="{int(w*PX)}" cy="{int(h*PX)}"/></a:xfrm>'
            f'<a:prstGeom prst="{prst}"><a:avLst/></a:prstGeom>{f}{ln}</p:spPr>'
            f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p/></p:txBody></p:sp>')
    def text(self, x,y,w,h, paras, anchor="t", fill=None, line=None, prst="rect",
             lIns=91440, tIns=45720, dash=None, lw=9525):
        sid=self._id()
        f = f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>' if fill else '<a:noFill/>'
        ln=""
        if line:
            d=f'<a:prstDash val="{dash}"/>' if dash else ''
            ln=f'<a:ln w="{lw}"><a:solidFill><a:srgbClr val="{line}"/></a:solidFill>{d}</a:ln>'
        pxml=""
        for p in paras:
            algn=p.get("align","l"); runs=p.get("runs",[])
            sb=f'<a:spcBef><a:spcPts val="{p["before"]}"/></a:spcBef>' if p.get("before") else ""
            rxml=""
            for r in runs:
                rp=(f'<a:rPr lang="en-US" sz="{r["sz"]}" b="{1 if r.get("b") else 0}" '
                    f'i="{1 if r.get("i") else 0}" dirty="0">'
                    f'<a:solidFill><a:srgbClr val="{r.get("color",INK)}"/></a:solidFill>'
                    f'<a:latin typeface="{r.get("font","Calibri")}"/></a:rPr>')
                rxml+=f'<a:r>{rp}<a:t>{esc(r["t"])}</a:t></a:r>'
            lnspc=f'<a:lnSpc><a:spcPct val="{p.get("lnpct",108000)}"/></a:lnSpc>' if p.get("lnpct") else ''
            pxml+=(f'<a:p><a:pPr algn="{algn}">{lnspc}{sb}<a:buNone/></a:pPr>{rxml}</a:p>')
        self.body.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{sid}" name="t{sid}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{int(x*PX)}" y="{int(y*PX)}"/>'
            f'<a:ext cx="{int(w*PX)}" cy="{int(h*PX)}"/></a:xfrm>'
            f'<a:prstGeom prst="{prst}"><a:avLst/></a:prstGeom>{f}{ln}</p:spPr>'
            f'<p:txBody><a:bodyPr wrap="square" lIns="{lIns}" tIns="{tIns}" '
            f'rIns="{lIns}" bIns="{tIns}" anchor="{anchor}"/><a:lstStyle/>{pxml}</p:txBody></p:sp>')
    def xml(self):
        return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
          'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
          '<p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
          '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/>'
          '<a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
          + "".join(self.body) +
          '</p:spTree></p:cSld><p:clrMapOvr><a:overrideClrMapping '
          'bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" '
          'accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" '
          'hlink="hlink" folHlink="folHlink"/></p:clrMapOvr></p:sld>')

def R(t, sz, color=INK, b=False, i=False, font="Calibri"):
    return {"t":t,"sz":sz,"color":color,"b":b,"i":i,"font":font}
def P(runs, align="l", before=0, lnpct=108000):
    return {"runs":runs,"align":align,"before":before,"lnpct":lnpct}

SERIF="Georgia"
def base(s, kicker, title, title_sz=3400, title_color=NAVY, navybar=True):
    if navybar: s.rect(0,0,1280,16, fill=NAVY)
    if kicker: s.text(70,44,900,30,[P([R(kicker,1300,RED,b=True)])])
    if title: s.text(66,72,1150,110,[P([R(title,title_sz,title_color,font=SERIF)])], anchor="t")
def foot(s, time=None):
    s.text(70,672,760,26,[P([R("U.S. History Hack · Don't just learn history. Hack it.",950,GREY)])])
    if time:
        s.text(1030,668,180,34,[P([R(time,1000,GOLDINK,b=True)],align="ctr")],
               fill=TINT, line=GOLD, prst="roundRect", anchor="ctr", tIns=9144)

def card(s,x,y,w,h,fill=CREAM,leftbar=None,topbar=None):
    s.rect(x,y,w,h, fill=fill, line=CARDBD, lw=12700, prst="roundRect")
    if leftbar: s.rect(x,y,7,h, fill=leftbar)
    if topbar: s.rect(x,y,w,6, fill=topbar)

def build_slides():
    S=[]
    # 1 WELCOME
    s=Slide(); base(s,"U.S. HISTORY HACK · DAY ONE","Welcome aboard.")
    s.text(70,185,1050,80,[P([R("Find your seat, open your Chromebook, and take a breath.",1500,"33475B")]),
        P([R("We're about to hack a whole century — together.",1500,"33475B")])])
    card(s,70,300,1140,120,fill=CREAM,leftbar=GOLD)
    s.text(96,312,1090,100,[P([R("Bell-ringer: ",1500,NAVY,b=True),
        R("On the sticky note at your seat, write one word for how you feel about history right now. Stick it on the board on your way in.",1500,INK)])],anchor="ctr")
    foot(s,"as you enter"); S.append(s)

    # 2 AGENDA
    s=Slide(); base(s,"AGENDA · 20 MINUTES","Today's flight plan")
    rows=[("1","Log into Schoology","4 min"),("2","Quick tour — where everything lives","3 min"),
          ("3","Syllabus","2 min"),("4","Our one rule","1 min"),("5","You write the rules","3 min")]
    y=175
    for n,label,t in rows:
        s.rect(70,y,1140,72, fill=COOL, prst="roundRect")
        s.rect(92,y+14,44,44, fill=NAVY, prst="ellipse")
        s.text(92,y+14,44,44,[P([R(n,1600,"FFFFFF",b=True)],align="ctr")],anchor="ctr")
        s.text(150,y,760,72,[P([R(label,1700,INK)])],anchor="ctr")
        s.text(1010,y,180,72,[P([R(t,1300,GOLDINK,b=True)],align="r")],anchor="ctr")
        y+=88
    foot(s,"1 min"); S.append(s)

    # 3 TWO TRUTHS
    s=Slide(); base(s,"MEET YOUR PILOT","Mr. Reynolds — Two Truths & a Lie",title_sz=3000)
    s.text(70,175,1120,44,[P([R("Two of these are true. One is a bald-faced lie. ",1400,"33475B"),
        R("Vote with your hands.",1400,"33475B",b=True)])])
    labels=["[ write something true about you ]","[ write the lie — make it believable ]","[ write something true about you ]"]
    x=70
    for i,lab in enumerate(labels,1):
        s.rect(x,235,360,190, fill=COOL, prst="roundRect")
        s.text(x+20,250,320,50,[P([R(str(i),2600,RED,b=True,font=SERIF)])])
        s.text(x+20,320,320,90,[P([R(lab,1300,"94794F",i=True)])])
        x+=390
    s.text(70,440,1120,40,[P([R("Teacher: fill these three in with your real facts before class.",1200,"5A6675",i=True)])])
    foot(s,"3 min"); S.append(s)

    # 4 YEAR AHEAD
    s=Slide(); base(s,"THE YEAR AHEAD","Don't just learn history. Hack it.",title_sz=4200)
    cols=[("You're the historian.","You'll weigh real primary sources and make your own call — there's no answer key."),
          ("1877 to today.","Ten stops, one flight across modern America — every unit builds on the last."),
          ("It's about you.","Different experiences, same journey. Your voice is part of the story.")]
    x=70
    for head,bodyt in cols:
        card(s,x,205,360,215,fill=CREAM,leftbar=GOLD)
        s.text(x+22,222,320,50,[P([R(head,1550,NAVY,b=True)])])
        s.text(x+22,278,320,130,[P([R(bodyt,1350,INK)])])
        x+=390
    foot(s,"1 min"); S.append(s)

    # 5 HOOK
    s=Slide(); base(s,"REAL TALK",None)
    s.text(66,72,1150,90,[P([R("Think you hate history? ",4200,NAVY,font=SERIF),
        R("Good.",4200,RED,b=True,font=SERIF)])])
    s.text(70,180,1140,70,[P([R("If history meant memorizing names and dates for a test you'd forget by Friday — yeah, that's boring. ",1500,"33475B"),
        R("We don't do that here.",1500,NAVY,b=True)])])
    # vs panels
    s.rect(70,270,570,210, fill=PINK, prst="roundRect")
    s.rect(640,270,570,210, fill=NAVY, prst="roundRect")
    s.text(92,285,530,30,[P([R("WHAT MADE IT BORING",1200,RED,b=True)])])
    s.text(662,285,530,30,[P([R("WHAT WE ACTUALLY DO",1200,GOLD,b=True)])])
    old=["Memorize dates","Copy the textbook",'One "right" answer',"Forget it by Friday"]
    new=["Investigate real evidence","Make your own call","Argue it — and back it up","Use it to decode today"]
    oy=325
    for a,b in zip(old,new):
        s.text(92,oy,530,34,[P([R("×  ",1400,RED,b=True),R(a,1400,"7A5B5B")])])
        s.text(662,oy,530,34,[P([R("→  ",1400,GOLD,b=True),R(b,1400,"FFFFFF")])])
        oy+=38
    s.text(70,500,1140,60,[P([R("Every fight you care about now — money, power, who gets a say — started here. This is the origin story.",1450,GOLDINK,b=True)],align="ctr")],
        fill=TINT, prst="roundRect", anchor="ctr")
    foot(s,"1 min"); S.append(s)

    # 6 STEP1 SCHOOLOGY
    s=Slide(); base(s,"STEP 1","Log into Schoology")
    s.text(70,185,1140,220,[
        P([R("1.  Go to ",1800,INK),R("[ app.schoology.com ]",1800,NAVY,b=True),R("  (or your district portal)",1400,"94794F",i=True)],before=600),
        P([R("2.  Sign in with your ",1800,INK),R("school Google account",1800,NAVY,b=True)],before=600),
        P([R("3.  Join our class with the access code:",1800,INK)],before=600)])
    s.text(430,430,420,80,[P([R("[ ____ – ____ ]",2600,RED,b=True)],align="ctr")],
        line=RED, dash="dash", lw=28575, prst="roundRect", anchor="ctr")
    s.text(70,540,1140,40,[P([R("We'll do this together — thumbs up when you're in.",1300,"5A6675",i=True)])])
    foot(s,"4 min"); S.append(s)

    # 7 TOUR
    s=Slide(); base(s,"STEP 2","Where everything lives")
    tiles=[("Materials","Lessons + your Flight Log (where all your writing goes)"),
           ("Calendar","What's due, and when"),
           ("Grades","How you're doing — check it weekly"),
           ("Messages","The fastest way to reach me")]
    x=70
    for head,bodyt in tiles:
        card(s,x,200,270,190,fill=CREAM,topbar=NAVY)
        s.text(x+16,214,240,40,[P([R(head,1450,NAVY,b=True)])])
        s.text(x+16,258,240,120,[P([R(bodyt,1200,INK)])])
        x+=288
    s.text(70,415,1140,70,[P([R("Challenge: find the Unit 1 folder and open the Flight Log. Thumbs up when you see it.",1500,GOLDINK,b=True)],align="ctr")],
        fill=TINT, prst="roundRect", anchor="ctr")
    foot(s,"3 min"); S.append(s)

    # 8 SYLLABUS
    s=Slide(); base(s,"STEP 3","The syllabus")
    cols=[("Bring every day","Charged Chromebook · something to write with · your brain"),
          ("How grades work","[ grading + redo/retake policy — edit ]"),
          ("Reach me","[ email / Schoology message / room # — edit ]")]
    x=70
    for head,bodyt in cols:
        card(s,x,200,360,175,fill=CREAM,leftbar=GOLD)
        s.text(x+22,214,320,40,[P([R(head,1450,NAVY,b=True)])])
        s.text(x+22,258,320,110,[P([R(bodyt,1300,INK)])])
        x+=390
    s.text(70,400,1140,60,[P([R("Skim it now and star ONE question you want answered before you leave.",1500,GOLDINK,b=True)],align="ctr")],
        fill=TINT, prst="roundRect", anchor="ctr")
    foot(s,"2 min"); S.append(s)

    # 9 RESPECT (full navy)
    s=Slide()
    s.rect(0,0,1280,720, fill=NAVY)
    s.text(0,190,1280,40,[P([R("OUR ONE RULE",1700,GOLD,b=True)],align="ctr")])
    s.text(0,235,1280,180,[P([R("RESPECT",9600,GOLD,b=True,font=SERIF)],align="ctr")])
    s.text(0,430,1280,50,[P([R("We have exactly one rule. ",2200,CREAM),
        R("Everything else fits under it.",2200,CREAM,b=True)],align="ctr")])
    s.text(1030,668,180,34,[P([R("1 min",1000,GOLD,b=True)],align="ctr")],line=GOLD,prst="roundRect",anchor="ctr",tIns=9144)
    S.append(s)

    # 10 WHAT DOES RESPECT LOOK LIKE
    s=Slide(); base(s,"TURN & TALK","What does respect look like — here?",title_sz=3400)
    for i,h in enumerate(["Yourself","Each other","This room","Our learning"]):
        x=70+i*288
        card(s,x,205,270,150,fill=CREAM,topbar=NAVY)
        s.text(x+16,220,240,40,[P([R(h,1450,NAVY,b=True)])])
    s.text(70,385,1140,60,[P([R('With your partner (60 sec): "Respect looks like ______ and sounds like ______."',1500,GOLDINK,b=True)],align="ctr")],
        fill=TINT, prst="roundRect", anchor="ctr")
    foot(s,"2 min"); S.append(s)

    # 11 YOU WRITE THE RULES
    s=Slide(); base(s,"YOU MAKE THE CALL","You write the rules — under RESPECT",title_sz=3200)
    s.text(70,170,1140,60,[P([R("Every rule we keep has to pass one test: ",1500,"33475B"),
        R("does it show respect?",1500,NAVY,b=True),
        R(" You propose them. We adopt them. They're ours.",1500,"33475B")])])
    for i,h in enumerate(["Yourself","Each other","This room","Our learning"]):
        x=70+i*288
        card(s,x,240,270,190,fill=CREAM,topbar=NAVY)
        s.text(x+16,254,240,40,[P([R(h,1400,NAVY,b=True)])])
        s.rect(x+16,320,238,2, fill=LINEG)
        s.rect(x+16,365,238,2, fill=LINEG)
    s.text(70,450,1140,54,[P([R("Wheels up. Welcome to the year.",1700,GOLDINK,b=True)],align="ctr")],
        fill=TINT, prst="roundRect", anchor="ctr")
    foot(s,"3 min"); S.append(s)
    return S

def build(base_path, out_path):
    zin=zipfile.ZipFile(base_path)
    names=zin.namelist()
    def is_slide(n): return re.match(r"ppt/slides/slide\d+\.xml$",n) or \
        re.match(r"ppt/slides/_rels/slide\d+\.xml\.rels$",n)
    def is_notes(n): return n.startswith("ppt/notesSlides/")
    slides=build_slides(); N=len(slides)

    # rewrite [Content_Types].xml : drop slide/notesSlide overrides, add N slides
    ct=zin.read("[Content_Types].xml").decode("utf-8")
    ct=re.sub(r'<Override PartName="/ppt/slides/slide\d+\.xml"[^>]*/>','',ct)
    ct=re.sub(r'<Override PartName="/ppt/notesSlides/[^"]*"[^>]*/>','',ct)
    adds="".join(f'<Override PartName="/ppt/slides/slide{i}.xml" '
        f'ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1,N+1))
    ct=ct.replace("</Types>",adds+"</Types>")

    # rewrite presentation.xml.rels : keep non-slide rels, add N slide rels
    prels=zin.read("ppt/_rels/presentation.xml.rels").decode("utf-8")
    rels=re.findall(r'<Relationship [^>]*/>',prels)
    keep=[r for r in rels if 'slides/slide' not in r]
    used=[int(m.group(1)) for r in keep for m in [re.search(r'Id="rId(\d+)"',r)] if m]
    nextid=max(used)+1 if used else 1
    slide_rels=[]; sldids=[]
    for i in range(1,N+1):
        rid=f"rId{nextid}"; nextid+=1
        slide_rels.append(f'<Relationship Id="{rid}" '
            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" '
            f'Target="slides/slide{i}.xml"/>')
        sldids.append((256+i-1,rid))
    new_prels=('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + "".join(keep)+"".join(slide_rels)+'</Relationships>')

    # rewrite presentation.xml sldIdLst
    pres=zin.read("ppt/presentation.xml").decode("utf-8")
    lst='<p:sldIdLst>'+"".join(f'<p:sldId id="{sid}" r:id="{rid}"/>' for sid,rid in sldids)+'</p:sldIdLst>'
    if re.search(r'<p:sldIdLst.*?</p:sldIdLst>',pres,re.DOTALL):
        pres=re.sub(r'<p:sldIdLst.*?</p:sldIdLst>',lst,pres,flags=re.DOTALL)
    elif '<p:sldIdLst/>' in pres:
        pres=pres.replace('<p:sldIdLst/>',lst)
    else:  # insert after sldMasterIdLst
        pres=re.sub(r'(</p:sldMasterIdLst>)',r'\1'+lst,pres)

    slide_rel_xml=('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" '
        'Target="../slideLayouts/slideLayout1.xml"/></Relationships>')

    zout=zipfile.ZipFile(out_path,"w",zipfile.ZIP_DEFLATED)
    for n in names:
        if is_slide(n) or is_notes(n): continue
        if n=="[Content_Types].xml": zout.writestr(n,ct); continue
        if n=="ppt/_rels/presentation.xml.rels": zout.writestr(n,new_prels); continue
        if n=="ppt/presentation.xml": zout.writestr(n,pres); continue
        # strip notesSlide refs from any slideMaster/other rels? not needed
        zout.writestr(n, zin.read(n))
    for i,s in enumerate(slides,1):
        zout.writestr(f"ppt/slides/slide{i}.xml", s.xml())
        zout.writestr(f"ppt/slides/_rels/slide{i}.xml.rels", slide_rel_xml)
    zout.close(); zin.close()
    print(f"WROTE {out_path} ({N} slides)")

if __name__=="__main__":
    build(sys.argv[1], sys.argv[2])
