import sys

N = int(sys.stdin.readline())
D =[0,1,2]
for i in range(3,N+1):
     D.append(D[i - 2] + D[i - 1])
     D[i] = D[i] %10007

print(D[N])
