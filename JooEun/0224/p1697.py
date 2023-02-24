# BFS!!
import sys
n, k = map(int, sys.stdin.readline().split())

from collections import deque
MAX = 100001
di = [0] * (MAX) # distance and check whether it is visitied
def bfs():
  q = deque([n])
  # di[n] = 1
  while q:
    now = q.popleft()
    if(now == k):
      print(di[now])
      break
    for next in (now-1, now+1, 2*now):
      if(0 <= next < MAX and di[next]==0):
        q.append(next)
        di[next] = di[now] + 1

bfs()