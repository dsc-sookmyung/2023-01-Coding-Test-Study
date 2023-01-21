'''
    [해설]
    '(' 는 스택에 넣어준다
    ')'는 2가지로 경우를 나눈다.
        1. 이전 문자도 동일하면 쇠막대기를 나타내는 괄호
        2. 이전 문자가 '('인 경우 레이저를 나타내는 괄호 -> 스택에 쌓인 '('의 갯수만큼 더해준다(쇠막대기 갯수)
'''
import sys

str = list(sys.stdin.readline().rstrip())
result = 0
stack = []

for i in range(len(str)):
    if str[i] == '(':
        stack.append(str[i])
    else:  # )
        if str[i-1] == '(':  # 레이저
            stack.pop()
            result += len(stack)
        else:  # 쇠막대기
            stack.pop()
            result += 1
print(result)