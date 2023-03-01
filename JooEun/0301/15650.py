# 참고: https://zidarn87.tistory.com/331

N, M = map(int, input().split())

visited = [False] * (N+1)
s = []
def dfs(next):
  if(len(s) == M):
    print(" ".join(map(str, s)))
    return
  for i in range(next, N+1):
    s.append(i)
    dfs(i+1)
    s.pop()

dfs(1)