import sys
import heapq

n = int(input())
data = []
for _ in range(n):
    xlist = list(map(int, sys.stdin.readline().split()))
    if not data:
        for x in xlist:
            heapq.heappush(data, x)
    else:
        for x in xlist:
            if data[0] < x:
                heapq.heappush(data, x)
                heapq.heappop(data)

print(data[0])
