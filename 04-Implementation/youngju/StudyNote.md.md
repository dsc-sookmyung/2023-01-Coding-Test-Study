# Implementation
## 21918 전구
문제가 요구한 순서대로 입력 받고 명령어에 따라 나누어 구현했다.

```python
import sys  
  
n, m = map(int, sys.stdin.readline().split())  
stateList = list(map(int, sys.stdin.readline().strip().split()))  
  
for _ in range(m):  
    command = list(map(int, sys.stdin.readline().split()))  
    if command[0] == 1:  
        stateList[command[1] - 1] = command[2]  
    elif command[0] == 2:  
        for i in range(command[2] - command[1] + 1):  
            stateList[command[1] - 1 + i] = (lambda x: 1 if x == 0 else 0)(stateList[command[1] - 1 + i])  
    elif command[0] == 3:  
        for i in range(command[2] - command[1] + 1):  
            stateList[command[1] - 1 + i] = 0  
  else:  
        for i in range(command[2] - command[1] + 1):  
            stateList[command[1] - 1 + i] = 1  
  
print(*stateList)
```

**[풀이]**
1) 전구의 개수 n과 명령어의 개수 m 입력 받기
2) 전구의 상태를 stateList에 저장
3) 명령어를 한 줄씩 입력 받아 command에 저장
4) 명령어 번호에 따라 명령어 내용 구현 후 stateList 출

<br/>

## 2798 블랙잭
카드를 3장 묶어서 나올 수 있는 합의 모든 경우의 수를 구한 다음 m을 넘지 않는 값들 중 최댓값을 구한다.

```python
import sys  
  
n, m = map(int, sys.stdin.readline().split())  
num = list(map(int, sys.stdin.readline().split()))  
l = len(num)  
answer = 0  
for i in range(0, l-2):  
    for j in range(i+1, l-1):  
        for k in range(j+1, l):  
            if num[i] + num[j] + num[k] > m:  
                continue  
 else:  
                answer = max(answer, num[i] + num[j] + num[k])  
  
print(answer)
```


**[풀이]**
1) 카드 개수 n과 숫자 m을 입력 받는다
2) 카드들을 list에 저장한다
3) 카드 list에서 첫 번째 원소부터 시작해서 두 번째와 세 번째를 선택하는 반복문을 돌려 모든 경우의 수를 구한다
4) 반복문을 돌면서 세 카드의 합이 m을 넘으면 그저 계속 진행되게 한다
5) 세 카드의 합이 m보다 작거나 같으면 answer의 현재 값과 비교하여 더 큰 수로 계속 갱신

<br/>

## 14467 소가 길을 건너간 이유 1
소를 key로 딕셔너리를 만들어서 value를 비교하면서 소의 위치 변화를 카운트한다.

```python
import sys  
  
n = int(sys.stdin.readline().strip())  
cow = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  
dic = {}  
answer = 0  
for i in range(n):  
    if cow[i][0] not in dic.keys():  
        dic[cow[i][0]] = cow[i][1]  
    else:  
        if cow[i][1] != dic[cow[i][0]]:  
            dic[cow[i][0]] = cow[i][1]  
            answer += 1  
  else:  
            dic[cow[i][0]] = cow[i][1]  
  
print(answer)
```

**[풀이]**
1) n을 입력 받은 후 소에 따른 위치를 리스트로 입력 받아 cow라는 리스트에 저장한다
2) cow 리스트를 돌면서 소의 번호가 dic에 없다면 key값으로 하고 소의 위치를 value에 저장한다
3) 소의 번호가 dic에 있다면 위치를 나타내는 value를 비교하는데 현재 위치와 dic에 저장된 위치가 다르다면 answer를 +1하여 최종 answer를 구한

<br/>

## 2578 빙고
이 문제를 푸는데 생각보다 더 오래 걸렸다😱
코드를 짜면서 빙고 개수를 세는 메서드를 따로 만드는 것이 보기에 더 좋을 것 같아서 따로 만들었다

```python
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
```

**[풀이]**
1) 빙고판을 이중 리스트 board로 입력 받는다 
2) 사회자가 부르는 수 또한 이중 리스트 check로 입력 받는다
3) 반복문을 돌릴 때 더 쉽게 돌리기 위하여 check리스트를 일차원 리스트로 바꾼다
4) check 리스트를 하나씩 돌면서 그 안에서 board 리스트를 순회하며 check리스트의 원소와 같은 값을 찾아 0으로 바꾼다
5) 0으로 바꾼 후 count_bingo()를 이용하여 빙고의 개수를 찾는다
6) 빙고의 개수가 3보다 작으면 반복문을 계속 진행하고 3보다 크거나 같은 경우에는 인덱스에 +1을 하여 저장한다
7) 최소 12개가 0으로 변경되어야 빙고가 제대로 만들어 진 것이므로 12보다 answer가 크면 모든 반복문을 멈추고 answer를 출력한다
