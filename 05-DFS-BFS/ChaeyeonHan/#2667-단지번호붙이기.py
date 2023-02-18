# bfs
from collections import deque
import sys
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y):
    n=len(graph)
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0  # 맨 처음 지점도 방문처리
    count = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0   #값을 0으로 바꿔준다
                queue.append((nx, ny))
                count += 1
    return count


n = int(sys.stdin.readline().rstrip())
graph=[]
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

nums = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            nums.append(bfs(graph, i, j))
            # print(nums)
nums.sort()
print(len(nums))
for i in range(len(nums)):
    print(nums[i])