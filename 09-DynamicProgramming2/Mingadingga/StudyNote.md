# [1463 1로 만들기](https://www.acmicpc.net/problem/1463)

> 접근 방식

dp[i] : i를 1로 만드는데 필요한 최소 연산 횟수

dp[0] = 0
dp[1] = 0
dp[2] = 1 = dp[1] + 1 (2%2==0)
dp[3] = 1 = dp[1] + 1 (3%3==0)
dp[4] = 2 = dp[2] + 1 (4%2==0)
dp[5] = 3 = dp[4] + 1 (5%2!=0 and 5%3!=0)
dp[6] = 2 = dp[3] + 1 (6%3==0)
dp[7] = 3 = dp[6] + 1 (7%2!=0 and 7%3!=0)
dp[8] = 3 = dp[4] + 1 (8%2==0)
dp[9] = 2 = dp[3] + 1 (9%3==0)
dp[10] = 3 = dp[5] + 1 (10%2==0)
dp[11] = 4 = dp[10] + 1 (11%2!=0 and 11%3!=0)

점화식 도출
- 초기화 : dp[1] = 0
- 점화식 : dp[i] = min(dp[i-1]+1, dp[i//2]+1, dp[i//3]+1)

> 통과한 코드

```python
import sys

read = sys.stdin.readline

n = int(read())
dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
  dp[i] = dp[i-1] + 1
  if i%3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1)
  if i%2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])
```


# [9095 1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)

> 접근 방식

dp[i] : i를 1, 2, 3의 합으로 나타내는 방법의 수 (1 <= 1 <= 10)

* 초기화 *
dp[0] = 0
dp[1] = 1 (1)
dp[2] = 2 (1+1, 2)
dp[3] = 4 (1+1+1, 1+2, 2+1, 3)

* 점화식 *
dp[4] = 7 = dp[3] + dp[2] + dp[1] (마지막 수를 각각 1, 2, 3 사용)
dp[5] = 13 = dp[4] + dp[3] + dp[2] (마지막 수를 각각 1, 2, 3 사용)
dp[6] = 24 = dp[5] + dp[4] + dp[3]] (마지막 수를 각각 1, 2, 3 사용)
dp[7] = 44 = dp[6] + dp[5] + dp[4] (마지막 수를 각각 1, 2, 3 사용)

그런데 점화식을 쓰고 보니, dp[0] = 1로 놓으면 dp[2]와 dp[3]도 점화식으로 표현 가능하다.
다만 반복문 안에서 조건문을 제외하기 위해 dp[2]만 조건 검사해서 초기화했다.

점화식 도출
- 초기화 : dp[0] = 1, dp[1] = 1, dp[2] = 2, dp[3] = 3
- 점화식 : dp[i] = min(dp[i-1]+1, dp[i//2]+1, dp[i//3]+1)

> 통과한 코드

```python
import sys

read = sys.stdin.readline

t = int(read())
targets = []
dp = []

# 입력 받기
for _ in range(t):
  targets.append(int(read()))
  dp = [0 for _ in range(max(targets)+1)]

# dp 채우기
dp[0], dp[1] = 1, 1
if len(dp) > 2: dp[2] = 2
for i in range(3, max(targets) + 1):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 출력하기
for target in targets:
  print(dp[target])
```



# [1149 RGB 거리](https://www.acmicpc.net/problem/149)

> 접근 방식

dp[i][j] : i번째 집에 j 색을 사용했을 때, i번째 집까지 칠하는데 드는 최소 비용

* 초기화 *

dp[1][0] = price[1][0]
dp[1][1] = price[1][1]
dp[1][2] = price[1][2]

* 점화식 *
dp[2][0] = min(dp[1][1]+dp[1][2]) + price[2][0]
dp[2][1] = min(dp[1][0]+dp[1][2]) + price[2][1]
dp[2][2] = min(dp[1][0]+dp[1][1]) + price[2][2]

...

dp[n][i] = min(dp[n] 중 i번째 제외한 요소들) + price[n][i]


=====

처음 접근했을 떄는 dp를 1차원 배열로 놓고 i번째 요소를 집까지 칠하는데 드는 최소 비용이라고 가정했다. 
그리고 초기화에서 dp[0]을 min(prices[0])이라고 뒀는데,
이러면 첫번째 라인에서 min을 포함하지 않는 경우의수는 고려되지 않아서 5번째 예제에서 답이 틀렸다.
그레서 모든 색상을 비교하도록 2차원 배열을 만들었다.


> 통과한 코드

```python
import sys

read = sys.stdin.readline

n = int(read())
prices = [list(map(int, read().split())) for _ in range(n)]

INF = 1001
dp = [[INF]*3 for _ in range(n)]

dp[0][0] = prices[0][0]
dp[0][1] = prices[0][1]
dp[0][2] = prices[0][2]

for house in range(1, n):
  dp[house][0] = min(dp[house-1][1], dp[house-1][2])+prices[house][0]
  dp[house][1] = min(dp[house-1][0], dp[house-1][2])+prices[house][1]
  dp[house][2] = min(dp[house-1][0], dp[house-1][1])+prices[house][2]

print(min(dp[-1]))
```


# [2156 포도주 시식](https://www.acmicpc.net/problem/2156)

> 접근 방식

dp[i] : i번째 잔 위치에서 마실 수 있는 최대 양

| i-3 | i-2 | i-1 | i | dp[i] |
|-----|-----|-----|---|-------|
| o | o | x | o | dp[i] = dp[i-2] + wine[i] |
| o | x | o | o | dp[i] = dp[i-3] + wine[i-1] + wine[i] |
| x | o | o | x | dp[i] = dp[i-1] |

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(dp[1], wine[0]+wine[2], wine[1]+wine[2])
...
dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])


dp[5] 정도까지 모든 경우의 수를 그려보다가 이건 아닌 것 같아서
순서를 알 수 없는 i번째 자리에서 그 값을 결정할 수 있는 방법을 찾았다.


> 통과한 코드

```python
import sys

read = sys.stdin.readline

n = int(read())
wine = [int(read()) for _ in range(n)]
dp = [0 for _ in range(n)]

dp[0] = wine[0]

if n > 1:
  dp[1] = wine[0] + wine[1]

if n > 2:
  dp[2] = max(dp[1], wine[0]+wine[2], wine[1]+wine[2])

for i in range(3, n):
  dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[-1])
```

> 접근 방법

모르겠어서 구글링해서 풀었습니다 -> https://myjamong.tistory.com/319

dp[i] : 무게 i만큼 담았을 때 최대 가치합

6 -> 0 0 0 0 0 0 | 13 13(max(dp[7], valueOf[6]+dp[1]))<br>
4 -> 0 0 0 0 | 8 8 13 13(max(dp[7], valueOf[4]+dp[3]))<br>
3 -> 0 0 | 6 8 8 13 14(max(dp[7], valueOf[3]+dp[4]))<br>
5 -> 0 0 6 8 | 12 13 14(max(dp[7], valueOf[5]+dp[2]))<br>

> 통과한 코드

```python
import sys
read = sys.stdin.readline

N, K = map(int, read().split())
cache = [0] * (K+1)

for _ in range(N):
    w, v = map(int, read().split())
    for j in range(K, w-1, -1):
        cache[j] = max(cache[j], cache[j-w] + v)
print(cache[-1])
```