import sys

read = sys.stdin.readline
T = int(read())
for _ in range(T):
  N = int(read())
  coins = list(map(int, read().split()))
  M = int(read())
  
  d = [0]*(10001)
  
  for coin in coins:
    d[coin] += 1
    for i in range(coin, M+1):
      d[i] += d[i-coin]

  print(d[M])