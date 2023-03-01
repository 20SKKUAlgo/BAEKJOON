comN = int(input())
netN = int(input())

graph = [[0 for i in range(comN+1)] for j in range(comN+1)]
for i in range(netN):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1

from collections import deque
def bfs():
  q = deque([1])
  ss = -1
  while q:
    v = q.popleft()
    for i in range(v, len(graph[v])):
      if graph[v][i] == 1:
        graph[v][i] = 0
        graph[i][v] = 0
        q.append(i)
        ss+=1
  print(ss)

bfs()
