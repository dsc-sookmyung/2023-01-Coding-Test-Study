import sys
input = sys.stdin.readline
from collections import deque

computerNum = int(input())
edgeNum = int(input())

visit_dfs = [False] * (computerNum+1)

#양방향 그래프 만들기
edges = [[] for _ in range(computerNum+1)]
for i in range(edgeNum):
  v1, v2 = map(int,input().split())
  edges[v1].append(v2)
  edges[v2].append(v1)

result = 0
def dfs(x):
  global result
  visit_dfs[x] = True
  result += 1
  for i in edges[x]:
    if(visit_dfs[i] == False):
      dfs(i)
   
dfs(1)
#1번 컴퓨터의 수는 제외시켜줘야한다.
print(result-1)