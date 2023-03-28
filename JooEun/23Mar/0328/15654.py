n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False] * (n)

s = []
def dfs():
  if len(s) == m:
    print(" ".join(map(str, s)))
    return
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      s.append(lst[i])
      dfs()
      visited[i] = False
      s.pop()
dfs()