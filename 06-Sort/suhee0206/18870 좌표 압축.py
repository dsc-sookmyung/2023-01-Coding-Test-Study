import sys

read = sys.stdin.readline
N = int(read())

x_list = list(map(int, read().split()))

sorted_x_list = sorted(set(x_list))
dict = dict()
for i in range(len(sorted_x_list)):
  dict[sorted_x_list[i]] = i

for x in x_list:
  print(dict[x], end=' ')