#카드
import sys

N = int(sys.stdin.readline())
cards ={}
for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp in cards:
        cards[tmp] += 1
    else:
        cards[tmp] = 1

result = sorted(cards.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])