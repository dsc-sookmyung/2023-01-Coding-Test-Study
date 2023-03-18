import sys
input = sys.stdin.readline

n = int(input())
amount = []
for _ in range(n):
    amount.append(int(input()))

d = [0] * (n+1)
d[1] = amount[0]
if n >= 2:
    d[2] = amount[0] + amount[1]
    for i in range(3, n+1):
        d[i] = max(d[i-2] + amount[i-1], d[i-3] + amount[i-2] + amount[i-1], d[i-1])
print(d[n])