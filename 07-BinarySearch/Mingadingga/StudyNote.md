배열 내부의 데이터가 정렬되어 있을 때 빠르게 데이터를 찾을 수 있다. 이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다. 시간 복잡도는 O(logN)이다. 처리해야할 데이터의 개수가 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN)의 속도를 낼 수 있는 알고리즘으로 접근하자.

파라메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다. 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 파라메트릭 서치를 사용한다. 코딩 테스트에서 보통 파라메트릭 서치 유형은 이진 탐색을 이용해 해결한다.

## 이진 탐색

탐색 범위의 시작점, 끝점, 중간점 변수가 필요하다. 타겟 데이터와 중간점의 데이터를 반복적으로 비교해서 원하는 데이터를 찾는다. 만약 타겟이 더 작다면 중간점의 왼쪽에 위치한 것이므로 끝점을 중간점-1로 수정, 타겟이 더 크다면 오른쪽에 위치한 것이므로 시작점을 중간점+1로 수정하여 탐색한다. 재귀함수 혹은 반복문으로 구현할 수 있다.

```python
def binary_search(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	if array[mid] == target:
		return mid
	elif array[mid] > target: # 왼쪽
		return binary_search(array, target, start, mid - 1)
	else: # 오른쪽
		return binary_search(array, target, mid + 1, end)
```

```python
def binary_search(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		if array[mid] == target:
			return mid
		elif array[mid] > target: # 왼쪽
			end = mid - 1
		else: # 오른쪽
			start = mid + 1
```

## 이진 탐색 트리

큰 데이터를 처리하는 소프트웨어는 대부분 트리 자료구조로 저장해서 이진탐색과 같은 탐색 기법을 이용해 빠른 탐색이 가능하다. 이진 탐색 트리는 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다. 이진 탐색 트리는 자료를 **왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드** 규칙에 따라 저장한다. 탐색하고자하는 타겟 데이터가 부모 노드보다 작다면 왼쪽 서브트리를, 크다면 오른쪽 서브트리를 탐색한다. 자식 노드가 없을 때까지 원소를 찾지 못했다면, 이진 탐색 트리에 원소가 없는 것이다.

```python
class Node:
    def __init__(self, value):
        # double linked list
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head  # 루트노드

    # 삽입
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:  # 이미 가지고 있다면
                    self.current_node = self.current_node.left  # 비교대상을 바꾼다.
                else:
                    self.current_node.left = Node(value)  # 없다면 새로 만들어 연결시킨다.
                    break
            else:
                if self.current_node.right != None:  # 이미 가지고 있다면
                    self.current_node = self.current_node.right  # 비교대상을 바꾼다.
                else:
                    self.current_node.right = Node(value)
                    break

    # 이진 탐색 트리 출력
    def search(self, value):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:  # 찾았다
                return True
            elif value < self.current_node.value: # 왼쪽
                self.current_node = self.current_node.left  # 비교대상 바꾸기
            else: # 오른쪽
                self.current_node = self.current_node.right  # 비교대상 바꾸기
        return False  # 다 찾아봤는데 없다.

# 실행
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)

print(BST.search(2))
print(BST.search(5))
```

# [1789 수들의 합](https://www.acmicpc.net/problem/1789)

> 접근 방법

원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 파라메트릭 서치를 사용한다. 
코딩 테스트에서 보통 파라메트릭 서치 유형은 이진 탐색을 이용해 해결한다. 
이 문제에서도 이진 탐색을 사용하여 n의 최댓값을 찾았다.
1부터 n까지의 합이 s보다 작으면 n의 탐색 범위를 중간값의 오른쪽으로 잡고,
1부터 n까지의 합이 s보다 크다면 n의 탐색 범위를 중간값의 왼쪽으로 잡는다.
이때 n의 최댓값을 찾고 있으므로 이왕이면 중간값의 오른쪽에서 탐색할 때 결과값을 업데이트한다.


> 통과한 코드

```python
import sys

read = sys.stdin.readline
s = int(read())

def binary_search(start, end):
  answer = s
  while start <= end:
    mid = (start + end) // 2
    total = (mid * (mid + 1)) // 2
    # 최댓값 찾으니까 이왕이면 오른쪽으로 범위를 좁힐 때 저장
    if total <= s:
      answer = mid
      start = mid + 1
    else:
      end = mid - 1
  return answer
  
print(binary_search(1, s))
```


# [2152 예산](https://www.acmicpc.net/problem/2512)

> 접근 방법

원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제이므로 이진 탐색을 사용해보자.
다음과 같이 이진 탐색을 진행하면 된다. 시간 복잡도는 O(logN)이다.
1. 상한선이 mid 값일 때 지급 가능한 예산 총액을 구한다
2. 계산한 총액이 보유 총액보다 작다면, 상한선을 더 올려도 된다는 뜻이므로 오른쪽을 탐색한다. 상한선의 최댓값을 찾고 있으므로 이때 결과값을 업데이트한다.
3. 계산한 총액이 보유 총액보다 크다면, 상한선을 내려야 한다는 뜻이므로 왼쪽을 탐색한다.


> 통과한 코드

