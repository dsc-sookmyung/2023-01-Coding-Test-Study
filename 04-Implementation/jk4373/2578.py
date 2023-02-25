# 2578 빙고
import sys

# 빙고 dict
# bingo = dict()
# for i in range(5):
#     a = list(map(int,sys.stdin.readline().split()))
#     for j in range(5):
#         bingo[a[j]] = (i,j)

#불린 숫자 기록
check = [[0]*5 for i in range(5)]
# 불린 답
bingo = [list(map(int,sys.stdin.readline().split()))  for _ in range(5)]
answer = [list(map(int,sys.stdin.readline().split()))  for _ in range(5)]

#빙고 찾는 함수
def find_bingo(check):
    bingo =0
    for j in range(5):
        if sum(check[j]) ==5: # 가로
            bingo +=1
        if sum([t[j] for t in check]) == 5:
            bingo+=1
    if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5:
        bingo +=1
    if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5:
        bingo +=1
    return bingo

idx = 0
# for i in range(5):
#     for j in range(5):
#         idx +=1
#         tmp = answer[i][j]
#         print(tmp)
#         if tmp in bingo:
#             check[bingo[tmp][0]][bingo[tmp][1]] = 1
            
#             #빙고 찾기
#             bingo = find_bingo(check)
#             if bingo >=3:
#                 print(idx)
#                 break

for i in range(5):
    for j in range(5):
        for k in range(5):
            for h in range(5):
                if answer[i][j] == bingo[k][h]:  
                    bingo[k][h] = 0  
                    idx += 1  
                    if find_bingo(bingo) >= 3:  
                        print(idx)  
                        exit() 