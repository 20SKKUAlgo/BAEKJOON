import sys
input = sys.stdin.readline

a, b, v = map(int,input().split())

day = a-b
before = v-a
count = int(before/day)

#모든 경우에서 목표지점에 도달했을때는 막 올라갔을 때이다. 따라서 before를 봐야 함
#예를 들어 100 99 1000000000에서는 전날에 999999900만큼 올라가 있다.
#따라서 하루만 더 100을 가면 목표지점에 도달하기 때문에
#전날까지 가는데 걸린 일수인 count를 계산해야 한다.
#그리고 마지막 날을 더해줘서 count+1이 된다.
#if count != 0:
if before%day == 0:
    print(count+1)
    
#여기서 만약 5 2 10 처럼 before%day가 0이 아닐때는
#전날에서 바로 다음 날 도착하는 것이 아니다
#전날인 5m를 넘기 위해 하루를 더 지내야 하고 +1
#마지막 날을 더해주어야 한다 +1 
else:
    print(count+2)

#즉 전날에 언제 도착하냐가 중요한 문제
#전날에 딱 도착할 수 있는지, 아니면 하루를 더 보내고 전날을 넘어서 도착할 수 있는지
