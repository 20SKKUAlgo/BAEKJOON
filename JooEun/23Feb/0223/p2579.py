import sys
N = int(input())

stairs = []
for i in range(N):
  stairs.append(int(input()))

cost = [ 0 for i in range(N) ] # 이렇게 해야 요소 각각 처리됨
# cost = [ [0, 0] ] * N 으로 하면 안에 요소들 값이 모두 동일하게 출력됨.. 와이??
cost[0] = stairs[0]
if(N>=2):
  cost[1] = stairs[0] + stairs[1]
if(N>=3):
  cost[2] = max(stairs[0], stairs[1]) + stairs[2]
if(N>=4):
  for i in range(3, N):
    cost[i] = max(cost[i-3] + stairs[i-1], cost[i-2]) + stairs[i]

print(cost[-1])