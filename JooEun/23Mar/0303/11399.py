N = int(input())
lst = sorted(list(map(int, input().split())))

for i in range(1, N):
  lst[i] = (lst[i-1] + lst[i])
print(sum(lst))