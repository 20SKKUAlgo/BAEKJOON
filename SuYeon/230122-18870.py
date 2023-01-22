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
