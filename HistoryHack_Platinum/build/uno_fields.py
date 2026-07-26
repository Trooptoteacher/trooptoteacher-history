#!/usr/bin/env python3
"""Open a DOCX in LibreOffice, update indexes (TOC) + all fields so page numbers are
BAKED into the field result, then save back as DOCX (correct in Word/Google Docs on open)
and also export a PDF. Usage: uno_fields.py in.docx out.docx out.pdf"""
import sys, os, subprocess, time, uno
from com.sun.star.beans import PropertyValue
def url(p): return uno.systemPathToFileUrl(os.path.abspath(p))
def prop(n,v): pv=PropertyValue(); pv.Name=n; pv.Value=v; return pv
IN, OUTDOC, OUTPDF = sys.argv[1], sys.argv[2], sys.argv[3]
os.system("pkill -9 soffice 2>/dev/null"); time.sleep(1)
subprocess.Popen(['soffice','--headless','--invisible','--norestore','--nologo','--nofirststartwizard',
  '-env:UserInstallation=file:///tmp/uno_fields','--accept=socket,host=localhost,port=2013;urp;StarOffice.ComponentContext'])
local=uno.getComponentContext()
res=local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',local)
ctx=None
for _ in range(40):
    try: ctx=res.resolve('uno:socket,host=localhost,port=2013;urp;StarOffice.ComponentContext'); break
    except Exception: time.sleep(0.5)
if ctx is None: sys.exit('no soffice')
smgr=ctx.ServiceManager
desktop=smgr.createInstanceWithContext('com.sun.star.frame.Desktop',ctx)
doc=desktop.loadComponentFromURL(url(IN),'_blank',0,(prop('Hidden',True),))
try:
    idx=doc.getDocumentIndexes()
    for i in range(idx.getCount()): idx.getByIndex(i).update()
except Exception as e: print('idx warn',e)
try: doc.getTextFields().refresh()
except Exception as e: print('fld warn',e)
try: doc.refresh()
except Exception: pass
# save DOCX (fields baked) then PDF
doc.storeToURL(url(OUTDOC),(prop('FilterName','MS Word 2007 XML'),))
doc.storeToURL(url(OUTPDF),(prop('FilterName','writer_pdf_Export'),))
doc.close(False)
try: desktop.terminate()
except Exception: pass
print('saved',OUTDOC,'and',OUTPDF)
