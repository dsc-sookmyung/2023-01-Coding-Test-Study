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