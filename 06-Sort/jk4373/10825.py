# 국영수

import sys
N = int(sys.stdin.readline())
Score = [list(sys.stdin.readline().split())for _ in range(N)]

Score.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for idx in Score:
    print(idx[0])
