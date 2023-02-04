import sys

n = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().strip().split()))
oil = list(map(int, sys.stdin.readline().strip().split()))

answer = road[0] * oil[0]
oil_min = oil[0]
for i in range(1, n-1):
    if oil[i] <= oil_min:
        oil_min = oil[i]
    answer += oil_min * road[i]

print(answer)


