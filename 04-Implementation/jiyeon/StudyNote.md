# 04-구현

 - 정리한 문제
 1. 21918 전구
 2. 2798 블랙잭
 3. 14467 소가 길을 건너간 이유1
 4. 2578 빙고
 <br>

 ## 21918 전구

 ### 설명
 -  초기에 전구의 상태를 배열에 담아놓고 명령어에 따라 해당 인덱스에 접근해 상태를 바꿔주면 되는 문제이다.
 - 전구의 상태를 바꾸는 로직을 따로 분리해 함수로 만들었다.

```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bulbs = list(map(int, input().split()))

def changeStateTo(idx, state):
  bulbs[idx-1] = state

def reverseState(idx):
  if(bulbs[idx-1] == 0):
    bulbs[idx-1] = 1
  else:
    bulbs[idx-1] = 0

def offBulb(idx):
  bulbs[idx-1] = 0

def onBulb(idx):
  bulbs[idx-1] = 1

for _ in range(m):
  command = list(map(int, input().split()))
  if(command[0] == 1):
    changeStateTo(command[1], command[2])
  elif(command[0] == 2):
    for i in range(command[1], command[2]+1):
      reverseState(i)
  elif(command[0] == 3):
    for i in range(command[1], command[2]+1):
      offBulb(i)
  elif(command[0] == 4):
    for i in range(command[1], command[2]+1):
      onBulb(i)

print(*bulbs)

```

 ## 2798 블랙잭
 ### 설명
 - 카드의 개수가 최대 100개 이므로 N^3이어도 100,000,000이다. 따라서 브루스포스로 풀어도 시간내에 풀이가 가능하다.
 - for을 세번 돌면서 3개의 수가 선택되면 합을 구하고, 그 합이 m을 넘지 않는다면 최대값을 갱신해준다.

```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_result = 0

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      sum = cards[i] + cards[j] + cards[k]
      if(sum <= m):
        max_result = max(max_result, sum)

print(max_result)
```

## 14467 소가 길을 건너간 이유1

 ### 설명
 - "3번 소가 1번 위치에 있다"라는 명령이 들어왔을 때 다음의 정보를 알아야 한다.
	 - 3번 소가 이전에 나왔었는지
	 - 그랬다면 전에 3번 소의 위치는 어디였는지
- 따라서 소의 번호를 key로 가지고 소의 위치를 value로 가지는 dict을 이용하였다.
- 소의 번호와 위치를 입력 받았을 때 이전에 나온 적이 없다면 dict에 추가해주고 넘어간다.
- 이전에 나온 적이 있다면 위치를 비교해 count해준다.


```python
import sys
input = sys.stdin.readline

n = int(input())
count = 0
dict = {}

for i in range(n):
  cow_num, location = map(int, input().split())
  if(cow_num in dict):
    if(dict[cow_num] != location):
      count += 1
  dict[cow_num] = location

print(count)
```

## 2578 빙고

 ### 설명
 - 사회자가 부른 수를 빙고판(board)을 돌며 어디 자리인지 찾아준다.
 - [y][x]자리라면 해당 자리를 0으로 바꿔준다.(x표시 되었다는 뜻)
 - 그 후 해당 자리를 포함한 빙고선이 생겼는지 체크해준다. 다음의 경우를 확인해주면 된다.
	 - 해당 자리를 포함한 수직선
	 - 해당 자리를 포함한 수평선
	 - 만약 해당 자리가 / 대각선에 있을 경우 대각선 확인해주기
	 - 만약 해당 자리가 \대각선에 있을 경우 대각선 확인해주기
 - 빙고선인지 확인하는 방법 : 선에 있는 5개의 수를 다 더했을 때 0이면 빙고선이다.
- 만약 체크 후 빙고선이 3개 이상일 경우 사회자가 몇 번째로 부른 수인지 출력 후 break

```python
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for i in range(5)]
order = []
for i in range(5):
  order.extend(list(map(int, input().split())))
count = 0

def deleteAndCheck(num):
  for i in range(5):
    for j in range(5):
      if(board[i][j] == num):
        board[i][j] = 0  #x표시
        countBingo(i, j)

def countBingo(y, x):  #[y][x]를 포함한 빙고선이 생겼는지 확인
  verticalCheck(x)
  horizontalCheck(y)
  if(y==x):
    diagonalLeftTopCheck()
  if(y+x==4):
    diagonalLeftBottomCheck()

def verticalCheck(x):  #세로줄 확인
  global count
  sum = 0
  for i in range(5):
    sum += board[i][x]
  if(sum == 0):
    count += 1

def horizontalCheck(y):  #가로줄 확인
  global count
  if(sum(board[y]) == 0):
    count += 1

def diagonalLeftBottomCheck():  #왼쪽아래->오른쪽 위 대각선 확인
  global count
  if(board[4][0] + board[3][1] + board[2][2] + board[1][3] +board[0][4] == 0):
    count += 1

def diagonalLeftTopCheck():  #왼쪽위 -> 오른쪽아래 대각선 확인
  global count
  if(board[0][0] + board[1][1] + board[2][2] + board[3][3] +board[4][4] == 0):
    count += 1

for i in range(25):
  deleteAndCheck(order[i])
  if(count >= 3):
    print(i+1)
    break

```
