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