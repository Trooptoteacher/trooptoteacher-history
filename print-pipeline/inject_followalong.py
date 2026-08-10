#!/usr/bin/env python3
"""
Add a "FOLLOW ALONG" wayfinding box to each STANDARD divider slide of the
teacher deck, so students know exactly what to open at the start of every stop:
the Mission Book stop and the Flight Log entry that match this standard.

Placed in the open gap on the divider (right side, below the SSP list, above the
TN standard) so nothing is renumbered — the Flight Log's Cornell references to
DI slide numbers stay valid.
"""
import sys, re, zipfile, shutil, os

# STANDARD divider slide -> standard number
DIVIDERS = {5:1, 19:2, 33:3, 49:4, 64:5, 79:6, 94:7}
BOX_ID = 960
NAVY="1F3A5F"; GOLD="C9A227"

def box(std):
    # x=7.45in y=3.42in w=4.90in h=0.70in  (EMU)
    x=int(7.45*914400); y=int(3.42*914400); w=int(4.90*914400); h=int(0.70*914400)
    def run(t,sz,color,b=False):
        return (f'<a:r><a:rPr lang="en-US" sz="{sz}" b="{1 if b else 0}" dirty="0">'
                f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>'
                f'<a:latin typeface="Calibri" pitchFamily="34" charset="0"/></a:rPr>'
                f'<a:t>{t}</a:t></a:r>')
    para=lambda runs,sb=0: (f'<a:p><a:pPr><a:spcBef><a:spcPts val="{sb}"/></a:spcBef>'
                            f'<a:buNone/></a:pPr>{runs}</a:p>')
    body=(para(run("FOLLOW ALONG",1000,GOLD,b=True))
          + para(run("Open the Mission Book → Stop "+str(std),1100,"FFFFFF"),300)
          + para(run("Open the Flight Log → Entry "+str(std),1100,"FFFFFF"),300))
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{BOX_ID}" name="FollowAlong"/>'
            '<p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr>'
            f'<a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm>'
            '<a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom>'
            f'<a:solidFill><a:srgbClr val="{NAVY}"/></a:solidFill>'
            f'<a:ln w="12700"><a:solidFill><a:srgbClr val="{GOLD}"/></a:solidFill></a:ln>'
            '</p:spPr><p:txBody>'
            '<a:bodyPr wrap="square" lIns="82296" rIns="45720" tIns="27432" bIns="18288" anchor="ctr"/>'
            f'<a:lstStyle/>{body}</p:txBody></p:sp>')

def main(src, dst):
    zin=zipfile.ZipFile(src); tmp=dst+".tmp"
    zout=zipfile.ZipFile(tmp,"w",zipfile.ZIP_DEFLATED)
    done=0
    for it in zin.infolist():
        data=zin.read(it.filename)
        m=re.match(r"ppt/slides/slide(\d+)\.xml$", it.filename)
        if m and int(m.group(1)) in DIVIDERS:
            xml=data.decode("utf-8")
            if "FollowAlong" not in xml:
                xml=xml.replace("</p:spTree>", box(DIVIDERS[int(m.group(1))])+"</p:spTree>", 1)
                done+=1
            data=xml.encode("utf-8")
        zout.writestr(it, data)
    zout.close(); zin.close(); shutil.move(tmp,dst)
    print(f"{os.path.basename(dst)}: FOLLOW ALONG boxes added to {done}/7 divider slides")

if __name__=="__main__":
    main(sys.argv[1], sys.argv[2])
