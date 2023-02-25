import sys

read = sys.stdin.readline
N = int(read())

members = []

for i in range(N):
  age, name = read().split()
  members.append([int(age), name, i])	# i는 가입한 순서 정보

sorted_members = sorted(members, key = lambda x: (x[0], x[2]))

for x in sorted_members:
  print(x[0], x[1])