import sys; read = sys.stdin.readline
In, Out = map(int, input().split())

dic = dict({})
for i in range(1, In+1):
  name = read()
  dic[i]= name
  dic[name] = i

for i in range(Out):
  ins = read()
  try:
    num = int(ins)
    print(dic[num], end="")
  except:
    print(dic[ins])

# lst = []
# for i in range(In):
#   lst.append(read())

# for i in range(Out):
#   ins = read()
#   try:
#     num = int(ins)
#     print(lst[num-1])
#   except:
#     print(lst.index(ins)+1)