# https://www.youtube.com/watch?v=GTvGRCEwUKU
n, k = map(int, input().split())
lst = list(map(int, input().split()))

# cost = consecutive d days + K
cost = 0
grd = [-2**31] + lst
for i in range(1, n+1):
  cost += min(k + 1, grd[i]-grd[i-1])

print(cost)