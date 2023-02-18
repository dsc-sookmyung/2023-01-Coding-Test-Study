import sys
input = sys.stdin.readline
from collections import deque
import copy

dy = (1,0,-1,0)
dx = (0,1,0,-1)

def bfs(start_y, start_x, tmp):
  dq = deque()
  dq.append((start_y, start_x))
  while(dq):
    y, x = dq.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if(0<=nx<m and 0<=ny<n):
        if(tmp[ny][nx] == 0):
          dq.append((ny, nx))
          tmp[ny][nx] = 5

def calSafeArea(tmp):
  safe_area = 0
  for y in range(n):
    for x in range(m):
      if(tmp[y][x] == 0):
        safe_area += 1
  return safe_area

def checkSafeArea():
  global maxArea
  tmp = copy.deepcopy(field)
  for y in range(n):
    for x in range(m):
      if(tmp[y][x] == 2):
        bfs(y, x, tmp)
  maxArea = max(maxArea, calSafeArea(tmp))
   
def makeWall(count):
  if(count == 3):
    checkSafeArea()
    return
  else:
    for y in range(n):
      for x in range(m):
        if(field[y][x] == 0):
          field[y][x] = 1
          makeWall(count+1)
          field[y][x] = 0


n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

maxArea = 0
tmp = [[0] * m for _ in range(n)]

makeWall(0)
print(maxArea)