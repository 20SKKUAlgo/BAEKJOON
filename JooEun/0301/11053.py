N = int(input())

lst = list(map(int, input().split()))

dp = [1] * (N)
if N > 1:
  for i in range(1, N):
    for j in range(i):
      if lst[i] > lst[j] and dp[i] <= dp[j]:
        dp[i] = dp[j] + 1

print(max(dp))