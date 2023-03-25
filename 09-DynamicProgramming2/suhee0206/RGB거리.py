import sys

read = sys.stdin.readline
N = int(read())
dp = [[0,0,0] for _ in range(N)]
dp[0] = list(map(int, read().split()))
for i in range(1, N):
  R, G, B = map(int, read().split())
  dp[i][0] = R + min(dp[i-1][1], dp[i-1][2])
  dp[i][1] = G + min(dp[i-1][0], dp[i-1][2])
  dp[i][2] = B + min(dp[i-1][0], dp[i-1][1])
print(min(dp[N-1]))