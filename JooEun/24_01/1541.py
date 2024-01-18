import sys
import re

def remove_leading_zero(number_string):
  pattern = re.compile(r'\b0*([1-9][0-9]*)\b')
  result = re.sub(pattern, r'\1', number_string)
  return result

string = sys.stdin.readline()
lst = string.split('-')

rlst = 0
for i in range(len(lst)):
  processed = int(eval(remove_leading_zero(lst[i])))
  if i == 0:
    rlst = processed
  else:
    rlst -= processed
print(rlst)
