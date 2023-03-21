N = int(input())
lst = list(map(int, input().split()))
lstSorted = list(set(lst))
lstSorted.sort()

## dictionary 이용 방법 1
# dic = dict()
# index = 0
# for i in lstSorted:
#   dic[i] = index
#   index+=1 

## dictionary 이용 방법 2
dic = {lstSorted[i]: i for i in range(len(lstSorted))}

for i in lst:
  print(dic[i], end=" ")