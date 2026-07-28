// Teacher-deck <-> student-workbook ALIGNMENT LAYER (History Hack, any unit).
// Builds: 1 teacher intro ("How This Deck Drives the Workbook") + one
// "LESSON -> WORKBOOK MAP" slide per standard. These are INSERTED into the
// authentic teacher deck by merge_align.py — the authentic slides/images are
// never edited. The hero of each map slide is the DI -> Cornell (Activity 3)
// pairing, using the deck's real slide numbers.
//
// Usage:  NODE_PATH=<node_modules> node build_align_layer.js align.json teacher_align_layer.pptx
const pptx = require("pptxgenjs"), fs = require("fs");
const A = JSON.parse(fs.readFileSync(process.argv[2] || "align.json", "utf8"));
const OUT = process.argv[3] || "teacher_align_layer.pptx";
const dq = t => (t || "").replace(/&quot;/g, '"').replace(/&amp;/g, "&");
const tidy = t => { t = dq(t).trim(); return /[.!?]$/.test(t) ? t : t.replace(/\s+\S*$/, "") + "…"; };
const p = new pptx(); p.defineLayout({ name: "HH", width: 13.333, height: 7.5 }); p.layout = "HH";
// Canonical History Hack tokens (see references/design-tokens in the course-standard skill).
const NAVY="15223E",CARDBG="1E2C4C",PANEL="24345A",GOLD="C89B3C",CREAM="F7F5EF",INK="1A1A1A",
 WHITE="FFFFFF",BLUE="2F5FA6",GREY="6B7280",BORD="D9D5C8",RED="B22234",REDLT="FF6B7A",MUTE="9AA6BF",
 GREEN="2E7D46",NAVY2="1B2A4A",PAPER="EEF1F7";
const FOOT="U.S. History Hack   ·   TEACHER DECK   ·   Aligned to the Student Workbook & TN TCAP EOC";
let N=0;
function foot(s){N++; s.addText(FOOT,{x:0.5,y:7.06,w:11.4,h:0.3,fontFace:"Arial",fontSize:8,color:MUTE,margin:0});
  s.addText(String(N),{x:12.5,y:7.06,w:0.4,h:0.3,fontFace:"Arial",fontSize:9,color:MUTE,align:"right",margin:0});}
function chrome(s,tag,tagcol,code){ s.background={color:NAVY};
  s.addText(tag,{x:0.5,y:0.42,w:6.1,h:0.34,fontFace:"Arial",fontSize:11,bold:true,color:WHITE,fill:{color:tagcol},align:"center",valign:"middle",margin:2,charSpacing:1});
  s.addText(code,{x:11.4,y:0.42,w:1.43,h:0.34,fontFace:"Arial",fontSize:11,bold:true,color:NAVY,fill:{color:GOLD},align:"center",valign:"middle",margin:2}); foot(s);}

/* ---------- Intro: how the deck drives the workbook ---------- */
(function(){let s=p.addSlide(); s.background={color:NAVY};
 s.addText("How This Deck Drives the Workbook",{x:0.6,y:0.5,w:12.2,h:0.6,fontFace:"Cambria",fontSize:33,bold:true,color:WHITE,margin:0});
 s.addText("Teacher reference · every slide has a home in the student workbook — students never wonder where to write",
   {x:0.62,y:1.18,w:12,h:0.35,fontFace:"Arial",fontSize:14,italic:true,color:GOLD,margin:0});
 const flow=[
   ["QUICK REVIEW · CONFIDENCE · HOOK","Spaced recall + goal-setting","Before You Begin — Set Your Goal"],
   ["DIRECT INSTRUCTION  (3–4 slides)","You teach; students take Cornell notes live","Activity 3 — Direct Teaching Cornell Notes"],
   ["PRIMARY SOURCE ANALYSIS","Model close reading of the source","Activity 4 Close Read · Activity 5 Source"],
   ["KEY VOCABULARY · WORD WALL","Terms in EN + ES with definitions","Activity 1 Word Bank · Activity 2 Studio"],
   ["GUIDED PRACTICE · STUDENT ACTIVITY","We-do, then they-do","Guided Support · Activity 7 CER"],
   ["CHECK FOR UNDERSTANDING · REVEAL","TCAP-style item + answer key","Activity 6 Practice Quiz · Progress Check"],
 ];
 let y=1.75; const rh=0.72;
 flow.forEach((f,i)=>{
   s.addShape(p.ShapeType.rect,{x:0.6,y,w:5.75,h:rh-0.1,fill:{color:CARDBG},line:{color:i===1?GOLD:PANEL,width:i===1?1.5:1}});
   s.addText(f[0],{x:0.78,y:y+0.03,w:5.4,h:0.32,fontFace:"Arial",fontSize:12.5,bold:true,color:i===1?GOLD:WHITE,valign:"middle",margin:0});
   s.addText(f[1],{x:0.78,y:y+0.34,w:5.4,h:0.26,fontFace:"Arial",fontSize:10.5,italic:true,color:MUTE,valign:"middle",margin:0});
   s.addText("→",{x:6.45,y,w:0.5,h:rh-0.1,fontFace:"Arial",fontSize:18,bold:true,color:GOLD,align:"center",valign:"middle",margin:0});
   s.addShape(p.ShapeType.rect,{x:7.0,y,w:5.73,h:rh-0.1,fill:{color:i===1?"1F3320":PANEL},line:{color:i===1?GREEN:PANEL,width:i===1?1.5:1}});
   s.addText(f[2],{x:7.2,y,w:5.4,h:rh-0.1,fontFace:"Arial",fontSize:12.5,bold:i===1,color:i===1?"BDE6C8":"E7EAF2",valign:"middle",margin:0});
   y+=rh;
 });
 s.addText([{text:"MTSS:  ",options:{bold:true,color:GOLD}},
   {text:"the Check for Understanding is Tier-1 evidence — miss it and students route to reteach (Teacher Guide §16); master it and they take the extension. ",options:{color:WHITE}},
   {text:"The goal never lowers.",options:{bold:true,color:REDLT}}],
   {x:0.6,y:6.15,w:12.13,h:0.62,fontFace:"Arial",fontSize:12.5,valign:"middle",fill:{color:PANEL},margin:8,lineSpacingMultiple:1.03}); foot(s);})();

