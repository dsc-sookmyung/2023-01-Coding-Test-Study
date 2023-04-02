import sys

read = sys.stdin.readline
board = []
max_row_len = 0
for _ in range(5):
  row = list(read().rstrip())
  max_row_len = max(len(row), max_row_len)
  board.append(row)
answer = []
for i in range(max_row_len):
  for j in range(5):
    if len(board[j]) > i:
      answer.append(board[j][i])
print(''.join(answer))