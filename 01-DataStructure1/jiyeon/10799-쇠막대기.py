import sys
input = sys.stdin.readline
from collections import deque

brackets = list(input().rstrip())
dq = deque()
count = 0

for i in range(len(brackets)):  
  if(brackets[i] == '('):
    dq.append(brackets[i])
  else:
    dq.pop()
    if(brackets[i-1] == '('):
      count += len(dq)
    else:
      count += 1

print(count)