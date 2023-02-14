import sys

read = sys.stdin.readline

card_count, target = map(int, read().split())
cards = list(map(int, read().split()))

# 연산(더하기) 횟수는 카드를 고르는 조합의 개수에 비례한다
# 100C3은 161700이므로 파이썬 1초 안에 풀 수 있다 (2000만번 이하)

max_sum = 0
for i in range(card_count):
  for j in range(i+1, card_count):
    for k in range(j+1, card_count):
      sum = cards[i] + cards[j] + cards[k]
      if (sum <= target) and (max_sum < sum):
        max_sum = sum

print(max_sum)