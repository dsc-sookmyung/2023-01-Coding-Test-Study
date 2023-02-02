import sys

read = sys.stdin.readline

N = int(read())
C = [int(read()) for _ in range(N)]
C.sort(reverse=True)

answer = 0
for i in range(N):
  if (i+1) % 3 == 0:
    pass
  else:
    answer = answer + C[i]

print(answer)