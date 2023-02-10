import sys

yogurt_count = int(input())
yogurt_price = []

for i in range(yogurt_count):
    yogurt_price.append(int(input()))
yogurt_price.sort(reverse=True)

free_price = 0
for i in range(2, len(yogurt_price), 3):
  free_price += yogurt_price[i]

print(sum(yogurt_price) - free_price)