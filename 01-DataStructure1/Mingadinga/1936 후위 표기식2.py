import sys
from collections import deque

read = sys.stdin.readline
stack = deque()

n = int(read())
expression = read().rstrip()
number = [int(read().rstrip()) for _ in range(n)]

for token in expression:
  if token >= 'A' and token <= 'Z':
    stack.append(number[ord(token)-ord('A')])
  else:
    second = stack.pop()
    first = stack.pop()
    if token == '+':
      stack.append(first + second)
    elif token == '-':
      stack.append(first - second)
    elif token == '*':
      stack.append(first * second)
    elif token == '/':
      stack.append(first / second)

print("{:.2f}".format(stack.pop()))