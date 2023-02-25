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