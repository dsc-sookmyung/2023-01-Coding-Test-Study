import sys

read = sys.stdin.readline

board = []
check = []
for _ in range(5):
  board.append(list(map(int, read().split())))
  check.append([0,0,0,0,0])

call = []
for _ in range(5):
  call = call + list((map(int, read().split())))

def check_bingo(check, board):
  bingo = 0
  
  sum_diagonal_l = 0
  sum_diagonal_r = 0
  
  for i in range(5):
    if sum(check[i]) == 5:  # sum_row
      bingo = bingo + 1

    sum_col = 0
    for j in range(5):
      sum_col = sum_col + check[j][i]
      if i==j:
        sum_diagonal_l = sum_diagonal_l + check[i][j]
      if i+j==4:
        sum_diagonal_r = sum_diagonal_r + check[i][j]
    if sum_col == 5:
      bingo = bingo + 1
      
  if sum_diagonal_l == 5:
    bingo = bingo + 1
  if sum_diagonal_r == 5:
    bingo = bingo + 1

  return bingo

answer = 0
for index in range(25):
  for i in range(5):
    for j in range(5):
      if board[i][j] == call[index]:
        check[i][j] = 1
        if check_bingo(check, board) >= 3:
          answer = index + 1
          break
    if answer: break
  if answer: break

print(answer)