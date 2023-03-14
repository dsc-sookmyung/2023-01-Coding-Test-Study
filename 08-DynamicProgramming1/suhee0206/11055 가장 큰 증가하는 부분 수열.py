import sys

read = sys.stdin.readline
N = int(read())
A = list(map(int, read().split()))
d = [x for x in A]
answer = d[0]

for i in range(N):
  for j in range(i+1):
    if (A[j] < A[i]) and (d[j] + A[i] > d[i]):
      d[i] = d[j] + A[i]
  answer = max(d[i], answer)

print(answer)