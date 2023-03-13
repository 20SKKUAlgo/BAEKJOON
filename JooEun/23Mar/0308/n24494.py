# 정답은 적긴했으나, 풀이를 참고함
correct = [0] * 26
given = [0] * 26

cwords = []
gwords = []

green = 0
yellow = 0

for i in range(3):
  co = input()
  cwords.append(co)
  for j in co:
    correct[int(ord(j))-65] += 1

for i in range(3):
  gi = input()
  gwords.append(gi)
  for j in gi:
    given[int(ord(j))-65] += 1

for i in range(3):
  for j in range(3):
    if cwords[i][j] == gwords[i][j]:
      green += 1
      correct[int(ord(cwords[i][j]))-65] -= 1
      given[int(ord(gwords[i][j]))-65] -= 1

for i in range(26):
  yellow += min(correct[i], given[i])

print(green)
print(yellow)