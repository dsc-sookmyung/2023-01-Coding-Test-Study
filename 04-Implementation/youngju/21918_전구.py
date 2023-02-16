import sys

n, m = map(int, sys.stdin.readline().split())
stateList = list(map(int, sys.stdin.readline().strip().split()))

for _ in range(m):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        stateList[command[1] - 1] = command[2]
    elif command[0] == 2:
        for i in range(command[2] - command[1] + 1):
            stateList[command[1] - 1 + i] = (lambda x: 1 if x == 0 else 0)(stateList[command[1] - 1 + i])
    elif command[0] == 3:
        for i in range(command[2] - command[1] + 1):
            stateList[command[1] - 1 + i] = 0
    else:
        for i in range(command[2] - command[1] + 1):
            stateList[command[1] - 1 + i] = 1

print(*stateList)
