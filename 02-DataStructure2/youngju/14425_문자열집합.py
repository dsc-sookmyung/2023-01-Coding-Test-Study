import sys

n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(sys.stdin.readline().strip())

answer = 0
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q in s:
        answer += 1

print(answer)
