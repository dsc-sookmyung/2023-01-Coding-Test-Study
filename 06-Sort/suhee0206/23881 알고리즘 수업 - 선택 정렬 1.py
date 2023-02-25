import sys

read = sys.stdin.readline
N, K = map(int, read().split())
A = list(map(int, read().split()))

# A의 마지막 인덱스부터 1번째 인덱스(두 번째 수)까지 반복
for i in range(len(A)-1, 0, -1):
  max_index = i
  max_index = A.index(max(A[:i+1]))
  if i != max_index:
    K = K-1
    A[i], A[max_index] = A[max_index], A[i]
  if K==0:
    print(A[max_index], A[i])
    break
if K:
  print(-1)