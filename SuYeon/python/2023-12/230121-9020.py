import sys
input = sys.stdin.readline

num = int(input())

dec = [True for _ in range(10001)]
dec[0] = False
dec[1] = False

for i in range(2,10001): #i가 소수이면 dec[i]는 True로 설정, 소수가 아니면 False로 설정함
    for j in range(2,int(i*0.5)+1):
        if i % j == 0:
            dec[i] = False

for i in range(num):
    n = int(input())
    nlist = [] #n보다 작은 소수의 리스트
    closehalf = [] #int(n/2)보다 작은 소수의 리스트. 두 소수의 차이가 가장 작을 확률이 제일 높음 
    #n보다 작은 소수들 찾기
    for j in range(n):
        if dec[j]: #소수이면
            if j <= int(n/2): #소수면서 int(n/2)보다 작거나 같을 때 closehalf에 추가
                closehalf.append(j)
            nlist.append(j) #소수이면 nlist에 추가
    index = len(closehalf)-1
    while True:
        bestclose = closehalf[index] #가장 가까운 소수는 closehalf에 들어온 제일 마지막 소수
        if dec[n - bestclose]: # n-bestclose도 소수이면 결과를 찾은 것임 출력하기
            print(bestclose, n-bestclose)
            break
        else: # n-bestclose가 소수가 아니면 closehalf에 들어온 두번째 마지막 소수를 bestclose로 설정하기 위해 index를 1 빼주기
            index -= 1
