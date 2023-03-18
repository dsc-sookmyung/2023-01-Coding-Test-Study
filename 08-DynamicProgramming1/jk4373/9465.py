import sys

T = int(input())

for i in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    if N> 1:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
    for j in range(2,N):
        arr[0][j] += max(arr[1][j-1],arr[1][j-2])
        arr[1][j] += max(arr[0][j-1],arr[0][j-2])
    print(max(arr[0][N-1],arr[1][N-1]))
