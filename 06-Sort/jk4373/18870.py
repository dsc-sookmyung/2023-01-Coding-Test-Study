# 좌표 압축

import sys
N = int(sys.stdin.readline())
map = list(map(int,sys.stdin.readline().split()))

map_sorted = []
map_sorted = list(sorted(set(map)))

map_dic = {map_sorted[i]:i for i in range(len(map_sorted))}

for i in map:
    print(map_dic[i], end=' ')