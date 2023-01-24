#######백준 런타임 에러 나는 경우#######
#1. 배열 인덱스 범위를 벗어났을 경우
#2. 0으로 나눌 때
#3. 사용하는 라이브러리에서 예외를 발생시켰을 때
#4. 재귀 호출이 너무 깊어질 때

#4번 때문에 런타임 에러가 난 것 같음... 다른 tool로 실행했을 때 답은 맞게 출력됨

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

card = list(map(int,input().split()))

card.sort() #카드리스트 정렬

#앞에서부터 2개 더한 후 목표 값과의 차이가 나는 수가 있는지 확인
#없으면 M의 값을 하나씩 빼면서 M과 합이 맞다면 출력함

def find(M):   
    for i in range(N-1):
        stop = 0
        for j in range(i+1,N):
            two = card[i]+card[j]
            dis = M - two
            if (dis!= card[i]) and (dis!=card[j]) and (dis in card):
                print(M)
                stop = 1
                break
            else:
                continue
        if stop == 1:
            break
        if i == N-2:
            find(M-1)

find(M)


########################################################
#재귀호출 없애고 while문으로 함
#런타임 에러 안 뜸. 재귀때문에 런타임 에러 뜬거 맞았음
#근데 시간초과
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

card = list(map(int,input().split()))

card.sort() #카드리스트 정렬

#앞에서부터 2개 더한 후 목표 값과의 차이가 나는 수가 있는지 확인
#없으면 M의 값을 하나씩 빼면서 M과 합이 맞다면 출력

while M >= 0:   
    for i in range(N-1):
        stop = 0
        for j in range(i+1,N):
            two = card[i]+card[j]
            dis = M - two
            if (dis!= card[i]) and (dis!=card[j]) and (dis in card):
                print(M)
                stop = 1
                break
            else:
                continue
        if stop == 1:
            M = -1
            break
        if i == N-2:
            M -= 1
            break
        
########################################################
import sys
from itertools import combinations
#파이썬에서 제공하는 순열 조합 library itertools 모듈의 combinations 함수 사용

input = sys.stdin.readline

N, M = map(int,input().split())

card = list(map(int,input().split()))

maxnum = 0

for i in combinations(card,3):
    sumnum = sum(i)
    if maxnum < sumnum <= M:
        maxnum = sumnum

print(maxnum)
