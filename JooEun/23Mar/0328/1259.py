import sys; read = sys.stdin.readline
while True:
  a = int(read())
  isT = True
  if a == 0:
    break
  else:
    st = str(a)
    if str(a) == str(a)[::-1]:
      print("yes")
    else:
      print("no")
    # for i in range(len(st)//2):
    #   if st[i] != st[len(st)-i-1]:
    #     isT = False
    #     print("no")
    # if isT:
    #   print("yes")