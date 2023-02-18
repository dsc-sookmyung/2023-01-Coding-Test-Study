# 04-DFS&BFS

 - 정리한 문제
 1. 2606 바이러스
 2. 2667 단지번호붙이기
 3. 7576 토마토
 4. 14502 연구소
 <br>

 ## 2606 바이러스

 ### 설명
 -  1번 컴퓨터와 연결된 컴퓨터의 수를 구하는 문제이다.
 - 양방향 그래프를 만들어 연결된 컴퓨터일 경우 DFS를 진행하여 수를 세준다.
 - "1번 컴퓨터를 통해" 바이러스에 걸리는 컴퓨터의 수이므로 개수에 1번 컴퓨터를 포함하지 않도록 주의한다.

```python
import sys
input = sys.stdin.readline
from collections import deque

computerNum = int(input())
edgeNum = int(input())

visit_dfs = [False] * (computerNum+1)

#양방향 그래프 만들기
edges = [[] for _ in range(computerNum+1)]
for i in range(edgeNum):
  v1, v2 = map(int,input().split())
  edges[v1].append(v2)
  edges[v2].append(v1)

result = 0
def dfs(x):
  global result
  visit_dfs[x] = True
  result += 1
  for i in edges[x]:
    if(visit_dfs[i] == False):
      dfs(i)

dfs(1)
#1번 컴퓨터의 수는 제외시켜줘야한다.
print(result-1)
```

 ## 2667 단지번호붙이기
 ### 설명
 - 정사각형 지도가 주어졌을 때 1로 연결된 단지의 수와 그 단지수를 출력하는 문제이다.
 - 정사각형 지도를 이중 for문으로 돌면서 1(집이 있는 곳)을 발견하면 그 위치부터 dfs를 시작해 연결된 집의 모임을 찾아준다. 이 때 개수도 같이 세준다.
 - dfs가 끝나면 연결된 집의 수를 다 센 것이므로 result 배열에 수를 더해준다.
 - dfs설명 => 해당 위치를 0으로 바꿔주고 위, 아래, 양 옆에 집이 있다면 dfs 재귀를 탄다. 이때 범위체크는 필수!( 인덱스 초과나지 않도록 범위가 넘지 않았는지 확인해준다.)

```python
import sys
input = sys.stdin.readline

dy = (1,0,-1,0)
dx = (0,1,0,-1)

N = int(input())
houses = [list(input().rstrip()) for _ in range(N)]
result = []

def dfs(y, x):
  global cnt
  houses[y][x] = '0'
  cnt += 1
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if(0<=ny<N and 0<=nx<N):
      if(houses[ny][nx] == '1'):
        dfs(ny, nx)

for i in range(N):
  for j in range(N):
    if(houses[i][j] == '1'):
      cnt = 0
      dfs(i, j)
      result.append(cnt)

result.sort()
print(len(result))
for i in result:
  print(i)
```

## 7576 토마토

 ### 풀이 설명
 - 익은 토마토(숫자 1)에서 연결된 토마토 중 안 익은 토마토(숫자 0)이면 익은 토마토의 영향을 받아 익는다.
 - 위 과정은 하루에 한 번, 인접한 토마토끼리 진행되기 때문에 bfs를 써서 풀이 하였다.
 - 처음 입력 받았을 때 토마토가 다 익었으면 0프린트 하고 종료, 아니면
 - 토마토 배열을 돌면서 익은 토마토가 있으면 해당 위치와 현재 며칠인지(여기서는 0번째 날이므로 0) 를 dp에 넣어준다.
 - 이제 본격적으로 bfs를 시작한다. 위, 아래, 양 옆에 안 익은 토마토가 있으면 익었다고 표시 후 day+1을 시켜 dq에 넣는다.
 - day를 셀 때 제일 큰 day를 계속해서 갱신해주는데, 이 값이 토마토가 다 익었을 때 최소 일수이다.
 - 바로 위 과정을 dp가 빌 때까지 진행하고 나면(= 토마토가 다 익고 나면) 토마토가 다 익었는지 확인해주고 다 익었다면 최소 일수를, 다 익지 않았다면 -1을 프린트 해준다.

