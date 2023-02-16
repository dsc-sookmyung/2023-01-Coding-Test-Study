import sys

read = sys.stdin.readline

n, k = map(int, read().split())
people = [i for i in range(1, n + 1)]
result = []
remove_index = 0

for _ in range(n):
    remove_index += k - 1
    if remove_index >= len(people):
        remove_index %= len(people)
    result.append(str(people[remove_index]))
    people.pop(remove_index)

print("<", ', '.join(result), ">", sep="")