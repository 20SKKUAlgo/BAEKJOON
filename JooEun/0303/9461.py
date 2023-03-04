N = int(input())

dp = [0,1,1,1,2,2,3,4]

k = 7
for i in range(N):
  M = int(input())
  if M > k:
    for j in range(k+1, M+1):
      dp.append(dp[j-1]+dp[j-5])
    k = M
  print(dp[M])