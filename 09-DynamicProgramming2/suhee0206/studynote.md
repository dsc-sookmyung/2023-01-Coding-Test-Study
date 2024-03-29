# Dynamic Programming (2)

## 목차

- **개념**
  - [다이나믹 프로그래밍](#다이나믹-프로그래밍)
- 문제
  - [1149 RGB거리](https://www.acmicpc.net/problem/1149)
  - [2156 포도주 시식](https://www.acmicpc.net/problem/2156)
  - [1463 1로 만들기](https://www.acmicpc.net/problem/1463)
  - [12865 평범한 배낭](https://www.acmicpc.net/problem/12865)



## 개념

### 다이나믹 프로그래밍

동적 계획법이라고 표현하기도 하는 다이나믹 프로그래밍, Dynamic Programming은 한 번 계산한 문제는 다시 계산하지 않도록 하는 알고리즘이다.

다음 조건을 만족할 때 사용할 수 있다.

1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다. 

피보나치 수열은 이러한 조건을 만족하는 문제다. 다이나믹 프로그래밍을 적용했을 때의 피보나치 수열 알고리즘의 시간 복잡도는 `O(N)`이다.

**다이나믹 프로그래밍의 2가지 방식**

- Top-Down (Memoization)

  탑 다운 방식은 '하향식'이라고도 하며, 메모이제이션은 탑다운 방식에 국한되어 사용되는 표현이다. 

- Bottom-Up

  보텀업 방식은 '상향식'이라고도 하며, 다이나믹 프로그래밍의 전형적인 형태다. 보텀업 방식에서 사용되는 결과 저장용 리스트는 'DP 테이블'이라고 부른다.

#### Top-Down

메모제이션, Memoization은 다이나믹 프로그래밍을 구현하는 방법 중 한 종류로, 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법을 의미한다. 메모이제이션은 값을 저장하는 방법이므로 캐싱, Caching이라고도 한다.

메모이제이션은 한 번 구한 정보를 리스트에 저장하는 것으로 구현할 수 있다. 다이나믹 프로그래밍을 재귀적으로 수행하다가 같은 정보가 필요할 때는 이미 구한 정답을 그대로 리스트에서 가져오면 된다.

메모이제이션은 때에 따라서 다른 자료형, 예를 들어 사전(`dict`) 자료형을 이용할 수도 있다. 사전 자료형은 수열처럼 연속적이지 않은 경우에 유용하다. 

```python
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현(Top-Down 다이나믹 프로그래밍)
def fibo(x):
  # 종료 조건(1 혹은 2일 때 1을 반환)
  if x == 1 or x == 2:
    return 1
  # 이미 계산한 적 있는 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]
  # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  d[x] = fibo(x - 1) + f(x - 2)
  return d[x]

print(fibo(99))
```

*피보나치 수열을 다이나믹 프로그래밍 없이 재귀 함수로만 표현하면 구현은 간편하지만, `O(2^n)`의 지수 시간이 소요되므로 심각한 문제가 발생할 수 있다.*

#### Bottom-Up

재귀 함수를 사용하면 컴퓨터 시스템에서는 함수를 다시 호출했을 때 메모리 상에 적재되는 일련의 과정을 따라야 하므로 오버헤드가 발생할 수 있다. 따라서 재귀 함수 대신에 반복문을 사용하여 오버헤드를 줄일 수 있다. 

```python
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(Bottom-Up 다이나믹 프로그래밍)
for i in range(3, n+1):
  d[i] = d[i - 1] + d[i - 2]
```

#### 다이나믹 프로그래밍 문제 접근

특정한 문제를 완전 탐색 알고리즘으로 접근했을 때 시간이 매우 오래 걸리면 다이나믹 프로그래밍을 적용할 수 있는지 해결하고자 하는 부분 문제들의 중복 여부를 확인해보자.

일단 단순히 재귀 함수로 비효율적인 프로그램을 작성한 뒤에 (탑다운) 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면, 즉 메모이제이션을 적용할 수 있으면 코드를 개선하는 방법도 좋은 아이디어다.

가능하다면 재귀 함수를 이용하는 탑다운 방식보다는 보텀업 방식으로 구현하는 것을 권장한다. 시스템상 재귀 함수의 스택 크기가 한정되어 있을 수 있기 때문이다. `recursion depth, 재귀 함수 깊이`와 같은 오류가 발생하면, `sys` 라이브러리에 포함되어 있는 `setrecursionlimit()` 함수를 호출하여 재귀 제한을 완화할 수 있다.



## 문제

### [1149 RGB거리](https://www.acmicpc.net/problem/1149)

문제) 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 인접한 집의 색을 다르게 칠하면서, 모든 집을 칠하는 비용의 최솟값을 출력하라. 

분류) 다이나믹 프로그래밍

해설) 다이나믹 프로그래밍을 이용하여 하나씩 다 저장하면 된다. i번째 행의 0번째 열에는 i+1번 집에 빨간 색, i번째 행의 1번째 열에는 초록색, i번째 행의 2번째 열에는 파란색을 칠하면서 최소 비용이 저장된다. 1번 집에 빨강, 초록, 파랑을 칠하는 모든 경우를 저장한 후에, 다음 집도 모든 색을 칠하는 경우의 비용을 저장한다. 다음 집부터는 앞 집의 색과 다르게 칠하면서 적은 비용을 저장한다. 예를 들어 빨간색을 칠하는 경우에는 앞집이 초록 또는 파란색을 칠한 것 중에 더 적은 비용으로 칠한 경우의 비용을 더해준다. 그렇게 마지막 집까지 칠해준 후, 마지막 집을 칠한 비용 중 최솟값을 출력한다. 

```python
import sys

read = sys.stdin.readline
N = int(read())
dp = [[0,0,0] for _ in range(N)]
dp[0] = list(map(int, read().split()))
for i in range(1, N):
  R, G, B = map(int, read().split())
  dp[i][0] = R + min(dp[i-1][1], dp[i-1][2])
  dp[i][1] = G + min(dp[i-1][0], dp[i-1][2])
  dp[i][2] = B + min(dp[i-1][0], dp[i-1][1])
print(min(dp[N-1]))
```



### [2156 포도주 시식](https://www.acmicpc.net/problem/2156)

문제) n개의 포도주 잔이 있을 때, 다음 규칙을 따르면서 최대로 마실 수 있는 포도주의 양을 출력하라. 

1. 포도주 잔을 선택하면, 그 잔에 들어있는 포도주는 모두 마셔야 한다.
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다. 

분류) 다이나믹 프로그래밍

