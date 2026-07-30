// Unit 1 — TEACHER Assessment Book (Formative + Summative Form A/B + Teacher Key/Analysis).
// Items pulled from the canonical question bank (unit1_assessment.json). Platinum tokens.
const fs=require('fs'); const D=require('docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,
  WidthType,BorderStyle,ShadingType,PageBreak,Header,Footer,PageNumber,TableOfContents}=D;
const A=JSON.parse(fs.readFileSync('analysis/unit2_assessment.json','utf8'));
const C=JSON.parse(fs.readFileSync('analysis/unit2_content.json','utf8')).standards;
const UNIT=JSON.parse(fs.readFileSync('analysis/unit2_content.json','utf8')).unit;
const BRAND=(UNIT.brand||'Government Hack'); const BRANDTM=BRAND+'\u2122'; const UCODE=UNIT.code||'Unit 1'; const UTITLE=UNIT.title||'';
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
const header=new Header({children:[P(R(BRANDTM+' · '+UCODE+' · Assessment Book (Teacher)',{s:16,b:true,c:GOLD}),{align:AlignmentType.RIGHT,spacing:{after:0}})]});
const footer=new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,children:[R(BRANDTM+' · '+UCODE+' (Course Standard) © 2026 TroopToTeacher Technologies LLC   |   Page ',{s:16,c:GREY}),new TextRun({children:[PageNumber.CURRENT],size:16,color:GREY,font:FONT})]})]});
const cover=[
 new Paragraph({spacing:{before:1400,after:0},children:[R(BRANDTM.toUpperCase(),{s:30,b:true,c:GOLD})]}),
 new Paragraph({spacing:{after:0},children:[R('Unit Assessment Book',{s:52,b:true,c:NAVY})]}),
 new Paragraph({spacing:{after:200},children:[R(UCODE+' — '+UTITLE+'  \u00b7  Teacher Edition',{s:26})]}),
 callout('HOW TO USE THIS BOOK',[
   'Three parts: (1) Formative Checkpoints — a short check per standard for progress monitoring (MTSS); (2) Unit Summative — two parallel forms (A and B) for pre/post or retakes; (3) Teacher Answer Key + Item Analysis + Reteach.',
   'All items are pulled from the '+BRAND+' question bank. '+A.disclosure,
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

// ---- Section 5: Psychometric Blueprint (teacher-facing; design-time estimates) ----
function psychTable(title,items){const ws=[600,980,700,1560,600,600,600,680,720,2568];
  const rows=[dhead(['Item','Std','DOK','Bloom’s (Hess cell)','a','b','c','C3','FT?','Distractor codes'],ws)];
  items.forEach((q,i)=>{
    const dt=(q.distractor_tags||[]).map(t=>`${t.label}:${t.code}`).join(' ');
    rows.push(drow([i+1,q.std,q.dok,(q.hess_crm_cell||q.blooms||'—'),
      (q.irt_a!=null?q.irt_a:'—'),(q.irt_b!=null?q.irt_b:'—'),(q.irt_c!=null?q.irt_c:'—'),
      (q.c3_dimension||'—'),(q.field_test_ready?'Y':'N'),dt||'—'],ws));});
  return [H(title,2),table(rows,ws)];}
const PS=A._psychometric_summary||{};
function distRow(obj){return obj?Object.keys(obj).map(k=>`${k}: ${obj[k]}`).join('   ·   '):'—';}
const psych=[H('Part 5 — Psychometric Blueprint (Teacher)',1,{brk:true}),
 callout('ABOUT THESE NUMBERS',[
   'Every item carries a cognitive-rigor classification (Webb’s DOK × Bloom’s, located on the Hess Cognitive Rigor Matrix) and a pre-calibration IRT 3PL estimate: a = discrimination, b = difficulty, c = pseudo-guessing.',
   'These IRT parameters are DESIGN-TIME ESTIMATES, not empirical calibrations. '+(PS.note||'They are refined once field-test response data is collected.')+' '+A.disclosure,
   'Distractor codes: PK prior-knowledge · MC misconception · PE partial evidence · NE nearby error · CA causal attribution · AN anachronism · OG overgeneralization.']),
 ...(PS.dok_distribution?[callout('BANK DISTRIBUTION',[
   'DOK: '+distRow(PS.dok_distribution),
   'Bloom’s: '+distRow(PS.blooms_distribution),
   'Mean discrimination a ≈ '+(PS.irt_a_mean!=null?PS.irt_a_mean:'—')+'   ·   Mean difficulty b ≈ '+(PS.irt_b_mean!=null?PS.irt_b_mean:'—'),
   'Field-test-ready items: '+(PS.field_test_ready_count!=null?PS.field_test_ready_count:'—')+' of '+(PS.total_items!=null?PS.total_items:'—')])]:[]),
 ...psychTable('Form A — item psychometrics',A.formA),
 ...psychTable('Form B — item psychometrics',A.formB),
 ...psychTable('Formative — item psychometrics',flatFormative)];


// ---- Section 6: UDL Supports & Remediation (teacher) ----
function udlRemedSection(title,items){const out=[H(title,2)];
  items.forEach((q,i)=>{const rem=q.remediation||{};
    out.push(H(`Item ${i+1} — ${q.std} · DOK ${q.dok}`,3));
    out.push(P([R('If missed:  ',{s:22,b:true,c:NAVY}),R(rem.if_missed||'—',{s:22})]));
    const bd=rem.by_distractor||[];
    if(bd.length){const ws=[900,4400,4348];
      const rows=[dhead(['Wrong choice','Signals misconception','Targeted reteach'],ws)];
      bd.forEach(d=>rows.push(drow([d.choice,d.signals_misconception,d.reteach],ws)));
      out.push(table(rows,ws));
    } else { out.push(P(R('Open-response item — score against the rubric criteria; no distractor routing.',{s:21,i:true}))); }
    const m=rem.mtss||{};
    out.push(callout('MTSS ROUTING',['Tier 2 — '+(m.tier2||'—'),'Tier 3 — '+(m.tier3||'—')]));
  });
  return out;}
const _u=((A.formA[0]||A.formB[0]||flatFormative[0]||{}).udl_supports)||{};
const part6=[H('Part 6 — UDL Supports & Remediation (Teacher)',1,{brk:true}),
 callout('UNIVERSAL DESIGN FOR LEARNING (UDL 3.0) SUPPORTS — APPLIES TO EVERY ITEM',[
   R('These supports vary the MEANS of access, not the mastery target. They apply to every item on the formative checkpoints and both summative forms.',{s:22,i:true}),
   'Representation — '+(_u.representation||'—'),
   'Action & Expression — '+(_u.action_expression||'—'),
   'Engagement — '+(_u.engagement||'—'),
   (_u.firm_goal_note||''),
   (_u.udl_citation||'')]),
 callout('HOW TO USE THIS SECTION',['For each item: if a student misses it, start with the If-missed reteach, then route by the SPECIFIC wrong choice the student picked (each distractor signals a distinct misconception), and escalate through MTSS Tier 2 → Tier 3 if the misconception persists across parallel forms. '+A.disclosure]),
 ...udlRemedSection('Form A — UDL & distractor-based remediation',A.formA),
 ...udlRemedSection('Form B — UDL & distractor-based remediation',A.formB),
 ...udlRemedSection('Formative Checkpoints — UDL & distractor-based remediation',flatFormative)];

const doc=new Document({styles:{default:{document:{run:{font:FONT,size:22,color:INK}}}},
  sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1152,bottom:1152,left:1296,right:1296,header:720,footer:720}}},
  headers:{default:header},footers:{default:footer},
  children:[...cover,...formative,...formA,...formB,...key,...psych,...part6]}]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync('deliverables/Unit2_Assessment_Book_Teacher.docx',b);console.log('WROTE assessment book',b.length,'bytes');});
