import sys

read = sys.stdin.readline
K, N = map(int, read().split())
cables = list(int(read().strip()) for _ in range(K))

start = 1
end = max(cables)
answer = 0

while start <= end:
  mid = (start + end) // 2
  count = 0
  for cable in cables:
    count += cable // mid
  if count >= N:
    answer = mid
    start = mid + 1
  else:
    end = mid - 1

print(answer)