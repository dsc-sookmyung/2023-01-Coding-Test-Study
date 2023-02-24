### 2606 바이러스
#### 풀이) 
- 컴퓨터의 갯수와 연결된 링크의 수를 입력받는다.
- matrix에 연결된 정보를 2차원 배열로 저장하고(양방향 연결되어있음을 표시), visited 배열을 만들어 해당 컴퓨터를 방문했는지 표시해준다.
- dfs방법으로는, 처음 방문하는 컴퓨터 번호 v를 받고, 방문처리 후 for문을 통해 연결된 컴퓨터들을 재귀호출하며 방문한다.
- bfs방법으로는, 큐를 사용해준다. 큐에 값이 있는 동안 while문을 돌면서 아직 방문하지 않은 연결된 컴퓨터들을 방문처리하고, 큐에 append 시켜주는 작업을 반복해 총 result배열의 길이를 출력한다.
```python
# dfs를 사용한 풀이
N = int(input())
links = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(links):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1  # 연결된거 표시

result=[]
def dfs(v):
    visited[v] = 1  # 방문처리
    for i in range(1, N+1):
        if visited[i] == 0 and matrix[v][i] == 1:   # 연결되어있는데 방문안한곳
            result.append(i)
            dfs(i)
    return len(result)

print(dfs(1))



# bfs를 사용한 풀이
from collections import deque
N = int(input())
M = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)]  # 연결된 노드를 표시하기 위해
visited = [0]*(N+1)  # 방문처리를 해주기 위해

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1  #연결표시

result=[]
def bfs(v):
    queue = deque([v])
    visited[v] = 1  # 방문처리
    while queue:  #큐가 빌때까지 반복
        v = queue.popleft()
        for i in range(1, N+1):
            if visited[i] == 0 and matrix[v][i] == 1:  # 방문안했고 연결되어있으면
                visited[i] = 1  # 방문처리
                queue.append(i)
                result.append(i)
    return len(result)

print(bfs(1))
```

### 2667 단지번호 붙이기
#### 풀이) 
- graph 리스트에 전체 지도를 넣어주고, 위 아래 오른쪽 왼쪽으로 한칸씩 이동하는 좌표를 나타내기 위해 dx, dy라는 리스트를 만들어 움직임을 저장한다.
- 그래프의 원소가 1일 때마다 bfs를 실행시킨다.
- bfs에서는 큐를 만들어 처음 x, y를 방문처리 해주고, 큐가 비어있을 때까지 각 좌표마다 위 아래 오른쪽 왼쪽으로 이동하는 경우를 모두 고려한다.
- 좌표 이동시 그래프를 벗어나는 경우라면 continue로 넘어가고, 범위에 벗어나지 않고 아직 방문하지 않았다면 방문처리를 하고 큐에 해당 좌표를 추가시키고 갯수를 1 증가시키며 세준다.
```python
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
```

### 7576 토마토
#### 풀이) 
- 토마토의 상태를 tomato 배열에 2차원 리스트로 저장한다.
- 처음에 queue에 받는 토마토의 위치를(=1의 위치) append하고, bfs()를 실행한다.
- bfs()에서는 처음 좌표를 x, y에 꺼내고 상하좌우 움직이는 토마토의 좌표를 dx, dy로 설정하여 토마토의 좌표가 범위를 넘어가지 않고, 아직 익지 않았다면 1씩 더하며 횟수를 세어준다.
- 여기서 가장 큰 값이 정답이 된다.
- 마지막에 0인 토마토가 있다면 모두 익지 않았기에 -1을 출력해주고, exit()해준다. 다 익었다면 (최댓값-1)을 출력한다.

```python
import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())  # 가로, 세로칸의 수
tomato = []

for _ in range(N):
    tomato.append(list(map(int, input().split())))

queue = deque()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0  # 일수 체크

# 처음에 1인 토마토의 위치를 append
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and  tomato[nx][ny] == 0:  # 범위를 벗어나지 않고 아직 안익었다면
                tomato[nx][ny] = tomato[x][y] + 1  # 횟수 세어주기
                queue.append((nx, ny))

bfs()

for i in tomato:
    for j in i:
        if j == 0:  # 안익은 토마토 있으면
            print(-1)
            exit()
    count = max(count, max(i))

print(count-1)
```

### 14502 연구소
#### 풀이) 
- 안전 영역의 최댓값을 구하기 위해서 벽을 세울 수 있는 모든 경우의 수를 고려한다.
- 이중 for문을 반복하며 순서대로 3개의 칸씩 선택해서 벽을 세운 뒤 안전영역의 갯수를 카운트해서 최댓값을 찾아내야 한다.
- 벽을 어떻게 세우는지에 대해 감을 잡지 못해 어려웠다..

```python
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
```