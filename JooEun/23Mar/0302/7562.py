from collections import deque
import sys
read = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
def bfs(graph, v):
  q = deque([v])
  while q:
    now = q.popleft()
    x, y = now[0], now[1]
    for i in range(len(dx)):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
        continue
      if graph[nx][ny] == 1:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))

CASE = int(input())

for i in range(CASE):
  N = int(read())
  x, y = map(int, read().split())
  fx, fy = map(int, read().split())

  graph = [[0 for i in range(N)] for i in range(N)]

  if x == fx and y == fy:
    print(0)
  else:
    bfs(graph, (x, y))
    print(graph[fx][fy])
