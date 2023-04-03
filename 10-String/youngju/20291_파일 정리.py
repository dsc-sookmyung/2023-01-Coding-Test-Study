import sys

read = sys.stdin.readline

N = int(input())
files = [read().strip().split('.') for _ in range(N)]

dic = {}
for i in range(N):
    if files[i][1] in dic.keys():
        dic[files[i][1]] += 1
    else:
        dic[files[i][1]] = 1

dic = dict(sorted(dic.items()))

for k,v in dic.items():
    print(k, v)
