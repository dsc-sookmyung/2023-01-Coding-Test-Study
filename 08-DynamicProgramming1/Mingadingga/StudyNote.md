# [11726 2xN 타일링](https://www.acmicpc.net/problem/11726)

> 접근 방법

dp[i] : i번째를 채우는 경우의 수
1) i-1까지가 채워진 경우 : 1가지 (1*2)
2) i-2까지가 채워진 경우 : 1가지 (2*1) - 1*2 두개를 세로로 놓는 경우는 1번에 포함됨

- 점화식 : dp[i] = dp[i-1] + dp[i-2]
- 초기화 : dp[0] = 0, dp[1] = 1, dp[2] = 2

> 통과한 코드

```python
import sys

read = sys.stdin.readline
n = int(read())
dp = [0 for _ in range(n+1)]

dp[0], dp[1], dp[2] = 0, 1, 2
for i in range(3, n+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
```

# [11055 가장 큰 증가하는 부분 수열](https://www.acmicpc.net/problem/11055)

> 접근 방법

dp[i] : i번째 요소를 포함했을 때 증가하는 수열의 최대 합
dp[i]는 누적합의 임시배열로 사용될 수 있음을 이용한다.

1) numbers[i] >= numbers[i 전의 것] : 증가함. dp[i] = max(dp[i], dp[i 전의 것] + numbers[i])
2) numbers[i] < numbers[i-1] : 감소함. 누적합에 반영 안함


> 통과한 코드

```python
import sys

read = sys.stdin.readline
n = int(read())
numbers = list(map(int, read().split()))
dp = numbers[:]

for i in range(n):
    for j in range(0, i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

print(max(dp))
```

# [9465 스티커](https://www.acmicpc.net/problem/9465)

> 접근 방법

점화식이 직관적으로 떠오르지 않아서 점화식 세우는 부분만 구글링했다.
d[행][i] : arr[헹][i]를 선택했을 때 스티커의 최대 합

🔖 점화식 구하기
- arr[0][i]를 선택했을 때 지난 경로에서 선택할 수 있는 경우는 arr[1][i-1]을 지나오거나 arr[0][i-2]를 지나온 경우이다.
    => dp[0][i] = max(dp[1][i-1]+values[0][i], dp[1][i-2]+values[0][i])
- arr[1][i]를 선택했을 때 지난 경로에서 선택할 수 있는 경우는 arr[0][i-1]을 지나오거나 arr[1][i-2]를 지나온 경우이다.
    => dp[1][i] = max(dp[0][i-1]+values[1][i], dp[0][i-2]+values[1][i])

🔖 초기화
- n의 최솟값이 1이다. 따라서 dp[0][0], dp[1][0]는 배열값으로 바로 초기화한다.
- n이 1 이상인 경우에 dp[0][1], dp[1][1]을 초기화한다. 값은 각각 대각선에 있는 점수 + 자신의 점수이다.


> 통과한 코드

```python
import sys

read = sys.stdin.readline
t = int(read())
values = []

def max_value(values):
  dp = [[], []]
  dp[0] = [0 for i in range(len(values[0]))]
  dp[1] = [0 for i in range(len(values[0]))]

  dp[0][0], dp[1][0] = values[0][0], values[1][0]
  if len(values[0]) > 1:
    dp[0][1], dp[1][1] = dp[1][0] + values[0][1], dp[0][0] + values[1][1]

  for i in range(2, n):
    dp[0][i] = max(dp[1][i-1]+values[0][i], dp[1][i-2]+values[0][i])
    dp[1][i] = max(dp[0][i-1]+values[1][i], dp[0][i-2]+values[1][i])

  return max(max(dp[0]), max(dp[1]))

for i in range(t):
  values = [[], []]
  n = int(read())
  values[0] = list(map(int, read().split()))
  values[1] = list(map(int, read().split()))
  print(max_value(values))

```


# [9084 동전](https://www.acmicpc.net/problem/9084)

> 접근 방법

부분합이 전체합에 포함되므로 dp를 사용할 수 있다.
무슨 말이냐면 화폐 단위가 2원, 5원 있을 때 9원을 만드는 경우의 수에 7원을 만드는 경우의 수가 그대로 포함된다.

- dp[k] : k원을 만들 수 있는 경우의 수
- 점화식 : 현재 탐색 중인 화폐 단위 coin에 대하여
  - (k - coin)원을 만들 수 있는 경우의 수가 존재하면 그대로 누적합
  - 경우의 수가 존재하지 않으면 패스
- 초기화 : dp[0] = 1


> 통과한 코드

```python
import sys

read = sys.stdin.readline


def combination_count(coins, target):
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for coin in coins:
        for k in range(target + 1):
            if k >= coin:
                dp[k] += dp[k - coin]

    return dp[target]


t = int(read())

for _ in range(t):
    n = int(read())
    coins = list(map(int, read().split()))
    m = int(read())
    print(combination_count(coins, m))

```


# [9655 돌게임](https://www.acmicpc.net/problem/9655)

> 접근 방식

dp[i] : i번째 돌을 마지막으로 가져갔을 때 상근이가 이기는가(1)
- dp[1] = 1
- dp[2] = 0
- dp[3] = 1
...

