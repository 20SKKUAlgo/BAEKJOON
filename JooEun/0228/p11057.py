N = int(input())

dp = [[0]*10 for _ in range((N+1))]
dp[1] = [1]*10

for i in range(2, N+1):
  for j in range(10):
      if j == 0:
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[N])%10007)

# 밑에 코드도 동일한 결과 보임
# https://jainn.tistory.com/91
# n = int(input())
# num = [1]*10

# for i in range(n-1):
#     for j in range(1, 10):
#         num[j] += num[j-1]

# print(sum(num)%10007)