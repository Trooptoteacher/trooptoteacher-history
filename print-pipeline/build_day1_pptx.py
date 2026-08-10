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
          '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>')

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

XMLDECL='<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
RELNS='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKREL='http://schemas.openxmlformats.org/package/2006/relationships'

THEME=(XMLDECL+'<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
 'name="Office Theme"><a:themeElements><a:clrScheme name="Office">'
 '<a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1>'
 '<a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>'
 '<a:dk2><a:srgbClr val="1F3A5F"/></a:dk2><a:lt2><a:srgbClr val="F8F5EF"/></a:lt2>'
 '<a:accent1><a:srgbClr val="1F3A5F"/></a:accent1><a:accent2><a:srgbClr val="B22234"/></a:accent2>'
 '<a:accent3><a:srgbClr val="C9A227"/></a:accent3><a:accent4><a:srgbClr val="846009"/></a:accent4>'
 '<a:accent5><a:srgbClr val="EAF0F7"/></a:accent5><a:accent6><a:srgbClr val="8A94A3"/></a:accent6>'
 '<a:hlink><a:srgbClr val="0563C1"/></a:hlink><a:folHlink><a:srgbClr val="954F72"/></a:folHlink>'
 '</a:clrScheme><a:fontScheme name="Office">'
 '<a:majorFont><a:latin typeface="Georgia"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>'
 '<a:minorFont><a:latin typeface="Calibri"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont>'
 '</a:fontScheme><a:fmtScheme name="Office">'
 '<a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill>'
 '<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>'
 '<a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst>'
 '<a:lnStyleLst>'
 '<a:ln w="6350" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/></a:ln>'
 '<a:ln w="12700" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/></a:ln>'
 '<a:ln w="19050" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/></a:ln>'
 '</a:lnStyleLst>'
 '<a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle>'
 '<a:effectStyle><a:effectLst/></a:effectStyle>'
 '<a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>'
 '<a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill>'
 '<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>'
 '<a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst>'
 '</a:fmtScheme></a:themeElements><a:objectDefaults/><a:extraClrSchemeLst/></a:theme>')

_GRP=('<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
 '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>'
 '<a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>')

MASTER=(XMLDECL+'<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
 'xmlns:r="'+RELNS+'" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
 '<p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>'
 '<p:spTree>'+_GRP+'</p:spTree></p:cSld>'
 '<p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" '
 'accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>'
 '<p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>'
 '<p:txStyles>'
 '<p:titleStyle><a:lvl1pPr><a:defRPr sz="4400"><a:solidFill><a:schemeClr val="tx1"/></a:solidFill><a:latin typeface="+mj-lt"/></a:defRPr></a:lvl1pPr></p:titleStyle>'
 '<p:bodyStyle><a:lvl1pPr><a:defRPr sz="1800"><a:solidFill><a:schemeClr val="tx1"/></a:solidFill><a:latin typeface="+mn-lt"/></a:defRPr></a:lvl1pPr></p:bodyStyle>'
 '<p:otherStyle><a:lvl1pPr><a:defRPr sz="1800"><a:solidFill><a:schemeClr val="tx1"/></a:solidFill><a:latin typeface="+mn-lt"/></a:defRPr></a:lvl1pPr></p:otherStyle>'
 '</p:txStyles></p:sldMaster>')

MASTER_RELS=(XMLDECL+'<Relationships xmlns="'+PKREL+'">'
 '<Relationship Id="rId1" Type="'+RELNS+'/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>'
 '<Relationship Id="rId2" Type="'+RELNS+'/theme" Target="../theme/theme1.xml"/></Relationships>')

LAYOUT=(XMLDECL+'<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
 'xmlns:r="'+RELNS+'" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
 'type="blank" preserve="1"><p:cSld name="Blank"><p:spTree>'+_GRP+'</p:spTree></p:cSld>'
 '<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>')

LAYOUT_RELS=(XMLDECL+'<Relationships xmlns="'+PKREL+'">'
 '<Relationship Id="rId1" Type="'+RELNS+'/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>')

