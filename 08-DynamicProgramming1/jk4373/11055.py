import sys


N = int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))

D=[1]*N
D[0]=arr[0]
for i in range(1,N):
  for j in range(i):
    if arr[j]<arr[i]:
      D[i]=max(D[i], D[j]+arr[i])
    else:
      D[i]=max(D[i], arr[i])

print(max(D))