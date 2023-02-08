import sys

read = sys.stdin.readline

N = int(read())
data = [int(read()) for _ in range(N)]

data.sort(reverse=True)
max_weight = 0

for i in range(N):
  weight = (i+1) * data[i]
  if weight > max_weight:
    max_weight = weight

print(max_weight)