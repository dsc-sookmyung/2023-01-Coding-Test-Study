# 나이순 정렬

import sys

N = int(sys.stdin.readline())
Table = []
for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    Table.append((age, name))
Table.sort(key = lambda x: x[0])

for i in Table:
    print(i[0], i[1])