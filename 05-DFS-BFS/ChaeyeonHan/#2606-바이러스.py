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