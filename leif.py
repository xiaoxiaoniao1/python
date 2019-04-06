#!/usr/bin/env python 
keylist=[]
valuelist=[]
keyrepeat=[]
with open("1.txt","r+") as f:
    line=f.readline()
    while line.strip():
        key=line.split("=")[0]
        val=line.split("=")[1]
        if key in keylist:
            keyrepeat.append(key)
            if val in valuelist:
                print ("\033[1;31;40mkey and value repeat:%s=%s\033[0m" %(key,val))
            else:
                print("key repeat but value no repeat:%s=%s"%(key,val))
        else:
            keylist.append(key)
            valuelist.append(val)
        line=f.readline()
print("key repeat:",keyrepeat)
