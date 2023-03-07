ladderN, snakeN = map(int, input().split())

visited = [0 for i in range(108)]

for i in range(ladderN + snakeN):
  start, dest = map(int, input().split())
  visited[start] = dest

roll = 0

from collections import deque
def bfs():
  global roll
  q = deque([1])
  while q:
    v = q.popleft()
    for i in range(1, 7):
      # if 0< v+i <= 100:
      #   if(graph[v+i] > tmp):
      #     tmp = graph[v+i]
    if tmp == v:
      for i in range(6,0,-1):
        # print("g "+ str(graph[v+i]) + " v+i "+ str(v+i))
        # if(graph[v+i] <= v+i and graph[v+i] != 0):
          # print("g "+ str(graph[v+i]) + " v+i "+ str(v+i))
          continue
        else:
          tmp = v+i
          break
    q.append(tmp)
    roll += 1

bfs()
print(roll)