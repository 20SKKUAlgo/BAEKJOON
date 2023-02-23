# dfs는 stack을 이용
# bfs는 queue를 이용
# 미완성
from collections import deque

info = list(map(int, input().split()))


N = info[0]
M = info[1]
startV = info[2]
Dvisited = [False] * (N+1)
Bvisited = [False] * (N+1)
# Bvisited = Dvisited

graphed = []
for i in range(M):
  nodeConnect = list(map(int, input().split()))
  graphed.append(nodeConnect)

graphed.sort()
graph = [[0]*(N+1) for _ in range(N+1)]
for item in graphed:
  x = item[0]; y = item[1]
  graph[x][y] = 1
  graph[y][x] = 1

############
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=" ")
  for i in graph[v]:
    if (not visited[i] and graph[v][i]):
      dfs(graph, i, visited)

dfs(graph, startV, Dvisited)

# print()
# def bfs(graph, v, visited):
#   queue = deque([v])
#   visited[v] = True
#   while queue:
#     vertex = queue.popleft()
#     print(vertex, end=" ")
#     for i in graph[vertex]:
#       if not visited[i]:
#         queue.append(i)
#         visited[i] = True

# bfs(graph, startV, Bvisited)



