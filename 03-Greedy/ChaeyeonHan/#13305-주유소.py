# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# routes = list(map(int, input().split()))  # 도로 길이
# costs = list(map(int, input().split()))  # 리터당 가격
#
# result = 0
# for i in range(N-1):
#     min_costs = min(costs[i:N-1])
#     # print(min_costs)
#     if costs[i] == min_costs:
#         result += costs[i] * sum(routes[i:])
#         break
#     else:
#         result += costs[i] * routes[i]
# print(result)

import sys
input = sys.stdin.readline

N = int(input())
routes = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = 0
min_costs = costs[0]
for i in range(N-1):
    if costs[i] < min_costs:
        min_costs = costs[i]
    result += min_costs * routes[i]
print(result)