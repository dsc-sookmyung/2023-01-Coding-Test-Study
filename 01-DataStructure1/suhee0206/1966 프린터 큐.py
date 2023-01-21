import sys
from collections import deque

T = int(sys.stdin.readline())
while T:
  order = []	# 인쇄 순서 저장
  
  N, M = map(int, sys.stdin.readline().split())
  
  deq = deque(list(map(int, sys.stdin.readline().split())))
  for i in range(len(deq)):
    deq[i] = [deq[i], i]

  while len(deq):
    if max(deq)[0] > deq[0][0]:
      deq.append(deq.popleft())
    else:
      order.append(deq.popleft())

  for i in range(N):
    if order[i][1] == M:
      print(i+1)
      break
  
  T = T-1