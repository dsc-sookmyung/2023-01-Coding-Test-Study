# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# S = []
# check = []
# result = 0
# for _ in range(N):
#     S.append(input())
# for _ in range(M):
#     check.append(input())
# # print(check)
#
# for i in range(N):
#     for j in range(M):
#         if S[i] == check[j]:
#             result += 1
# print(result)
#
# => 시간 초과 발생

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()  # 빈 집합 생성
result = 0
for _ in range(N):
    S.add(input())

for _ in range(M):
    check = input()
    if check in S:
        result += 1

print(result)