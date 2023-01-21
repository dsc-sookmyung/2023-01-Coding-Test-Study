import sys
input = sys.stdin.readline
from collections import deque

testcaseNum = int(input())

for _ in range(testcaseNum):
  n, m = map(int, input().split())
  dq = deque([i for i in range(n)])
  importance = list(map(int, input().split()))
  count = 0
  while(dq):
    index = dq.popleft()
    if(importance[index] == max(importance)):
      importance[index] = 0
      count += 1
      if(index == m):
        print(count)
        break
    else:
      dq.append(index)