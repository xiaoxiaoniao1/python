#code:UTF-8

import os 
d = raw_input("dir:")
i = raw_input("s:")

a = os.listdir(d)
b = []
for i in a:
        if 'p' in i:
                b.append(i)
        else:
                continue
print(b)
