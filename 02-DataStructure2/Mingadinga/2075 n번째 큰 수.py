import sys
import heapq

read = sys.stdin.readline
n = int(read())
max_heap = []

for _ in range(n):
  targets = list(map(int, read().split()))
  for target in targets:
    if len(max_heap) < n:
      heapq.heappush(max_heap, target)
    if target > max_heap[0]:
      heapq.heappop(max_heap)
      heapq.heappush(max_heap, target)
print(max_heap[0])