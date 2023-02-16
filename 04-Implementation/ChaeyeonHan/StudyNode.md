### 21918 전구
#### 풀이) 
- 전구의 갯수 N, 입력받는 명령어의 갯수 M을 입력받는다.
- 전구의 상태를 저장하는 status 배열을 만들어 상태를 입력한다. 
- 명령어 입력시에 a값을 확인해서 케이스를 나눠준다. 
- *참고 : 배열을 print(*status) 처럼 앞에 *을 붙여주게 되면, 반복문을 사용하지 않고 리스트 요소를 한번에 출력할 수 있다. 
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
status = list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:  # b번째 전구 상태 c로
        status[b-1] = c
    elif a == 2:  # b부터 c까지 전구상태 반대로 변경
        for i in range(b-1, c):
            if status[i] == 0:
                status[i] = 1
            else:
                status[i] = 0
    elif a == 3:  # b부터 c까지 전구 끄기
        for i in range(b-1, c):
            if status[i] == 1:
                status[i] = 0
    elif a == 4:  # b부터 c까지 전구 켜기
        for i in range(b-1, c):
            if status[i] == 0:
                status[i] = 1
# print(*status)
for i in status:
    print(i, end=' ')
```

### 14467 소가 길을 건너간 이유1
#### 풀이) 
- 소의 위치를 저장하기 위한 딕셔너리 cows를 선언해준다.
- 관찰 결과가 하나씩 입력될 때마다, 소의 번호를 확인해서 딕셔너리에 소의 번호가 없다면 왼쪽/오른쪽 중 해당하는 값을 저장한다.
- 소의 번호가 이미 있다면, 딕셔너리에 저장된 값과 일치하는지 확인하고 일치하지 않는다면 길을 건넌 횟수를 1 증가시켜준다.

```python
# 딕셔너리 사용하기
import sys
input = sys.stdin.readline

N = int(input())

cows = {}  # 소의 번호와 위치를 저장하는 딕셔너리 선언
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    if a not in cows:  # 소의 번호가 없으면
        cows[a] = b
    else:
        if cows[a] != b:
            cnt += 1
            cows[a] = b
print(cnt)


# 딕셔너리 방법 말고, 소의 위치를 저장하는 배열을 만든다. 
import sys
input = sys.stdin.readline

N = int(input())
cows = [-1] * 11
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    if cows[a] == -1:
        cows[a] = b
    else:
        if cows[a] != b:
            cnt += 1
            cows[a] = b
print(cnt)
```

### 2798 블랙잭
#### 풀이)
- 카드의 갯수와 M을 입력받는다. 
- 3개의 카드를 뽑아야 하기에, 3중 for문을 이용하여 입력받는 숫자 리스트 nums의 맨 앞에서부터 숫자를 3개씩 더해나간다.
- 카드 3장을 합친 sum이 M을 넘지 않고, 카드 3장을 더한 최댓값을 저장하는 max_n보다 크다면, max_n의 값을 갱신시켜 최댓값을 찾는다.

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
max_n = 0

nums.sort()
for i in range(N-1, 1, -1):
    for j in range(i-1, 0, -1):
        for k in range(j-1, -1, -1):
            # print(i, j, k)
            sum = nums[i] + nums[j] + nums[k]
            if sum <= M and max_n < sum:
                max_n = sum  # sum값 갱신
print(max_n)
```

### 2578 빙고
#### 풀이) 
- 구현 접근이 어려웠다..
- 빙고에 넣을 숫자를 2차원 배열로 받고, 사회자가 부르는 숫자를 num 배열에 넣어준다.
- 사회자가 숫자를 하나씩 부르면, 그 숫자와 일치하는 빙고판의 숫자를 찾아서 해당 숫자를 0으로 바꿔주고, 빙고인지 매번 체크해준다.
- 빙고의 갯수를 확인하는 cnt_bingo 함수는 대각선, 가로, 세로 방향으로 빙고인지 모두 확인해준다.
- 빙고 확인시, 해당 방향으로 값들이 모두 0이라면 빙고이기에, 1을 리턴해준다.
- 빙고가 3개 이상이면, 부른 숫자의 갯수를(count+1) 출력해준다.
```python
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

```