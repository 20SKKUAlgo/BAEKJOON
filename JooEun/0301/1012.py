import sys
read = sys.stdin.readline
CASE = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# dfs 로 풀기 => recursion error
def dfs(graph, x, y):
  if x < 0 or x >= len(graph) or y < 0 or y>=len(graph[0]) :
    return False
  
  if graph[x][y] == 1:
    graph[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(graph, nx, ny)
    return True
  return False

# in bfs
from collections import deque
def bfs(graph, v):
  q = deque([v])
  while q:
    nv = q.popleft()
    x, y = nv[0], nv[1]
    if not(x < 0 or x >=len(graph) or y < 0 or y >=len(graph[0])): 
      if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          q.append((nx, ny))

for i in range(CASE):
  w, h, n = map(int, read().split())
  graph = [[0 for i in range(h)] for j in range(w) ]

  for j in range(n):
    x, y = map(int, read().split())
    graph[x][y] = 1

  need = 0
  for j in range(w):
    for k in range(h):
      if graph[j][k] == 1:
        bfs(graph, (j, k))
        need+=1
  
  print(need)
