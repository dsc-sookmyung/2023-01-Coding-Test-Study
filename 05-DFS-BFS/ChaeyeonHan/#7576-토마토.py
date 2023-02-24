import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())  # 가로, 세로칸의 수
tomato = []

for _ in range(N):
    tomato.append(list(map(int, input().split())))

queue = deque()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0  # 일수 체크

# 처음에 1인 토마토의 위치를 append
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and  tomato[nx][ny] == 0:  # 범위를 벗어나지 않고 아직 안익었다면
                tomato[nx][ny] = tomato[x][y] + 1  # 횟수 세어주기
                queue.append((nx, ny))

bfs()

for i in tomato:
    for j in i:
        if j == 0:  # 안익은 토마토 있으면
            print(-1)
            exit()
    count = max(count, max(i))

print(count-1)