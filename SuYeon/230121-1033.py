##################################################################################시간초과 뜸... 답은 맞음...
import sys
import math
input = sys.stdin.readline

num = int(input())

listnum = [[0 for _ in range(num-1)] for _ in range(num)] #비율을 겹쳐서 담을 배열

totalnum = 1

abcq = [] #abcq를 담는 배열

overlap = [] #index가 겹치는 배열

count1 = 1
count2 = 1
for i in range(num-1):
    a, b, p, q = map(int,input().split())
    if listnum[a][0] == 0:
        listnum[a][0] = p
    else:
        if count1 == 1:
            totalnum *= listnum[a][0]
            totalnum *= p
        else:
            totalnum *= p
        if a not in overlap:
            overlap.append(a)
        listnum[a][count1] = p
        count1 += 1
    if listnum[b][0] == 0:
        listnum[b][0] = q
    else:
        if count2 == 1:
            totalnum *= listnum[b][0]
            totalnum *= q
        else:
            totalnum *= q
        if b not in overlap:
            overlap.append(b)
        listnum[b][count2] = q
        count2 += 1
    abcq.append([a,b,p,q])

reslist = [totalnum]*num  #결과를 담을 배열
gcd = 1 # reslist의 최대공약수 

donotchange = [] #바꾸면 안되는 index를 저장함

notoverlap = [ k for k in range(num) if k not in overlap]

def donotchangeoverlap(a,b,p,q):
    if a in overlap:
        reslist[b] = reslist[a]//p*q
    elif b in overlap:
        reslist[a] = reslist[b]//q*p
    else: #abcq에 들어온 배열이 하나일 
        reslist[a] = p
        reslist[b] = q
    #print(reslist)

for k in range(len(abcq)):
    a = abcq[k][0]
    b = abcq[k][1]
    p = abcq[k][2]
    q = abcq[k][3]
    # 두개의 index가 다 겹칠때는 다시 정비해줘야 함 
    if a in overlap and b in overlap:
            reslist[b] = reslist[a]//p*q
            for t in range(k):
                a = abcq[t][0]
                b = abcq[t][1]
                p = abcq[t][2]
                q = abcq[t][3]
                #print(a,b,p,q)
                donotchangeoverlap(a,b,p,q)
    else: #겹쳐있는 것이 바뀌면 안된다
        donotchangeoverlap(a,b,p,q)

#제일 작은 수로 만들기 
for i in range(2,min(reslist)+1):
    while True:
        div = 1
        for x in reslist:
            if x%i != 0:
                div = 0
                break
        if div == 1:
            for y in range(len(reslist)):
                reslist[y] = reslist[y]//i
            gcd *= i
        else:
            break

for r in reslist:
    print(r, end=' ')

##################################################################################