### 코드 설명
- isEveryThingRipe() 토마토가 모두 익었는지 구하는 함수이다. 익지 않은 토마토는 숫자  0이므로 토마토 배열에서 숫자 0의 개수를 세었을 때 익지 않은 토마토의 개수가 0이면 모두 익은 것 이므로 True를 리턴한다.
- getMinDayWhenAllRipe() 토마토가 익을 수 있는 한 모두 익었을 경우 최소 날짜를 리턴해주는 함수이다. 익은 토마토를 dp에 넣고 bfs를 시작해준다. 이 때 위치와 함께 날짜를 넣어 며칠 차 인지 알 수 있도록 하고 day의 최대값을 계속해서 갱신해준다.
```python
import sys
input = sys.stdin.readline
from collections import deque

dy = (1,0,-1,0)
dx = (0,1,0,-1)

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]

def isEveryThingRipe():
  unRipeNum = 0
  for row in tomatos:
    unRipeNum += row.count(0)
  if(unRipeNum == 0):
    return True
  else:
    return False

def getMinDayWhenAllRipe():
  dq = deque()
  maxDay = 0
  for i in range(N):
    for j in range(M):
      if(tomatos[i][j] == 1):
        dq.append((i, j, 0))

  while(dq):
    y, x, day = dq.popleft()
    maxDay = max(maxDay, day)
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if(0<=ny<N and 0<=nx<M):
        if(tomatos[ny][nx] == 0):
          tomatos[ny][nx] = 1
          dq.append((ny, nx, day+1))

  return maxDay

if(isEveryThingRipe()):
  print(0)
else:
  minDay = getMinDayWhenAllRipe()
  if(isEveryThingRipe()):
    print(minDay)
  else:
    print(-1)

```

## 14502 연구소

 ### 풀이 설명
 - [0은 빈 칸, 1은 벽, 2는 바이러스], 벽은 빈칸에만 세울 수 있다.
 - 1️⃣ 벽 3개를 세우고(=> 1로 바꿔준다.)
 - 2️⃣ 바이러스가 퍼지도록 만들고(=>dfs를 이용해서 바이러스와 인접한 곳을 2로 바꿔준다.)
 - 3️⃣ 안전 영역을 세준다.(=> 0의 개수를 센다.)
 - 벽 3개를 세운 <span style='background-color: #fff5b1'>배열</span>에서 바이러스가 퍼지도록 만들 때 배열이 변하는데, 이 때 기존 벽 3개를 세웠던 <span style='background-color: #fff5b1'>배열</span>을 기억해줘야 한다.
 - 따라서 2️⃣, 3️⃣번 과정을 진행할 때 벽을 3개 세운 상태인 배열을 복사해서  tmp라는 배열을 만들고 이 tmp로 해당 과정을 진행하도록 하였다.

 ### 코드 설명
 - makeWall(count) => count는 세운 벽의 개수이다. 이중 for문으로 연구소 배열을 돌며 벽 3개를 세웠으면 2️⃣, 3️⃣과정을 진행해주는 checkSafeArea()함수 호출
 - checkSafeArea() => 배열을 tmp배열에 복사 후 tmp배열을 돌며 바이러스를 발견하면 bfs로 연결된 칸을 5(문제에 주어진 0, 1, 2가 아닌 수)로 바꿔준다. 다 돌았다면 안전 영역의 크기를 구해 최대값을 갱신해준다.
 - calSafeArea(tmp) => tmp배열의 안전 영역 크기를 계산해주는 함수로, 0의 개수를 센다.


```python
import sys
input = sys.stdin.readline
from collections import deque
import copy

dy = (1,0,-1,0)
dx = (0,1,0,-1)

def bfs(start_y, start_x, tmp):
  dq = deque()
  dq.append((start_y, start_x))
  while(dq):
    y, x = dq.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if(0<=nx<m and 0<=ny<n):
        if(tmp[ny][nx] == 0):
          dq.append((ny, nx))
          tmp[ny][nx] = 5

def calSafeArea(tmp):
  safe_area = 0
  for y in range(n):
    for x in range(m):
      if(tmp[y][x] == 0):
        safe_area += 1
  return safe_area

def checkSafeArea():
  global maxArea
  tmp = copy.deepcopy(field)
  for y in range(n):
    for x in range(m):
      if(tmp[y][x] == 2):
        bfs(y, x, tmp)
  maxArea = max(maxArea, calSafeArea(tmp))

def makeWall(count):
  if(count == 3):
    checkSafeArea()
    return
  else:
    for y in range(n):
      for x in range(m):
        if(field[y][x] == 0):
          field[y][x] = 1
          makeWall(count+1)
          field[y][x] = 0


n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

maxArea = 0
tmp = [[0] * m for _ in range(n)]

makeWall(0)
print(maxArea)
```
