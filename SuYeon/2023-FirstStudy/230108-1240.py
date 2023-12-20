import sys
input = sys.stdin.readline

read = input()
N = int(read.split(' ')[0])
M = int(read.split(' ')[1])
graph = [[0 for j in range(4)] for i in range(N+1)]

def find(start,end,trace,dis2):
    res = 0
    #if문과 elif문은 한번에 찾았을 때
    if graph[start][0] == end:
        trace.append(start)
        dis2.append(int(graph[start][1]))
        for i in dis2:
            res += i
        #print(trace)
        print(res)
    elif graph[start][3] == end:
        trace.append(start)
        dis2.append(graph[start][2])
        for i in dis2:
            res += i
        #print(trace)
        print(res)
    #else문은 한번에 찾지 못했을 때
    else:
        trace.append(start)
        left = graph[start][0]
        right = graph[start][3]
        if left != 0 and left not in trace:
            #trace.append(left)
            dis2.append(graph[start][1])
            find(left,end,trace,dis2)
        if right != 0 and right not in trace:
            #trace.append(right)
            dis2.append(graph[start][2])
            find(right,end,trace,dis2)

        
for i in range(N-1):
    list = input().split(' ')
    a = int(list[0])
    b = int(list[1])
    dis = int(list[2])
    if graph[a][0] == 0: #왼쪽이 비어있을 때 
        graph[a][0] = b #왼쪽, 오른쪽에는 이어져 있을 다른 노드 번호를
        graph[a][1] = dis #가운데 2곳에는 거리를
    else:
        graph[a][3] = b
        graph[a][2] = dis
        
    if graph[b][0] == 0: #왼쪽이 비어있을 때 
        graph[b][0] = a #왼쪽, 오른쪽에는 이어져 있을 다른 노드 번호를
        graph[b][1] = dis #가운데 2곳에는 거리를
    else:
        graph[b][3] = a
        graph[b][2] = dis

#print(graph)
for i in range(M):
    list2 = input().split(' ')
    start = int(list2[0])
    end = int(list2[1])
    trace=[]
    dis2=[]
    find(start,end,trace,dis2)
