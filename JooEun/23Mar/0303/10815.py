N = int(input())
original = sorted(list(map(int, input().split())))
M = int(input())
given = list(map(int, input().split()))

# original에 set을 사용한다면 괜찮겠지
# for i in given:
#   print(1 if i in original else 0, end=" ")

# binary
for ele in given:
  st = 0
  end = (N-1)
  isOne = False
  while st <= end:
    mid = (st + end) // 2
    if original[mid] == ele:
      print(1, end=" ")
      isOne = True
      break
    if ele > original[mid]:
      st = mid + 1
    else:
      end = mid -1
  
  if not isOne:
    print(0, end=" ")