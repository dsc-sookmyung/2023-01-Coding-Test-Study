import sys
n = int(sys.stdin.readline())
scores=[]

for _ in range(n):
    a, b, c, d = map(str, sys.stdin.readline().split())
    scores.append([a, int(b), int(c), int(d)])

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
# 국어점수 감소 순서/영어점수 증가 순서/수학점수 감소 순서

for i in range(n):
    print(scores[i][0])