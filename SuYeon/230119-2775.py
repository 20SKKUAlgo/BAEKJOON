import sys
input = sys.stdin.readline

num = int(input())

def countPeople(k,n):
    sum = 0
    if k == 1:
        for i in range(1,n+1):
           sum += i
        return sum 
    else:
        res = 0
        for j in range(1,n+1):
            res += countPeople(k-1,j)
        return(res)

for i in range(num):
    k = int(input()) #k층
    n = int(input()) #n호
    result = countPeople(k,n)
    print(result)

###########################################위 풀이는 답은 맞음. but 시간 초과...
###########################################아래 풀이를 사용해야 함. 
import sys
input = sys.stdin.readline

num = int(input())

for i in range(num):
    floor = int(input())
    room = int(input())
    apt = [i for i in range(1,room+1)] #하나의 리스트를 계속 갱신할것임. 갱신이 되면 아래층의 
    for x in range(floor):
        for y in range(1,room):
            apt[y] += apt[y-1]
    print(apt[-1])
