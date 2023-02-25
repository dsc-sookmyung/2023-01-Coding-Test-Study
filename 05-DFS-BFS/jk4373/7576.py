from collections import deque
import sys
m, n = map(int,input().split())
# box = []
# for i in range(n):
#     box.append(list(map(int,input().split())))

box = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 1에 대해 모두 동시에bfs를 한 후 box 안에 0이 있는지 확인
def bfs(rot):
    to_visit = rot
    while to_visit:
        x,y = to_visit.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] +1  # 일수 계산
                to_visit.append([nx,ny])
                

rot =deque([])
#익은 토마토 rot에 저장하기
for i in range(n):
    for j in range(m):
        if box[i][j] ==1:
            rot.append([i,j])
# 익은 토마토들로 bfs 하여 일수 계산하기
bfs(rot)

m_ans = 0
for line in box:
    for tomato in line:
        if tomato == 0:
            #모두 익지 않는 경우
            print(-1)
            exit()
    m_ans = max(m_ans, max(line))
print(m_ans-1)