import sys

read = sys.stdin.readline
n = int(read())
card = {}

for i in range(n):
    c = int(read())
    if c in card.keys():
        card[c] += 1
    else:
        card[c] = 0

answer = sorted(card.items(), key=lambda x: (-x[1], x[0]))
print(answer[0][0])
