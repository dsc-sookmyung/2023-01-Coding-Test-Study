import sys

read = sys.stdin.readline
N = int(read())
A = list(map(int, read().split()))

INF = 1e9
d = [0] + [INF]*(N-1)
#d[1] = (1-0)*(1+abs(A[1]-A[0]))

for i in range(1, N):
  for j in range(i):
    force = max((i-j) * (1 + abs(A[i] - A[j])), d[j])
    d[i] = min(d[i], force)

print(d[N-1])