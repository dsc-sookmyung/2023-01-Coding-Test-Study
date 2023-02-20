# 스택
import sys
from collections import deque

def check_vps(ps):
  stack = deque()
  for bracket in ps:
    if bracket == '(':
      stack.appendleft(bracket)
    elif bracket == ')':
      if stack:
        stack.pop()
      else:
        print("NO")
        return
  if len(stack) == 0:
    print("YES")
  else:
    print("NO")

read = sys.stdin.readline

t = int(read())
pss = [read().rstrip() for _ in range(t)]

for ps in pss:
  check_vps(ps)