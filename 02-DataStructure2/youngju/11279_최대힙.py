import sys
import heapq

n = int(input())
data = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(data) != 0:
            print(heapq.heappop(data)[1])
        else:
            print(0)
    else:
        heapq.heappush(data, (-x, x))
