import sys
input = sys.stdin.readline

dy = (1,0,-1,0)
dx = (0,1,0,-1)

N = int(input())
houses = [list(input().rstrip()) for _ in range(N)]
result = []

def dfs(y, x):
  global cnt
  houses[y][x] = '0'
  cnt += 1
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if(0<=ny<N and 0<=nx<N):
      if(houses[ny][nx] == '1'):
        dfs(ny, nx)

for i in range(N):
  for j in range(N):
    if(houses[i][j] == '1'):
      cnt = 0
      dfs(i, j)
      result.append(cnt)

result.sort()
print(len(result))
for i in result:
  print(i)