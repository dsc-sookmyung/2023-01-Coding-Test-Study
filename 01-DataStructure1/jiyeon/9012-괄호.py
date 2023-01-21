import sys
from collections import deque
input = sys.stdin.readline

num = int(input().rstrip())
dq= deque()

def isVPS(testcase):
  dq.clear()
  for i in testcase:
    if(i == ')'):
      if(dq):
        dq.pop()
      else:
        return False
    else:
      dq.append(i)
  if(dq):
    return False
  else:
    return True

for i in range(num):
  testcase = list(input().rstrip())
  if(isVPS(testcase)):
    print("YES")
  else:
    print("NO")