import sys; read = sys.stdin.readline
import collections
n = int(read())
lst = []
for i in range(n):
  lst.append(int(read()))

lst.sort()
dic = collections.Counter(lst).most_common()
print(round(sum(lst)/n))
print(lst[n//2])
print(dic[1][0] if len(dic)>1 and dic[0][1]==dic[1][1] else dic[0][0])
print(lst[-1]-lst[0])
