import sys

read = sys.stdin.readline
N, M = map(int, read().split())
S = {read().rstrip() for _ in range(N)}
D = {}
for _ in range (M):
  word = read().rstrip()
  if word in D:
    D[word] += 1
  else:
    D[word] = 1

ans = 0
for key in D.keys():
  if key in S:
    ans += D[key]

print(ans)