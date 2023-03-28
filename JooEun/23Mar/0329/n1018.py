import sys; read = sys.stdin.readline
r, c = map(int, input().split())
lst = []
for i in range(r):
  lst.append(list(read().rstrip()))

for i in range(r):
  if i%2 == 0:
    a = lst[i].count("WB")
  else:
    a = lst[i].count("BW")