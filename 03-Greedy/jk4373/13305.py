# 13305 주유소
import sys

N =int(input())
road =list(map(int,input().split()))
price =list(map(int,input().split()))
lst =[]
ans = 0
# for i in range(N-1): # price
#     tmp=[]
#     for j in range(N-1): # road
#         if j > i:
#             continue
#         else:
#             cost = road[i]*price[j]
#             tmp.append(cost)
#     lst.append(tmp)

# for idx in range(len(lst)):
#     tmp = min(lst[idx])
#     ans = ans + tmp
# print(ans)
    
take = price[0]
ans = 0
for i in range(N-1):
    if price[i]< take:
        take = price[i]
    ans = ans + take*road[i]
print(ans)