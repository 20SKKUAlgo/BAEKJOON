N = int(input())
lst = list(map(int, input().split()))
cost = [0] + lst

dp = [0] * (N+1)
dp[1] = cost[1]

for i in range(2, N+1):
  for j in range(0, i+1):
    dp[i] = max(dp[i], cost[i-j]+dp[j])

print(dp[N])