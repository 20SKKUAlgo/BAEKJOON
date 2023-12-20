if,elif,else..문으로 하려다가 replace로 하는 방법을 인터넷으로 찾아냄
#####################################################################
import sys
input = sys.stdin.readline
    
pat = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input().strip()

for x in pat:
    string = string.replace(x,'*')

print(len(string))
