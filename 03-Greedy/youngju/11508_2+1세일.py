import sys

n = int(sys.stdin.readline())
price = [int(sys.stdin.readline()) for _ in range(n)]
price.sort(reverse=True)
answer = 0
for i in range(n):
    if i % 3 != 2:
        answer += price[i]

print(answer)
