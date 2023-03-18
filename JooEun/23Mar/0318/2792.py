# 규칙
# 1 7 19 37 61
# +6 12 18 24
n = int(input())
lst = [0, 1] * 1000000
k = 2
while lst[k-1] < n:
  lst[k] = lst[k-1] + 6*(k-1)
  k += 1

print(k-1)