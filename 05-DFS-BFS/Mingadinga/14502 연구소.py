import sys
from collections import deque
from itertools import combinations
import copy

read = sys.stdin.readline

n, m = map(int, read().split())
graph = [list(map(int, input().split())) for _ in range(n)]
origin_graph = copy.deepcopy(graph)
wall_able = [(x, y) for x in range(n) for y in range(m) if graph[x][y] == 0]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
result = 0

def bfs(x, y):
    queue.append((x, y))
    while queue:
        head = queue.popleft()
        # 상하좌우 탐색
        for direction in range(4):
            nx = head[0] + dx[direction]
            ny = head[1] + dy[direction]
            # 인덱스 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 1이면 무시
            elif graph[nx][ny] == 1:
                continue
            # 0이면 방문
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))
                x = nx
                y = ny

def make_walls(walls):
    for wall in walls:
        graph[wall[0]][wall[1]] = 1


def do_bfs():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                bfs(i, j)


def check_safety_count():
    safety_count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                safety_count += 1
    return safety_count

# 벽을 세울 수 있는 모든 조합에 대하여
# bfs로 감염 테스트하고 안전지대 개수 반환
# 안전지대 max 값으로 업데이트
walls_combinations = combinations(wall_able, 3)
for walls in walls_combinations:
    make_walls(walls)
    do_bfs()
    safety_count = check_safety_count()
    if safety_count > result:
        result = safety_count
    graph = copy.deepcopy(origin_graph)
print(result)