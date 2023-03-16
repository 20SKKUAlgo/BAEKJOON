# !!! 중요
import sys; read = sys.stdin.readline
n, k = map(int, input().split())

lst = [int(read()) for _ in range(n)]

start = 1
end = max(lst)
mid = 1
while start <= end:
  mid = (start + end) // 2
  count = 0
  for ele in lst:
    count += (ele//mid)

  if count < k:
    end = mid - 1
  else:
    start = mid + 1

print(end)
