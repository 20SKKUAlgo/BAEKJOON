N = int(input())
lst = []
for i in range(N):
  lst.append(input())

result = 0
for item in lst:
  newW = item
  isT = True
  for i in range(len(newW)-1):
    if item[i] != item[i+1]:
      newW = item[i+1:]
      if item[i] in newW:
        isT = False
        break
  
  if isT:
    result += 1

print(result)
    