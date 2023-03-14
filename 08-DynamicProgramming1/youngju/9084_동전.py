import sys

read = sys.stdin.readline

t = int(read())
for _ in range(t):
    n = int(read())
    coin = list(map(int, read().split()))
    m = int(read())

    dp = [[0] * (m+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for j in range(1, m+1):
            if i != 0:
                dp[i][j] = dp[i-1][j]
            if j - coin[i] >= 0:
                dp[i][j] += dp[i][j - coin[i]]

    print(dp[n-1][m])
