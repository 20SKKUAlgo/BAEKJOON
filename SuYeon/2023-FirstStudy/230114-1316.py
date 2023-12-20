import sys
input = sys.stdin.readline

num = int(input())
res = 0
for i in range(num):
    #print(i)
    arr = {}
    string = input().split()[0] #string에다가 문자열 입력받기
    
    #각 알파벳 문자의 개수를 저장한 딕셔너리형 만들기
    for x in string:
        if x not in arr:
            arr[x] = 1
        else:
            arr[x] += 1
    #print(arr)
    #print(string)
    y = 0
    while y < len(string):
        #print(f'현재 y: {y}')
        num = arr.get(string[y])
        #print(num)
        cnt = 0 #while문이 몇번 돌려졌는지 세는 변수
        group = 0 #group일때 0, group이 아닐 때 1
        while cnt < num:
            #print(cnt)
            #print('while문 진입')
            #print(string[y+cnt])
            #print(string[y])
            if string[y+cnt] != string[y]:
                #print('group이 아님')
                group = 1
                break
            else:
                cnt += 1
        if group == 0 and cnt == num: #하나의 알파벳이 연속으로 잘 있음을 확인했을 
            y += num
            #print(f'현재 y2: {y}')
        else:
            #print('다음 input으로')
            break
    if group == 0:
        res += 1
print(res)
