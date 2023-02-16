import sys

read = sys.stdin.readline

N, M = map(int, read().split())
s = list(map(int, read().split()))
for _ in range(M):
  a, b, c = map(int, read().split())
  if a==1:
    s[b-1] = c
  if a==2:
    for i in range(b-1, c):
      s[i] = not s[i]
  if a==3:
    for i in range(b-1, c):
      s[i] = 0
  if a==4:
    for i in range(b-1, c):
      s[i] = 1

for data in s:
  print(int(data), end=' ')