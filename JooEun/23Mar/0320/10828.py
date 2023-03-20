import sys; read = sys.stdin.readline
from collections import deque
N = int(input())

dq = deque([])
for i in range(N):
  tmp = list(read().rstrip().split())
  if len(tmp) == 2:
    cm = tmp[0]; num = int(tmp[1])  
    if cm == "push":
      dq.append(num)
  else:
    cm = tmp[0]
    if cm == "top":
      print(dq[-1] if len(dq) else -1)
    elif cm == "size":
      print(len(dq))
    elif cm == "empty":
      print(1 if len(dq)==0 else 0)
    elif cm == "pop":
      print(dq[-1] if len(dq) else -1)
      if len(dq):
        dq.pop()
    