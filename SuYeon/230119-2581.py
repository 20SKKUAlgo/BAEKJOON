import sys
input = sys.stdin.readline

minN = int(input())
maxN = int(input())

decimal = []


for x in range(minN,maxN+1):
    dec = 1
    for y in range(2,x):
        if x/y == int(x/y):
            dec = 0
            break
        else:
            continue
    if dec == 1:
        decimal.append(x)

#1은 소수가 아니므로 1을 제외해주어야 함
#시간초과 날까봐 for문 돌때 계속 if조건문 처리되지 않도록 바깥에다가 빼둠
if 1 in decimal:
    index = decimal.index(1)
    del decimal[index]
    
if len(decimal) == 0:
    print(-1)
else:
    print(sum(decimal))
    print(min(decimal))
