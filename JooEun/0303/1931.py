N = int(input())

times = []
for i in range(N):
  times.append(list(map(int, input().split())))
times.sort(key=lambda x: (x[1], x[0]))

result = 1
endT = times[0][1]
for i in range(1, N):
  if (times[i][0] >= endT):
    result+=1
    endT=times[i][1]
print(result)