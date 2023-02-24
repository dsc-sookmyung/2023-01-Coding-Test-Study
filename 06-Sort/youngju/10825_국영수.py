import sys

read = sys.stdin.readline

n = int(read().strip())
answer = {}

for _ in range(n):
    s = list(read().strip().split())
    answer[s[0]] = list(map(int, s[1:]))

answer1 = sorted(answer.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))

for i in range(n):
    print(answer1[i][0])



