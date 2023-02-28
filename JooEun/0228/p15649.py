# https://zidarn87.tistory.com/329 참고

N, M = map(int, input().split())
visited = [False] * (N+1)
s = []
def dfs():
  if len(s) == M:
    print(" ".join(map(str, s)))
    return
  for i in range(1, N+1):
    if not visited[i]:
      visited[i] = True
      s.append(i) 
      dfs()
      visited[i] = False
      s.pop()
dfs()
