import sys

read = sys.stdin.readline
N = int(read().strip())
budgets = list(map(int, read().split()))
M = int(read().strip())


def sum_budgets(limit):
    result = 0
    for b in budgets:
        if b > limit:
            result += limit
        else:
            result += b

    return result


answer = 0
if sum(budgets) <= M:
    answer = max(budgets)
else:
    cnt = 0
    left = 1
    right = max(budgets)
    while left <= right:
        mid = (left + right) // 2
        if sum_budgets(mid) > M:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid

print(answer)
