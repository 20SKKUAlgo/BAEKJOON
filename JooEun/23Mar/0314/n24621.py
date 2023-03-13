N = int(input())
real = list(map(int, input().split()))
goal = list(map(int, input().split()))

moved = [False] * (N+1)
r_index = 0
moves = 0
for i in range(N):
  # 이미 옮겼다면 패스
  if moved[r_index]: 
    r_index += 1
    continue

  # 이미 제자리에 있는 경우
  if goal[i] == real[r_index]:
    r_index+=1

  # 이동이 필요한 경우
  else:
    moved[r_index] = True
    moves +=1 # 이동 추가

print(moves)