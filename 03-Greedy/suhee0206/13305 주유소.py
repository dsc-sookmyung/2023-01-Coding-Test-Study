import sys

read = sys.stdin.readline

N = int(read())
L = list(map(int, read().split()))
C = list(map(int, read().split()))

answer = 0
min_cost = C[0]

for i in range(N-1):
  if C[i] < min_cost:
    min_cost = C[i]
  answer = answer + min_cost*L[i]

print(answer)  