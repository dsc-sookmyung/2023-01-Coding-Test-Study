import sys
import heapq

min_heap = []
max_heap = []
d = {}

def recommend(x):
  global min_heap, max_heap
  if x==1:		# max(가장 어려운 문제의 번호)
    while (-1)*max_heap[0][0] != d[(-1)*max_heap[0][1]]:
      heapq.heappop(max_heap)
    print((-1)*max_heap[0][1])
  elif x==-1:	# min(가장 쉬운 문제의 번호)
    while min_heap[0][0] != d[min_heap[0][1]]:
      heapq.heappop(min_heap)
    print(min_heap[0][1])
          
def add(p, l):
  global min_heap, max_heap
  heapq.heappush(min_heap, (l, p))
  heapq.heappush(max_heap, ((-1)*l, (-1)*p))
  d[p] = l

def solved(p):
  d[p] = 0

read = sys.stdin.readline
N = int(read())
for _ in range(N):
  P, L = map(int, read().split())
  heapq.heappush(min_heap, (L, P))
  heapq.heappush(max_heap, ((-1)*L, (-1)*P))
  d[P] = L

M = int(read())
for _ in range(M):
  command = read().split()
  if command[0] == "recommend":
    recommend(int(command[1]))
  elif command[0] == "add":
    add(int(command[1]), int(command[2]))
  elif command[0] == "solved":
    solved(int(command[1]))