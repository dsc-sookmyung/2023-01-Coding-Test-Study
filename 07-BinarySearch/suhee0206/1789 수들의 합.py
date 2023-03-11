import sys

read = sys.stdin.readline
S = int(read())

sum = 1
N = 1
while sum <= S:
  N += 1
  sum += N

print(N-1)