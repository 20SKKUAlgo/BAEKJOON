import heapq
CASES = int(input())

for i in range(CASES):
  N = int(input())
  lst = []
  for i in range(N):
    strs, datum = map(str, input().split())
    datum = int(datum)
    if strs == "I":
      heapq.heappush(lst, datum)
    if strs == "D":
      if len(lst) != 0:
        if datum == -1:
          heapq.heappop(lst)
        elif datum == 1:
          lst = lst[:-1]

  if len(lst) >= 2:
    print(str(lst[-1])+" "+str(lst[0]))
  elif len(lst) == 1:
    print(lst[0])
  else:
    print("EMPTY")