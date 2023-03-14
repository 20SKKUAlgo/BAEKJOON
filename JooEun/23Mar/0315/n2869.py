a, b, v = map(int, input().split())

now = v%(a-b)
day = v//(a-b)
if a == v:
  day = 1
elif a-b == 1:
  day = v -b
# elif now == 0:
#   day = day-1
else:
  while now > 0:
    now -= a
    if now <= 0:
      break
    now += b
    day+=1

print(day)