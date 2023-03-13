import sys
N = int(sys.stdin.readline())

dp = [0, 1, 2, 3]

if N>=4:
  for i in range(4,N+1):
    dp[(i)%4] = (dp[(i-1)%4] + dp[(i-2)%4])%15746

print(dp[(N)%4])