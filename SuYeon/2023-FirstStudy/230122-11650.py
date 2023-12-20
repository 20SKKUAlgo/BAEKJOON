###############################################시간초과 뜸. 답은 나옴
import sys
import math
input = sys.stdin.readline

num = int(input())
infor = [] #x와 y를 같이 저장할 배열 
#infor에 넣을 때 아예 정렬해서 넣기

for i in range(num):
    x,y = list(map(int,input().split()))
    if i == 0: #처음 넣을때는 그냥 넣기 
        infor.append([x,y])
        continue #조건에 해당된다면 다음 i로 넘어가기
    if infor[-1][0] < x: #정렬해서 넣기 때문에 infor[-1]의 x가 가장 큼. 이와 비교했을 때 크다면 infor의 마지막번째로 넣어준다
        infor.append([x,y])
        continue #조건에 해당된다면 다음 i로 넘어가기
    #아래 for문을 실행하려면 x가 infor[0]의 x보다 커야 함
    for j in range(i):
        if x < infor[j][0]: #infor의 배열을 앞에서부터 순회하다가 x가 뒤의 x보다 작다면 멈추고 그 자리에 삽입
            infor.insert(j,[x,y])
            break #삽입 후 for문을 빠져나가고 다음 input을 받는다
        elif x == infor[j][0]: #infor의 배열을 앞에서부터 순회하다가 x와 같은 값을 만나게 된다면 
            #y값 비교 시작
            k = j
            while x == infor[k][0]: #x가 같을때까지만 비교
                if y < infor[k][1]: #x가 같으면서 y가 비교하는것보다 작다면 그 자리에 삽입
                    infor.insert(k,[x,y])
                    break #알맞은 자리에 삽입 후 while문을 빠져나간다
                k += 1 #알맞은 자리를 찾지 못했으면 x가 다를때까지 다음 값 비교
            else: #while문이 break문 때문에 빠져나간게 아니라 k += 1 때문에 while의 조건문을 만족하지 못해서 빠져나왔을 때
                #x값은 같은 곳에서 y값이 제일 크기 때문에 맨 끝에 삽입 
                infor.insert(k,[x,y])
            break #if문이 아닌 elif문이 실행되었다면 for j in range(i)를 한번만 실행하고 for문을 빠져나가야 

for l in infor:
    print(l[0], l[1])
    
###############################################맞음
#key=lamda x : [x[0],x[1]]
#를 이용해서 sort를 함
"""
ex) 
data_list = [[1,2],[3,4],[4,5],[6,7],[8,9]]
data_list.sort(key=lambda x : x[1])
여기서 x는 data_list의 값 하나 [1,2]로 생각하면 됨
여기서 두번째 값을 기준으로 정렬하고 싶다면 
x[1]을 labmda x: 뒤에 붙여주면 된다.
"""
import sys
import math
input = sys.stdin.readline

num = int(input())
nlist = []

for i in range(num):
    nlist.append(list(map(int,input().split())))

nlist.sort(key = lambda x : [x[0],x[1]])

for i in nlist:
    print(i[0], i[1])
