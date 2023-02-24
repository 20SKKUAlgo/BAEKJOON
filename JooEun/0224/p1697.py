# BFS!!
n, k = map(int, input().split())

diff = abs(n-k)

MAX = 100001
dist = [0]*(MAX)

from collections import deque

def bfs():
  q = deque([n])
  while q:
    now = q.popleft()
    if now == k:
      print(dist[now])
      break
    for next in (now-1, now+1, now*2):
      if 0 <= next <= MAX and dist[next] == 0:
        dist[next] = dist[now] + 1
        q.append(next)

bfs()

