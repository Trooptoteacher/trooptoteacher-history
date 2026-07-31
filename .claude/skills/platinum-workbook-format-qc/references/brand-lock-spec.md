# Brand-Lock Spec — exact constants & helper contracts

Every measurement below is extracted from the U.S. History Hack Course Standard workbook (the brand
reference). Reproduce verbatim in any subject edition. All sizes are docx **half-points**; all page
metrics are **twips** (1440/inch). `SZ(n)=Math.round(n*LP)` applies the `LARGEPRINT` multiplier.

## Header block (top of every build_workbook.js)

```js
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,
  WidthType,BorderStyle,ShadingType,PageBreak,TableOfContents,Header,Footer,PageNumber,HeightRule,ImageRun}=D;

// ---- exact tokens ----
const NAVY='1B2A4A', RED='B22234', GOLD='C89B3C', INK='1A1A1A', CREAM='F7F5EF',
      WHITE='FFFFFF', GREY='6B7280', BORD='D9D5C8';
const FONT='Calibri';
const CW=9792;                          // printable width = 12240 − 1224 − 1224
const bd=(c=BORD,sz=4)=>({style:BorderStyle.SINGLE,size:sz,color:c});
const CELLB=(c=BORD)=>({top:bd(c),bottom:bd(c),left:bd(c),right:bd(c)});
const LP=process.env.LARGEPRINT?Number(process.env.LARGEPRINT):1;
const SZ=(n)=>Math.round(n*LP);
```

## Section / page (document assembly)
```js
sections:[{properties:{page:{
  size:{width:12240,height:15840},
  margin:{top:1152,bottom:1152,left:1224,right:1224,header:720,footer:720}}}, ... }]
```
- Letter portrait. **Never** change margins or page size — CW is derived from them.
- Header/footer at 720. Footer carries `BRAND™ · Unit N (Course Standard) · © YEAR · Page N`.

## Core text/paragraph/heading helpers (LOCKED signatures)
```js
function R(text,{s=22,b=false,i=false,c=INK,caps=false}={}){
  return new TextRun({text,size:SZ(s),bold:b,italics:i,color:c,font:FONT,allCaps:caps});}

function P(runs,{align,spacing,indent,border}={}){
  return new Paragraph({alignment:align,spacing:spacing||{after:100},indent,border,
    children:Array.isArray(runs)?runs:[runs]});}

function H(text,lvl,{brk=false,mins=null}={}){
  const map={1:HeadingLevel.HEADING_1,2:HeadingLevel.HEADING_2,3:HeadingLevel.HEADING_3};
  const kids=[R(text,{s:lvl===1?36:lvl===2?28:24,b:true,c:lvl===3?RED:NAVY})];
  if(mins) kids.push(R(`    ⏱ ~${mins} min`,{s:18,b:true,c:GOLD}));
  return new Paragraph({heading:map[lvl],pageBreakBefore:brk,spacing:{before:lvl===1?220:150,after:90},
    keepNext:true,children:kids});}
```
- Body text = size **22**. Heading sizes **36 / 28 / 24**. Use `{brk:true}` to start an activity on a
  fresh page, `{mins:N}` for the time chip.

## Table & cell (LOCKED)
```js
function cell(children,{w,fill,borders}={}){return new TableCell({width:{size:w,type:WidthType.DXA},
  shading:fill?{type:ShadingType.CLEAR,fill,color:'auto'}:undefined,
  margins:{top:55,bottom:55,left:110,right:110},
  borders:borders||CELLB(),children:Array.isArray(children)?children:[children]});}

function table(rows,widths){return new Table({width:{size:CW,type:WidthType.DXA},columnWidths:widths,rows});}
```
- **columnWidths must sum to `CW` (9792).** Common splits: `[4896,4896]`, `[3264,3264,3264]`,
  `[2723,4347,2722]` (word bank), `[2448,7344]` (cornell body), self-check `[3092,1675,1675,1675,1675]`.

