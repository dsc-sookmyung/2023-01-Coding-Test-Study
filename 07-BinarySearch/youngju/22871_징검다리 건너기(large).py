import sys

INF = 999999999
read = sys.stdin.readline

n = int(read())
nlist = list(map(int, read().strip().split()))
dp = [0] + [INF] * (n - 1)

for i in range(1, n):
    for j in range(0, i):
        power = max((i - j) * (1 + abs(nlist[i] - nlist[j])), dp[j])
        dp[i] = min(dp[i], power)

print(dp[-1])
