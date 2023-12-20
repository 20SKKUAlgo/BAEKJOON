# 2023.01.17 https://www.acmicpc.net/problem/10814
# 정렬 여러개: 참고 https://dev-note-97.tistory.com/125

num = int(input())

lst = []
for i in range(num):
  oneline = input()
  tmp = oneline.split()
  lst.append((int(tmp[0]), tmp[1]))

lst = sorted(lst, key=lambda x: x[0])
# lst = sorted(lst, key=lambda x: x[1], reverse=True) # 이건 이름 내림차순

for i in range(num):
  print(str(lst[i][0])+" "+lst[i][1])
