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