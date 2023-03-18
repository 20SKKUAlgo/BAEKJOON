# https://ggasoon2.tistory.com/11
N, r, c = map(int, input().split())

# # N이 30일 경우, 수가 엄청나지니까 배열을 채우는 방식이 아닌 다른 방안을 찾아야한다.
# start = 0
# end = 2
# num = 0
# dx = [0, 2, 0, 2]
# dy = [0, 0, 2, 2]
# lst = [[-1 for i in range(2**N)] for i in range(2**N)]
# for i in range(2**N//2):
#   for j in range(end):
#     for k in range(end):
#       if (lst[j][k] == -1):
#         lst[j][k] = num
#         num += 1
#   end = 2 * i

# print(lst)
# print(lst[r][c])

clst = [4**i-1 for i in range(N)]
rlst = [2*4**i for i in range(N)]
