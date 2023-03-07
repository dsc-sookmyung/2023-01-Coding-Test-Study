import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())  # 예산
start, end = 0, max(nums)
# 예산 index를 기준으로 잡고 탐색할지, 예산 값을 기준으로 탐색할지

# 이진탐색으로 0~m까지의 수에서 상한액찾기
while start <= end:
    mid = (start + end)//2
    total = 0
    for i in nums:
        if i >= mid:  # 상한액 초과
            total += mid
        else:
            total += i
    if total <= m:
        start = mid+1
    else:
        end = mid-1
print(end)