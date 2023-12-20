import sys
input = sys.stdin.readline

scanf = input()
scanf_list = scanf.split(' ')
num = int(scanf_list[0])
money = int(scanf_list[1])

coinList = []
for i in range(num):
    a = int(input())
    if money % a == money:
        continue
    else:
        coinList.append(a)
    
count = 0
coinList.reverse()
for i in coinList:
    if i > money:
        continue
    else:
        count += int(money/i)
        money = money%i
print(count)
