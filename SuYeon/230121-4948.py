############################################# <에라토스테네스의 체 공식>을 사용하여도 시간초과가 뜬다. while문 안에 for문이 2번 중첩되어있음. 더 줄여야 함
import sys
input = sys.stdin.readline

n = int(input())

while n!= 0:
    count = 0
    for i in range(n+1,2*n+1):
        if i == 1:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            count += 1
    print(count)
    n = int(input())
   
#############################################
