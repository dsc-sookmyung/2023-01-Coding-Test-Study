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