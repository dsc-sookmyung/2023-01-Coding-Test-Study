import sys
read = sys.stdin.readline

n = int(read())
card_count_dict = {}

for _ in range(n):
  card = int(read())
  if card in card_count_dict:
    card_count_dict[card] += 1
  else:
    card_count_dict[card] = 1

result = sorted(card_count_dict.items(), key = lambda item : (-item[1], item[0]))
print(result[0][0])
