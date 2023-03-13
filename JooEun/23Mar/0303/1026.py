N = int(input())

down = sorted(list(map(int, input().split())), reverse=True)
up = sorted(list(map(int, input().split())))

result = 0
for i in range(N):
  result += down[i]*up[i]

print(result)