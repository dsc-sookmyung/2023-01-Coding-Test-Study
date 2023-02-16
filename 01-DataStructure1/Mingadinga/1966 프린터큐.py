import sys
from collections import deque

read = sys.stdin.readline

test_count = int(read())
for _ in range(test_count):
  n, m = map(int, read().split())
  arr = list(map(int, read().split()))
  queue = deque(arr)
  target_index = m

  answer = 0
  while target_index >= 0:
    max_value = max(queue)
    front = queue.popleft()
    target_index -= 1
    if front == max_value:
      answer += 1
      if target_index < 0:
        print(answer)
        break
    else:
      queue.append(front)
      if target_index < 0:
        target_index = len(queue) - 1

