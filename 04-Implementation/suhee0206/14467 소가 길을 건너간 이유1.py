import sys

read = sys.stdin.readline

answer = 0
cows = {}

N = int(read())
for _ in range(N):
  i, p = map(int, read().split())
  if i in cows.keys():
    if cows[i] != p:
      answer = answer + 1
  cows[i] = p

print(answer)