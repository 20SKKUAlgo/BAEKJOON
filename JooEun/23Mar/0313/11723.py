import sys
read = sys.stdin.readline
N = int(read())

lst = set()
for i in range(N):
  command = read().strip().split()
  if len(command) != 1:
    com, num = command[0], int(command[1])
  
    if com == "add":
      lst.add(num)
    elif com == "check":
      print(1 if num in lst else 0)
    elif com == "remove":
      # if num in lst:
      lst.discard(num)
    elif com == "toggle":
      if num in lst:
        lst.remove(num)
      else:
        lst.add(num)
  else:
    if command[0] == "all":
      lst = set([i for i in range(1, 21)])
    elif command[0] == "empty":
      lst = set()