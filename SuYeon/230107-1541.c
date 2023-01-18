import sys
input = sys.stdin.readline

read = input()
operator = []
operand = [] #연산자를 순서대로 담는 배열 

for i in read:
    if i.isdecimal() or i=='\n': #연산자가 아닐 경우
        continue
    else: #연산자일 경우 
        operand.append(i)


#operator만 뽑기
read = read.split('\n')[0]
plusrm = read.split('+')
for i in plusrm:
    if '-' in i: #'-'가 있다면 문자열에서 '-'를 제거해서 minusrm 배열에 넣기
        minusrm = i.split('-')
        for j in minusrm:
            operator.append(int(j))
    else:
        operator.append(int(i))


#'-'다음에 '+'가 나올때 가장 큰 -값을 얻을 수 있음
archive = [] #'-'값을 취해야할 index들의 집합
cir = 0
minus = 0 #앞에 '-'가 있는지 확인 해주는 변수
for i in operand:
    cir += 1
    if i=='-' and minus == 0:
        archive.append(cir)
        minus = 1
    elif i=='+' and minus == 1:
        archive.append(cir)
    elif i=='-' and minus == 1:
        archive.append(cir)


result = 0
for i in range(len(operator)):
    if i in archive:
        result -= operator[i]
    else:
        result += operator[i]

print(result) 
