import sys

read = sys.stdin.readline

n, k = map(int, read().split())
numbers = list(map(int, read().split()))
exchange_count = 0

for last in range(n - 1, 0, -1):
    maxIndex = numbers.index(max(numbers[0:last]))
    if numbers[maxIndex] > numbers[last]:
        numbers[maxIndex], numbers[last] = numbers[last], numbers[maxIndex]
        exchange_count += 1
    if exchange_count == k:
        print(numbers[maxIndex], numbers[last])
        break

if exchange_count < k:
    print(-1)