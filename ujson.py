# -*- coding: UTF-8 -*-
import os
import json
import codecs

def Hjson_open(hfile):
    if (True == os.path.isfile(hfile)):
        hjson = json.loads(open(hfile, 'r',encoding='utf8').read())
    else:
        hjson = {}
    return hjson
        
def Update_hjson(hpath, hfile):
    fp = codecs.open(hpath, 'w', 'utf-8')
    fp.write(json.dumps(hfile, ensure_ascii=False, indent=4 ))
    fp.close()
    return
