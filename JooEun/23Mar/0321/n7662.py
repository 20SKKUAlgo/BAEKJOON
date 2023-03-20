import heapq
import sys
read = sys.stdin.readline
CASES = int(input())

for i in range(CASES):
  N = int(read())
  lst = []
  for i in range(N):
    strs, datum = map(str, read().strip().split())
    datum = int(datum)
    if strs == "I":
      lst.append(datum)
    if strs == "D":
      if len(lst) != 0:
        heapq.heapify(lst)
        if datum == -1:
          heapq.heappop(lst)
        elif datum == 1:
          lst = lst[:len(lst)-1]

  if len(lst) >= 2:
    print(str(lst[-1])+" "+str(lst[0]))
  elif len(lst) == 1:
    print(lst[0])
  else:
    print("EMPTY")