N = int(input())
lst = list(map(int, input().split()))

r = 1
from itertools import combinations

news = []
for i in range(2,len(lst)+1):
  combi = list(combinations(lst, i))
  for j in combi:
    news.append(sum(j))

while True:
  if r in lst:
    r+=1
    continue
  if r in news:
    r+=1
    continue
  break

print(r)
