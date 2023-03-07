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


