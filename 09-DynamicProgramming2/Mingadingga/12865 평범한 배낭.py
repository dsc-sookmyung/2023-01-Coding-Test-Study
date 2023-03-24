import sys
read = sys.stdin.readline

N, K = map(int, read().split())
cache = [0] * (K+1)

for _ in range(N):
    w, v = map(int, read().split())
    for j in range(K, w-1, -1):
        cache[j] = max(cache[j], cache[j-w] + v)
print(cache[-1])