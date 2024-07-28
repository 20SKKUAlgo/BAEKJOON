import sys
input = sys.stdin.readline

arr = []
for i in range(1,10001):
    ten = 10000
    res = i
    while int(i/ten) == 0:
        ten = ten/10
    num = i
    if i < 10:
        res = 2*i
    else:
        while num > 10:
            res += int(num/ten)
            num = num%ten
            res += num
    if res == i:
        continue
    else:
        arr.append(res)


for i in range(1,10001):
    if i in arr:
        continue
    else:
        print(i)
        

########################################위가 내가 한 방식 -> 시간이 너무 오래 걸림. 따라서 맞는지 확인을 못함
########################################위, 아래의 방식은 비슷한 알고리즘을 사용하였음 
#set은 두가지 특징이 있음 : 1. 중복을 허용하지 않는다 2. 순서가 없다 -> 인덱싱으로 값을 얻을 수 없다.
#set 자료형에 저장된 값을 인덱싱으로 접근하려면 튜플로 변환한 후 접근해야 한다
natural_num = set(range(1,10001))
generated_num = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)
                  