점화식
- dp[i-3] 혹은 dp[i-1]이 1이면 dp[i]은 0이다 
- dp[i] = dp[i-1] or dp[i-3]

> 통과한 코드

```python
import sys

read = sys.stdin.readline

n = int(read())
dp = [-1 for _ in range(n+1)]

if n < 4:
  dp[n] = n % 2

else:
  dp[1] = 1
  dp[2] = 0
  dp[3] = 1

for i in range(4, n+1):
  dp[i] = not dp[i-1] or not dp[i-3]
print('SK' if dp[n]==1 else 'CY')
```


# [2839 설탕배달](https://www.acmicpc.net/problem/2839)

> 접근 방식

dp[i] : i 킬로그램의 설탕을 운반할 수 있는 최소 봉지 개수

라고 놓고 아래와 같이 전개했다.

- dp[1] = -1
- dp[2] = -1
- dp[3] = 1 (초기화)
- dp[4] = -1 (정확하게 4 킬로그램을 만들 수 없다)
- dp[5] = 1 (초기화)
- dp[6] = 2 = 후보 : dp[3] + 1(2), dp[1] + 1 (0)
- dp[7] = -1 =  후보 : dp[4] + 1(0), dp[2] + 1(0)
- dp[8] = 2 = 후보 : dp[3] + 1(2), dp[5] + 1(2)
- dp[9] = 3 = 후보 : dp[6] + 1(3), dp[4] + 1(0)
- dp[10] = 2 = 후보 : dp[7] + 1(0), dp[5] + 1(2)
- dp[11] = 3 = 후보 : dp[8] + 1(3), dp[6] + 1(3)
- dp[12] = 4 = 후보 : dp[9] + 1(4), dp[7] + 1(0)
- dp[13] = 3 = 후보 : dp[10] + 1(3), dp[8] + 1(3)
- dp[15] = 3 = dp[12] + 1(5), dp[10] + 1(3) // 3 3 3 3 3 or 5 5 5

점화식
- 초기화 : 전부 -1, 3과 5는 1로
- dp[i] = i 킬로그램의 설탕을 운반할 수 있는 최소 봉지 개수
  - dp[i-3]+1과 dp[i-5]이 모두 0이면 : 만들 수 없으므로 -1 저장
  - dp[i-3]+1과 dp[i-5]이 하나면 0이면 : 더 큰 것(0이 아닌 것)
  - dp[i-3]+1과 dp[i-5]이 모두 0이 아니면 : 더 작은 것

> 통과한 코드

```python
import sys

read = sys.stdin.readline

n = int(read())
dp = [-1 for _ in range(5001)]

dp[3], dp[5] = 1, 1
for i in range(6, n+1):
  taken_3 = dp[i-3] + 1
  taken_5 = dp[i-5] + 1

  temp = 0
  # 둘다 0
  if not taken_3 and not taken_5:
    temp = -1
  # 둘다 0 아님
  elif taken_3 and taken_5:
    temp = min(taken_3, taken_5)
  # 하나만 0
  else:
    temp = max(taken_3, taken_5)
  dp[i] = temp
print(dp[n])
```

# [17626 Four Squares](https://www.acmicpc.net/problem/17626)

> 접근 방식

dp[i] : 합이 i가 되는 제곱수의 최소 개수

dp[0] = 0
dp[1] = 1 (1^2) (초기화)
dp[2] = 2 = dp[1] + dp[1]
dp[3] = 3 = dp[2] + dp[1]
=====
dp[4] = 1 (2^2) (초기화)
dp[5] = 2 = min(dp[4] + dp[1], dp[1] + dp[4]) : 2, 2
dp[6] = 3 = min(dp[4] + dp[2], dp[1] + dp[5]) : 3, 3
dp[7] = 4 = min(dp[4] + dp[3], dp[1] + dp[6]) : 4, 4
dp[8] = 2 = min(dp[4] + dp[4], dp[1] + dp[7]) : 2, 5
=====
dp[9] = 1 (3^2) (초기화)
dp[10] = 2 = min(dp[9] + dp[1], dp[4] + dp[6], dp[1] + dp[9]) : 2, 4, 2
dp[11] = 3 = min(dp[9] + dp[2], dp[4] + dp[7], dp[1] + dp[10]) : 3, 5, 3
dp[12] = 3 = min(dp[9] + dp[3], dp[4] + dp[8], dp[1] + dp[11]) : 4, 3, 4
dp[13] = 2 = min(dp[9] + dp[4], dp[4] + dp[9], dp[1] + dp[12]) : 2, 2, 4
dp[14] = 3 = min(dp[9] + dp[5], dp[4] + dp[10], dp[1] + dp[13]) : 3, 3, 3

점화식
- dp[0] = 0, dp[1] = 1
- dp[i] = min(dp[i-(i보다 작은 제곱수*)]+1)


> 통과한 코드

```python
import sys
import math

read = sys.stdin.readline

INF = 50001
n = int(read())
dp = [0, 1]

for i in range(2, n+1):
  min_value = INF
  for j in range(1, int(math.sqrt(i)) + 1):
    min_value = min(min_value, dp[i-j*j]+1)
  dp.append(min_value)
print(dp[n])
```




