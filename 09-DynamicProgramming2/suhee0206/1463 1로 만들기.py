import sys

read = sys.stdin.readline
N = int(read())
dp = [int(1e6)]*(int(1e6)+1)
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, N+1):
  if i%3 == 0:
    dp[i] = dp[i//3] + 1
  if i%2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)
  dp[i] = min(dp[i], dp[i-1] + 1, dp[i-2] + 2)
print(dp[N])