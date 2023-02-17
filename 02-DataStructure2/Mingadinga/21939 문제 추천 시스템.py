import sys
import heapq

read = sys.stdin.readline
n = int(read())
min_heap = []
max_heap = []
problems = {}

for _ in range(n):
  prob_number, diff = map(int, read().split())
  heapq.heappush(min_heap, (diff, prob_number))
  heapq.heappush(max_heap, (-diff, prob_number))
  problems[prob_number] = True

m = int(read())
for _ in range(m):
  commands = list(read().split())
  print(commands)
  if commands[0][0] == "a":
    prob_number, diff = int(commands[1]), int(commands[2])
    while not problems[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while not problems[min_heap[0][1]]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, (diff, prob_number))
    heapq.heappush(max_heap, (-diff, prob_number))
    problems[prob_number] = True

  elif commands[0][0] == "s":
    prob_number = int(commands[1])
    problems[prob_number] = False

  elif commands[0][0] == "r":
    if commands[1] == "1":
      while not problems[max_heap[0][1]]:
        heapq.heappop(max_heap)
      print(max_heap[0][1])
    elif commands[1] == "-1":
      while not problems[min_heap[0][1]]:
        heapq.heappop(min_heap)
      print(min_heap[0][1])
      print(min_heap[0][1])