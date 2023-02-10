def check_call(target):
  print("call : ")
  for i in range(5):
    for j in range(5):
      if bingo[i][j] == target:
        bingo[i][j] = 0

    print(bingo[i])

def is_bingo_three():
    bingo_count = 0
    for row in bingo:
        if [0, 0, 0, 0, 0] == row:
            print("row bingo!")
            bingo_count += 1

    for column in range(5):
        bingo_column = []
        for index in range(5):
            bingo_column.append(bingo[index][column])
        if [0, 0, 0, 0, 0] == bingo_column:
            print("column bingo!")
            bingo_count += 1

    diagonal_left, diagonal_right = [], []
    for i in range(5):
        diagonal_left.append(bingo[i][i])
        diagonal_right.append(bingo[i][4 - i])
    if [0, 0, 0, 0, 0] == diagonal_left:
        print("diagnal bingo!")
        bingo_count += 1
    if [0, 0, 0, 0, 0] == diagonal_right:
        print("diagnal bingo!")
        bingo_count += 1

    print(bingo_count)
    if bingo_count >= 3:
        return True
    return False

bingo = [[11, 12, 2, 24, 10], [16, 1, 13, 3, 25], [6, 20, 5, 21, 17], [19, 4, 8, 14, 9], [22, 15, 7, 23, 18]]
calls = [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]

for call in calls:
  check_call(call)
  if is_bingo_three():
    print(calls.index(call) + 1)
    break