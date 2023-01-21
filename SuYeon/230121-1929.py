#i까지 다 검사하면 시간초과가 뜸
#-> 2부터 i의 제곱근까지만 검사하면 나머지는 검사하나 마나여서 제곱근까지만 검사하면 된다.

import sys
input = sys.stdin.readline

m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)
