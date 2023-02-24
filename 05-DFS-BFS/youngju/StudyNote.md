# DFS/BFS
## 2606 바이러스
문제가 요구한 순서대로 입력 받고 BFS를 이용해서 풀었다.

```python
import sys  
from collections import deque  
  
read = sys.stdin.readline  
  
n = int(read())  
pair = int(read())  
graph = [[] for _ in range(n+1)]  
visited = [0] * (n+1)  
  
for i in range(pair):  
    x, y = map(int, read().split())  
    graph[x].append(y)  
    graph[y].append(x)  
  
  
# BFS  
visited[1] = 1  
q = deque([1])  
while q:  
    now = q.popleft()  
    for node in graph[now]:  
        if visited[node] == 0:  
            q.append(node)  
            visited[node] = 1  
  
print(sum(visited) - 1)
```

**[풀이]**
1) 전체 컴퓨터의 수 n과 컴퓨터 쌍의 수 pair 입력 받기
2) 감염된 컴퓨터를 체크할 visited 리스트 생성
3) 컴퓨터 쌍을 입력 받아 graph 이중 리스트에 저장
4) 1번 컴퓨터가 감염 시작이므로 visited[1]에 값을 1로 체크해주고 시작
5) q라는 deque에 1번 컴퓨터를 먼저 넣음 
6) q에 원소가 없을 때까지 popleft하면서 popleft한 원소와 연결된 컴퓨터를 graph에서 찾고 감염되지 않았다면(visited 리스트에서 값이 0이라면) q에 append하고 visited값을 1로 변경하여 감염 표시
7) 감염된 컴퓨터가 총 몇 대인지 출력해야 하므로 visited리스트에서 1로 표시된 것들만 찾으면 되므로 sum(visited)에서 1번 컴퓨터의 값만 빼주면 된다 

<br/>

## 2667 단지 번호 붙이기
아파트 지도를 돌면서 집의 수를 리스트에 저장하고 오름차순으로 출력해서 풀었다.

```python
import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
apt = [list(map(int, read().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


answer = []
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            answer.append(bfs(apt, i, j))

print(len(answer))
print(*sorted(answer), sep="\n")
```


**[풀이]**
1) 아파트 지도의 크기 n을 입력 받고 아파트 지도를 입력 받아 apt 이중 리스트에 저장
2) 상하좌우로 움직이기 위해 dx와 dy 리스트 생성
3) queue라는 deque를 생성 후 탐색 시작 위치의 x, y좌표를 queue에 넣는다
4) 탐색 시작 위치의 apt에서의 값을 0으로 변경하여 방문 표시를 한다
5) 시작 위치부터 집의 개수를 카운트해야하므로 count를 1로 설정
6) queue에 원소가 없을 때까지 popleft하면서 popleft한 원소와 연결된 원소를 찾는다
7) 이때 연결된 원소를 찾는 방법은 dx와 dy를 한 칸씩 더하면서 상하좌우의 좌표 값을 구하여 nx와 ny에 저장
8) 이때 nx와 ny가 지도를 빠져나가는지 그리고 아직 방문하지 않은 곳이 맞는지(apt에서의 값이 1인지)를 확인한 후 지도에서의 값을 0으로 변경하고 queue에 append해주고 count를 +1 한다
9) 위의 3번부터 8번까지의 과정을 apt 이중 리스트를 돌면서 apt의 값이 1일 때마다 실행하고 return 값을 정답 리스트인 anwer에 저장
10) answer의 길이와 원소를 오름차순으로 출력 

<br/>

## 7576 토마토
바로 전 문제인 2667번과 유사하다

```python
import sys
from collections import deque

read = sys.stdin.readline

m, n = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(n)]
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])


bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer - 1)
```

**[풀이]**
1) 상자의 크기를 m, n에 입력 받는다
2) matrix라는 이중 리스트에 토마토의 상태를 저
3) 2667번과 유사하게 상하좌우만 고려하면 되므로 상하좌우 좌표값을 구하기 위한 리스트 dx와 dy 생성
4) queue라는 deque를 생성 후 popleft하면서 해당 원소의 상하좌우 좌표값을 구한 후 상하좌우 좌표에 해당하는 matrix에서의 값이 0이라면 1로 변경 후 queue에 append하여 queue에 원소가 없을 때까지 반복
5) 토마토가 모두 익지 못하는 상황이라면 -1를 출력하고 아니라면 첫 시작인 1을 빼준 값이 정

<br/>

## 14502 연구소 
벽을 만드는 경우까지 생각해야 해서 많이 고민했던 문제이다😭 

```python
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
```

**[풀이]**
1) 상하좌우로 바이러스가 퍼질 수 있으므로 상하좌우로 움직일 좌표를 계산할 d라는 이중 리스트를 생성
2) 연구소의 크기 n, m을 입력 받고 lab이라는 이중 리스트에 연구소 상태 저장
3) bfs를 사용하기 위해 queue라는 deque생성
4) 벽이 세워진 연구소 상태를 저장하기 위해 원본 연구소 상태 이중 리스트(lab)을 변경하지 않을 테스트 이중 리스트인 test_matrix를 만듦
5) 상태가 2인 곳이라면 queue에 append
6) queue에 원소가 없을 때까지 popleft하면서 상하좌우의 연구소 상태를 확인한다
7) 상하좌우의 상태가 0이라면 바이러스가 퍼질 수 있으므로 2로 변경 후 queue에 append
8) 안전 영역의 크기를 구해야 하므로 0인 곳을 찾아서 cnt라는 변수에 저장
9) 벽을 총 3개 세울 수 있는데 어디에 세울 지 모르기 때문에 lab리스트를 순회하면서 0인 곳을 1로 바꾼 후 make_wall함수를 다시 호출하고 벽이 총 3개라면 bfs를 실행하도록 한다
10) 이때 벽이 세워질 수 있는 경우를 다 돌면서 bfs 수행 후 answer에 안전 영역의 크기가 저장되고 만약 후에 더 큰 값(cnt)이 구해진다면 그 값이 answer가 되면서 최종 답으로 answer를 출력 

