import sys

read = sys.stdin.readline
t = int(read())

for _ in range(t):
    n = int(read())
    sticker1 = list(map(int, read().split()))
    sticker2 = list(map(int, read().split()))
    sticker = [sticker1, sticker2]

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
    else:
        dp = sticker
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    
        for i in range(2, n):
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    
        print(max(dp[0][n - 1], dp[1][n - 1]))