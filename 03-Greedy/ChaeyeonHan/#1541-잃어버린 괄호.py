import sys
input = sys.stdin.readline

cal = input().rstrip().split('-')  # input을 받을 때 -를 기준으로 split()해준다
num = []

for i in cal:
    tmp = i.split('+')
    sum = 0
    for j in tmp:
        sum += int(j)
    num.append(sum)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)

