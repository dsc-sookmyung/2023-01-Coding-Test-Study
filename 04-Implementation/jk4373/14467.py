#14467 소가 길을 건너간 이유
import sys
n = int(input())
cows = [-1]*10
cows_cnt = {}
cnt = 0
for i in range(n):
    c,go = map(int,sys.stdin.readline().split())
    if c in cows_cnt:
        if cows_cnt[c] != go:
            cnt +=1
    cows_cnt[c] = go
print(cnt)