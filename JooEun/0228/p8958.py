N = int(input())

strlst = []
for i in range(N):
  strlst.append(input())

for strs in strlst:
  score = 0
  contig = 0
  for i in strs:
    if i == "O":
      score += (1 + contig)
      contig+=1
    else:
      contig = 0
  print(score)
