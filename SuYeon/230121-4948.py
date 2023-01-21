############################################# <에라토스테네스의 체 공식>을 사용하여도 시간초과가 뜬다. while문 안에 for문이 2번 중첩되어있음. 더 줄여야 함
import sys
input = sys.stdin.readline

n = int(input())

while n!= 0:
    count = 0
    for i in range(n+1,2*n+1):
        if i == 1:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            count += 1
    print(count)
    n = int(input())
   
#############################################while문 돌때마다 소수 판별하는 것을 고침 -> 미리 판별해 놓고 소수인지 아닌지 리스트에서 확인만 하기
# dec리스트에 True, False로 소수인지 아닌지 확인할 수 있도록 만들어 놓음
# n+1~2*n까지 이므로 dec 리스트의 크기도 최대 값인 123456의 *2로 설정함
# 추가로 생각해 봄 : i in list를 쓰는것보다는 dec[i] == True인지로 판별하는 것이 시간이 더 적게 걸리는 것 같음. 후자는 index로 바로 찾아가면 되기 때문
import sys
input = sys.stdin.readline

end = 123456

dec = [True for _ in range(2*end+1)]
dec[0], dec[1] = False, False

for i in range(2,2*end+1):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            dec[i] = False
            break

n = int(input())

while n!= 0:
    count = 0
    for i in range(n+1,2*n+1):
        if dec[i]:
            count += 1
    print(count)
    n = int(input())
