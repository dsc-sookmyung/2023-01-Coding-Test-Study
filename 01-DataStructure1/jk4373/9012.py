import sys

n = int(input())

for i in range(n):
    a = input()
    stack = []
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else :
                print("NO")
                break
    else:
        if not stack:
            print('YES')
        elif stack:
            print("NO")