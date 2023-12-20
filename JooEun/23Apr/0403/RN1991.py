# dictionary를 이용하는 것이 핵심!!
import sys; read = sys.stdin.readline
n = int(input())

dic = dict()
for i in range(n):
  d, l, r = read().rstrip().split()
  dic[d] = [l, r]

def preorder(root):
  if root != ".":
    print(root, end="")
    preorder(dic[root][0])
    preorder(dic[root][1])

def inorder(root):
  if root != ".":
    inorder(dic[root][0])
    print(root, end="")
    inorder(dic[root][1])

def postorder(root):
  if root != ".":
    postorder(dic[root][0])
    postorder(dic[root][1])
    print(root, end="")

preorder("A")
print()
inorder('A')
print()
postorder('A')