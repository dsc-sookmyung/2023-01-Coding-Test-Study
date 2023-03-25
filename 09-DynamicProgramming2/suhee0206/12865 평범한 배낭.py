import sys

read = sys.stdin.readline
N, K = map(int, read().split())
things = [[0,0]]
for _ in range(N):
  W, V = list(map(int, read().split()))
  things.append([W, V])
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
  for j in range(1, K+1):
    w, v = things[i][0], things[i][1]
    if j < w:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[N][K])