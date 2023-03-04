import sys
input = sys.stdin.readline

K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]

# 탐색할 자를 길이의 범위가 (1 ~ 가장 긴 랜선의 길이)
start, end = 1, max(length)
# print(start, end)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in length:
        cnt += i // mid  # 주어진 랜선 길이에서 몇 개 만들수 있는지
    if cnt >= N:
        start = mid + 1
    else:
        end = mid -1
print(end)