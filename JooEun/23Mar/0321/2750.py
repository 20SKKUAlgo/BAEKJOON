import sys; read = sys.stdin.readline
lst = [int(read()) for i in range(int(read()))]
lst = sorted(lst)
print("\n".join(map(str, lst)))