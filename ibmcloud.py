# -*- coding: UTF-8 -*-
import os
import ujson
from  api import api
import codecs

def fileRec(msg):
    fp = codecs.open("日志文件路径", 'a', 'utf-8')
    fp.writelines(msg+"\r\n")
    fp.close()

def main():
    hpath = "config文件路径"
    hsjon = ujson.Hjson_open(hpath)
    fileRec("开始执行脚本")
    for cfg in hsjon:
        o = api(ID=cfg, passwd=hsjon[cfg]["passwd"], debug = True)
        o.reset()
        
main()
