import sys

read = sys.stdin.readline
t = int(read())
values = []

def max_value(values):
  dp = [[], []]
  dp[0] = [0 for i in range(len(values[0]))]
  dp[1] = [0 for i in range(len(values[0]))]

  dp[0][0], dp[1][0] = values[0][0], values[1][0]
  if len(values[0]) > 1:
    dp[0][1], dp[1][1] = dp[1][0] + values[0][1], dp[0][0] + values[1][1]

  for i in range(2, n):
    dp[0][i] = max(dp[1][i-1]+values[0][i], dp[1][i-2]+values[0][i])
    dp[1][i] = max(dp[0][i-1]+values[1][i], dp[0][i-2]+values[1][i])

  return max(max(dp[0]), max(dp[1]))

for i in range(t):
  values = [[], []]
  n = int(read())
  values[0] = list(map(int, read().split()))
  values[1] = list(map(int, read().split()))
  print(max_value(values))
