import sys

read = sys.stdin.readline

N = int(read())

dp = []
for i in range(N):
  dp.append(list(map(int, read().split())))

if N >=2:
  dp[1][0] += dp[0][0]
  dp[1][1] += dp[0][0]

if N >=3:
  for i in range(2, N):
    for j in range(len(dp[i])):
      if j ==0:
        dp[i][j] += dp[i-1][j]
      elif j == len(dp[i])-1:
        dp[i][j] += dp[i-1][j-1]
      else:
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
        
print(max(dp[N-1]))