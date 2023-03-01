import sys
from collections import Counter

read = sys.stdin.readline
N = int(read())

cards = []
for _ in range(N):
  cards.append(int(read()))

cards.sort()
counter = Counter(cards)
print(counter.most_common(1)[0][0])