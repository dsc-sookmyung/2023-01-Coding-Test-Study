import sys

input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

num = (list(map(int, sys.stdin.readline().strip().split(" "))))
for i in range(4):
    num += list(map(int, sys.stdin.readline().strip().split(" ")))

count = 0
bingo = 0

def cnt_bingo(i, j):
    global bingo
    bingo += check_diagonal(i, j) + check_row(i) + check_col(j)
    return bingo


# 대각선인지 위치 확인
def is_diagonal(i, j):
    if i == j or i + j == 4:
        return True
    else:
        return False


# 값을 체크하면서 모두 0으로 바뀌어있다면 빙고이므로 1을 리턴
def check_diagonal(i, j):
    if is_diagonal(i, j):
        tmp = 0
        if i == j:
            for x in range(5):
                if board[x][x]:
                    break
                if x == 4:
                    tmp += 1
        if i + j == 4:
            for x in range(5):
                if board[x][4 - x]:
                    break
                if x == 4:
                    tmp += 1
        return tmp
    else:
        return 0


def check_row(i):
    for j in range(5):
        if board[i][j]:
            return 0
    return 1


def check_col(j):
    for i in range(5):
        if board[i][j]:
            return 0
    return 1

def main():
    for count, number in enumerate(num):
        for i in range(5):
            for j in range(5):
                if number == board[i][j]:  # 사회자가 부른 숫자와 일치하면
                    board[i][j] = 0  # 값을 0으로 바꿔주고
                    if cnt_bingo(i, j) >= 3:
                        return count + 1
print(main())