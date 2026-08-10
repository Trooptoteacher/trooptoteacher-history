#!/usr/bin/env python3
"""
Point the teacher deck at the Flight Log where students take notes / write.

(1) DIRECT INSTRUCTION (first slide of each standard: 9,23,37,53,68,83,98):
    inject a gold-ruled cue strip -> "FLIGHT LOG · Cornell Notes — US.0N: jot
    notes on the US.0N page as we go through these Direct Instruction slides."
    (Cornell notes in the Flight Log align 1:1 to these slides.)

(2) STUDENT ACTIVITY (15,29,45,60,75,90,106): the existing bottom strip pointed
    to "Companion printable ... (Teacher Tools > Worksheets)". Per the LOCKED
    standard, ALL writing + Cornell notes live in the Flight Log, so rewrite it
    to name the Flight Log as the write-point.

Font-safe (no emoji — Calibri/Carlito may not carry them in PowerPoint).
Surgical XML edits; shape ids kept unique per slide.
"""
import sys, re, zipfile, shutil, os

FIRST_DI = {1:9, 2:23, 3:37, 4:53, 5:68, 6:83, 7:98}
ACTIVITY = {1:15, 2:29, 3:45, 4:60, 5:75, 6:90, 7:106}
CUE_ID = 950   # safe: real ids are <= ~40 on these slides

def di_cue_sp(std):
    # x=0.60in y=6.78in w=7.50in h=0.24in  (below content, above footer at 7.08)
    return (
      f'<p:sp><p:nvSpPr><p:cNvPr id="{CUE_ID}" name="FlightLogCue"/>'
      '<p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr>'
      '<a:xfrm><a:off x="548640" y="6199200"/><a:ext cx="6858000" cy="219456"/></a:xfrm>'
      '<a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom>'
      '<a:solidFill><a:srgbClr val="F3EAD0"/></a:solidFill>'
      '<a:ln w="9525"><a:solidFill><a:srgbClr val="C9A227"/></a:solidFill></a:ln>'
      '</p:spPr><p:txBody>'
      '<a:bodyPr wrap="square" lIns="73152" rIns="45720" tIns="9144" bIns="9144" anchor="ctr"/>'
      '<a:lstStyle/><a:p><a:pPr indent="0" marL="0"><a:buNone/></a:pPr>'
      '<a:r><a:rPr lang="en-US" sz="1000" b="1" dirty="0"><a:solidFill><a:srgbClr val="1F3A5F"/></a:solidFill>'
      '<a:latin typeface="Calibri" pitchFamily="34" charset="0"/></a:rPr>'
      f'<a:t>FLIGHT LOG · Cornell Notes — US.0{std}: </a:t></a:r>'
      '<a:r><a:rPr lang="en-US" sz="1000" dirty="0"><a:solidFill><a:srgbClr val="1F2430"/></a:solidFill>'
      '<a:latin typeface="Calibri" pitchFamily="34" charset="0"/></a:rPr>'
      f'<a:t>jot notes here as we go.</a:t></a:r>'
      '</a:p></p:txBody></p:sp>')

def fix_activity(std, xml):
    # run 1 label
    xml = xml.replace('<a:t>Companion printable:  </a:t>',
                      '<a:t>Flight Log — write here:  </a:t>')
    # run 2 value (starts with "Cornell Notes — US.0N:")
    new2 = (f'US.0{std} — write your response in your Flight Log; the Cornell '
            f'Notes page for US.0{std} aligns to these Direct Instruction slides.')
    xml2 = re.sub(r'<a:t>Cornell Notes — US\.0\d:.*?</a:t>',
                  f'<a:t>{new2}</a:t>', xml, count=1)
    return xml2

def main(src, dst):
    zin = zipfile.ZipFile(src)
    tmp = dst + ".tmp"
    zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    di_done = act_done = 0
    di_slides = {v: k for k, v in FIRST_DI.items()}
    act_slides = {v: k for k, v in ACTIVITY.items()}
    for it in zin.infolist():
        data = zin.read(it.filename)
        m = re.match(r"ppt/slides/slide(\d+)\.xml$", it.filename)
        if m:
            idx = int(m.group(1)); xml = data.decode("utf-8")
            if idx in di_slides:
                std = di_slides[idx]
                if "FlightLogCue" not in xml:
                    xml = xml.replace("</p:spTree>", di_cue_sp(std) + "</p:spTree>", 1)
                    di_done += 1
            if idx in act_slides:
                before = xml
                xml = fix_activity(act_slides[idx], xml)
                if xml != before: act_done += 1
            data = xml.encode("utf-8")
        zout.writestr(it, data)
    zout.close(); zin.close()
    shutil.move(tmp, dst)
    print(f"{os.path.basename(dst)}: DI Cornell cues injected={di_done}/7, "
          f"activity strips repointed to Flight Log={act_done}/7")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
