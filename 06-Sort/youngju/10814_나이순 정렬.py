import sys

read = sys.stdin.readline
n = int(read().strip())
answer = {}
for i in range(n):
    s = list(read().strip().split())
    s[0] = int(s[0])
    answer[i] = s

answer1 = sorted(answer.items(), key=lambda x: (x[1][0], x[0]))
answer1 = dict(answer1)
for i in answer1.values():
    print(*i)
