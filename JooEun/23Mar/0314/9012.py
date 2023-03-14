N = int(input())

for i in range(N):
  strs = input()
  lst = []
  isT = True
  for j in strs:
    if j == "(":
      lst.append(0)
    else:
      if len(lst) != 0:
        lst.pop()
      else:
        isT = False
        break
  if len(lst) != 0:
    isT = False
  print("YES" if isT else "NO")