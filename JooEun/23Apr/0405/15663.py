import sys; read = sys.stdin.readline
n, m = map(int, read().rstrip().split())
lst = list(set(map(int, read().rstrip().split())))
lst.sort()

s = []
def dfs():
  if len(s) == m:
    print(" ".join(map(str, s)))
    return
  