N = int(input())
original = sorted(list(map(int, input().split())))
M = int(input())
comp = list(map(int, input().split()))

for i in comp:
  if i in original: print(1)
  else: print(0)