n = int(input())
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])

room.sort(key = lambda x: x[0]) # 회의 시작 시간 기준 정렬
room.sort(key = lambda x: x[1]) # 회의 마감 시간 기준 정렬

cnt = 1
end = room[0][1] # 제일 이른 회의 선택
for i in range(1, n):
    if room[i][0] >= end: # 회의시작시간이 이전 회의 마감시간보다 크다면
        cnt += 1 # 회의수+1
        end = room[i][1] # 마감시간 재설정

print(cnt)
