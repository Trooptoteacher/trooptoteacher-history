#!/usr/bin/env python3
"""Open a DOCX via LibreOffice UNO, update all indexes (TOC) + fields, export PDF."""
import sys, os, subprocess, time
import uno
from com.sun.star.beans import PropertyValue
def url(p): return uno.systemPathToFileUrl(os.path.abspath(p))
def prop(n,v): pv=PropertyValue(); pv.Name=n; pv.Value=v; return pv
IN, OUT = sys.argv[1], sys.argv[2]
os.system("pkill -9 soffice 2>/dev/null"); time.sleep(1)
subprocess.Popen(['soffice','--headless','--invisible','--norestore','--nologo','--nofirststartwizard',
  '-env:UserInstallation=file:///tmp/uno_profile',
  '--accept=socket,host=localhost,port=2002;urp;StarOffice.ComponentContext'])
ctx=None
local=uno.getComponentContext()
resolver=local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',local)
for _ in range(40):
    try:
        ctx=resolver.resolve('uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext'); break
    except Exception: time.sleep(0.5)
if ctx is None: sys.exit('could not connect to soffice')
smgr=ctx.ServiceManager
desktop=smgr.createInstanceWithContext('com.sun.star.frame.Desktop',ctx)
doc=desktop.loadComponentFromURL(url(IN),'_blank',0,(prop('Hidden',True),))
try:
    idxs=doc.getDocumentIndexes()
    for i in range(idxs.getCount()): idxs.getByIndex(i).update()
except Exception as e: print('index update warn:',e)
try: doc.refresh()
except Exception as e: print('refresh warn:',e)
doc.storeToURL(url(OUT),(prop('FilterName','writer_pdf_Export'),))
doc.close(False)
try: desktop.terminate()
except Exception: pass
print('exported',OUT)
