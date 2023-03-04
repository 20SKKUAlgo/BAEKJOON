ladderN, snakeN = map(int, input().split())

graph = [0 for i in range(101)]

for i in range(ladderN + snakeN):
  start, dest = map(int, input().split())
  graph[start] = dest

roll = 0

from collections import deque
def bfs():
  global roll
  q = deque([1])
  while q:
    v = q.popleft()
    tmp = v
    isT = False
    for i in range(1, 7):
      if 0< v+i <= 100:
        # print(-2)
        if(graph[v+i] > tmp):
          print("this is tmp!! "+ str(tmp))
          isT = True
          tmp = graph[v+i]
        # print(-3)
    if not isT:
      q.append(tmp+6)
      continue
    q.append(tmp)
    roll += 1
    print("v "+str(v)+ " tmp "+str(tmp)+" graph "+str(graph[i]))

bfs()
print(roll)