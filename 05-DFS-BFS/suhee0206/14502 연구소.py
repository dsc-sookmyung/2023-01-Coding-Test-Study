import sys
from collections import deque
import copy
  
read = sys.stdin.readline
N, M = map(int, read().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, read().split())))   

queue = deque([])

for i in range(N):
  for j in range(M):
    if graph[i][j] == 2:
      queue.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]  

def bfs(g, q):
  virus = copy.deepcopy(g)
  while q:
    v = q.popleft()
    for k in range(4):
      i = v[0] + dx[k]
      j = v[1] + dy[k]
      if i >= 0 and i < N and j >=0 and j < M and virus[i][j] == 0:
        virus[i][j] = 2
        q.append((i, j))
  count = 0
  for x in range(N):
    for y in range(M):
      if virus[x][y] == 0:
        count += 1
  return count

answer = 0
for i in range(N):
  for j in range(M):
    walls = 3
    g = copy.deepcopy(graph)
    if g[i][j] == 0:
      walls -= 1
      g[i][j] = 1
      for ii in range(N):
        for jj in range(M):
          if g[ii][jj] == 0:
            walls -= 1
            g[ii][jj] = 1
            for iii in range(N):
              for jjj in range(M):
                if g[iii][jjj] == 0:
                  walls -= 1
                  g[iii][jjj] = 1
                  if walls == 0:
                    q = copy.deepcopy(queue)
                    answer = max(bfs(g, q), answer)
                    g[iii][jjj] = 0
                    walls += 1
            g[ii][jj] = 0
            walls += 1
      g[i][j] = 0
      walls += 1
      
print(answer)