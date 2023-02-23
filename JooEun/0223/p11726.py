import sys

read = sys.stdin.readline

N = int(read())

dp = [0]*(N+1)
dp[0] = 0; dp[1] = 1; dp[2] = 2
for i in range(3, N+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[N]%10007)