from albertv0 import *
import subprocess
__iid__ = "PythonInterface/v0.1"
__prettyname__ = "howdoi"
__version__ = "0.1"
__trigger__ = "howdoi "

def handleQuery(query):
    if query.isTriggered:
        return [Item(text=subprocess.check_output("howdoi " + query.string, shell=True))]
