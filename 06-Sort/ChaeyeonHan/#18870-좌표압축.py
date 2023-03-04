import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(list(set(nums)))

dict = {sorted_nums[i]: i for i in range(len(sorted_nums))}
# print(dict)

for i in nums:
    print(dict[i], end=' ')