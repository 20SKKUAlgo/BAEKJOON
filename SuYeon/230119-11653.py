import sys
input = sys.stdin.readline

num = int(input())
res = [] #num의 소인수를 저장할 배열
#소인수분해의 요소는 소수이다
decimal = [] #num까지의 소수가 들어간다

for i in range(2,num):
    dec = 1
    for j in range(2,i):
        if i/j == int(i/j):
            dec = 0
            break
        else:
            continue
    if dec == 1:
        decimal.append(i)
        
next = num #계속해서 쪼개어지는 수
#decimal의 작은 수부터 나머지가 0일때까지 next를 쪼갠다
#나머지가 0이 아니면 다음 decimal로 쪼갠
for i in decimal:
    while next%i == 0:
        res.append(i)
        next = next//i

if num == 1:
    exit()
else:
    if len(res) == 0:
        print(num)
    else:
        for i in res:
            print(i)
#######################################################시간초과 나옴. 푸는 방식은 맞음. 중간에 소수 구해서 decimal 배열 구하는거 안 해줘도 된다. 오히려 구하는게 더 시간 오래 걸림
import sys
input = sys.stdin.readline

num = int(input())

if num == 1:
    exit()

for i in range(2,num+1):
    if num % i == 0:
        while num % i == 0:
            print(i) #굳이 res라는 배열 또 만들어서 저장하고 다시 출력하지 말고 확정될때마다 즉시즉시 print 하기
            num = num / i
