N, M = map(int, input().split())

graph = [[0 for i in range(N)]] * N

info = []
for i in range(M):
  info.append(list(map(int, input().split())))
for item in info:
  x = item[0]; y = item[1]
  graph[x][y] = 1; graph[y][x] = 1

visited = [False] * N

def dfs(v, depth):
  visited[v] = True