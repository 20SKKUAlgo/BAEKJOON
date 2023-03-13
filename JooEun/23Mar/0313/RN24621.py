# 재 이해할 필요가 있음
# https://www.youtube.com/watch?v=hBB6MciGZFc

N = int(input()) # 개수
real = list(map(int, input().split())) # 바꿔야 되는 값들
goal = list(map(int, input().split())) # 목표로 하는 값들

moved = [False] * (N+1) # 해당 인덱스 = 값 : 움직였는지 확인
ins_A = [0] * (N+1) # 해당 인덱스의 본 위치를 저장

# 위치 저장
for i in range(N):
  ins_A[real[i]] = i

r_index = 0 # 본래의 인덱스
moves = 0 # 움직인 정도
for i in range(N):
  # 이미 옮겼다면 인덱스 올려주기
  while moved[r_index]: 
    r_index += 1

  # 이미 제자리에 있는 경우
  if goal[i] == real[r_index]:
    r_index += 1

  # 이동이 필요한 경우
  else:
    # 옮겼다는 것을 체크 / 해당 값에 대한 인덱스 정보를 이용
    moved[ins_A[goal[i]]] = True
    moves += 1 # 이동 추가

print(moves)