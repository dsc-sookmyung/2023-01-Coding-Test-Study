# 20291 파일 정리

import sys 

N = int(sys.stdin.readline())
expand_dict ={}
for i in range(N):
    file = sys.stdin.readline().rstrip().split('.')
    expand = file[1]
    if expand in expand_dict:
        expand_dict[expand] +=1
    else :
        expand_dict[expand] =1

expand_dict = sorted(expand_dict.items(),key = lambda x:x[0], reverse=False)

for j in expand_dict:
    print(j[0], j[1])