해설) 연속 세 개를 마시면 안되므로, 다이나믹 프로그래밍을 사용하며 다양한 경우를 비교한다. dp의 `i`(0 ≤ `i` ≤ n-1)번째 값에는 i번째 포도주를 마시면서, 최대로 마실 수 있는 값이 저장된다. 3번째 값까지는 최대가 될 수 있는 경우를 각각 생각하고, 4번째 값부터는 점화식으로 값을 계산한다. `i`번째 포도주와 붙어있는 포도주(`i-1`번째 포도주)를 선택하는 경우와 `i`번째 포도주와 떨어져있는 포도주를 선택하는 경우로 나뉘어서 이 두 중 큰 값을 선택하면 된다. 떨어져있는 포도주를 선택하면 연속 세 개를 마시는 건 항상 피하게 되므로 바로 `dp[i-2]`를 더해주면 되고, 붙어있는 포도주를 선택하면 연속 세 개를 방지하기 위해서 `dp[i-4]`와 `dp[i-3]` 중 큰 값에 붙어있는 포도주(`i-1`번째 포도주)를 더해주면 된다. **`dp[i-4]`와도 비교를 해줘야 한다!** 마지막으로 `dp`에 저장된 값 중 최댓값을 출력하면 된다. 

참고) 좋은 반례 : https://www.acmicpc.net/board/view/67805

```python
import sys

read = sys.stdin.readline
n = int(read())
glasses = [0] * 10000
for i in range(n):
  glasses[i] = int(read())
dp = [0] * 10000
dp[0] = glasses[0]
dp[1] = glasses[0] + glasses[1]
dp[2] = max(glasses[0], glasses[1]) + glasses[2]
dp[3] = max((dp[0] + glasses[2]), dp[1]) + glasses[3]
for i in range(4, n):
  dp[i] = max((max(dp[i-3], dp[i-4]) + glasses[i-1]), dp[i-2]) + glasses[i]
print(max(dp))
```



### [1463 1로 만들기](https://www.acmicpc.net/problem/1463)

문제) 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들 때, 연산을 하는 횟수의 최솟값을 출력하라. 

분류) 다이나믹 프로그래밍

해설) 모든 가능한 경우를 저장하기 위해 다이나믹 프로그래밍을 사용한다. 경우를 세분화해서 복잡하게 생각하려고 하지 말고, 조건에 나온걸 단순하게 반영해야 하는 편이 더 좋다. 6의 배수는 3으로도 나누어 떨어지고, 2로도 나누어 떨어지므로 if-else문을 사용하지 말고 if문을 두 번 사용하여 두 경우 모두 계산한다. 1을 한 번 빼서 2의 배수가 되는 경우와 1을 두 번 빼서 3의 배수가 되는 경우까지 모두 계산하여 가장 작은 값을 매번 갱신한다.

```python
import sys

read = sys.stdin.readline
N = int(read())
dp = [int(1e6)]*(int(1e6)+1)
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, N+1):
  if i%3 == 0:
    dp[i] = dp[i//3] + 1
  if i%2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)
  dp[i] = min(dp[i], dp[i-1] + 1, dp[i-2] + 2)
print(dp[N])
```



### [12865 평범한 배낭](https://www.acmicpc.net/problem/12865)

문제) N개의 물건의 무게와 가치, 배낭에 넣을 수 있는 최대 무게 K가 주어질 때, 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력하라. 

분류) 다이나믹 프로그래밍

해설) `i`개의 물건을 담았을 때 무게가 `j`인 경우를 저장하는 `dp` 배열을 이용한다. 물건의 무게가 가능한 무게보다 무거울 때는 물건을 추가할 수 없으므로 `i-1` 개의 물건을 담았을 때와 가치합이 같다. 물건을 추가할 수 있다면, 이 물건을 추가하기 전과 이 물건의 무게만큼 물건을 빼고 이 물건을 추가했을 때의 가치합을 비교하여 더 큰 값을 갱신한다. 이를 반복하면 `N`개의 물건을 담았을 때 무게가 `K`인 값이 잘 저장되므로 이를 출력한다. 

메모) 어떤 값을 저장해야 도무지 아이디어가 떠오르지 않아서 구글링해서 푼 문제다. 다시 풀자!

```python
import sys

read = sys.stdin.readline
N, K = map(int, read().split())
things = [[0,0]]
for _ in range(N):
  W, V = list(map(int, read().split()))
  things.append([W, V])
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
  for j in range(1, K+1):
    w, v = things[i][0], things[i][1]
    if j < w:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[N][K])
```

