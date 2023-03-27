import sys
read = sys.stdin.readline

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

# 입력값 받기
lst = []
while True:
  try:
    lst.append(int(read()))
  except:
    break

def preTraversal(node, child):
  parent = node.data
  if parent > child:
    node.left = Node(child)
  else:
    node.right = Node(child)

root = Node(lst[0])
nn = root
np = None
for i in range(1, len(lst)):

  
