import sys
INF = 2e9

read = sys.stdin.readline
n = int(read())
stones = list(map(int, read().split()))
dp = [0] + [INF] * (n - 1) # dp[i]: i번째 돌에 도착하는 힘의 최솟값

for i in range(1, n): # 도착하는 돌이 두번째~마지막일때, 각 경우의 최솟값을 구한다
  for j in range(0, i): # 도착 돌이 i이고 중간에 j를 밟고 갈때, i번째까지 가는 힘의 최소값을 구한다
    power = max(dp[j], (i - j) * (1 + abs(stones[i] - stones[j]))) # 0부터 j까지의 최솟값과 j부터 i까지
    dp[i] = min(dp[i], power)
print(dp[n - 1])