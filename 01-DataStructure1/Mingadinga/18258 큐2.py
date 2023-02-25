import sys
from collections import deque

read = sys.stdin.readline

queue = deque()
n = int(read())

for _ in range(n):
    command = read().rstrip()
    if command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "p":
        push, item = map(str, command.split())
        queue.append(item)
    elif command[0] == "f":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "b":
        if queue:
            print(queue[len(queue) - 1])
        else:
            print(-1)
    elif command[0] == "s":
        print(len(queue))
    elif command[0] == "e":
        print(1 if len(queue) == 0 else 0)
