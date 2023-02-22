import sys
input = sys.stdin.readline
from collections import deque

dy = (1,0,-1,0)
dx = (0,1,0,-1)

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]

def isEveryThingRipe():
  unRipeNum = 0
  for row in tomatos:
    unRipeNum += row.count(0)
  if(unRipeNum == 0):
    return True
  else:
    return False

def getMinDayWhenAllRipe():
  dq = deque()
  maxDay = 0
  for i in range(N):
    for j in range(M):
      if(tomatos[i][j] == 1):
        dq.append((i, j, 0))

  while(dq):
    y, x, day = dq.popleft()
    maxDay = max(maxDay, day)
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if(0<=ny<N and 0<=nx<M):
        if(tomatos[ny][nx] == 0):
          tomatos[ny][nx] = 1
          dq.append((ny, nx, day+1))

  return maxDay
      
if(isEveryThingRipe()):
  print(0)
else:
  minDay = getMinDayWhenAllRipe()
  if(isEveryThingRipe()):
    print(minDay)
  else:
    print(-1)