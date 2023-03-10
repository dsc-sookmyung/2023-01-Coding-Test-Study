import sys
import math

read = sys.stdin.readline

INF = 50001
n = int(read())
dp = [0, 1]

for i in range(2, n+1):
  min_value = INF
  for j in range(1, int(math.sqrt(i)) + 1):
    min_value = min(min_value, dp[i-j*j]+1)
  dp.append(min_value)
print(dp[n])