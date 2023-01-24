import sys

def vps(str):
  stack = list(str.strip())
  right = 0
  
  while stack: 
    char = stack.pop()
    if char == '(':
      if right > 0:
        right = right - 1
      else:
        return False
    else:
      right = right + 1

  if right == 0:
    return True
  else:
    return False
    
count= int(sys.stdin.readline())
for _ in range(count):
  str = sys.stdin.readline()
  if vps(str):
    print("YES")
  else:
    print("NO")