N = int(input())

lst = []
for i in range(N):
  strs, num = map(str, input().split())  
  lst.append([strs, int(num)])

lst.sort(key=lambda x: x[1])
# print(lst)

# 숫자를 기준으로 정렬하여, 왼편에 L이 있거나 오른편에 G가 있다면 증가시키기
# 같은 숫자일 경우엔 라이어가 아니므로 넘어가기
minLiar = N
for i in range(N):
  liarN = 0
  for j in range(i):
    if lst[j][0] == 'L' and lst[j][1] < lst[i][1]:
      liarN += 1

  for j in range(i+1, N):
    if lst[j][0] == 'G' and lst[j][1] > lst[i][1]:
      liarN +=1

  minLiar = min(liarN, minLiar)

print(minLiar)