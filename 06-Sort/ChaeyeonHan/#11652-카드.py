import sys
input = sys.stdin.readline

N = int(input())
cards_dict = {}

for _ in range(N):
    a = int(input())
    if a not in cards_dict:
        cards_dict[a] = 1
    else:
        cards_dict[a] += 1

max_key = sorted(cards_dict.items(), key=lambda x: (-x[1], x[0]))
print(max_key[0][0])