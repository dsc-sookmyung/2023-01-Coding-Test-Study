import sys
from collections import deque
read = sys.stdin.readline

m, n = map(int, read().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
queue = deque([(x, y) for x in range(n) for y in range (m) if graph[x][y] == 1])

def bfs():
  while queue:
    head = queue.popleft()
    x, y = head[0], head[1]
    # 상하좌우 탐색
    for direction in range(4):
      nx = x + dx[direction]
      ny = y + dy[direction]
      # 인덱스 벗어나면 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 벽이면 무시
      elif graph[nx][ny] == -1:
        continue
      # 익지 않은 토마토면 익힘
      elif graph[nx][ny] == 0:
        # 원래 방문한 토마토의 값(익은 날짜) + 1
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

bfs()
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      print(-1)
      exit(0)
  result = max(result, max(graph[i]))
print(result - 1)