# 참고 https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/

import sys;read=sys.stdin.readline
import heapq

for T in range(int(read())):
  visited=[False]*1000001
  minH,maxH=[],[]
  for i in range(int(read())):
    s=read().split()
    if s[0]=='I':
      heapq.heappush(minH,(int(s[1]),i))
      heapq.heappush(maxH,(-int(s[1]),i))
      visited[i]=True
    elif s[1]=='1':
      while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
      if maxH:
        visited[maxH[0][1]]=False
        heapq.heappop(maxH)
    else:
      while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
      if minH:
        visited[minH[0][1]]=False
        heapq.heappop(minH)
  while minH and not visited[minH[0][1]]:heapq.heappop(minH)
  while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
  print(f'{-maxH[0][0]} {minH[0][0]}'if maxH and minH else'EMPTY')