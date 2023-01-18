import sys
input = sys.stdin.readline

a, b = list(map(int,input().split()))
while a!=' ':
    print(a+b)
    a, b = list(map(int,input().split()))
###########################################위 방법으로 하였을 경우 런타임 에러 발생

import sys
input = sys.stdin.readline

while 1:
    try:
        a, b = list(map(int,input().split()))
        print(a+b)
    except:
        break

###########################################위 방법과 같이 try와 except으로 오류(a,b에 값이 제대로 저장이 안될 경우)가 났을 경우에 break문으로 while을 빠져나갈 수 있게 함
