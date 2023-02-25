from collections import deque
n = int(input())

graph = [list(map(int,input().rstrip())) for _ in range(n)] # 지도
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs1(x1,y1):
    #1인 경우에만 확인하기

    to_visit = deque()
    to_visit.append((x1,y1))
    # visited[x][y] = 1 visit로 두번 관리하지 않고 1인 자리를 0으로 바꿔버려서 1일 떄만 검색할 수 있도록 만듦
    graph[x1][y1] = 0
    cnt =1
    while to_visit:
        x,y = to_visit.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>= 0 and ny<n :
                if graph[nx][ny] ==1:
                    graph[nx][ny] = 0  # 0으로 바꿔서 더 못오게
                    to_visit.append((nx,ny))
                    cnt +=1
    return cnt 

# 모든 경우를 다 돌아서 count를 세기
cnt =[]
for i in range(n):
    for j in range(n):
        if graph[i][j] ==1:
            cnt.append(bfs1(i,j))


cnt.sort() # 첫째줄에는 집 종류
print(len(cnt))
for i in range(len(cnt)): # 마을별 집 개수
    print(cnt[i])