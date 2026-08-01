// Unit 5 — TEACHER Assessment Book (Formative + Summative Form A/B + Teacher Key/Analysis).
// Items pulled from the canonical question bank (unit2_assessment.json). Platinum tokens.
const fs=require('fs'); const D=require('docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,
  WidthType,BorderStyle,ShadingType,PageBreak,Header,Footer,PageNumber,TableOfContents}=D;
const A=JSON.parse(fs.readFileSync('analysis/unit5_assessment.json','utf8'));
const C=JSON.parse(fs.readFileSync('analysis/unit5_content.json','utf8')).standards;
const NAVY='1B2A4A',RED='B22234',GOLD='C89B3C',INK='1A1A1A',CREAM='F7F5EF',WHITE='FFFFFF',GREY='6B7280',BORD='D9D5C8',FONT='Calibri',CW=9648;
const bd=(c=BORD)=>({style:BorderStyle.SINGLE,size:4,color:c,space:0});
const CELLB=(c=BORD)=>({top:bd(c),bottom:bd(c),left:bd(c),right:bd(c)});
function R(t,{s=22,b=false,i=false,c=INK}={}){return new TextRun({text:t,size:s,bold:b,italics:i,color:c,font:FONT});}
function P(runs,{align,spacing,indent}={}){return new Paragraph({alignment:align,spacing:spacing||{after:80},indent,children:Array.isArray(runs)?runs:[runs]});}
function H(t,lvl,{brk=false}={}){const map={1:HeadingLevel.HEADING_1,2:HeadingLevel.HEADING_2,3:HeadingLevel.HEADING_3};
  return new Paragraph({heading:map[lvl],pageBreakBefore:brk,spacing:{before:lvl===1?200:150,after:90},keepNext:true,children:[R(t,{s:lvl===1?36:lvl===2?28:24,b:true,c:lvl===3?RED:NAVY})]});}
function cell(children,{w,fill}={}){return new TableCell({width:{size:w,type:WidthType.DXA},shading:fill?{type:ShadingType.CLEAR,fill,color:'auto'}:undefined,margins:{top:55,bottom:55,left:110,right:110},borders:CELLB(),children:Array.isArray(children)?children:[children]});}
function table(rows,widths){return new Table({width:{size:CW,type:WidthType.DXA},columnWidths:widths,rows});}
function callout(label,lines=[]){const kids=[P(R(label,{s:21,b:true,c:NAVY}),{spacing:{after:lines.length?60:0}})];
  (Array.isArray(lines)?lines:[lines]).forEach(l=>kids.push(P(typeof l==='string'?R(l,{s:22}):l,{spacing:{after:40}})));
  return table([new TableRow({children:[cell(kids,{w:CW,fill:CREAM})]})],[CW]);}
function dhead(hs,ws){return new TableRow({tableHeader:true,children:hs.map((h,i)=>cell(P(R(h,{s:18,b:true,c:WHITE}),{spacing:{after:0}}),{w:ws[i],fill:NAVY}))});}
function drow(cs,ws){return new TableRow({children:cs.map((cx,i)=>cell(P(R(String(cx),{s:18}),{spacing:{after:0}}),{w:ws[i]}))});}

// ---- student item (no answer shown) ----
function item(q,n){const out=[
  P([R(`${n}.  `,{s:22,b:true}),R(q.stem,{s:22,b:true}),R(`   [${q.std} · DOK ${q.dok} · pre-field-test]`,{s:15,c:GREY})],{spacing:{after:40}})];
  q.choices.forEach(c=>out.push(P(R(`${c.id}.  ${c.text}`,{s:21}),{indent:{left:360},spacing:{after:24}})));
  out.push(P(R('',{s:8}),{spacing:{after:60}}));
  return out;}
function studentForm(title,items,{brk=true}={}){const out=[H(title,1,{brk})];
  out.push(callout('DIRECTIONS',['Choose the best answer for each question. '+A.disclosure]));
  out.push(P(R('Name: ______________________________     Class / Period: __________     Date: __________',{s:21})));
  let n=1; items.forEach(q=>item(q,n++).forEach(p=>out.push(p)));
  return out;}

