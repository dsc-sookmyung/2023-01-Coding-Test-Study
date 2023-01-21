import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
deque = deque(i+1 for i in range(n))
result = []

while(deque):
  deque.rotate(-(k-1))
  result.append(deque.popleft())

print("<%s>"%", ".join(map(str, result)))