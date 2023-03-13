N = int(input())
lst = list(map(int, input().split()))

r = 1
from itertools import combinations

news = []
for i in range(2,len(lst)+1):
  for j in combinations(lst, i):
    news.append(sum(j))

# 중복제거를 위해 작성 / 안쓰면 시간 초과
news = set(news) 

while True:
  if r in lst:
    r+=1
    continue
  if r in news:
    r+=1
    continue
  break

print(r)
