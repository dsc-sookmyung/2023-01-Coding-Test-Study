import sys

read = sys.stdin.readline
T = int(read())
for _ in range(T):
  n = int(read())
  stickers = []
  for _ in range(2):
    stickers.append([0]+list(map(int, read().split())))
  d = [[0,0] for _ in range(n+1)]
  d[1][0] = stickers[0][1]
  d[1][1] = stickers[1][1]
  for i in range(2, n+1):
    d[i][0] = max(d[i-1][1], max(d[i-2])) + stickers[0][i]
    d[i][1] = max(d[i-1][0], max(d[i-2])) + stickers[1][i]
  print(max(max(d[n]), max(d[n-1])))