SLIDE_RELS=(XMLDECL+'<Relationships xmlns="'+PKREL+'">'
 '<Relationship Id="rId1" Type="'+RELNS+'/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>')

ROOT_RELS=(XMLDECL+'<Relationships xmlns="'+PKREL+'">'
 '<Relationship Id="rId1" Type="'+RELNS+'/officeDocument" Target="ppt/presentation.xml"/>'
 '<Relationship Id="rId2" Type="'+PKREL+'/metadata/core-properties" Target="docProps/core.xml"/>'
 '<Relationship Id="rId3" Type="'+RELNS+'/extended-properties" Target="docProps/app.xml"/></Relationships>')

CORE=(XMLDECL+'<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
 'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
 'xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
 '<dc:title>Day One — Welcome &amp; Respect</dc:title>'
 '<dc:creator>TroopToTeacher Technologies</dc:creator>'
 '<cp:lastModifiedBy>TroopToTeacher Technologies</cp:lastModifiedBy></cp:coreProperties>')

def build(base_path, out_path):
    slides=build_slides(); N=len(slides)
    # presentation
    sldids="".join(f'<p:sldId id="{256+i-1}" r:id="rId{i+1}"/>' for i in range(1,N+1))
    pres=(XMLDECL+'<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
     'xmlns:r="'+RELNS+'" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
     'saveSubsetFonts="1"><p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>'
     '<p:sldIdLst>'+sldids+'</p:sldIdLst>'
     '<p:sldSz cx="12192000" cy="6858000" type="screen16x9"/>'
     '<p:notesSz cx="6858000" cy="9144000"/></p:presentation>')
    prels=[XMLDECL+'<Relationships xmlns="'+PKREL+'">',
        '<Relationship Id="rId1" Type="'+RELNS+'/slideMaster" Target="slideMasters/slideMaster1.xml"/>']
    for i in range(1,N+1):
        prels.append(f'<Relationship Id="rId{i+1}" Type="'+RELNS+'/slide" Target="slides/slide{}.xml"/>'.format(i))
    prels.append('</Relationships>'); prels="".join(prels)
    # content types
    ct=[XMLDECL,'<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '<Default Extension="xml" ContentType="application/xml"/>',
        '<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>',
        '<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>',
        '<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>',
        '<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>',
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
        '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>']
    for i in range(1,N+1):
        ct.append(f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>')
    ct.append('</Types>'); ct="".join(ct)
    app=(XMLDECL+'<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
     'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
     '<TotalTime>0</TotalTime><Words>0</Words><Application>Microsoft Office PowerPoint</Application>'
     '<PresentationFormat>Widescreen</PresentationFormat><Slides>'+str(N)+'</Slides>'
     '<Company>TroopToTeacher Technologies</Company><AppVersion>16.0000</AppVersion></Properties>')

    z=zipfile.ZipFile(out_path,"w",zipfile.ZIP_DEFLATED)
    z.writestr("[Content_Types].xml", ct)
    z.writestr("_rels/.rels", ROOT_RELS)
    z.writestr("docProps/core.xml", CORE)
    z.writestr("docProps/app.xml", app)
    z.writestr("ppt/presentation.xml", pres)
    z.writestr("ppt/_rels/presentation.xml.rels", prels)
    z.writestr("ppt/theme/theme1.xml", THEME)
    z.writestr("ppt/slideMasters/slideMaster1.xml", MASTER)
    z.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", MASTER_RELS)
    z.writestr("ppt/slideLayouts/slideLayout1.xml", LAYOUT)
    z.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", LAYOUT_RELS)
    for i,s in enumerate(slides,1):
        z.writestr(f"ppt/slides/slide{i}.xml", s.xml())
        z.writestr(f"ppt/slides/_rels/slide{i}.xml.rels", SLIDE_RELS)
    z.close()
    print(f"WROTE {out_path} ({N} slides, clean minimal package)")

if __name__=="__main__":
    out = sys.argv[2] if len(sys.argv)>2 else sys.argv[1]
    build(None, out)
