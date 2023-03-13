lst = list(input())

d = 0; c = 0; r = 1
for i in range(len(lst)-1):
  if lst[i] == lst[i+1]:
    if lst[i] == 'd':
      d += 1
    if lst[i] == 'c':
      c += 1
  else:
    if lst[i] == 'd':
      r *= 10
    if lst[i] == 'c':
      r *= 26

if lst[-1] == 'd':
  r *= 10
if lst[-1] == 'c':
  r *= 26

for i in range(1, d+1):
  r *= (10-i)
for i in range(1, c+1):
  r *= (26-i)

print(r)


# def dfs(lst, i, c):
#   if i == len(lst)-1:
#     return c +1
  
#   if lst[i] != lst[i+1]:
#     return c

#   if lst[i] == lst[i+1]:
#     print("same!")
#     dfs(lst, i+1, c+1)

#   return c


