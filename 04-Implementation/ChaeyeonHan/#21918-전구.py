import sys
input = sys.stdin.readline

N, M = map(int, input().split())
status = list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:  # b번째 전구 상태 c로
        status[b-1] = c
    elif a == 2:  # b부터 c까지 전구상태 반대로 변경
        for i in range(b-1, c):
            if status[i] == 0:
                status[i] = 1
            else:
                status[i] = 0
    elif a == 3:  # b부터 c까지 전구 끄기
        for i in range(b-1, c):
            if status[i] == 1:
                status[i] = 0
    elif a == 4:  # b부터 c까지 전구 켜기
        for i in range(b-1, c):
            if status[i] == 0:
                status[i] = 1
# print(*status)
for i in status:
    print(i, end=' ')