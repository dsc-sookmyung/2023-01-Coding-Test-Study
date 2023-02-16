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