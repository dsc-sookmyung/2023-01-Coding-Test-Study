import sys

n = int(sys.stdin.readline())

balance = 0
two = 0
five = n // 5

while True:
  balance = n - five*5
  two = balance // 2
  balance = balance - two*2
  if balance == 0:
    print(five + two)
    break
  if balance:
    if five:
      five = five - 1
    else:
      print(-1)
      break