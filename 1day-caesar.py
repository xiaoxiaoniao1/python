#!/usr/bin/python
import re
a = []
b = []
c = []
with open("44.txt") as f:
    for _ in f:
        if _ != '':
            a.append(_.strip())
#list1=sorted(set(a),key=a.index)

for x in a:
    if a.count(x) == 1:
        b.append(x)
    else:
        c.append(x)
print b
new = []
for _ in a:
    new.append(_.split('=')[0])
new2 = []
for i in new:
    if new.count(i)>1:
        #print  i
        new2.append(i)
l3 = list(set(new2))
d=[]
for aa in l3:
        for l in b:
                rule=re.compile(aa)
                if rule.findall(l):
                        print l