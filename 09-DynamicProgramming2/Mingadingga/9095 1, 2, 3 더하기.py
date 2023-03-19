import sys

read = sys.stdin.readline

t = int(read())
targets = []
dp = []

# 입력 받기
for _ in range(t):
  targets.append(int(read()))
  dp = [0 for _ in range(max(targets)+1)]

# dp 채우기
dp[0], dp[1] = 1, 1
if len(dp) > 2: dp[2] = 2
for i in range(3, max(targets) + 1):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 출력하기
for target in targets:
  print(dp[target])