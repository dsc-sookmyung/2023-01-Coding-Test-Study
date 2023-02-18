import copy
import sys
from collections import deque

read = sys.stdin.readline
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

n, m = map(int, read().split())
lab = [list(map(int, read().split())) for _ in range(n)]
answer = 0


def bfs():
    queue = deque()
    test_matrix = copy.deepcopy(lab)
    for x in range(n):
        for y in range(m):
            if test_matrix[x][y] == 2:
                queue.append((x,y))

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na = a + d[i][0]
            nb = b + d[i][1]
            if 0 <= na < n and 0 <= nb < m:
                if test_matrix[na][nb] == 0:
                    test_matrix[na][nb] = 2
                    queue.append((na, nb))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if test_matrix[i][j] == 0:
                cnt += 1

    global answer
    answer = max(answer, cnt)


def make_wall(wall):
    if wall == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(wall + 1)
                lab[i][j] = 0


make_wall(0)
print(answer)
