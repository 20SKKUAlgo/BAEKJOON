import sys

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

read = sys.stdin.readline
lst = []
while True:
  try:
    lst.append(int(read()))
  except:
    break

def dfs(node, child):
  parent = node.data
  if parent > child:
    node.left = Node(child)
  else:
    node.right = Node(child)