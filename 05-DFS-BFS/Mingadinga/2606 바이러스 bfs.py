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