import sys
from collections import deque

read = sys.stdin.readline
n = int(read())
balloons = list(map(int, read().split()))
spin_queue = deque()
result = []

for i in range(len(balloons)):
  spin_queue.append((i, balloons[i]))

while spin_queue:
  index, move_value = spin_queue.popleft()
  result.append(index + 1)
  if move_value > 0:
    spin_queue.rotate(-(move_value - 1))
  else:
    spin_queue.rotate(-move_value)

print(' '.join(map(str, result)))