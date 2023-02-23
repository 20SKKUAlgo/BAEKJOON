# 최대한 3으로 많이 나누는 것이 포인트 => 그리디적 접근
# 그리디로 최적해가 나오지 않을 경우 -> 동적계획법
# Bottom-up 방식
N = int(input())

count = 0
cost = [0 for i in range(N+1)]
# cost = [0] * (N+1)

if(N>1):
  cost[2] = 1
if(N>2):
  cost[3] = 1
for i in range(4, N+1):
  # 3가지 내용을 모두 비교하기 위해
  tmp_lst = [cost[i-1]] 

  # K로 나누어떨어지는 것 뿐만 아니라 K를 곱했을 때 본래 정수형으로 돌아온다면 K의 배수이므로 확인
  if((i//2 * 2) == i):
    tmp_lst.append(cost[i//2])
  if((i//3 * 3) == i):
    tmp_lst.append(cost[i//3])
  
  cost[i] = min(tmp_lst) + 1

print(cost[-1])
