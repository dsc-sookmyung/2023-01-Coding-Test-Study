import sys

str = sys.stdin.readline().rstrip()

ans = 0
stack = []
for i in range(len(str)):
  if str[i]=='(':
    stack.append(str[i])
  else:
    stack.pop()
    if str[i-1]=='(':
      ans += len(stack)
    else:
      ans += 1
      
print(ans)