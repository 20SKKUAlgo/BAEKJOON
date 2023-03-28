x, y, w, h = map(int, input().split())
lst = [x, y, abs(w-x), abs(h-y)]
print(min(lst))