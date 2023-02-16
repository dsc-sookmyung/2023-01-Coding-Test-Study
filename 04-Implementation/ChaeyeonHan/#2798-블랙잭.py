import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
max_n = 0

nums.sort()
for i in range(N-1, 1, -1):
    for j in range(i-1, 0, -1):
        for k in range(j-1, -1, -1):
            # print(i, j, k)
            sum = nums[i] + nums[j] + nums[k]
            if sum <= M and max_n < sum:
                max_n = sum  # sum값 갱신
print(max_n)