// ---- COVER + front ----
const header=new Header({children:[P(R('U.S. History Hack™ · Unit 5 · Assessment Book (Teacher)',{s:16,b:true,c:GOLD}),{align:AlignmentType.RIGHT,spacing:{after:0}})]});
const footer=new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,children:[R('U.S. History Hack™ · Unit 5 (Course Standard) © 2026 TroopToTeacher Technologies LLC   |   Page ',{s:16,c:GREY}),new TextRun({children:[PageNumber.CURRENT],size:16,color:GREY,font:FONT})]})]});
const cover=[
 new Paragraph({spacing:{before:1400,after:0},children:[R('U.S. HISTORY HACK™',{s:30,b:true,c:GOLD})]}),
 new Paragraph({spacing:{after:0},children:[R('Unit Assessment Book',{s:52,b:true,c:NAVY})]}),
 new Paragraph({spacing:{after:200},children:[R('Unit 5 — The Great Depression & New Deal (1929–1941)  ·  Teacher Edition',{s:26})]}),
 callout('HOW TO USE THIS BOOK',[
   'Three parts: (1) Formative Checkpoints — a short check per standard for progress monitoring (MTSS); (2) Unit Summative — two parallel forms (A and B) for pre/post or retakes; (3) Teacher Answer Key + Item Analysis + Reteach.',
   'All items are pulled from the History Hack question bank. '+A.disclosure,
   'Administering these forms is what generates the response data to CALIBRATE the pre-calibrated items — the first cycle of use closes the loop.',
   'Keys and reteach live in this teacher book only — reproduce the student sections (formative + Form A/B) without the key section.']),
 H('Contents',1), new TableOfContents('Contents',{hyperlink:true,headingStyleRange:'1-1'}),
];

// ---- Section 1: Formative Checkpoints ----
const formative=[H('Part 1 — Formative Checkpoints (by standard)',1,{brk:true}),
 P(R('A quick DOK-balanced check for each standard. Use for progress monitoring; reteach routing is in the Teacher Key.',{s:22}))];
Object.keys(A.formative).forEach(std=>{
  formative.push(H(`${std} — ${C[std].title}`,2));
  let n=1; A.formative[std].forEach(q=>item(q,n++).forEach(p=>formative.push(p)));
});

// ---- Sections 2 & 3: Summative Form A / B ----
const formA=studentForm('Part 2 — Unit Summative · Form A',A.formA);
const formB=studentForm('Part 3 — Unit Summative · Form B',A.formB);

// ---- Section 4: Teacher Key + Item Analysis + Reteach ----
function keyTable(title,items){const ws=[900,1100,900,900,1900,3948];
  const rows=[dhead(['Item','Standard','DOK','Key','Reporting cat.','What’s Next if missed (reteach)'],ws)];
  items.forEach((q,i)=>{const reteach=`Revisit ${C[q.std].title} — Cornell cues + Guided Support; re-check with the Exit Ticket.`;
    rows.push(drow([i+1,q.std,q.dok,q.key,q.rc||'—',reteach],ws));});
  return [H(title,2),table(rows,ws)];}
const flatFormative=[]; Object.keys(A.formative).forEach(s=>A.formative[s].forEach(q=>flatFormative.push(q)));
const key=[H('Part 4 — Teacher Answer Key + Item Analysis + Reteach',1,{brk:true}),
 callout('READING THE ANALYSIS',['Each item shows its standard, DOK, correct key, and TCAP reporting category, plus a reteach move. Distractor-based routing: a wrong choice signals which idea to reteach — pair with the workbook Cornell notes and Guided Support. '+A.disclosure]),
 ...keyTable('Form A — key & reteach',A.formA),
 ...keyTable('Form B — key & reteach',A.formB),
 ...keyTable('Formative Checkpoints — key & reteach',flatFormative)];

const doc=new Document({styles:{default:{document:{run:{font:FONT,size:22,color:INK}}}},
  sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1152,bottom:1152,left:1296,right:1296,header:720,footer:720}}},
  headers:{default:header},footers:{default:footer},
  children:[...cover,...formative,...formA,...formB,...key]}]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync('deliverables/Unit5_Assessment_Book_Teacher.docx',b);console.log('WROTE assessment book',b.length,'bytes');});
