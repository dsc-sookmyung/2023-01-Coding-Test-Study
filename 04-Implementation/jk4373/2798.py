# 2798 블랙잭
import sys

n,m = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))

cards.sort(reverse=True)

sum_tmp = 0
sum = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum_tmp = cards[i]+ cards[j] + cards[k]
            # print(cards[i], cards[j] , cards[k], "합은 = ",sum_tmp)
            sum.append(sum_tmp)
# print("sum is",sum)
min_gap = sys.maxsize
min_sum = 0
for i in range(len(sum)):
    gap = m - sum[i]
    if gap >=0 and min_gap> gap:
        min_gap = gap
        min_sum = sum[i]
print(min_sum)