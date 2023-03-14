import sys

read = sys.stdin.readline

n = int(read())
dp = [-1 for _ in range(5001)]

dp[3], dp[5] = 1, 1
for i in range(6, n+1):
  taken_3 = dp[i-3] + 1
  taken_5 = dp[i-5] + 1

  temp = 0
  # 둘다 0
  if not taken_3 and not taken_5:
    temp = -1
  # 둘다 0 아님
  elif taken_3 and taken_5:
    temp = min(taken_3, taken_5)
  # 하나만 0
  else:
    temp = max(taken_3, taken_5)
  dp[i] = temp

print(dp[n])