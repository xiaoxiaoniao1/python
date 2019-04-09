# coding=UTF-8
import os

d = raw_input("檢索目錄:")
s = raw_input("內容:")
os.chdir(d)
a = os.listdir(d)
for i in a:
        with open("./"+i ,"r") as f:
                if s in f.read():
                        print(i)
                else:
                        continue