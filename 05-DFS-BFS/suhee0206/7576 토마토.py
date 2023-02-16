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