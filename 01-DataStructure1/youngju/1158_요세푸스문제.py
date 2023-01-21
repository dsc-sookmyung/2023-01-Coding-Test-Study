from collections import deque

n, k = map(int, input().split())
circle = deque([i for i in range(1, n+1)])
result = []
while len(circle) != 0:
    cnt = k
    while cnt != 1:
        circle.append(circle.popleft())
        cnt -= 1
    x = circle.popleft()
    result.append(x)

print("<", end="")
print(*result, sep=", ", end="")
print(">")
