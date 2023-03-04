import sys

read = sys.stdin.readline
k, n = map(int, read().split())
length = [int(read().strip()) for _ in range(k)]
line = max(length)

left = 1
right = line
while left <= right:
    mid = (left + right) // 2

    result = 0
    for l in length:
        result += l // mid

    if result < n:
        right = mid - 1
    else:
        left = mid + 1

print(right)
