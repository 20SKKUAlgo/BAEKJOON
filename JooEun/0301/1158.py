N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]
newN = K-1

result = []
for i in range(N-1):
  result.append(lst[(newN)])
  lst = lst[:(newN)] + lst[newN+1:]
  newN = (newN + (K-1)) % len(lst)
result.append(lst[0])

print("<", end="")
print(", ".join(map(str,result)), end="")
print(">", end="")

# 위의 세 문장을 다음과 같이 바꿀 수도 있다!!
# print(str(result).replace('[', '<').replace(']', '>'))