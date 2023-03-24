import sys

read = sys.stdin.readline

n = int(read())
costs = [list(map(int, read().split())) for _ in range(n)]
dp = [[0]*3 for i in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i-1][2]

print(min(dp[n][0], dp[n][1], dp[n][2]))
