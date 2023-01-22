#########################################################################################################
#set를 사용하면 집합이 된다. {}형이 된다. 중복이 자동으로 제거된다.
#set은 appennd 대신 add를 사용해야 함
#set은 sort가 적용이 안됨 -> set로 중복제거를 한 후 list()를 사용해서 list로 변환 후 sort를 적용할 수 있음

import sys
import math
input = sys.stdin.readline

num = int(input())
strlist = []

for i in range(num):
    string = input().strip()
    strlist.append(string)

strlist = list(set(strlist)) #set로 중복제거를 한 후 list()를 사용해서 list로 변환 후 sort를 적용할 수 있음
strlist.sort(key = lambda x : [len(x),x]) # 아마도 lamda x : 뒤에 [] 또는 ()로 묶은 후 순서 조건을 차례대로 쓰면, 그 차례대로 순서가 적용되는 것 같음
#ex) lamda x : [x,len(x)]로 하면 알파벳 순으로 정렬 후 단어의 첫문자 알파벳이 같다면 두번째 조건인 길이순으로 정렬이 됨

for i in strlist:
    print(i)
