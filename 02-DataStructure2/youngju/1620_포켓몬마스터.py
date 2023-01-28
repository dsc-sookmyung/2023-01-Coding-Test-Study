import sys

n, m = map(int, input().split())
data = {}
for i in range(n):
    data[i] = sys.stdin.readline().strip()

re_data = dict(map(reversed, data.items()))
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(data[int(q) - 1])
    else:
        print(re_data[q] + 1)

