import sys
# queue
from collections import deque

T = int(input())

for _ in range(T):
    n,m = map(int, input().split())
    data = deque(list(map(int,sys.stdin.readline().split())))
    idx = 0

    while data:
        tmp = data.popleft()
        m -=1
        if tmp ==max(data):
            idx +=1
            if m < 0:
                print(idx)
                break
        else:
            data.append(tmp)
            if m<0:
                m = len(data) -1