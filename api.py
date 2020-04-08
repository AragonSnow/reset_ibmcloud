# -*- coding: UTF-8 -*-
import os
import codecs

def fileRec(msg):
    fp = codecs.open("日志文件路径", 'a', 'utf-8')
    fp.writelines(msg+"\r\n")
    fp.close()

class api:
    def __init__(self, *args, **kwargs):
        self.ID = kwargs['ID']
        self.passwd = kwargs['passwd']
        if ("debug" in kwargs): self.debug = kwargs['debug']
    
    def findstr(self, out , target):
        lines = out.split("\n")
        for line in lines:
            if (line.find("FAILED") > -1):
                return out
        return "OK"

    def reset(self):
        fileRec("1")
        if (self.status() == "OK"):
            fileRec('2')
            login = "/usr/local/bin/ibmcloud login -u {ID} -p {passwd} -r us-south".format(ID = self.ID,passwd = self.passwd)
            cflogin = "/usr/local/bin/ibmcloud target --cf-api https://api.ng.bluemix.net -o {ID} -s dev".format(ID = self.ID)
            out = os.popen(login, "r").read()
            if (self.debug): 
                print(out)
                fileRec(out)
            out = self.findstr(out, "FAILED")
            if (out == "OK"):
                fileRec('3')
                out = os.popen(cflogin, "r").read()
                if (self.debug): 
                    print(out)
                    fileRec(out)
                out = self.findstr(out, "FAILED")
                if (out == "OK"):
                    fileRec('4')
                    applistcmd = "/usr/local/bin/ibmcloud cf apps"
                    out = os.popen(applistcmd, "r").read()
                    if (self.debug): 
                        print(out)
                        fileRec(out)
                    lines = out.split("\n")
                    prjs = []
                    out = self.findstr(out, "FAILED")
                    if (out == "OK"):
                        for line in lines:
                            if line.find("us-south.cf.appdomain.cloud") >-1:
                                prjs.append(line.split(" ")[0])
                        for prj in prjs:
                            resetcmd = "/usr/local/bin/ibmcloud cf restart {prj}".format(prj = prj)
                            out = os.popen(resetcmd, "r").read()
                            if (self.debug): 
                                print(out)
                                fileRec(out)
                            out = self.findstr(out, "FAILED")
            logout = "/usr/local/bin/ibmcloud logout"
            os.popen(logout, "r").read()
        else:
            out = "API正在被调用，请稍后重试"
            if (self.debug): 
                print(out)
                fileRec(out)
        return out

    def status(self):
        findii = "ps -A | grep ibmcloud"
        out = os.popen(findii, "r").read()
        out = self.findstr(out, "ibmcloud")
        return out
        
        


