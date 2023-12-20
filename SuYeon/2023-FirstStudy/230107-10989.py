#시도 1 : 시간 초과 뜸 > input() 대신 sys.stdin.readline 씀. 그래도 시간 초과 뜸 
import sys
input = sys.stdin.readline
num = int(input())
list = []
for i in range(num):
    a = int(input())
    if len(list)==0:
        list.append(a)
    else:
        if a < list[0]:
            list.insert(0,a)
        elif a >= list[len(list)-1]:
            list.append(a)
        else:
            for j in range(1,len(list)):
                if a <= list[j]:
                    list.insert(j,a)
                    break
           
for i in range(len(list)):
    print(list[i])


#시도 2 : sort의 존재 떠올림 > 그래도 시간 초과 뜸
import sys
input = sys.stdin.readline
num = int(input())
list = []
for i in range(num):
    a = int(input())
    list.append(a)
list.sort()
           
for i in range(len(list)):
    print(list[i])


#계수 정렬 이용 > 맞음 
import sys
inpurt = sys.stdin.readline
num = int(input())
arr = [0]*10000

for i in range(num):
    a = int(input())
    arr[a-1] += 1
for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)
