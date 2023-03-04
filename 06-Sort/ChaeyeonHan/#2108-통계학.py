import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()

def average(nums):
    total = sum(nums)
    return round(total/len(nums))

def middle(nums):
    return nums[int(N/2)]

def freq(nums):
    dic = dict()
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    dic = list(dic)
    if len(dic) == 1 or dic[0][1] != dic[1][1]:
        print(dic[0][0])
    else:
        print(dic[1][0])

def range(nums):
    return nums[len(nums)-1] - nums[0]

print(average(nums))
print(middle(nums))
freq(nums)
print(range(nums))