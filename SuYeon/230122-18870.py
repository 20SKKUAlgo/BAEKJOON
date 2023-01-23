#########################################시간초과 뜸. 답은 맞음.
import sys
import math
input = sys.stdin.readline

num = int(input())
nlist = list(map(int,input().split()))

setlist = set(nlist)

for i in nlist:
    count = 0
    for j in setlist:
        if i > j:
            count += 1
    print(count, end=' ')
    
#########################################
import sys
import math
input = sys.stdin.readline

num = int(input())

nlist = list(map(int,input().split()))
setnlist = set(nlist) #set은 순서에 상관이 없음 -> sort 하기 전에 list로 만들어줘야 함
setsortlist = sorted(list(setnlist))


"""
밑에 있는 수가 몇개인지는 상관이 없었음
archive = {}
for i in nlist:
    if i in archive:
        continue
    archive[i] = 1

sortedArchive = sorted(archive.items()) #딕셔너리의 x[0]순으로 정렬되서 tuple형태(items()역할)로 반환됨 
#sorted(archive.items(), key=lambda x:x[1])은 x[1]순으로 정렬되서 tuple형태(items()역할)로 반환됨

"""

#이렇게 하면 시간초과가 뜬다. setsortlist.index(i)의 형태는 시간복잡도 O(N)을 가지고 있기 때문에 매번 최대 1,000,000번의 수행이 이루어지게 돼서 시간초과가 뜸
"""
for  i in nlist:
    print(setsortlist.index(i), end=' ') #현재의 인덱스가 밑에 있는 숫자의 개수임
"""

count = {setsortlist[i] : i     for i in range(len(setsortlist))}
for i in nlist:
    print(count[i], end=' ')
