import sys
import heapq
read = sys.stdin.readline

N = int(read())
q = []

for i in range(N):
  num = int(read())
  if num == 0:
    if len(q) == 0:
      print(0)
    else:
      print(heapq.heappop(q))
  else:
    heapq.heappush(q, num)