```python
import sys

read = sys.stdin.readline
n = int(read())
requests = list(map(int, read().split()))
total = int(read())

def search_max_limit(start, end, requests, total):
  answer = 0
  while start <= end:
    mid = (start + end) // 2
    able_total = calculate_able_total(requests, mid)
    if able_total <= total:
      start = mid + 1
      answer = mid
    else:
      end = mid - 1
  return answer
  
def calculate_able_total(requests, mid):
  result = 0
  for request in requests:
      if request < mid:
        result += request
      else:
        result += mid
  return result
  
if sum(requests) < total:
  print(max(requests))
else:
  print(search_max_limit(1, max(requests), requests, total))
```


# [1654 랜선 자르기](https://www.acmicpc.net/problem/1654)

> 접근 방법

1. 탐색 범위는 가장 긴 막대에서 시작해 줄여나간다.
2. 길이가 mid 값일 때 만들 수 있는 랜선의 최대 개수를 구한다.
3. 개수가 n보다 작다면, 길이를 줄여야 하므로 왼쪽을 탐색한다.
4. 개수가 n보다 크다면, 길이를 늘여야 하므로 오른쪽을 탐색한다. 
잘리는 개수가 n보다 커도 되기 때문에 개수 == n인 경우도 큰 경우와 동일하게 취급한다.
이 문제는 잘리는 최대 길이를 구하는 것이므로 탐색이 끝났을 때 end를 출력해야한다.


> 통과한 코드

```python
import sys

read = sys.stdin.readline
k, n = map(int, read().split())
lengths = [int(read()) for _ in range(k)]


def search_max_cnt(start, end, lengths, n):
    while start <= end:
        mid = (start + end) // 2
        able_cnt = calculate_able_cnt(lengths, mid)
        if able_cnt < n:
            end = mid - 1
        else:
            start = mid + 1
    return end


def calculate_able_cnt(lengths, mid):
    result = 0
    for length in lengths:
        result += (length // mid)
    return result


print(search_max_cnt(1, max(lengths), lengths, n))
```


# [22871 징검다리 건너기](https://www.acmicpc.net/problem/22871)

> 접근 방법

이 문제... 구글링했다.
이진 탐색으로 풀려고 시도했으나 상한값을 정하고 줄여가면서 푸는 것보다는 dp가 더 효율적일 것 같아 dp로 시도했다.

dp[i]는 첫번째 돌에서 출발해 I번째 돌에 도착하는 경우의 최소 힘을 가진다. 최종 출력은 dp[n-1] 이다. 이제 반복문을 n번 돌면서 dp를 채우면 된다.
I번째 반복에서 dp[i] 값을 구한다. 이 값은 첫 돌에서 출발해 I번째 돌에 도착하는 최소 힘이다. 첫 돌에서 도착지로 바로 갈 수도 있고, 징검다리를 거쳐 갈 수도 있다. 첫번째 돌부터 I-1번째 돌까지 거쳐갈 수 있으므로 또 반복문을 돌면서 j번째 돌을 거칠 때 I에 도착하는 최소 힘을 구한다.
내부 반복문에서는 1->j->I 경로의 힘을 구한다. 주의할 것은 배열에 저장하는 값이 위 경로의 합이 아니라, j->I로 이동하는 힘이어야한다는 것이다. (이것 때문에 문제 이해가 어려웠다) 따라서 1->j의 최소 힘을 나타내는 dp[j]와 j->I 힘을 비교해 더 큰 값을 구한다. 그 이유는 합이 최소가 되어야 하는데, j->I 가 dp[j]보다 크다면 그 값은 최소가 될 수 없기 때문에 더하지 않는 것이다.
어찌저찌 이해는 했지만 아직 혼자 힘으로 풀기는 어려운 것 같다. 좀더 쉬운 문제부터 풀어야할 것 같다🥲


> 통과한 코드

```python
import sys
INF = 2e9

read = sys.stdin.readline
n = int(read())
stones = list(map(int, read().split()))
dp = [0] + [INF] * (n - 1) # dp[i]: i번째 돌에 도착하는 힘의 최솟값

for i in range(1, n): # 도착하는 돌이 두번째~마지막일때, 각 경우의 최솟값을 구한다
  for j in range(0, i): # 도착 돌이 i이고 시작으로 j를 밟고 갈때, i번째까지 가는 힘의 최소값을 구한다
    power = max(dp[j], (i - j) * (1 + abs(stones[i] - stones[j]))) # ??? 
    dp[i] = min(dp[i], power)
print(dp[n - 1])
```


# [3079 입국심사](https://www.acmicpc.net/problem/3079)

> 접근 방법

심사에 걸리는 시간을 상한값으로 두고 탐색한다.
상한값이 조정되는 조건은 제한 시간 안에 심사를 받을 수 있는 사람의 수로 한다.
- 심사 가능 인원 < 총 인원: 부족함. 상한값 올려서 오른쪽 탐색
- 심사 가능 인원 >= 총 인원: 여유 있음. 상한값 줄여서 왼쪽 탐색, 최솟값 구하니까 줄일 때 결과 업데이트


> 통과한 코드

```python
import sys

read = sys.stdin.readline
n, m = map(int, read().split())
counters = [int(read()) for _ in range(n)]
start, end = 0, max(counters) * m
answer = 0


def calculate_able_count(delays, time_limit):
  able_count = 0
  for delay in delays:
    able_count += (time_limit // delay)
  return able_count

while start <= end:
  mid = (start + end) // 2
  able_count = calculate_able_count(counters, mid)
  if able_count < m:
    start = mid + 1
  else:
    end = mid - 1
    answer = mid

print(answer)
```

