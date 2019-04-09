# coding=UTF-8

import os 
d = raw_input("檢索目錄:")
i = raw_input("文件名:")

a = os.listdir(d)
b = []
for i in a:
        if 'p' in i:
                b.append(i)
        else:
                continue
print(b)