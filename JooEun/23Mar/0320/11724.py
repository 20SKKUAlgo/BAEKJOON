# https://ji-gwang.tistory.com/292 참고

import sys; read = sys.stdin.readline
sys.setrecursionlimit(1001) # 이게 필수... 재귀 들어가는 것을 제한
n, m = map(int, input().split())

visited = [False] * (n+1) # 방문여부를 체크
graph = [[] for i in range(n+1)]

# 연결된 요소들을 모두 True로 체크 => 한번 돌떄마다 연결된 애들끼리 연결
def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

# 그래프 정보 저장하기
for i in range(m):
  a, b = map(int, read().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

# 둘러보면서 개수 찾기
result = 0
for i in range(1, n+1):
  if not visited[i]:
    if not graph[i]:
      result +=1
      visited[i] = True
    else:
      dfs(i)
      result += 1

print(result)