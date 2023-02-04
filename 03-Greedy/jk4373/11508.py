#11508 2+1 세일
import sys
n = int(input())
lst = []

for _ in range(n):
    m = int(sys.stdin.readline())
    lst.append(m)
# lst.sort()
# etc = len(lst) % 3
# sum=0
# for i in range(etc):
#     sum = sum + lst[i]
#     del lst[i]
lst.sort(reverse= True)
sum =0
for i in range(len(lst)):
    if (i+1) %3:
        sum = sum + lst[i]
print(sum)