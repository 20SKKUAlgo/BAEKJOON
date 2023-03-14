# 푸는 아이디어가 중요
n = input()

dc = 0
cc = 0
for i in range(len(n)-1):
  if n[i] == n[i+1]:
    if n[i] == "d":
      dc += 1
    elif n[i] == "c":
      cc += 1

result = 1
d = n.count("d")
c = len(n) - d
dlst = [10] * (d-dc) + [9]*dc
clst = [26] * (c-cc) + [25]*cc
lst = []
lst += dlst + clst

for i in lst:
  result *= i
print(result)