from collections import deque

m, n = map(int,input().split())
box = []
for i in range(n):
    box.append(list(map(int,input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 1에 대해 모두 동시에bfs를 한 후 box 안에 0이 있는지 확인
def bfs(rot):
    to_visit = deque()
    to_visit.append(rot)
    cnt = 0
    while to_visit:
        x,y = to_visit.popleft()
        for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx>=0 and nx<n and ny>= 0 and ny<n :
                    if box[nx][ny] ==0:
                        box[nx][ny] = box[x][y] +1  # 0으로 바꿔서 더 못오게
                        to_visit.append([nx,ny])
                        
    return cnt
        



rot =[]
#익은 토마토 rot에 저장하기
for i in range(n):
    for j in range(m):
        if box[i][j] ==1:
            rot.append((i,j))

# 익은 토마토들로 bfs 하여 일수 계산하기
if rot:
    bfs(rot)

ans = 0
for line in box:
    for tomato in line:
        if tomato == 0:
            # 안익은 토마토(0)이 있으면 바로 정지
            print(-1)
            exit()
    ans = max(ans, max(line))
# 1에서 시작했기 때문에 결과 값에서 1빼주기
print(ans-1)