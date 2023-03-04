import sys
input = sys.stdin.readline

N = int(input())
rocks = list(map(int, input().split()))

INF = 999999999
dp = [0] + [INF] * (N-1)

for i in range(1, N):
    for j in range(0, i):
        power = max((i-j) * (1 + abs(rocks[i]-rocks[j])), dp[j])
        dp[i] = min(dp[i], power)

print(dp[-1])