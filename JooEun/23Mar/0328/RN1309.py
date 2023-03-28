# https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1309-%EB%8F%99%EB%AC%BC%EC%9B%90-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# 규칙찾기

N = int(input())

dp = [[0, 0, 0] for i in range(N+1)]
dp[1] = [1, 1, 1]
for i in range(2, N+1):
  dp[i] = [(dp[i-1][0] + dp[i-1][1]+ dp[i-1][2])%9901, 
           (dp[i-1][0]+dp[i-1][2])%9901, 
           (dp[i-1][0]+dp[i-1][1])%9901
           ]

print(sum(dp[N])%9901)