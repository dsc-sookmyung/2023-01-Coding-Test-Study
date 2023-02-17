import sys

read = sys.stdin.readline
n, m = map(int, read().split())
set = set()
count = 0
for _ in range(n):
  set.add(read().rstrip()) # O(1)

for _ in range(m):
  if read().strip() in set: # O(1)
    count += 1

print(count)