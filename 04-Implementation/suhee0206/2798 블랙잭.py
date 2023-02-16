import sys

read = sys.stdin.readline

N, M = map(int, read().split())
cards = list(map(int, read().split()))

sums = []

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      sums.append(cards[i] + cards[j] + cards[k])

answer = 0
sub = 300001

for sum in sums:
  if M-sum >= 0 and M-sum < sub:
    answer = sum
    sub = M-sum
    
print(answer)