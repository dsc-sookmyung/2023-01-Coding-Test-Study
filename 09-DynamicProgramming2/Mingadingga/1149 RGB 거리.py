import sys

read = sys.stdin.readline

n = int(read())
prices = [list(map(int, read().split())) for _ in range(n)]

INF = 1001
dp = [[INF]*3 for _ in range(n)]

dp[0][0] = prices[0][0]
dp[0][1] = prices[0][1]
dp[0][2] = prices[0][2]

for house in range(1, n):
  dp[house][0] = min(dp[house-1][1], dp[house-1][2])+prices[house][0]
  dp[house][1] = min(dp[house-1][0], dp[house-1][2])+prices[house][1]
  dp[house][2] = min(dp[house-1][0], dp[house-1][1])+prices[house][2]

print(min(dp[-1]))