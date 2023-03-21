# https://ggasoon2.tistory.com/11
N, r, c = map(int, input().split())

# # N이 30일 경우, 수가 엄청나지니까 배열을 채우는 방식이 아닌 다른 방안을 찾아야한다. => 이걸 생각해내야 함

result = 0

while N > 0:
    N -= 1
    tmp = (2 ** N) *(2**N)
    # 1 사분면
    if r<2**N and c<2**N:
      result +=  tmp*0
    # 2 사분면
    elif r<2**N and c>=2**N:
      result +=  tmp*1
      c -= (2 ** N)
    # 3 사분면
    elif r>=2**N and c<2**N:
      result +=  tmp*2
      r -= (2 ** N)
    # 4 사분면
    else:
      result +=  tmp*3
      r -= (2 ** N)
      c -= (2 ** N)

print(result)