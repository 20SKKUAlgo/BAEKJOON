import math
n = int(input())
var = str(math.factorial(n))
fz = False

result = 0
for i in range(len(var)-1, -1, -1):
  if not fz and var[i]=="0":
    fz = True
    result += 1
  elif fz and var[i]=="0":
    result += 1
  elif fz and var[i]!="0":
    break

print(result)
  