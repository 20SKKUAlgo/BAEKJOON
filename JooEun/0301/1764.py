N, M = map(int, input().split())

nh = set()
ns = set()
for i in range(N):
  nh.add(input())
for i in range(M):
  ns.add(input())

nhs = sorted(list(nh & ns))
print(len(nhs))
print("\n".join(map(str, nhs)))