# 완전탐색 + bfs
# 0의 갯수(안전지대)가 가장 많을때를 찾아줘야한다
# 브루트 포스로 벽3개의 위치로 가능한 경우의 수를 모두 구해주고, 그때마다 bfs함수를 돌려준다.

import sys
from collections import deque

n, m= map(int, sys.stdin.readline().rstrip().split())
graph=[]
max_result=0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1  # 처음0의개수

# 바이러스 퍼지는 함수
def virus():
    visited = [[0]*m for _ in range(n)]
    result = 0
    global max_result
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:  # 바이러스이면
                visited[i][j] = 1  # 방문처리 해주고 큐에 넣어주기
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    result += 1  # 하나 증가
                    q.append((nx, ny)) # 큐에 넣어주기]
    max_result = max(max_result, cnt-result)

def walls(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1  # 벽세우기기
                walls(cnt+1)
                graph[i][j] = 0

walls(0)
print(max_result-3)