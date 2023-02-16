import itertools
import sys

def count_bingo():
    bingo = 0

    for i in range(5):
        if board[i].count(0) == 5:
            bingo += 1

    for j in range(5):
        cnt = 0
        for r in range(5):
            if board[r][j] == 0:
                cnt += 1
        if cnt == 5:
            bingo += 1

    if board[0][0] == 0 and board[1][1] == 0 \
            and board[2][2] == 0 and board[3][3] == 0 and board[4][4] == 0:
        bingo += 1
    if board[0][4] == 0 and board[1][3] == 0 \
            and board[2][2] == 0 and board[3][1] == 0 and board[4][0] == 0:
        bingo += 1

    return bingo


board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
check = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
check = list(itertools.chain(*check))
answer = 0

for i in range(25):
    for j in range(5):
        for k in range(5):
            if check[i] == board[j][k]:
                board[j][k] = 0
                print(count_bingo())
                if count_bingo() < 3:
                    continue
                else:
                    answer = i + 1
            else:
                continue
        if answer >= 12:
            break
    if answer >= 12:
        break

print(answer)
