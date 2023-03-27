import sys; read = sys.stdin.readline
N, T = map(int, input().split())

days = [[0] for i in range(N+1)]
hays = [[0] for i in range(N)]
for i in range(N):
  day, hay = map(int, read().rstrip().split())
  days[i] = day
  hays[i] = hay
days[N] = T+1

result = 0
d = 0
for i in range(N):
  d += hays[i]
  v = min(d, days[i+1]-days[i])
  result += v
  d -= v

print(result)

# haybale = [0]
# for i in range(N):
#   day, hay = map(int, read().rstrip().split())
#   haybale.append((day, hay))

# result = 0
# prevday = haybale[0][0]
# prevhay = haybale[0][1]
# for item in haybale:
#   if item[1] - (T-item[0]+1) > 0:
#     result += (T-item[0]+1)
#     break
  
#   # 부족하게 될 경우
#   if prevday + prevhay -1 < item[0]:
#     prevday = item[0]
#     prevhay = item[1]
#     result += item[1]
#   # 넘칠 경우
#   else:
    
# print(result)


# fill = haybale[0][0] + haybale[0][1]
# longday = 0
# result = haybale[0][1]
# if result > T:
#   result = T
# else:
#   for i in range(1, len(haybale)):
#     day, hay = haybale[i][0], haybale[i][1]
#     if fill <= day:
#       if result + hay > T:
#         result += (T-day+1)
#       else:
#         result += hay
#     fill = day + hay
# print(result)


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