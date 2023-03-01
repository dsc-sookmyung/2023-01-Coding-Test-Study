# Binary Search

- **개념**
  - [이진 탐색](#이진-탐색)
- **문제**
  - [1789 수들의 합](#1789-수들의-합)
  - [2512 예산](#2512-예산)
  - [1654 랜선 자르기](#1654-랜선-자르기)
  - [22871 징검다리 건너기 (large)](#22871-징검다리-건너기-(large))




## 개념

### 이진 탐색

```python
# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
      end = mid - 1
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
      start = mid + 1
  return None

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)
```

탐색 범위가 2,000만을 넘어가면 이진 탐색으로 문제에 접근해보자! 처리해야 할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 `O(logN)`의 속도를 내야 하는 알고리즘을 떠올려야 문제를 풀 수 있는 경우가 많다.



## 문제 

### [1789 수들의 합](https://www.acmicpc.net/problem/1789)

문제) 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값을 구하라.

분류) 그리디 알고리즘

해설) 자연수를 최대한 많이 사용해야 하므로, 작은 자연수부터 더해나가면 된다. 1부터 차례대로 더하다가 합이 S보다 커지면 그만 더하고, 정답을 출력한다.

`S = 200`인 경우, `1+2+3+...+18+19 = 190`이고, `1+2+3+...+18+19+20 = 210`이다. 따라서 19개의 자연수를 사용하면 자연수를 최대한 많이 사용하는 것이 된다. `1+2+3+...+18+29 = 200`

참고) `sum < S`말고 `sum <= S`로 해야 된다. 

메모) 자연수의 합이라고 하니까 또 자연수 분할을 하려고 하고, 이번 주차 주제가 이진 탐색이니까 이진 탐색으로 풀려고 하면서 의미없는 고민을 한 문제다. 결국 이 쉬운 문제 때문에 오랜만에 정답 코드를 보러 가버리고 말았다. 편협해지지 말자! 

```python
import sys

read = sys.stdin.readline
S = int(read())

sum = 1
N = 1
while sum <= S:
  N += 1
  sum += N

print(N-1)
```



### [2512 예산](https://www.acmicpc.net/problem/2512)

문제) 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예상요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

배정된 예산들 중 최댓값인 정수를 출력하라. 

분류) 이진 탐색

해설) 이진 탐색을 이용하여 상한액을 구한다. 배정된 예산들 중 최댓값은, 상한액과 가장 큰 예산요청 중에서 더 작은 값이다. 

상한액의 최솟값(`start`)은 국가예산 총액을 지방의 개수로 나눈 값이며, 최댓값(`end`)은 가장 큰 예산요청이다. 

예산요청 값(`x`)이 상한액(`mid`)보다 작거나 같은 경우, 국가예산(`budget`)에서 예산요청 값(`x`)을 뺀다. 예산요청 값(`x`)이 상한액(`mid`)보다 큰 경우, 국가예산(`budget`)에서 상한액(`mid`)을 뺀다. 

각 지방의 예산요청에 대해 위 과정을 반복해준 후, 국가예산(`budget`)을 확인한다.

- 국가예산이 0이라면, 예산을 남김 없이 다 사용하여, 최대 상한액을 구한 것이므로 멈춘다. 
- 국가예산이 음수라면, 예산이 부족하여, 상한액을 높게 잡은 것이므로 설정되어 있던 상한액(`mid`)보다 작은 값들 중에서 상한액을 구한다.
- 국가예산이 양수라면, 예산이 남아서, 상한액을 적게 잡은 것이므로 설정되어 있던 상한액(`mid`)보다 큰 값들 중에서 상한액을 구한다. 국가예산이 남김 없이 다 사용되거나, 조금 남아야 올바르게 수행되는 것이므로, 최종 상한액(`limit`)은 국가예산이 양수일 때 계속 저장해준다.

이진 탐색을 구한 상한액(`limit`)과 가장 큰 예산요청(`max(requests)`)  중 더 작은 값이 구하고자 하는 배정된 예산들 중 최댓값이다. 

```python
import sys

read = sys.stdin.readline
N = int(read())
requests = list(map(int, read().split()))
M = int(read())

max_val = max(requests)

start = M // N
end = max_val
limit = 0

while start <= end:
  budget = M
  mid = (start + end) // 2
  for x in requests:
    if x <= mid:
      budget -= x
    else:
      budget -= mid
  if budget == 0:
    limit = mid
    break
  elif budget < 0:
    end = mid-1
  else:
    limit = mid
    start = mid+1

print(min(limit, max_val))
```



