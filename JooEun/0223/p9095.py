import sys
N = int(sys.stdin.readline())

# 초기화
nums = []
for _ in range(N):
  nums.append(int(sys.stdin.readline()))


unique = [1, 2, 3]
for i in range(N):
  cost = [ 0 ] * nums[i]
  if nums[i] >= 1:
    cost[0] = 1
  if nums[i] >= 2:
    cost[1] = 2
  if nums[i] >= 3:
    cost[2] = 4
  if nums[i] >= 4:
    for j in range(3, nums[i]):
      cost[j] = cost[j-3] + cost[j-2] + cost[j-1]
  
  print(cost[-1])
