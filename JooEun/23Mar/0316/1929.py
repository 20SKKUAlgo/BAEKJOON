# 에라토스테네스의 체 활용
# https://wikidocs.net/21638
n, m = map(int, input().split())

a = [False, False] + [True] * (m-1)
primes = []
for i in range(2, m+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, m+1, i):
      a[j] = False

print("\n".join(map(str, filter(lambda x: m >= x >= n, primes))))

# brute force 방식으로 :: 시간 초과!
# l = [2,3,5]
# q = 7
# while l[-1] < m:
#   tmp = q
#   for i in range(2, q//2):
#     if q%i == 0:
#       q += 1
#       break
#   if tmp == q:
#     l.append(q)
#     q += 1

# for i in l:
#   if n <= i <= m:
#     print(i)
#   if i > m:
#     break