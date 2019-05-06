a = [0,1,2,3,4,5,6,7,8,9]
# a
[i for i in a]

# remove 8
[i for i in a if i != 8]

# retain even number
[i for i in a if i % 2 == 0]

with open ("1.txt", "r") as f:
    print " ".join([line.strip() for line in f.readlines()])

def remove8(x):
    # if x != 8:
    #     return True
    # else:
    #     return False
    # return x != 8 and True or False
    return x != 8

#filter
b = filter(remove8, a)
c = filter(lambda x: x != 8, a)
print b
print c

#map
print map(lambda x: x * x, a)

d = []
for i in a:
    d.append(i * i)
print d

print [i * i for i in a]

print map(lambda x: x != 8, a)

#reduce
print reduce(lambda x, y: x + x + y, a)
