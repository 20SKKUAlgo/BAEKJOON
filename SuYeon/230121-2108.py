import sys
input = sys.stdin.readline

num = int(input())
nlist = []
many = {}
for i in range(num):
    n = int(input())
    if n not in nlist:
        many[n] = 0
    else:
        many[n] += 1
    nlist.append(n)

nlist.sort()

print(sum(nlist)//num)
print(nlist[2])

maxcnt = 0
res = 0

for x in many:
    if many.get(x) > maxcnt:
        maxcnt = many.get(x)
        res= x

maxlist = []
for x in many:
    if many.get(x) == maxcnt:
        maxlist.append(x)
maxlist.sort()

print(maxlist[1])
print(nlist[num-1]-nlist[0])
