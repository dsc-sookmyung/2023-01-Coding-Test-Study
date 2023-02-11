# 딕셔너리 사용하기
import sys
input = sys.stdin.readline

N = int(input())

cows = {}  # 소의 번호와 위치를 저장하는 딕셔너리 선언
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    if a not in cows:  # 소의 번호가 없으면
        cows[a] = b
    else:
        if cows[a] != b:
            cnt += 1
            cows[a] = b
print(cnt)

import sys
input = sys.stdin.readline

N = int(input())
cows = [-1] * 11
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    if cows[a] == -1:
        cows[a] = b
    else:
        if cows[a] != b:
            cnt += 1
            cows[a] = b
print(cnt)