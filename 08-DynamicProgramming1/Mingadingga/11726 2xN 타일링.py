import sys

read = sys.stdin.readline
n = int(read())
dp = [0 for _ in range(n+1)]

'''
dp[i] : i번째를 채우는 경우의 수
1) i-1까지가 채워진 경우 : 1가지 (1*2)
2) i-2까지가 채워진 경우 : 1가지 (2*1) - 1*2 두개를 세로로 놓는 경우는 1번에 포함됨
dp[i] = dp[i-1] + dp[i-2]
dp[0] = 0, dp[1] = 1, dp[2] = 2
'''

dp[0], dp[1], dp[2] = 0, 1, 2
for i in range(3, n+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)