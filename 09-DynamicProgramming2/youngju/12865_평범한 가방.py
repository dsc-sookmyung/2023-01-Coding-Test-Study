import sys

read = sys.stdin.readline
n, k = map(int, read().split())
bag = [(0, 0)]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    w, v = map(int, read().split())
    bag.append((w, v))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = bag[i][0]
        v = bag[i][1]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[n][k])
