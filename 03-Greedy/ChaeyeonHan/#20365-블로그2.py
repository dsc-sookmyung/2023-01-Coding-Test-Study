import sys
input = sys.stdin.readline

N = int(input())
colors = list(input().rstrip())
count = {'B': 0, 'R': 0}  # 칠할 횟수 저장

count[colors[0]] += 1  # 맨 처음 색칠하기
for i in range(1, N):
    if colors[i] != colors[i-1]:  # 이전색과 다르다면
        count[colors[i]] += 1
# print(count)
print(min(count['B'], count['R']) + 1)
