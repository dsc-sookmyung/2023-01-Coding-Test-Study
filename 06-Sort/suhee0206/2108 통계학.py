import sys
import math
from collections import Counter

read = sys.stdin.readline
N = int(read())

numbers = []
for _ in range(N):
  numbers.append(int(read()))

def mean(array):
  return round(sum(array) / len(array))

def median(array):
  array.sort()
  return array[int(len(array) / 2)]

def mode(array):
  array.sort()
  counter = Counter(array)
  two_modes = counter.most_common(2)
  if len(two_modes) == 2 and two_modes[0][1] == two_modes[1][1]:
    return two_modes[1][0]
  else:
    return two_modes[0][0]

def sub_max_min(array):
  return max(array) - min(array)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(sub_max_min(numbers))