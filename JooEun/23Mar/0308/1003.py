import sys
read = sys.stdin.readline
N = int(read())

dp = [[1, 0], [0, 1], [1, 1]]

limit = 2
for i in range(N):
  num = int(read())
  if num > limit:
    for i in range(limit+1, num+1):
      dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])
    limit = num

  print(" ".join(map(str, dp[num])))