## Ruled writing lines — the anti-merge helper (CRITICAL)
```js
function ruled(n=3){const out=[];for(let i=0;i<n;i++){
  out.push(new Paragraph({widowControl:false,spacing:{before:SZ(28),after:SZ(28)},
    border:{bottom:{style:BorderStyle.SINGLE,size:8,color:'8892A0',space:1}},
    children:[new TextRun({text:' ',size:SZ(16),font:FONT})]}));
  if(i<n-1) out.push(new Paragraph({spacing:{before:0,after:0,line:SZ(50),lineRule:'exact'},
    children:[new TextRun({text:' ',size:SZ(2),font:FONT})]}));
}return out;}
function linesFor(h){return Math.max(2,Math.round(h/380));}
```
- Line color **`8892A0`**, size **8**. The border-less spacer between lines is what makes each line
  render separately (Word/Spire otherwise collapse adjacent identical-border paragraphs to one line).
- To put lines inside a table cell, pass `ruled(n)` as the cell's children.

## Callouts (cream info box / navy CORE-PATH bar)
```js
function callout(label,lines=[]){const kids=[P(R(label,{s:21,b:true,c:NAVY}),{spacing:{after:lines.length?60:0}})];
  (Array.isArray(lines)?lines:[lines]).forEach(l=>kids.push(P(typeof l==='string'?R(l,{s:22}):l,{spacing:{after:40}})));
  return table([new TableRow({children:[cell(kids,{w:CW,fill:CREAM})]})],[CW]);}

function coreCallout(label,lines=[]){const kids=[P(R(label,{s:23,b:true,c:GOLD}),{spacing:{after:lines.length?70:0}})];
  (Array.isArray(lines)?lines:[lines]).forEach(l=>kids.push(P(typeof l==='string'?R(l,{s:22,c:WHITE}):l,{spacing:{after:40}})));
  return table([new TableRow({children:[cell(kids,{w:CW,fill:NAVY,borders:CELLB(NAVY)})]})],[CW]);}
```
- **Bolding part of a callout line:** pass an **array of runs** as the line (not a string). The helper
  detects non-strings and passes them straight to `P()`. Example — bold just the label:
  `callout('LANGUAGE SUPPORT',[[R('Pronunciations: ',{s:22,b:true}),R(rest,{s:22})]])`.
- `callout` = cream `F7F5EF`, navy label. `coreCallout` = navy fill, gold label, white text (the firm,
  universal CORE-PATH bar).

## Write helpers
```js
// header row + data/writing rows; blank cell => ruled lines, text cell => bold-first-col text
function writeTable(headers,rows,widths,{rowH=560,lines}={}){ ... uses cell()/ruled()/linesFor ... }
// cream label bar over a full-width ruled writing area
function writeBox(label,nLines=3){return table([
  new TableRow({children:[cell(P(R(label,{s:21,b:true,c:NAVY}),{spacing:{after:0}}),{w:CW,fill:CREAM})]}),
  new TableRow({children:[cell(ruled(nLines),{w:CW})]})],[CW]);}
```

## Cornell notes (LOCKED layout)
- Grid `4896|4896`; **body cells `2448` (cue) | `7344` (notes)**; navy header row
  (`Guiding cues` | notes label), zebra rows (`CREAM`/`WHITE`), `cantSplit`, `HeightRule.ATLEAST`.
- The wide notes column is filled with `ruled(n)` so notes run as notebook lines across the page.
- Cornell cell padding `top/bottom 50, left/right 80`.

## Data table (navy header)
```js
function dataTable(headers,rows,widths){ // navy header row, body rows size-20; used for word bank etc.
```

## Open draw / diagram box (no lines — for sketching)
A single-cell full-width table with a tall `HeightRule.ATLEAST` row and one blank paragraph:
```js
table([new TableRow({height:{value:H,rule:HeightRule.ATLEAST},
  children:[cell(P(R(' ',{s:12}),{spacing:{after:0}}),{w:CW})]})],[CW])
```
Use for DIAGRAM/DOODLE/concept-map areas. Typical heights: 1050 (small), 1900–2100 (term box),
2300–2600 (concept map).

## Verification after copying into a new course
Grep the new builder and confirm, before building:
- `const CW=9792;`  · margins `1224` and page `12240×15840`  · palette hexes above  · `Calibri`
- a `ruled(` with color `8892A0`  · a `cornell` function with `2448`/`7344`  · every `table(...,widths)`
  columnWidths summing to 9792.
