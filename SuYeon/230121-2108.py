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

######################################################################
#아래 알고리즘은 런타임 에러가 뜸.... 왜......????? 답은 나옴...
import sys
import math
input = sys.stdin.readline

num = int(input())
nlist = {} #입력받은 수와 그 수의 개수를 저장할 dictionary

for i in range(num):
    n = int(input())
    if n not in nlist:
        nlist[n] = 1
    else:
        nlist[n] += 1

keylist = list(nlist.keys()) #key만을 저장할 리스트
valuelist = list(nlist.values()) #value형만 저장할 리스트
maxvalue = max(valuelist) #최빈값의 개수
maxindex = valuelist.index(maxvalue) #최빈값의 index
final = [] # 최빈값의 index들을 넣을 리스트
final.append(maxindex) 
valuelist[maxindex] = 0 #valuelist[maxindex]값을 0으로 설정하여 더 있을 maxvalue를 찾을 때 다시 찾아지지 않도록 한다

while maxvalue in valuelist:
    maxindex = valuelist.index(maxvalue)
    final.append(maxindex)
    valuelist[maxindex] = 0


mode = [] #실제 최빈값의 값을 담을 리스트
for i in final:
    mode.append(keylist[i])

mode.sort()
modenum = 0
if len(mode) == 1:
    modenum = mode[0]
else:
    modenum = mode[1]

keylist.sort()
print(math.ceil(sum(keylist)/num))
print(keylist[int(num/2)])
print(modenum)
print(keylist[-1]-keylist[0])
