import sys

read = sys.stdin.readline

n = int(read())
wine = [0] + [int(read()) for _ in range(n)] + [0]
dp = [0] * (n+2)
dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[n])

