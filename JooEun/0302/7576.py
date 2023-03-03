import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())

graph = []
for i in range(M):
  graph.append(list(map(int, read().split())))

# bfs
def bfs(graph):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  # q에 토마토 위치 집어넣기
  q = deque([])
  for i in range(M):
    for j in range(N):
      if graph[i][j] == 1:
        q.append((i,j))
  
  #####  중요 파트 #####
  while q:
    v = q.popleft()
    x, y = v[0], v[1]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue
      if graph[nx][ny] == -1 or graph[nx][ny] == 1:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
  #####  중요 파트 #####

bfs(graph)

day = 0
for row in graph:
  if 0 in row:
    day = -1
    print(-1)
    break
  row.append(day)
  day = max(row)
if day != -1:
  print(day-1)
