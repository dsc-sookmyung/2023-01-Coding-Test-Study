import sys
read = sys.stdin.readline

n = int(read())
age_name_list = []
result = []

for i in range(n):
  age, name = map(str, read().split())
  age_name_list.append((int(age), name, i))

result = sorted(age_name_list, key = lambda x:(x[0], x[2]))

for name_score in result:
  print(name_score[0], name_score[1])