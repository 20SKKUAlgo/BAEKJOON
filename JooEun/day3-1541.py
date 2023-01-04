string = input()

tmp = ""
num = "" # 숫자만을 입력받음
flag = 0 # 1: 괄호 시작 / 0: 괄호 끝
for i in range(len(string)):
  if(string[i] != "+" and string[i] != "-"):
    # 숫자인 경우
    num += string[i]
  else:
  # 문자인 경우
    num2 = int(num) # 00009 와 같은 경우를 위해 처리
    num ="" # 숫자를 정수로 변환해주었으니 비우기
    if(flag == 1 and string[i] == "-"):
      # -가 끝날때
      tmp += str(num2) + ")-("
      flag = 1
    elif(string[i] == "-"):
      # -가 시작할 때
      tmp += str(num2) + "-("
      flag = 1
    elif((flag == 1) and (i==(len(string)-1))):
      tmp += string[i]+")"  
      flag = 0
    else:
      tmp += str(num2) + "+"

# 마지막 남은 숫자 처리
num2 = int(num)
tmp += str(num2)
if(flag == 1):
  tmp += ")"

result = eval(tmp)
print(result)

