def check_call(target):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == target:
                bingo[i][j] = 0

def is_bingo_three():
    bingo_count = 0
    for row in bingo:
        if [0, 0, 0, 0, 0] == row:
            bingo_count += 1

    for column in range(5):
        bingo_column = []
        for index in range(5):
            bingo_column.append(bingo[index][column])
        if [0, 0, 0, 0, 0] == bingo_column:
            bingo_count += 1

    diagonal_left, diagonal_right = [], []
    for i in range(5):
        diagonal_left.append(bingo[i][i])
        diagonal_right.append(bingo[i][4 - i])
    if [0, 0, 0, 0, 0] == diagonal_left:
        bingo_count += 1
    if [0, 0, 0, 0, 0] == diagonal_right:
        bingo_count += 1

    if bingo_count >= 3:
        return True
    return False


import sys

read = sys.stdin.readline

bingo = []
calls = []

for _ in range(5):
    bingo.append(list(map(int, read().split())))
for _ in range(5):
    calls.append(list(map(int, read().split())))
calls = sum(calls, [])

for call in calls:
    check_call(call)
    if is_bingo_three():
        print(calls.index(call) + 1)
        break