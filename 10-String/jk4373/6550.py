# 6550 부분 문자열

import sys

def find_st(s,t):
    s_last = len(s) -1
    b_idx = -1
    for i in range(len(t)):
        for j in range(len(s)):
            t_str = s[j]
            idx = t.find(t_str,i)
            if idx == -1:
                return('NO')
            else:
                if idx > b_idx:
                    b_idx = idx
                    if j == s_last:
                        return('YES')
                else:
                    break
    return('NO')

while True:
    try :
        s,t = sys.stdin.readline().rstrip().split()
        flag = 0
        idx = 0
        
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx+=1
                if idx == len(s):
                    flag = 1
                    break
        
        if flag == 1:
            print('Yes')
        else:
            print('No')
    except:
        break



