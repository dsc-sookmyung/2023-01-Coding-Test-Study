# 14916 거스름돈

n = int(input())
count = 0

for i in range(n):
    rest = n - 5*i
    if rest % 2 ==0 and rest >=0:
        temp = i + rest //2
        if temp < count or count ==0:
            count = temp 
if count ==0:
    print(-1)
else:
    print(count)