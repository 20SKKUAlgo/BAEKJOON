import sys
read = sys.stdin.readline

lst = []
for i in range(9):
  m = int(read().rstrip())
  lst.append(m)
lst.sort()

maxNum = sum(lst)
isFind = False
for i in range(8, 0, -1):
  for j in range(7, -1, -1):
    a = sum(lst)
    a = a - lst[i] - lst[j]
    if (a == 100):
      lst.remove(lst[i])
      lst.remove(lst[j])
      isFind = True
      break
  if(isFind):
    break
print('\n'.join(map(str, lst)), end="")
