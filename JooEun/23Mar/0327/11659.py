import sys; read = sys.stdin.readline
n, m = map(int, read().rstrip().split())
lst = list(map(int, read().rstrip().split()))
pre = [0]

tmp = 0
for i in lst:
  tmp += i
  pre.append(tmp)

for i in range(m):
  a, b = map(int, read().rstrip().split())
  print(pre[b] - pre[a-1])