userinput = input()
res = 0
if "-" not in userinput: # case1_ input에 -가없을때
    arr = userinput.split("+")
    res = sum(list(map(int, arr)))

else: #case2_ input에 +가있을때
    arr = userinput.split("-")

    if "+" in arr[0]: # arr[0]에 +가 있을때 ex_ arr[0] : 3+4
        ar = arr[0].split("+")  # arr[0]을 +로 찢어 더함
        for i in ar:
            res = res + int(i)
    else: # arr[0]에 +가 없을때 ex_ arr[0] : 3
        res = int(arr[0])

    for ar in arr[1:]:
        for i in ar.split("+"):
            res = res - int(i)

print(res)
