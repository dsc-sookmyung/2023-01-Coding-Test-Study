import sys
input = sys.stdin.readline

N = int(input())
costs = []
for _ in range(N):
    costs.append(int(input()))
costs.sort(reverse=True)

result = 0
for i in range(N):
    if i % 3 != 2:  # 나머지가 2가 아니면 -> result에 더해준다
        result += costs[i]
print(result)