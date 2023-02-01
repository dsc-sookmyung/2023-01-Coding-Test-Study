import sys

n = int(input())
P = {}
for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    if l in P:
        P[l].append(p)
    else:
        P[l] = [p]

m = int(input())
for _ in range(m):
    c = list(sys.stdin.readline().split())
    new_P = {key: value for key, value in P.items() if len(value) != 0}
    if c[0] == 'solved':
        for k, v in P.items():
            if int(c[1]) in v:
                P[k].remove(int(c[1]))
    elif c[0] == 'add':
        if int(c[2]) in P:
            P[int(c[2])].append(int(c[1]))
        else:
            P[int(c[2])] = [int(c[1])]
    else:
        if c[1] == '1':
            print(max(new_P[max(new_P)]))
        else:
            print(min(new_P[min(new_P)]))

"""
pypy3를 통해 통과
힙을 사용해야 python으로 통과 할거같다
"""