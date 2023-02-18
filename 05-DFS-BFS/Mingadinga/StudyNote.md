[#2606 바이러스](https://www.acmicpc.net/problem/2606)

> 접근 방법

주어진 컴퓨터 연결 상태를 그래프로 표현할 수 있고, 문제 요구사항이 그래프를 탐색하는 문제이므로 dfs나 bfs를 사용해 풀 수 있다.
문제에서는 별다른 조건이 없어서 dfs나 bfs 둘 다 사용할 수 있을 것 같아서 둘다 구현해서 풀어봤다.
이코테에서는 보통 재귀함수 호출이 느려서 dfs보다는 bfs가 빠르다고 했는데, 돌려보니 dfs가 좀 더 빨랐다..! 왜지

> 통과한 코드

```python
# 113112 kb	124 ms

def dfs(graph, v, visited):
  visited[v] = True
  for neighbor in graph[v]:
    if not visited[neighbor]:
      global infected_count
      infected_count += 1
      dfs(graph, neighbor, visited)

import sys
read = sys.stdin.readline

computer_count = int(read())
pair_count = int(read())
visited = [False for _ in range(computer_count + 1)]

graph = [[] for _ in range(computer_count + 1)]
infected_count = 0

for _ in range(pair_count):
  parent, child = map(int, read().split())
  graph[parent].append(child)
  graph[child].append(parent)

dfs(graph, 1, visited)
print(infected_count)
```

```python
# 114436 kb	140 ms

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        head = queue.popleft()
        for neighbor in graph[head]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                global infected_count
                infected_count += 1

import sys
from collections import deque

read = sys.stdin.readline

computer_count = int(read())
pair_count = int(read())
visited = [False for _ in range(computer_count + 1)]

graph = [[] for _ in range(computer_count + 1)]
infected_count = 0

for _ in range(pair_count):
    parent, child = map(int, read().split())
    graph[parent].append(child)
    graph[child].append(parent)

bfs(graph, 1, visited)
print(infected_count)
```



[#2667 단지번호 붙이기](https://www.acmicpc.net/problem/2667)

> 접근 방법

아파트를 그래프로 표현하면 2차원 리스트를 탐색할 수 있으므로, dfs 혹은 bfs로 풀 수 있다. 
문제에 특별한 조건이 없어 dfs나 bfs 둘다 사용 가능한데, dfs로 재귀함수 사용 중에 값 리턴하는걸 더 연습하고 싶어서 dfs로 풀었다.
문제의 요구사항은 탐색 가능한 집단의 개수와 각 집단에 포함된 노드 개수를 출력하는 것이다.
모든 원소에 대해서 dfs를 돌리되, 방문 가능한 노드를 만나면 0으로 값을 변경해 방문 처리하여, 같은 집단 내의 다른 원소에서 dfs를 돌릴 때 중복 카운트되지 않도록 한다.
집단에 포함된 노드 개수는 재귀 함수가 호출되는 동안 임시 변수로 저장해두었다가, 재귀함수 호출이 끝나고 집단을 발견하면 리스트에 저장한다.


> 통과한 코드

```python
import sys
read = sys.stdin.readline

n = int(read())

graph = []
village_count = 0
temp_count = 0
house_count = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
  # 인덱스 벗어나면 False
  if (x < 0 or x >= n) or (y < 0 or y >= n):
    return False
  # 현재 노드가 미방문이라면
  if graph[x][y] == 1:
    graph[x][y] = 0
    # house_count[village_count] += 1
    global temp_count
    temp_count += 1
    # 상하좌우 탐색
    for i in range(len(dx)):
      dfs(x + dx[i], y + dy[i])
    return True
  # 방문 노드라면 더이상 탐색하지 않는다
  return False
  
for i in range(n):
  graph.append(list(map(int, read().rstrip())))

for i in range(n):
  for j in range(n):
    if dfs(i, j):
      village_count += 1
      house_count.append(temp_count)
      temp_count = 0

house_count.sort()
print(village_count)
for count in house_count:
  print(count)
```


[#14052 연구소](https://www.acmicpc.net/problem/14502)

> 접근 방법

통과를 하긴 했는데 너무 비효율적인게 아닌지 당황스러운 문제.
감염 테스트는 가장 가까운 것부터 우선 탐색하는 것이 적합해보여 bfs를 사용했다.
원소가 2이면 거기서부터 bfs를 시작해서 상하좌우로 탐색, 0이면 감염시키고 1이거나 인덱스를 벗어나면 그쪽으로는 탐색하지 않는다.
bfs를 마치고 나면 그래프에 0인 곳이 남는데, 그 개수가 안전 지대의 개수이다.
그런데 문제에서 벽 3개를 세웠을 때 최대한의 안전 지대 개수를 구하라고 했다.
모든 벽의 조합에 대해 탐색해야할지, 가짓수를 쳐낼 수 있는 패턴이 있나 고민하다가 딱히 보이지 않아서 모든 조합에 대해 bfs를 반복했다.
벽의 조합에 대해 bfs할 때 그래프 값이 변경되므로, 처음 입력 받은 원본 배열을 보관하기 위해 깊은 복사 라이브러리를 사용했다.


> 통과한 코드

```python
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
```


[#7576 토마토](https://www.acmicpc.net/problem/7576)

> 접근 방법

익은 토마토와 인접한 토마토부터 익기 시작하므로, 가까운 노드부터 탐색하는 bfs를 사용한다.
bfs로 탐색은 하는데 일수는 도대체 어떻게 세야하는건지 모르겠어서 구글링의 힘을 빌렸다.
직전에 방문한 노드 값에 +1 해주면 되는거였음..! 시작은 익은 토마토에서 하니까 1, 2, ... 이렇게 증가한다.
bfs로 모든 탐색을 마친 후에는 행을 돌면서 가장 큰 값을 찾으면 되는 거였다.
해설을 보니 간단한데 막상 풀려니까 갈피를 못 잡았던 문제.

> 통과한 코드

```python
import sys
from collections import deque
read = sys.stdin.readline

m, n = map(int, read().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
queue = deque([(x, y) for x in range(n) for y in range (m) if graph[x][y] == 1])

def bfs():
  while queue:
    head = queue.popleft()
    x, y = head[0], head[1]
    # 상하좌우 탐색
    for direction in range(4):
      nx = x + dx[direction]
      ny = y + dy[direction]
      # 인덱스 벗어나면 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 벽이면 무시
      elif graph[nx][ny] == -1:
        continue
      # 익지 않은 토마토면 익힘
      elif graph[nx][ny] == 0:
        # 원래 방문한 토마토의 값(익은 날짜) + 1
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

bfs()
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      print(-1)
      exit(0)
  result = max(result, max(graph[i]))
print(result - 1)
```
