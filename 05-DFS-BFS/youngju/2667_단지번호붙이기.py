import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
apt = [list(map(int, read().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


answer = []
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            answer.append(bfs(apt, i, j))

print(len(answer))
print(*sorted(answer), sep="\n")

