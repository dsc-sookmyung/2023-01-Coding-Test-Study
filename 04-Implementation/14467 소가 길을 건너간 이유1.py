import sys

read = sys.stdin.readline

look_count = int(read())
look_results = {}

result = 0
for i in range(look_count):
  cow, position = map(int, read().split())
  if cow not in look_results.keys():
    look_results[cow] = position
  elif look_results[cow] != position:
    result += 1
    look_results[cow] = position

print(result)