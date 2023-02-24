import sys
from collections import deque

read = sys.stdin.readline

m, n = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(n)]
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])


bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer - 1)
