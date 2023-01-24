steel = list(input())
stack = []
result = 0
for i in range(len(steel)):
    if steel[i] == '(':
        stack.append('(')
    else:
        if steel[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)
