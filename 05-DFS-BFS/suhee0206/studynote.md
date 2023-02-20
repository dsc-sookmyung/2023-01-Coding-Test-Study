# DFS/BFS

## 목차

- **개념**
  - 선행 개념
    - [스택과 큐](#스택과-큐)
    - [재귀 함수](#재귀-함수)
  - [DFS와 BFS](#DFS와-BFS)
    - [DFS](#DFS)
    - [BFS](#BFS)
- **문제**
  - [2606 바이러스](#2606-바이러스)
  - [2667 단지번호 붙이기](#2667-단지번호-붙이기)
  - [7576 토마토](#7576-토마토)
  - [14502 연구소](#14502-연구소)




## 개념

> 다음은 [이것이 취업을 위한 코딩테스트다 with 파이썬](http://www.yes24.com/Product/Goods/91433923)에서 발췌한 내용입니다.

### 스택과 큐

탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미한다.

대표적인 탐색 알고리즘으로 DFS와 BFS를 꼽을 수 있는데, DFS와 BFS를 제대로 이해하려면 기본 자료구조인 스택과 큐에 대한 이해가 전제되어야 한다.

스택과 큐 설명은 [Stack, Queue, Deque 스터디 노트](../../01-DataStructure1/suhee0206/studynote.md)를 참고하자.

### 재귀 함수

DFS와 BFS를 구현하려면 재귀 함수도 이해하고 있어야 한다. **재귀 함수(Recursive Function)**란 자기 자신을 다시 호출하는 함수를 의미한다.

```python
# 재귀 함수 예제
def recursive_function():
	print('재귀 함수를 호출합니다.')
	recursive_function()

recursive_function()
```

#### 재귀 함수의 종료 조건

재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시해야 한다. 자칫 종료 조건을 명시하지 않으면 함수가 무한 호출될 수 있다.

컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다. 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문이다. 따라서 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다. DFS가 대표적인 예다.

재귀 함수를 이용하는 대표적 예제로는 팩토리얼 문제가 있다. 팩토리얼 기호는 느낌표(!)를 사용하며 n!는 1 x 2 x 3 x ... x (n-1) x n을 의미한다. 팩토리얼 함수는 n이 1이하가 되었을 때 함수를 종료하는 재귀 함수의 형태로 구현할 수 있다.

```python
# 반복문으로 구현한 n!
def factorial_iterative(n):
	result = 1
  # 1부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n+1):
    result *= i
   return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1:	# n이 1이하인 경우 1을 반환
    return 1
 	# n! = n * (n-1)!를 그대로 코드로 작성하기
  retun n * factorial_recursive(n-1)
```

재귀 함수의 소스코드는 점화식과 매우 닮아있으며, 반복문을 이용하는 것과 비교했을 때 더욱 간결한 형태다. 

### DFS와 BFS

|               | DFS            | BFS               |
| ------------- | -------------- | ----------------- |
| **동작 원리** | 스택           | 큐                |
| **구현 방법** | 재귀 함수 이용 | 큐 자료 구조 이용 |

DFS와 BFS는 그래프를 탐색하는 알고리즘이며, 그래프는 크게 2가지 방식으로 표현할 수 있다.

- 인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식

  ```python
  INF = 999999999 # 무한의 비용 선언
  
  # 2차원 리스트를 이용해 인접 행렬 표현
  graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
  ]
  ```

- 인접 리스트(Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식

  ```python
  # 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
  graph = [[] for _ in range(3)]
  
  # 노드 0에 연결된 노드 정보 저장(노드, 거리)
  graph[0].append((1, 7))
  graph[0].append((2, 5))
  
  # 노드 1에 연결된 노드 정보 저장(노드, 거리)
  graph[1].append((0, 7))
  
  # 노드 2에 연결된 노드 정보 저장(노드, 거리)
  graph[2].append((0, 5))
  ```

### DFS

DFS는 Depth-First-Search, 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

DFS는 스택 자료구조를 이용하는 알고리즘이기 때문에 재귀 함수를 이용했을 때 매우 간결하게 구현할 수 있다.

탐색을 수행할 때 데이터의 개수가 N개인 경우 `O(N)`의 시간이 소요된다는 특징이 있다. 

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

### BFS

BFS는 Breadth First Search, 너비 우선 탐색이라는 의미를 가지며, 가까운 노드부터 탐색하는 알고리즘이다. 

BFS 구현에서는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 된다. 

실제로 구현함에 있어 `deque` 라이브러리를 사용하는 것이 좋으며 탐색을 수행함에 있어 `O(N)`의 시간이 소요된다. 

일반적인 경우 실제 수행 시간은 DFS보다 좋은 편이다.

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```



## 문제

### [2606 바이러스](https://www.acmicpc.net/problem/2606)

문제) 1번 노드(컴퓨터)와 연결된 노드의 개수를 구하라. 

분류) **dfs**/bfs

해설) 인접 리스트를 이용하여 연결된 컴퓨터를 그래프로 표현한다. dfs나 bfs를 이용해서, 1번 노드에서 출발하여 방문한 노드의 개수를 구한다.

메모) 그래프로 표현할 때, 단방향이 아니라 **양방향**으로 표현해야 한다!!! `graph[a].append(b)` 뿐만 아니라, `graph[b].append(a)`도 해줘야 한다.

예를 들어 (9 1) 쌍이 들어왔을 때, `graph[9].append([1])`만 하게 된다면, 1번 노드 입장에서는 9번 노드가 연결되어있다는 사실을 모른다! 따라서 `graph[1].append(9)`도 해줘야 한다. 

```python
import sys

def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited);

read = sys.stdin.readline
n = int(read())
m = int(read())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, read().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)

dfs(graph, 1, visited)

print(len([x for x in visited if x == True]) - 1)
```



### [2667 단지번호 붙이기](https://www.acmicpc.net/problem/2667)

문제) 연결된 집의 모임인 단지의 개수와, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하라. 

분류) **dfs**/bfs

해설) NxN 배열의 원소가 1인 경우, dfs를 통해 연결된 집의 개수를 센다. 방문한 집은 0으로 값을 변경해주고, count를 한 개 증가시킨다. 연결된 집을 다 셌다면, 집의 수를 배열에 저장하고 또 NxN 배열에서 1인 원소를 찾아 dfs를 반복한다. 배열에는 각 단지에 속하는 집의 수가 저장되어 있으므로, 배열의 길이가 곧 단지수다. 각 단지의 속하는 집의 수를 오름차순으로 정렬해야 하므로, `sort()`를 이용해 배열을 정렬한다. 

```python
import sys

count = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(graph, x, y):
  global count
  graph[x][y] = 0
  count += 1
  for k in range(4):
    i = x+dx[k]
    j = y+dy[k]
    if i >= 0 and i < n and j >=0 and j < n and graph[i][j] == 1:
      dfs(graph, i, j)

read = sys.stdin.readline
n = int(read())

graph = []
for i in range(n):
  graph.append(list(map(int, list(read().rstrip()))))

answer = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      count = 0
      dfs(graph, i, j)
      answer.append(count)

answer.sort()
num = len(answer)

print(num)
for i in range(num):
  print(answer[i])
```



### [7576 토마토](https://www.acmicpc.net/problem/7576)

문제) 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하라. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력하고, 토마토가 모두 익지 못하는 상황이면 1을 출력하라. 

분류) dfs/**bfs**

해설) 익은 토마토에서 안 익은 토마토까지 도달하는 최소 거리를 구하면 된다.

1. 시작 노드(주어진 익은 토마토, 값=1)를 찾아서 그 위치를 모두 큐에 넣는다. 
2. 창고를 탐색하면서 익지 않은 토마토(값=0)가 나오면, 이전 노드로부터 1만큼 더한 거리를 저장한다. 첫 번째 시작 노드로부터 갈 수 있는 모든 토마토를 다 익힌 후에, 그 다음 시작 노드가 익힐 수 있는 토마토를 계산한다. 이미 익은 토마토인 경우, 현재 시작 노드로부터의 거리가 이전에 저장된 거리보다 더 짧다면, 현재 거리 값을 갱신한다. 이 과정을 반복하면 가능한 거리가 모두 계산이 된다. 
3. 이제 창고를 탐색하면서 0이 하나라도 나오면, 토마토가 모두 익지 못하는 상황이므로 -1을 출력하고, 아니라면 가장 먼 거리를 출력한다. 

메모1) 주어진 익은 토마토가 여러 개일 수 있다! 시작 노드가 한 개라고 가정하고 풀면 안된다. *Cf. 예제 입력 3*

메모2) 여러 개의 시작 노드에 대해 for 문을 돌려가며 bfs를 시작 노드 개수만큼 실행하면 **시간 초과**가 발생한다. 큐에 여러 개의 시작 노드를 모두 넣은 후에, bfs를 한 번만 수행해야 한다!

메모3) `dfs`가 아니라 `bfs`를 사용하기 때문에, 한 토마토가 도달할 수 있는 토마토를 모두 익힌 후에 다음 토마토가 가능한 모두 토마토를 익히는 방식이 아니다! (Cf. queue를 출력해보면 작동 방식을 알 수 있다.) 따라서 `graph[i][j] > graph[v[0]][v[1]] + 1` 은 필요 없는 코드다. 

```python
import sys
from collections import deque
  
read = sys.stdin.readline
M, N = map(int, read().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, read().split())))    

queue = deque([])

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      queue.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]  

while queue:
  v = queue.popleft()
  for k in range(4):
    i = v[0] + dx[k]
    j = v[1] + dy[k]
    if i >= 0 and i < N and j >=0 and j < M and (graph[i][j] == 0 or graph[i][j] > graph[v[0]][v[1]] + 1):
      graph[i][j] = graph[v[0]][v[1]] + 1
      queue.append((i, j))
  
answer = 0
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      answer = -1
      break
    elif graph[i][j] > 0:
      answer = max(answer, graph[i][j])
  if answer == -1:
    break

if answer == -1:
  print(answer)
else:
  print(answer - 1)
```



### [14502 연구소](https://www.acmicpc.net/problem/14502)

문제) 크기가 NxM인 직사각형 연구소에 빈 칸(0), 벽(1), 바이러스(2)가 존재한다. 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있고, 바이러스의 확산을 막기 위해 벽을 3개 세우려고 한다. 벽 3개를 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하라. 

분류) 구현, **bfs**/dfs, 완전탐색

해설) 시간 제한이 2초고, (3 <= N, M <= 8) 이므로 완전 탐색을 시도해본다! 벽 3개를 가능한 모든 경우의 수로 세운다. 모든 경우의 수에 대해 바이러스를 퍼뜨리고 안전 영역을 구해본다. 바이러스는 bfs를 이용해 퍼뜨리고, 안전 영역은 for 문을 돌면서 0의 개수를 세서 구한다. 안전 영역 크기가 가장 큰 값을 갖도록 값을 갱신해준다. 

메모) 온라인 에디터로 코드를 실행했을 때는 매우 오래 걸렸으나, 백준에서 실행했을 때는 무사 통과했다! 일단 코드를 작성했다면, 제출해보자! 

```python
import sys
from collections import deque
import copy
  
read = sys.stdin.readline
N, M = map(int, read().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, read().split())))   

queue = deque([])

for i in range(N):
  for j in range(M):
    if graph[i][j] == 2:
      queue.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]  

def bfs(g, q):
  virus = copy.deepcopy(g)
  while q:
    v = q.popleft()
    for k in range(4):
      i = v[0] + dx[k]
      j = v[1] + dy[k]
      if i >= 0 and i < N and j >=0 and j < M and virus[i][j] == 0:
        virus[i][j] = 2
        q.append((i, j))
  count = 0
  for x in range(N):
    for y in range(M):
      if virus[x][y] == 0:
        count += 1
  return count

answer = 0
for i in range(N):
  for j in range(M):
    walls = 3
    g = copy.deepcopy(graph)
    if g[i][j] == 0:
      walls -= 1
      g[i][j] = 1
      for ii in range(N):
        for jj in range(M):
          if g[ii][jj] == 0:
            walls -= 1
            g[ii][jj] = 1
            for iii in range(N):
              for jjj in range(M):
                if g[iii][jjj] == 0:
                  walls -= 1
                  g[iii][jjj] = 1
                  if walls == 0:
                    q = copy.deepcopy(queue)
                    answer = max(bfs(g, q), answer)
                    g[iii][jjj] = 0
                    walls += 1
            g[ii][jj] = 0
            walls += 1
      g[i][j] = 0
      walls += 1
      
print(answer)
```

