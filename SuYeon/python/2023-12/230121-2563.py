import sys
input = sys.stdin.readline

num = int(input())

canvas = [[0 for _ in range(101)] for _ in range(101)]

for i in range(num):
    x, y = map(int,input().split())
    for j in range(x, x+10):
        for k in range(y,y+10):
            canvas[j][k] = 1

res = 0
for spot in canvas:
    res += spot.count(1)

print(res)

###########################################################
#위와 같은 방법으로 처음에 생각했는데
#좌표와 색종이의 넓이에서 헷갈림
#내가 원하는대로 출력할 수 있도록 설정해 주면 됨. 
#ex) 좌표가 행렬로 3,3에 찍혀있을때 넓이는 4임 -> 하지만 좌표는 9개가 1이 되서 1인 개수를 세주면 9가 됨 -> 하나씩 빼서 1로 설정하기 -> 1~3이 아닌 1~2로 (x좌표,y좌표)