### [1654 랜선 자르기](https://www.acmicpc.net/problem/1654)

문제) K개의 랜선을 잘라서 N개의 같은 길이의 랜선을 만들 때, 만들 수 있는 최대 랜선의 길이를 구하라. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 

분류) 이진 탐색

해설) 이진 탐색을 이용해 만들 수 있는 최대 랜선의 길이를 구한다. N개보다 많이 만드는 것도 N개를 만드는 것에 포함되므로, 이진 탐색 시에 만들어진 랜선의 개수(`count`)가 필요한 랜선의 개수(`N`)보다 1. 크거나 같을 때와, 2. 작을 때 두 가지로만 경우를 나누면 된다. 

랜선의 최소 길이는 정수이므로 1, 최대 길이는 가장 긴 랜선으로 두고, 이진 탐색을 수행한다.

메모) 실수 포인트

- `count == N`일 때 `break`를 해버리면 안된다! 같은 `count`라도 랜선 길이는 다를 수 있기에 `count == N`이더라도 이진 탐색을 계속해야 한다.
- `N`은 1이상이므로 `start`를 1로 초기화하자. `start`가 0이면, `ZeroDivisionError`가 발생할 수 있다. 

```python
import sys

read = sys.stdin.readline
K, N = map(int, read().split())
cables = list(int(read().strip()) for _ in range(K))

start = 1
end = max(cables)
answer = 0

while start <= end:
  mid = (start + end) // 2
  count = 0
  for cable in cables:
    count += cable // mid
  if count >= N:
    answer = mid
    start = mid + 1
  else:
    end = mid - 1

print(answer)
```



### [22871 징검다리 건너기 (large)](https://www.acmicpc.net/problem/22871)

문제) 수 A1, A2, ..., A3, ..., AN가 부여되어 있는 N개의 돌이 일렬로 나열되어 있다. 가장 왼쪽에 있는 돌에서 출발하여 가장 오른쪽에 있는 돌로 건너가려고 한다. 

1. 항상 오른쪽으로만 이동가능하다.
2.  i번째 돌에서 j(i < j)번째 돌로 이동할 때 (j - i) x (1 + |Ai - Aj|) 만큼 힘을 쓴다.
3. 돌을 한번 건너갈 때마다 쓸 수 있는 힘은 최대 K이다.

가장 왼쪽 돌에서 출발하여 가장 오른쪽에 있는 돌로 건너갈 수 있는 모든 경우 중 K의 최솟값을 구하라.

분류) 다이나믹 프로그래밍

해설) 힘을 최소로 사용해서 돌을 건너고, 돌을 건너며 사용한 힘 중 가장 큰 힘을 구하는 문제다. 힘을 최소로 사용한다고 하니, 다이나믹 프로그래밍을 이용한 풀이밖에 생각나지 않았다. 

배열 `d`를 이용하여 `d[i]`에 `i`번째 돌까지 가면서 한 번 건너갈 때 쓴 최대 힘 `K` 중 최솟값을 저장한다. 가장 마지막 돌은 `N-1`번째 돌이므로, `d[N-1]`을 출력하면 된다.

`i`번째 돌까지 갈 수 있는 모든 경우에 대해 다음을 수행한다.

`i`이전의 돌(`j`번째 돌)에 대하여, `j`번째 돌에서 `i`번째 돌로 이동할(건너갈) 때 쓰는 힘을 구한다. `d[j]`에는 `j`번째 돌까지 가면서 한 번 건너갈 때 쓴 최대 힘 `K`가 저장되어 있으므로, `i`번째 돌의 `K`는 앞에서 구한 힘과 `d[j]` 중 더 큰 값이다. `K`의 최솟값을 구해야하므로, `i` 왼쪽에 있는 돌(`j`)에서 `i`로 건너오는 모든 경우 중 가장 작은 `K`를 `d[i]`에 저장한다.

메모) 내 힘으로만 작성했던 풀이는 `d` 뿐만 아니라 다른 배열들도 이용했는데, 계속 `틀렸습니다`가 나왔다. 

```python
import sys

read = sys.stdin.readline
N = int(read())
A = list(map(int, read().split()))

INF = 1e9
d = [0] + [INF]*(N-1)
#d[1] = (1-0)*(1+abs(A[1]-A[0]))

for i in range(1, N):
  for j in range(i):
    force = max((i-j) * (1 + abs(A[i] - A[j])), d[j])
    d[i] = min(d[i], force)

print(d[N-1])
```

