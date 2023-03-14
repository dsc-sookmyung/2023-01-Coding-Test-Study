import sys

read = sys.stdin.readline

n = int(read())
alist = list(map(int, read().split()))
dp = [0] * n
dp[0] = alist[0]

for i in range(1, n):
    for j in range(i):
        if alist[j] < alist[i]:
            dp[i] = max(dp[j] + alist[i], dp[i])
        else:
            dp[i] = max(alist[i], dp[i])

print(max(dp))
