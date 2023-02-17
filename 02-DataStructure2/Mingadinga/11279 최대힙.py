import sys
import heapq

read = sys.stdin.readline
n = int(read())
heap = []

for _ in range(n):
  target = int(read().rstrip())
  if isinstance(target, int) and target > 0:
    heapq.heappush(heap, -target)
  elif target == 0:
    if heap:
      print(-heapq.heappop(heap))
    else:
      print(0)