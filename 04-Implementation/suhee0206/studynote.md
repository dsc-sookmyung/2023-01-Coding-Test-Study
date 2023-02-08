# 구현 (완전 탐색 & 시뮬레이션)

## 목차

- **[개념](#개념)**
  - [구현](#구현)
- **[문제](#문제)**
  - [21918 전구](#21918-전구)
  - [2798 블랙잭](#2798-블랙잭)
  - [14467 소가 길을 건너간 이유1](#14467-소가-길을-건너간-이유1)
  - [2578 빙고](#2578-빙고)



## 개념

### 구현

흔히 문제 해결 분야에서 구현 유형의 문제는 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 의미한다. 완전 탐색과 시뮬레이션은 구현이 핵심이 되는 경우가 많다. 

- **완전 탐색**은 모든 경우의 수를 주저 없이 다 계산하는 해결 방법을 의미한다.
- **시뮬레이션**은 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형을 의미한다.

### 메모리 제한

파이썬에서 int 자료형 데이터의 개수에 따른 메모리 사용량이다. 데이터 처리량이 많을 때는 메모리 제한을 고려하자.

| 데이터의 개수(리스트의 길이) | 메모리 사용량 |
| ---------------------------- | ------------- |
| 1,000 (10^3)                 | 약 4KB        |
| 1,000,000 (10^6)             | 약 4MB        |
| 10,000,000 (10^7)            | 약 40MB       |

### 시간 제한

파이썬으로 작성한 코드가 1초에 2,000만 번의 연산을 수행한다고 가정하고 문제를 풀면 실행 시간 제한에 안정적이다. 시간 제한이 1초이고, 데이터의 개수가 100만 개인 문제가 있다면 일반적으로 시간 복잡도 `O(NlogN)` 이내의 알고리즘을 이용하여 문제를 풀어야 한다. 알고리즘 문제를 풀 때는 시간 제한과 데이터의 개수를 먼저 확인한 뒤에 이 문제를 어느 정도의 시간 복잡도의 알고리즘으로 작성해야 풀 수 있을 것인지 예측할 수 있어야 한다.

*출처: [이것이 취업을 위한 코딩테스트다 with 파이썬](http://www.yes24.com/Product/Goods/91433923)*



## 문제

### [21918 전구](https://www.acmicpc.net/problem/21918)

문제) 전구를 제어하는 명령어를 수행한 후 전구의 상태를 출력하라. 

분류) 구현

해설) 주어진 명령어를 구현해내기만 하면 된다. 

```python
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
s = list(map(int, read().split()))
for _ in range(M):
  a, b, c = map(int, read().split())
  if a==1:
    s[b-1] = c
  if a==2:
    for i in range(b-1, c):
      s[i] = not s[i]
  if a==3:
    for i in range(b-1, c):
      s[i] = 0
  if a==4:
    for i in range(b-1, c):
      s[i] = 1

for data in s:
  print(int(data), end=' ')
```



### [2798 블랙잭](https://www.acmicpc.net/problem/2798)

문제) 세 개의 숫자를 더해서 합이 M이 넘지 않으면서 M에 최대한 가깝게 만들어라.

분류) 구현 - 완전 탐색

해설) **숫자의 개수가 최대 100개**여서, 완전 탐색을 해도 최대 10^6번의 연산만 하면 된다! 

모든 조합의 세 개 숫자 합을 구한 후, 모든 합 중에서 M과 가장 가까운 값을 구한다. 

참고) 문해력이 중요하다. 합이 M을 넘지 않는 카드 3장을 찾을 수 있다고 했지, 합이 항상 M이 넘지 않는다고 하지 않았다. 따라서 꼭 조건 `M-sum >= 0`이 필요하다!

```python
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
cards = list(map(int, read().split()))

sums = []

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      sums.append(cards[i] + cards[j] + cards[k])

answer = 0
sub = 300001

for sum in sums:
  if M-sum >= 0 and M-sum < sub:
    answer = sum
    sub = M-sum
    
print(answer)
```



### [14467 소가 길을 건너간 이유1](https://www.acmicpc.net/problem/14467)

문제) N번 관찰했을 때, 1번부터 10번까지의 소가 길을 건너간 최소 횟수를 출력하라. 

분류) 구현

해설) dictionary에 소의 번호, 위치 쌍을 저장하고 관찰한 위치가 저장된 위치와 다르다면 길을 건너간 횟수에 1을 더하고, dictionary를 갱신한다. 

참고) dictionary에서 key값 존재 여부를 `d.get(k)`로도 확인할 수 있는데, `get(k)` 함수는 딕셔너리 `d`에서 `k`라는 key에 대응되는 value를 리턴한다. key가 없을 때는 `None`을, key에 대응되는 value가 0일 때는 `0`을 리턴하기 때문에, `bool`로는 둘 다 `False`가 된다. 따라서 key 존재 여부는 **`if k in d.keys()`**로 확인하는 것이 확실하다!

```python
import sys

read = sys.stdin.readline

answer = 0
cows = {}

N = int(read())
for _ in range(N):
  i, p = map(int, read().split())
  if i in cows.keys():
    if cows[i] != p:
      answer = answer + 1
  cows[i] = p

print(answer)
```



### [2578 빙고](https://www.acmicpc.net/problem/2578)

문제) 25개의 칸으로 이루어진 빙고판이 있다. 사회자가 부르는 수를 차례로 지워나가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다. 이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 사회자가 몇 번째 수를 부른 후 "빙고"를 외치게 되는지를 출력하라. 

분류) 구현 - 완전 탐색

해설) **숫자의 개수가 25개**여서 `O(N^2)`도 거뜬하다! 빙고판을 하나하나 탐색하면서 사회자가 부른 수를 지운다. 수를 지울 때마다 선이 몇 개 그어졌는지 확인해서 3개 이상이면 멈춘다.

빙고판을 이중 배열로 만들었기에, 다음과 같이 계산하면 된다.

- 가로줄: 각 행의 총합이 5면, 선을 긋는다.
- 세로줄: 열을 고정해놓고, 5개의 행에 있는 원소들의 합을 더해서 총합이 5면, 선을 긋는다.
- 대각선: 좌상향 대각선과 우상향 대각선 위에 있는 수를 따로 체크하여, 같은 대각선 위에 있는 수의 총합이 5면, 선을 긋는다.
  - 좌상향 대각선: 행과 열의 인덱스가 같은 경우, 좌상향 대각선 위에 있는 수다.
  - 우상향 대각선: 헹과 열 인덱스의 합이 5인 경우, 우상향 대각선 위에 있는 수다.

메모) 반복문이 중첩될 때, 변수의 위치를 (어느 반복문 안, 또는 밖에 위치시킬지) 잘 선정하자. 

```python
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
```


