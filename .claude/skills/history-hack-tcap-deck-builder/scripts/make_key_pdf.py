#!/usr/bin/env python3
"""Render the Unit 1 Teacher Answer Key markdown to a branded PDF via ReportLab."""
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
                                Table, TableStyle, KeepTogether)
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor('#1A2332')
A250BLUE = colors.HexColor('#002858')
RED = colors.HexColor('#C62828')
GOLD = colors.HexColor('#C9A84C')
GOLDBR = colors.HexColor('#B8860B')
CREAM = colors.HexColor('#F7F4EC')
INK = colors.HexColor('#1F2430')
MUTE = colors.HexColor('#5C6470')

SRC = '/home/user/workspace/Unit1_Teacher_Answer_Key.md'
OUT = '/home/user/workspace/Unit1_Teacher_Answer_Key.pdf'

def md_inline(t):
    t = t.replace('&', '&amp;')
    # markdown links [text](url) -> clickable hyperlink (do before bold/italic)
    t = re.sub(r'\[([^\]]+?)\]\((https?://[^)]+?)\)',
               r'<a href="\2" color="#002858"><u>\1</u></a>', t)
    # bold
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    # italic *text*
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', t)
    # arrows / em dash already unicode
    return t

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Title'], fontName='Helvetica-Bold',
                    fontSize=22, textColor=NAVY, spaceAfter=2, leading=26, alignment=TA_LEFT)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=11, textColor=RED,
                     spaceAfter=10, leading=14)
INTRO = ParagraphStyle('INTRO', fontName='Helvetica-Oblique', fontSize=9.5,
                       textColor=MUTE, spaceAfter=6, leading=13)
BRAND = ParagraphStyle('BRAND', fontName='Helvetica-Bold', fontSize=9,
                       textColor=A250BLUE, spaceAfter=4, leading=12)
H2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=15, textColor=colors.white,
                    leading=18, spaceBefore=4, spaceAfter=4, leftIndent=6)
H3 = ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=11.5, textColor=A250BLUE,
                    leading=14, spaceBefore=8, spaceAfter=3)
BODY = ParagraphStyle('BODY', fontName='Helvetica', fontSize=10, textColor=INK,
                      leading=13.5, spaceAfter=3)
QUOTE = ParagraphStyle('QUOTE', fontName='Helvetica-Oblique', fontSize=10, textColor=NAVY,
                       leading=14, leftIndent=10, spaceAfter=3, backColor=colors.HexColor('#EFEAD9'),
                       borderPadding=(4,4,4,4))
LI = ParagraphStyle('LI', fontName='Helvetica', fontSize=10, textColor=INK,
                    leading=13.5, leftIndent=14, bulletIndent=4, spaceAfter=1)
LICORRECT = ParagraphStyle('LICORRECT', parent=LI, textColor=colors.HexColor('#1B5E20'),
                           fontName='Helvetica-Bold')

flow = []
lines = open(SRC, encoding='utf-8').read().split('\n')
i = 0
intro_done = False
while i < len(lines):
    ln = lines[i].rstrip()
    if ln.startswith('# '):
        flow.append(Paragraph(md_inline(ln[2:]), H1))
    elif ln.startswith('### '):
        flow.append(Paragraph(md_inline(ln[4:]), H3))
    elif ln.startswith('## '):
        # navy section band
        p = Paragraph(md_inline(ln[3:]), H2)
        tbl = Table([[p]], colWidths=[6.9*inch])
        tbl.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,-1),NAVY),
            ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
            ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
        ]))
        flow.append(Spacer(1,6))
        flow.append(tbl)
        flow.append(Spacer(1,4))
    elif ln.startswith('> '):
        flow.append(Paragraph(md_inline(ln[2:]), QUOTE))
    elif ln.startswith('- '):
        txt = ln[2:]
        style = LICORRECT if 'CORRECT' in txt else LI
        flow.append(Paragraph('• ' + md_inline(txt), style))
    elif ln.startswith('---'):
        flow.append(Spacer(1,4))
        flow.append(HRFlowable(width='100%', thickness=0.8, color=GOLD))
        flow.append(Spacer(1,2))
    elif ln.strip().startswith('**TroopToTeacher'):
        flow.append(Paragraph(md_inline(ln.strip()), BRAND))
    elif ln.strip().startswith('*') and ln.strip().endswith('*') and not intro_done:
        flow.append(Paragraph(md_inline(ln.strip().strip('*')), INTRO))
        intro_done = True
    elif ln.strip():
        flow.append(Paragraph(md_inline(ln), BODY))
    i += 1

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(MUTE)
    canvas.drawString(0.85*inch, 0.5*inch,
        'U.S. History Hack · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards & TCAP EOC')
    canvas.drawRightString(7.65*inch, 0.5*inch, f'Page {doc.page}')
    canvas.setFillColor(GOLD)
    canvas.rect(0.85*inch, 0.62*inch, 6.8*inch, 0.012*inch, fill=1, stroke=0)
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=letter,
                        leftMargin=0.85*inch, rightMargin=0.85*inch,
                        topMargin=0.7*inch, bottomMargin=0.8*inch,
                        title='U.S. History Hack — Unit 1 Teacher Answer Key',
                        author='Perplexity Computer')
doc.build(flow, onFirstPage=footer, onLaterPages=footer)
print('WROTE', OUT)
