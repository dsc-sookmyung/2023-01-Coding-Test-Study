import sys

read = sys.stdin.readline


def combination_count(coins, target):
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for coin in coins:
        for k in range(target + 1):
            if k >= coin:
                dp[k] += dp[k - coin]

    return dp[target]


t = int(read())

for _ in range(t):
    n = int(read())
    coins = list(map(int, read().split()))
    m = int(read())
    print(combination_count(coins, m))
