from collections import deque

# 초기화
comN = int(input())
netN = int(input())

graph = [[0 for i in range(comN+1)] for j in range(comN+1)]
for i in range(netN):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1

# 방문했는지 판단
visited = [False] * (comN+1) 

# bfs 방식으로 순회
def bfs():
  q = deque([1])
  graph[1][1] = 0
  ss = 0
  visited[1] = True
  while q:
    v = q.popleft()
    for i in range(1, comN+1):
      if graph[v][i] == 1 and not visited[i]:
        graph[v][i] = 0
        graph[i][v] = 0
        visited[i] = True
        q.append(i)
        ss+=1
  print(ss)

count = 0
def dfs(v):
  global count
  visited[v] = True
  for i in range(1, comN+1):
    if graph[v][i] == 1 and not visited[i]:
      graph[v][i] = 0
      count += 1
      dfs(i)

# bfs로 풀려면
# bfs()

# dfs로 풀려면
dfs(1)
print(count)
