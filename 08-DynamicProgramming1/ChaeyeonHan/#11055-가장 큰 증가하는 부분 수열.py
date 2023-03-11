import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [i for i in nums]

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])
print(max(dp))