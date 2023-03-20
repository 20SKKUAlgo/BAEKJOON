N = int(input())
lst = list(map(int, input().split()))

# 에라토스테네스의 체 활용
isT = [False, False] + [True] * 1000
for i in range(2, 1001):
  if isT[i]:
    for j in range(2*i, 1001, i):
      isT[j] = False

result = 0
for i in lst:
  if isT[i]:
    result += 1
print(result)
