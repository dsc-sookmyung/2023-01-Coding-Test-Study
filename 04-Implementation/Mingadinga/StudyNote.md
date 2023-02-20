# Implementation

구현이란 머리속에 있는 알고리즘을 소스코드로 바꾸는 과정이다. 문제 해결 분야에서의 구현 유형은 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 말한다. 

알고리즘은 간단한데 코드가 길어지는 문제, 소수점 자리까지 출력해야하는 문제, 문자열 처리, 큰 정수 처리 등 사소한 조건 설정이 많은 문제들이 코드로 구현하기 까다롭다. 사용하는 언어의 문법에 익숙하고 라이브러리를 충분히 많이 사용해봐야 한다. 만약 코딩 테스트 환경이 파이썬3와 Pypy3을 지원한다면 연산 속도가 빠른 Pypy3을 사용하자.

주로 완전 탐색과 시뮬레이션 유형에서 구현이 핵심인 경우가 많다. 완전 탐색은 모든 경우의 수를 모두 계산하는 해결 방법인데, 시간 제한과 데이터 개수를 먼저 확인한 후 시간 복잡도를 정해야 한다. 파이썬은 리스트의 크기가 1000만을 넘지 않고(40 MB) 1초에 2000만 번의 연산을 수행한다고 가정하면 통과할 수 있다. 

시뮬레이션은 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 문제 유형을 말한다. 일련의 명령에 따라 개체를 차례대로 이동시키는 유형이 대표적인데, 방향을 설정해야 한다면 그 방향에 따라 이동시킬 수 있는 거리를 리스트 dx, dy로 설정하면 좋다.

# [21918 전구](https://www.acmicpc.net/problem/21918)

> 접근 방법
> 

입력으로 주어지는 명령에 맞게 상태값을 업데이트하면 된다. Switch문을 쓰면 더 예쁠 것 같은데 아쉽게도 파이썬은 switch를 지원하지 않아 elif 문을 사용했다.

> 통과한 코드
> 

```python
import sys

read = sys.stdin.readline

n, m = map(int, read().split())
states = list(map(int, read().split()))

for i in range(m):
  a, b, c = map(int, read().split())

  if a == 1:
    states[b - 1] = c
  elif a == 2:
    for j in range(b - 1, c):
      states[j] = 1 - states[j]
  elif a == 3:
    for j in range(b - 1, c):
      states[j] = 0
  elif a == 4:
    for j in range(b - 1, c):
      states[j] = 1

for state in states:
  print(int(state), end = ' ')
```

# [2798 블랙잭](https://www.acmicpc.net/problem/2798)

> 접근 방법
> 

조건을 넘지 않은 최댓값을 구하는 문제라 그리디로 해볼까 다르게 풀어볼까 고민했는데, 삼중 for문으로 완전 탐색하는 풀이의 시간 복잡도를 생각해봤을 때 문제 조건을 통과할 수 있을 것 같아서 그냥 빨리 풀었다. 문제 조건이 1초 128 MB이고, 시간 복잡도는 100C3 상수 시간이 아닐까.. 싶다!

> 통과한 코드
> 

```python
import sys

read = sys.stdin.readline

card_count, target = map(int, read().split())
cards = list(map(int, read().split()))

# 연산(더하기) 횟수는 카드를 고르는 조합의 개수에 비례한다
# 100C3은 161700이므로 파이썬 1초 안에 풀 수 있다 (2000만번 이하)

max_sum = 0
for i in range(card_count):
  for j in range(i+1, card_count):
    for k in range(j+1, card_count):
      sum = cards[i] + cards[j] + cards[k]
      if (sum <= target) and (max_sum < sum):
        max_sum = sum

print(max_sum)
```

# [14467 소가 길을 건너간 이유1](https://www.acmicpc.net/problem/14467)

> 접근 방법
> 

가장 최근의 관찰 결과만 저장해두었다가, 새로 입력받은 관찰값이 변했다면 카운트를 증가시키면 된다. 관찰 결과는 소의 번호와 위치값으로 구성되므로 딕셔너리 자료형을 사용했다.

> 통과한 코드
> 

```python
import sys

read = sys.stdin.readline

look_count = int(read())
look_results = {}

result = 0
for i in range(look_count):
  cow, position = map(int, read().split())
  if cow not in look_results.keys():
    look_results[cow] = position
  elif look_results[cow] != position:
    result += 1
    look_results[cow] = position

print(result)
```

# [2578 빙고](https://www.acmicpc.net/problem/2578)

> 접근 방법
> 

생각보다 오래 걸렸던 문제. 구현 유형이니 너무 깊게 생각하지 말고 코드로 구현하는 것에 우선했다. 빙고판과 호출 숫자는 2차원 배열로 입력 받았고, 호출 순서는 코드를 좀 더 이쁘게 만들고 싶어서(ㅋㅋㅋ) 1차원 리스트로 바꿔 for문 돌렸다. 호출된 숫자를 지울 때는 원래 빙고판의 숫자를 0으로 업데이트하고, 빙고를 검사할 때는 가로 세로 대각선이 모두 0이면 빙고 카운트를 증가시켰다. 지금 보니 테스트하는 부분에서 call 인덱스가 15 이상인 경우 빙고 검사 메소드를 호출하도록 하면 성능이 약간 좋아질 것 같다.

> 통과한 코드
> 

```python
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
    diagonal_right.append(bingo[i][4-i])
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
```