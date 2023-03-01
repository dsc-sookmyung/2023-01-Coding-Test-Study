import sys

read = sys.stdin.readline
N = int(read())
requests = list(map(int, read().split()))
M = int(read())

max_val = max(requests)

start = M // N
end = max_val
limit = 0

while start <= end:
  budget = M
  mid = (start + end) // 2
  for x in requests:
    if x <= mid:
      budget -= x
    else:
      budget -= mid
  if budget == 0:
    limit = mid
    break
  elif budget < 0:
    end = mid-1
  else:
    limit = mid
    start = mid+1

print(min(limit, max_val))