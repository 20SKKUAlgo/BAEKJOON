import sys; read = sys.stdin.readline
N = int(input())

lst = set()
for i in range(N):
  lst.add(read().rstrip()) # rstrip을 하여 개행문자 제거
lst = list(lst)

lst.sort(key=lambda x: (len(x), x))
print("\n".join(lst))