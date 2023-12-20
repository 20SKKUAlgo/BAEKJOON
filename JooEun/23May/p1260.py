
import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty() == False:
            return self.stack.pop(-1)
        else:
            return None

    def peek(self):
        if self.isEmpty() == False:
            return self.stack[-1]
        else:
            return None

    def isEmpty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.stack)

    def print(self):
        print(self.stack)

class Queue:
    def __init__(self):
        self.queue = []

    def enQueue(self, item):
        self.queue.append(item)

    def deQueue(self):
        if self.isEmpty() == False:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True

    def peek(self):
        if self.isEmpty() == False:
            return self.queue[0]

    def delete(self, item):
        if item in self.queue:
            self.queue.remove(item)
        else:
            print("해당 아이템이 존재하지 않습니다.")

#graph-->DFS(stack)/BFS(queue)
class Graph:
    def __init__(self, graph, start, visit1, visit2):
        self.graph = graph
        self.start = start 
        self.visit1= visit1 #dfs
        self.visit2= visit2 #bfs
        self.s = Stack()
        self.q = Queue()
                   # 1 2 3 4
    def dfs(self): # T F F T  # stack 2 3 2
        self.s.push(self.start) # 첫번째 노드 1 4 
        while self.s.isEmpty() == False:
            curNode = self.s.pop() # 4
            print(curNode, end=" ") 
            if self.visit1[curNode] == False: 
                self.visit1[curNode] = True 
                for i in range(1, N+1): # 2
                    if self.graph[curNode][i] == True and self.visit1[i] == False:
                        self.s.push(i)
                        # break
    
    def bfs(self):
        self.visit2[self.start] = True
        self.q.enQueue(self.start)
        # for item in self.graph[self.start]:
        #     self.q.enQueue(item)

        while self.q.isEmpty() == False:
            item = self.q.deQueue()
            print(item, end=" ")
            # if not self.visit2[item]:  # 현재 아이템이 가본 곳이 아니면 ...
            for i in range(1, N+1):
                if self.graph[item][i] == True and self.visit2[i] == False:
                    self.q.enQueue(i)
                    self.visit2[i] = True
                
        # return visit

        # visit2[self]=True 
      
        # queue = Queue()
        # for item in self.graph[self.start]:
        #     queue.enQueue(item)

        # while queue.isEmpty() == False:
        #     item = queue.deQueue()
        #     if not item in visit2:  # 현재 아이템이 가본 곳이 아니면 ...
        #         for _item in self.graph[item]:
        #             queue.enQueue(_item)
        #         visit2.append(item)
        # return visit2


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().rstrip()
    sys.setrecursionlimit(int(1e9))
    N,M,V=input().split()
    N=int(N)
    M=int(M)
    V=int(V)
    visit1 = [False for j in range(N+1)]   #노드의 갯수만큼만 방문  #0번쨰 index는 방문하지 않는다고 생각 
    visit2= [False for j in range(N+1)] 
    graph = [[False for j in range(N+1)] for i in range(N+1)]

    for i in range(M):
        s,e = map(int, input().split())
        graph[s][e] = True 
        graph[e][s] = True

    g = Graph(graph, V, visit1, visit2)
    g.dfs()
    print()
    g.bfs()

