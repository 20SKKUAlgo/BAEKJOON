N = int(input())
original = sorted(list(map(int, input().split())))
M = int(input())
comp = list(map(int, input().split()))

for element in comp:
  start = 0
  end = N-1
  exist = False
  while (start <= end):
    mid = (start+end)//2
    if original[mid] == element:
      exist = True
      break
    if original[mid] > element:
      end = mid - 1
    else:
      start = mid + 1
  if exist:
    print(1)
  else:
    print(0)
  exist = False