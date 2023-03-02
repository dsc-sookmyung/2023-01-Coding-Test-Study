import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
queue = deque([i for i in range(1, n+1, 1)])

while len(queue) > 1:
  queue.popleft()
  queue.append(queue.popleft())
print(queue[0])