from collections import deque

while True:
    try:
        s, t = input().split()

        sq = deque(list(s))

        for i in t:
            if sq and sq[0] == i:
                sq.popleft()

        if sq:
            print("No")
        else:
            print("Yes")
    except:
        break