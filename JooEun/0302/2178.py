import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())

graph = []
for i in range(N):
  graph.append(list(map(int, input())))


def bfs(graph):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque([(0,0)])
  while q:
    v = q.popleft()
    x, y = v[0], v[1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if not(nx < 0 or nx >=N or ny < 0 or ny >= M) and graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))

bfs(graph)
# print(graph)
print(graph[N-1][M-1])