import sys

read = sys.stdin.readline

n = int(read())
dp = [-1 for _ in range(n+1)]

if n < 4:
  dp[n] = n % 2

else:
  dp[1] = 1
  dp[2] = 0
  dp[3] = 1

for i in range(4, n+1):
  dp[i] = not dp[i-1] or not dp[i-3]
print('SK' if dp[n]==1 else 'CY')

'''
dp[i] : i번째 돌을 마지막으로 가져갔을 때 상근이가 이기는가(1)
dp[1] = 1
dp[2] = 0
dp[3] = 1

dp[i-3] 혹은 dp[i-1]이 1이면 dp[i]은 0이다
dp[i] = dp[i-1] or dp[i-3]
'''