/* ---------- Per-standard LESSON -> WORKBOOK MAP ---------- */
for(const r of A.recs){
 let s=p.addSlide(); chrome(s,"LESSON → WORKBOOK MAP",BLUE,r.code);
 s.addText(dq(r.title),{x:0.6,y:0.95,w:12.1,h:0.5,fontFace:"Cambria",fontSize:23,bold:true,color:WHITE,valign:"top",margin:0});
 s.addText([{text:"I can ",options:{bold:true,color:GOLD}},{text:dq(r.ican).replace(/^I can\s*/i,""),options:{color:"E7EAF2"}}],
   {x:0.6,y:1.5,w:12.1,h:0.4,fontFace:"Arial",fontSize:12.5,italic:true,valign:"top",margin:0});

 const di=r.di_slides, cues=r.criteria;
 s.addShape(p.ShapeType.rect,{x:0.6,y:2.02,w:12.13,h:2.72,fill:{color:CARDBG},line:{color:GOLD,width:2}});
 s.addText([{text:"DIRECT INSTRUCTION",options:{bold:true,color:WHITE}},{text:"   →   ",options:{color:GOLD,bold:true}},
   {text:"ACTIVITY 3 · DIRECT TEACHING CORNELL NOTES",options:{bold:true,color:"BDE6C8"}}],
   {x:0.85,y:2.16,w:11.6,h:0.34,fontFace:"Arial",fontSize:13.5,charSpacing:0.5,valign:"middle",margin:0});
 s.addText("As you teach each slide below, students write in the matching Cornell cue row. Same words on the screen and on the page.",
   {x:0.85,y:2.5,w:11.6,h:0.32,fontFace:"Arial",fontSize:11,italic:true,color:MUTE,valign:"middle",margin:0});
 const nrow=Math.max(di.length,cues.length);
 const rowH=(4.62-2.9)/Math.max(nrow,3), y0=2.92;
 s.addText("DECK — Direct Instruction slide",{x:0.9,y:y0-0.02,w:5.5,h:0.24,fontFace:"Arial",fontSize:9.5,bold:true,color:GOLD,charSpacing:0.5,margin:0});
 s.addText("WORKBOOK — Cornell cue students write",{x:7.05,y:y0-0.02,w:5.5,h:0.24,fontFace:"Arial",fontSize:9.5,bold:true,color:"7FD69B",charSpacing:0.5,margin:0});
 for(let i=0;i<nrow;i++){
   const y=y0+0.26+i*rowH;
   const dlab=di[i]?`Slide ${di[i].n} · ${dq(di[i].label)}`:"—";
   const clab=cues[i]?dq(cues[i]):(i>=cues.length&&di[i]?"(folds into the cues above — capture in “Key terms →” row)":"—");
   s.addText([{text:(di[i]?`${i+1}. `:""),options:{bold:true,color:GOLD}},{text:dlab,options:{color:"E7EAF2"}}],
     {x:0.9,y,w:5.4,h:rowH,fontFace:"Arial",fontSize:11,valign:"top",margin:0,lineSpacingMultiple:0.98});
   s.addText([{text:(cues[i]?"▸ ":""),options:{bold:true,color:"7FD69B"}},{text:clab,options:{color:cues[i]?"D8F0E0":MUTE,italic:!cues[i]}}],
     {x:7.05,y,w:5.5,h:rowH,fontFace:"Arial",fontSize:11,valign:"top",margin:0,lineSpacingMultiple:0.98});
 }

 const xw=[
   ["PRIMARY SOURCE","Act. 4 Close Read + Act. 5 Source"],
   ["KEY VOCABULARY","Act. 1 Word Bank + Act. 2 Studio"],
   ["GUIDED / STUDENT ACTIVITY","Guided Support + Act. 7 CER"],
   ["CHECK + REVEAL","Act. 6 Practice Quiz + Progress Check"],
 ];
 const cw=(12.13-3*0.24)/4;
 xw.forEach((c,i)=>{const x=0.6+i*(cw+0.24);
   s.addShape(p.ShapeType.rect,{x,y:4.92,w:cw,h:1.32,fill:{color:PAPER},line:{color:BORD,width:1}});
   s.addText(c[0],{x:x+0.14,y:5.02,w:cw-0.28,h:0.5,fontFace:"Arial",fontSize:10,bold:true,color:NAVY2,valign:"top",margin:0,charSpacing:0.3});
   s.addText([{text:"→ ",options:{color:GREEN,bold:true}},{text:c[1],options:{color:INK}}],
     {x:x+0.14,y:5.5,w:cw-0.28,h:0.66,fontFace:"Arial",fontSize:10.5,valign:"top",margin:0,lineSpacingMultiple:1.0});});
 if(r.tn) s.addText([{text:"TN connection:  ",options:{bold:true,color:GOLD}},{text:tidy(r.tn),options:{color:MUTE}}],
   {x:0.6,y:6.34,w:12.13,h:0.34,fontFace:"Arial",fontSize:11,italic:true,valign:"middle",margin:0});
}
p.writeFile({fileName:OUT}).then(f=>console.log("WROTE",f,"slides:",N));
