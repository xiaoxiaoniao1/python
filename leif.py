#!/usr/bin/env python 
#!_*_coding:utf-8_*_
keylist=[]
valuelist=[]
keyrepeat=[]
key_val_repeat=[]
with open("1.txt","r+") as f:
    line=f.readline()
    while line.strip():
        key=line.split("=")[0]
        val=line.split("=")[1]
        if key in keylist:
            keyrepeat.append(key)
            if val in valuelist:
                print ("\033[1;31;40mkey and value repeat:%s=%s\033[0m" %(key,val))
                key_val=key+"="+val
                key_val_repeat.append(key)
            else:
                print("key repeat but value no repeat:%s"%key)
        else:
            keylist.append(key)
            valuelist.append(val)
        line=f.readline()
print("去重后的结果")
with open("1.txt","r+") as f:
    for line in f:
        for i in key_val_repeat:
            if i in line.split("=")[0] :
                continue
            else:
                print line.strip()
