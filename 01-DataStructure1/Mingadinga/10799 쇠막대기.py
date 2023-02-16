import sys
from collections import deque

read = sys.stdin.readline
brackets = read()
stack = deque()
count = 0
i = 0

while i < len(brackets) - 1:
  if brackets[i] == '(':
    # 다음꺼가 )이면 레이저니까 막대기개수 누적합
    if brackets[i + 1] == ')':
      count += len(stack)
      i += 1
    # 다음꺼가 (이면 얜 맥대기니까 스택에 추가하기
    elif brackets[i + 1] == '(':
      stack.appendleft('-')
  elif brackets[i] == ')':
    # 막대기 끝나면 하나 추가
    count += 1
    stack.pop()
  i += 1

print(count)
