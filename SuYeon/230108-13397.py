import sys
input = sys.stdin.readline

list = input().split(' ')
num = int(list[0])
sector = int(list[1])

list2 = input().split('\n')[0].split(' ')
number = [] #입력받은 숫자들 담는 배열 
for i in list2:
    number.append(int(i))

factor = []
for i in range(sector):
    factor.append(0)


for i in range(1,num+1):
    for j in range(i,num+1):
        for k in range(j,num+1):
            if i+j+k==num-sector:
              
 ###########################################막힘

