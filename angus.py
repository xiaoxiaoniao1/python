result = set()
with open("1.txt","r") as f:
  for line in f.readlines():
    result.add(line)

keys = []
for i in result:
  key = i.split("=")[0]
  if key in keys:
    print "key is exists %s" % key
  else:
    keys.append(key)

with open("2.txt", "w") as f:
  for i in result:
    f.write(i)
