import sys

read = sys.stdin.readline
n = int(read())
glasses = [0] * 10000
for i in range(n):
  glasses[i] = int(read())
dp = [0] * 10000
dp[0] = glasses[0]
dp[1] = glasses[0] + glasses[1]
dp[2] = max(glasses[0], glasses[1]) + glasses[2]
dp[3] = max((dp[0] + glasses[2]), dp[1]) + glasses[3]
for i in range(4, n):
  dp[i] = max((max(dp[i-3], dp[i-4]) + glasses[i-1]), dp[i-2]) + glasses[i]
print(max(dp))