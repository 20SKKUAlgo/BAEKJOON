# 중복된 값이 많다면 radix sort를 사용!
# https://coarmok.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACpython-%EB%B0%B1%EC%A4%80-10989%EB%B2%88-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%B4%88%EA%B3%BC
import sys; read = sys.stdin.readline

lst = [0] * 10001
for i in range(int(read())):
  ti = int(read())
  lst[ti] += 1

for i in range(1, len(lst)):
  if lst[i] != 0:
    for j in range(lst[i]):
      print(i)
