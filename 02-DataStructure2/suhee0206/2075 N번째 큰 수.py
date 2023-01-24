import sys
import heapq

read = sys.stdin.readline
N = int(read())
h = []
heapq.heappush(h, max(list(map(int, read().split()))))
for i in range(1, N):
  line = list(map(int, read().split()))
  min_val = heapq.heappop(h)
  for j in range(N):
    if line[j] > min_val:
      heapq.heappush(h, line[j])
  heapq.heappush(h, min_val)
  while len(h) > N:
    heapq.heappop(h)

print(heapq.heappop(h))