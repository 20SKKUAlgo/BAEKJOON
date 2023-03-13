import sys

read = sys.stdin.readline

costs = []
N = int(read())
if N<2 or N>1000:
  print(0)
else:
  for i in range(N):
    costs.append(list(map(int, read().split())))
  # 0 r / 1 g / 2 b

  # indR, indG, indB = 0, 1 ,2
  # startR, startG, startB = costs[0][0], costs[0][1], costs[0][2]
  for i in range(1, N):
    # 빨간색 / 초록색 / 파란색 비용을 i의 입장에서 i-1것을 더한다. 이렇게 되면 각 색을 사용했을 경우의 최소 비용 걸로 계속 업데이트 되겠지
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
    costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
    costs[i][2] = min(costs[i-1][1], costs[i-1][0]) + costs[i][2]

    # ~~ 처음 생각했던 아이디어 ~~
    # 시작만 다르게 하고, 각 경우마다 최소 비용을 선택 -> 그리디 접근 하지만 이러면 모든 경우에 대한 최소 비용이 선택이 안됨
    
  # result = [startR, startB, startG]

  print(min(costs[N-1]))