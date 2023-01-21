n, k = map(int,input().split())

a = []
for i in range(1,n+1):
     a.append(i)
res = []
num = k-1
for i in range(n):
    if len(a)> num:
        res.append(a.pop(num))
        num += k-1
    elif len(a) <= num:
        num = num % len(a)
        res.append(a.pop(num))
        num += k-1
print("<",', '.join(str(i) for i in res),">",sep ='')