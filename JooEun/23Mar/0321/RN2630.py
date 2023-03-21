# https://zidarn87.tistory.com/378
import sys; read = sys.stdin.readline
N = int(input())
graph = []
for i in range(N):
  graph.append(list(map(int, read().rstrip().split())))

blue, white = 0, 0

def divide(r, c, N):
  global blue, white
  color = graph[r][c]
  for k in range(r, r+N):
    for j in range(c, c+N):
      if color != graph[k][j]:
        Nhalf = N//2
        dr = [0, Nhalf, 0, Nhalf]
        dc = [0, 0, Nhalf, Nhalf]
        for i in range(4):
          divide(r + dr[i], c + dc[i], Nhalf)
        return
  if color == 0:
    white +=1
  else:
    blue += 1

divide(0,0,N)
print(white)
print(blue)