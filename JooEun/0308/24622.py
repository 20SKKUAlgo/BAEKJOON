N = int(input())

dice = []

for i in range(4):
  dice.append(set(input()))

made = set()
for m in range(4):
  for j in dice[m%4]:
    for q in dice[(m+1)%4]:
      for k in dice[(m+2)%4]:
        for z in dice[(m+3)%4]:
          made.add(j + q + k + z)
          made.add(j + q + z + k)
          made.add(j + k + z + q)
          made.add(j + k + q + z)
          made.add(j + z + q + k)
          made.add(j + z + k + q)
          made.add(j + z + k)
          made.add(j + k + q)
          made.add(j + k + z)
          made.add(j + q + k)
          made.add(j + z + q)
          made.add(j + q + z)
          made.add(j + z)
          made.add(j + q)
          made.add(j + k)
made.update(dice[0])
made.update(dice[1])
made.update(dice[2])
made.update(dice[3])


for i in range(N):
  word = input()
  
  if word in made:
    print("YES")
  else:
    print("NO")