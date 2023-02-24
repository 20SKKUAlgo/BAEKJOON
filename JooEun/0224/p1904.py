N = int(input())

dp2 = [0, 1, 2, 3]
dp = [0]*(N+1)
dp = dp2 + dp

if N>=4:
  for i in range(4,N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])