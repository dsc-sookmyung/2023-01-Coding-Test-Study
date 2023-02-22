import sys

read = sys.stdin.readline

n = int(read())
numbers = [int(read()) for _ in range(n)]
number_count = {}

# average
average = round((sum(numbers) / n), 0) + 1 - 1
print(f'{average:.0f}')

numbers.sort()

# mid
print(numbers[n // 2])

# max appearance
for number in numbers:
    if number in number_count:
        number_count[number] += 1
    else:
        number_count[number] = 1
sorted_number_count = sorted(number_count.items(), key=lambda x: (-x[1], x[0]))

max_count = sorted_number_count[0][1]
if len(sorted_number_count) > 1 and sorted_number_count[1][1] == max_count:
    print(sorted_number_count[1][0])
else:
    print(sorted_number_count[0][0])

# range
print(numbers[n - 1] - numbers[0])