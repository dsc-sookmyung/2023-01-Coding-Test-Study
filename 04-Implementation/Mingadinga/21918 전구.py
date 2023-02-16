import sys

read = sys.stdin.readline

n, m = map(int, read().split())
states = list(map(int, read().split()))

for i in range(m):
  a, b, c = map(int, read().split())

  if a == 1:
    states[b - 1] = c
  elif a == 2:
    for j in range(b - 1, c):
      states[j] = 1 - states[j]
  elif a == 3:
    for j in range(b - 1, c):
      states[j] = 0
  elif a == 4:
    for j in range(b - 1, c):
      states[j] = 1

for state in states:
  print(int(state), end = ' ')