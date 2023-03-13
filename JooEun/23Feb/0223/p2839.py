# 설탕 배달
# 동적 프로그래밍처럼 풂
N = int(input())

cost = [-1] * (N+1)
# 3, 5는 고정 숫자이므로 다음과 같이 처리
cost[3] = 1
if(N>=5):
  cost[5] = 1

# 6 이상일 경우 cost 리스트를 채워가며 계산
if(N>=6):
  for i in range(6, N+1):
    tmp = []
    if(cost[i-3]!=-1):
      tmp.append(cost[i-3])
    if(cost[i-5]!=-1):
      tmp.append(cost[i-5])
    
    if(len(tmp)!=0):
      cost[i] = min(tmp) + 1

print(cost[-1])