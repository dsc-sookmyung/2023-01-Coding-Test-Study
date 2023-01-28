# 문자열 집합

import sys

N,M = map(int,input().split())
S = set() # 배열로 검색시 시간 초과 
count =0
for _ in range(N):
    tmp = sys.stdin.readline()
    S.add(tmp)
    # print("집합 S에 포함되어있는 문자열")
for _ in range(M):
    test = sys.stdin.readline()
    if( test in S): # 배열은 시간복잡도 O(n), 집합,Dict는 O(1)
        count = count + 1
    # print("검사해야하는 문자열")
print(count)