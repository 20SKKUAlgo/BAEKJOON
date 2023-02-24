#=============== dfs
import sys
result = []

read = sys.stdin.readline
N = int(read())

mapp = []
for _ in range(N):
  mapp.append(list(map(int, input())))

count = 0
def dfs(x, y):
  if x <=-1 or x>=N or y<=-1 or y>=N:
    return False
  
  if mapp[x][y] == 1:
    global count
    count+=1
    # 해당 문제 방문처리
    mapp[x][y] = 0
    # 상하좌우
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

rn = 0
for i in range(N):
  for j in range(N):
    if dfs(i,j) == True:
      rn+=1
      result.append(count)
      count = 0

# 총 개수
print(rn)
# 오름차순 정렬
for i in sorted(result):
  print(i)

#=============== bfs

from collections import deque

countB = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(x1, y1):
  que = deque([(x1,y1)])
  mapp[x1][y1] = 0
  count = 1
  while que: 
    x, y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx>=N or ny < 0 or ny>=N:
        continue
      if mapp[nx][ny] == 1:
        count+=1
        mapp[nx][ny] = 0
        que.append((nx, ny))
  return count

result = []
for i in range(N):
  for j in range(N):
    if mapp[i][j] == 1:
      result.append(bfs(i,j))
      count = 0

# 총 개수
print(len(result))
# 오름차순 정렬
for i in sorted(result):
  print(i)