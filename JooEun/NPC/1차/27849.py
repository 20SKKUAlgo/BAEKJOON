import sys; read = sys.stdin.readline
N, T = map(int, input().split())
haybale = []
for i in range(N):
  day, hay = map(int, read().rstrip().split())
  haybale.append((day, hay))

fill = haybale[0][0] + haybale[0][1]
longday = 0
result = haybale[0][1]
if result > T:
  result = T
else:
  for i in range(1, len(haybale)):
    day, hay = haybale[i][0], haybale[i][1]
    if fill <= day:
      if result + hay > T:
        result += (T-day+1)
      else:
        result += hay
    fill = day + hay

print(result)

# # brute force
# import sys; read = sys.stdin.readline
# N, T = map(int, input().split())
# haybale = [0]*(T+1)
# for i in range(N):
#   day, hay = map(int, read().rstrip().split())
#   haybale[day] = hay

# duration = T
# days = 0
# d = 1
# while T > 0:
#   while haybale[d] == 0 and T > 0: d += 1; T -= 1
#   while haybale[d] > 0 and T > 0:
#     haybale[d] -= 1
#     T -= 1
#     days += 1

# if haybale[duration] > 0:
#   days+=1

# print(days)