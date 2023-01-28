# 이 풀이는 시간초과. 리스트에서 dictionary로 변경해주자!
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# answer = []
# for i in range(N):
#     answer.append([i, input()])  # 순서, 이름
#
# for _ in range(M):
#     question = input().rstrip()
#     if question.isdigit():  # 숫자면
#         # print(int(question)-1)
#         question = int(question) - 1
#         print(answer[question][1])
#     else:
#         for i in range(N):
#             if question == answer[i][1]:
#                 print(i+1)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict_name = {}
dict_number = {}

for i in range(N):
    name = input().rstrip()
    dict_name[i] = name
    dict_number[name] = i

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():  # 숫자인 경우
        print(dict_name[int(question)-1])
    else:
        print(dict_number[question]+1)