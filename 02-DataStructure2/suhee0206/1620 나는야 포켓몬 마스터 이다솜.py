import sys

N, M = map(int, sys.stdin.readline().split())
read = sys.stdin.readline
pocketmon_by_number = {(i+1): read().rstrip() for i in range(N)}
pocketmon_by_name = {name: number for number, name in pocketmon_by_number.items()}
for _ in range(M):
  problem = sys.stdin.readline().rstrip()
  if ord(problem[0]) >= 48 and ord(problem[0]) <= 57:	# ascii code
    print(pocketmon_by_number[int(problem)])
  else:
    print(pocketmon_by_name[problem])