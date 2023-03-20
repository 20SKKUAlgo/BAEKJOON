import heapq
# heapq는 기본적으로 min heap이기 때문에 max로 하기 위해선 튜플을 활용해야한다.
import sys; read = sys.stdin.readline
N = int(input())

q = []
for i in range(N):
  n = int(read())
  if n == 0 and len(q):
    print(heapq.heappop(q)[1])
  elif n == 0 and not len(q):
    print(0)
  else:
    heapq.heappush(q, (-n, n))