# 문제 조건 : 모든 로프를 사용할 필요는 없다!! 확인 잘 해주기
import sys
input = sys.stdin.readline

N = int(input())
weight = []
for _ in range(N):
    weight.append(int(input()))
weight.sort()

nums = []
for i in weight:
    nums.append(i*N)
    N -= 1
print(max(nums))