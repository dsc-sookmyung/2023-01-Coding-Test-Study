# DFS- BFS

## 바이러스 2606

### 문제
1번 컴퓨터가 바이러스에 걸렸을 때 그 컴퓨터와 연결되어있는 컴퓨터들은 모두 바이러스에 걸리게 된다. 이 때 바이러스가 걸린 컴퓨터의 수를 구하시오

### 풀이
기본적인 깊이관련 문제로 DFS, BFS 모두 풀이가 가능한 문제이다. 
두가지 경우로 모두 풀어보았는데, DFS는 전부 탐색해야 할때, 위치에 조건이 있을 때 주로 사용하고, BFS는 최단 경로를 사용할 때 주로 사용한다!

### 코드
```
from collections import deque

n = int(input())
pair = int(input())

# 그래프 만들기
graph ={}
for i in range(n):
    graph[i+1] = set()
for i in range(pair):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = [0] * (n+1) # 방문 리스트 초기화

# 넓이 우선 탐색 함수
def bfs(start):
    to_visit = deque([start])
    cnt = 0
    visited[start] = 1
    while to_visit:
        node = to_visit.popleft()
        for i in graph[node]:
            if not visited[i]:
                cnt +=1
                visited[i] = 1
                to_visit.append(i)
    return cnt

#깊이 우선 탐색 함수
def dfs(start):
    to_visit = [start]
    visited[start] = 1
    cnt = 0
    while to_visit:
        node = to_visit.pop()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                to_visit.append(i)
                cnt +=1
    return cnt

print(dfs(1))
```

## 단지 번호 붙이기 2667
### 문제
지도가 주어졌을 때 ( 1은 집, 0은 빈 곳)
붙어있는 마을을 단지로 정의하고, 단지의 수와 단지의 집의 수를 출력하기

### 풀이
bfs와 dfs로 모두 풀이할 수 있는 문제인데 bfs로 풀었다!움직일 수있는 x,y의 범위를 정하여 현 위치에서 4가지 방향으로 움직일 때 생길 수 있는 경우에 맞춰 탐색을 진행한다! 시작점이 주어지지 않았으므로 모든 경우에 대해 진행하게 되는데, 이 때 한 번 방문한 곳은 방문하지 않아야하기때문에 방문한 곳을 모두 0으로 바꿔버렸다.

### 코드
```
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
```

## 토마토 7576
### 문제
상자안에 토마토가 있다. 익은 토마토가 있을 경우에 다음날 주위의 4방향으로 다른 토마토가 익게 된다. 이 때 상자 안의 토마토가 익기까지 걸리는 최소 시간을 구하시오.

### 풀이
이 경우 동시에 탐색을 돌려야 하는지.. 고민을 했었는데, 최소범위를 구하기 때문에 동시에 할 필요는 없고 익은 토마토가 있는 경우에 모두 탐색을 돌려보면 된다! 
최단 시간을 구하기 위해 bfs로 구현하였다.
익은 토마토에 대해 bfs를 진행 한 후 한번 박스 안의 토마토를 다시 확인해보아 모두 익었으면 최소 시간을, 다 익지 않았으면 -1을 출력한다.

### 코드
```
from collections import deque
import sys
m, n = map(int,input().split())
# box = []
# for i in range(n):
#     box.append(list(map(int,input().split())))

box = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
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
```

## 연구소 14502

### 문제
바이러스의 확산을 최소화하기위해 연구소에 벽을 세워야 한다. 이 때 확보할 수 있는 안전 영역의 최대 크기를 구하기

### 풀이
벽을 세우는 함수에 탐색 함수를 넣어 가장 최대의 벽을 만드는 경우를 구할 수 있도록 한다

### 코드
```

from collections import deque
import copy
import sys

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = 0
makeWall(0)
print(answer)

```