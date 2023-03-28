import sys; read = sys.stdin.readline
n = int(input())

lst = []
for i in range(n):
  a, b = map(int, read().rstrip().split())
  lst.append((a, b))

lst.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
  print(str(lst[i][0])+" "+str(lst[i][1]))