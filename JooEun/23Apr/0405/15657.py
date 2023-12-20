# 중요!
import sys; read = sys.stdin.readline
n, m = map(int, read().rstrip().split())
lst = list(map(int, read().rstrip().split()))
lst.sort()

s = []
def dfs(st):
  global s
  if len(s) == m:
    print(" ".join(map(str, s)))
    return
  for i in range(st, n):
    s.append(lst[i])
    dfs(i)
    s.pop()

dfs(0)