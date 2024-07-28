import sys
input = sys.stdin.readline

alpha = 'abcdefghijklmnopqrstuvwxyz'
res = [-1]*(len(alpha)+1)
string = input().strip()

for i in range(len(string)):
    for j in range(len(string)):
        if string[i] == alpha[j]:
            if res[j] == -1:
                res[j] = i
            else:
                continue

result = ''
for i in res:
    result += str(i)+' '
print(result)

#####################################런타임 에러가 뜸... 이유를 모르겠음
#첫번째 방법 : for문 이용

S = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in S:
        print(S.index(i), end = ' ')
    else:
        print(-1, end=' ')


#####################################
#2번째 방법 : find 이용

S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')
