import sys

read = sys.stdin.readline

N = int(read())

dp = [0,1,2]
dp[0] = 0; dp[1] = 1; dp[2] = 2
if(N>=3):
  for i in range(3, N+1):
    dp[(i)%3] = (dp[(i-1)%3] + dp[(i-2)%3])%10007

print(dp[(N)%3])