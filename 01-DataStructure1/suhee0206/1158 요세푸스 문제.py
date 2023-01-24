import sys

read = sys.stdin.readline
N, K = map(int, read().split())

circular_list = []
josephus = []

for i in range(1, N+1):
  circular_list.append(i)

num = 0
while len(circular_list):
  num = (num+K-1) % len(circular_list)
  val = circular_list.pop(num)
  josephus.append(val)
  
print('<', end='')
print(', '.join(str(item) for item in josephus), end='')
print('>')