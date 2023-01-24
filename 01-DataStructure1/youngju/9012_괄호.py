t = int(input())
for _ in range(t):
    stack = []
    s = input()
    for j in s:
        if j == "(":
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")



