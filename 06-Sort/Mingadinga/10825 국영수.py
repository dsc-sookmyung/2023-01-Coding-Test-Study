import sys
read = sys.stdin.readline

n = int(read())
name_score_list = []
result = []

for _ in range(n):
  name, korean, english, math = map(str, read().split())
  name_score_list.append((name, int(korean), int(english), int(math)))

result = sorted(name_score_list, key = lambda x:(-x[1], x[2], -x[3], x[0]))

for name_score in result:
  print(name_score[0])