a = []
  
with open("1.txt", "r") as f:
  for line in f.readlines():
    a.append(line.strip())

print " ".join(a).replace("Angus", "your name")
