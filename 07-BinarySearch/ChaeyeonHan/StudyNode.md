# 이진탐색

- 데이터가 정렬되어 있을 때, 탐색 범위를 절반씩 좁혀가며 빠르게 데이터를 찾을 수 있다.
- 이진탐색은 탐색 범위가 큰 상황에서의 탐색을 가정하는 문제가 많다. 
```python
# 이진탐색 재귀함수 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:  # 중간값이 찾으려는 값보다 작은 경우 왼쪽으로
        return binary_search(array, target, start, mid-1)
    else:  # 중간값이 찾으려는 값보다 큰 경우 오른쪽으로
        return binary_search(array, target, mid+1, end)

# 이진탐색 반복문 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None
    
```

## 문제
### 1789 수들의 합
- 1부터 n까지의 합을 구하는 공식은 n*(n+1) /2 이다.
- n의 최댓값을 구하는 문제이므로, 1부터 차례대로 자연수를 더해나가다가, 더한 값이 S보다 커지게 되면 그 갯수에서 1을 빼서 답을 구한다.

```python
import sys
input = sys.stdin.readline
S = int(input())
n = 1

while n*(n+1) / 2 <= S:
    n += 1

print(n-1)
```
### 2512 예산
- 예산을 설정할 수 있는 금액의 범위를 가장 작은 0부터 상한선 max(nums)까지 둔다.
- 이분탐색을 실행해주는데, 총 예산을 카운트해주는 total 변수에 각 지방의 예산을 더해준다.
- 이때, 상한액인 mid보다 예산이 크다면 상한액을 더해주고, mid보다 예산이 작다면 예산을 total에 더해준다.
- 모든 지방에 대해 위의 과정을 반복해주고, 총 합산된 예산을 확인해준다. 
- 합산한 예산이 입력받은 예산 m보다 작으면, 시작점을 mid+1로 이동시켜준다.(즉, 상한선을 올린다)
- 합산한 예산이 입력받은 예산 m보다 크면, 끝점을 mid-1로 이동시켜준다.(상한선을 내려준다)

```python
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())  # 예산
start, end = 0, max(nums)
# 예산 index를 기준으로 잡고 탐색할지, 예산 값을 기준으로 탐색할지

# 이진탐색으로 0~m까지의 수에서 상한액찾기
while start <= end:
    mid = (start + end)//2
    total = 0
    for i in nums:
        if i >= mid:  # 상한액 초과
            total += mid
        else: 
            total += i
    if total <= m: 
        start = mid+1
    else: 
        end = mid-1
print(end)
```
### 1654 랜선 자르기
- 탐색할 랜선의 길이를 최소 1에서 가장 긴 랜선의 길이인 max(length)로 잡아준다.
- 자르는 랜선의 길이가 mid일때 가능한 갯수를 cnt변수에 저장해 갯수를 세준다.
- 갯수가 n보다 작다면, 자르는 길이를 줄여야 하기에 end = mid - 1을 해준다.
- 갯수가 n보다 크다면, 자르는 길이를 늘여야 하기에 start = mid + 1을 해준다. 
- 랜선의 최대 길이를 구하는 것이기에 end를 출력해줘야 한다!!
```python
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]

# 탐색할 자를 길이의 범위가 (1 ~ 가장 긴 랜선의 길이)
start, end = 1, max(length)
# print(start, end)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in length:
        cnt += i // mid  # 주어진 랜선 길이에서 몇 개 만들수 있는지
    if cnt >= N:
        start = mid + 1
    else:
        end = mid -1
print(end)
```
### 28871 징검다리 건너기
- 하나씩 모두 탐색하며 값을 찾아주려 했지만, 모두 다 탐색하는 것은 너무 많다는 생각이 들어 고민하다 구글링을 통해 참고했다.
- DP를 사용해서 풀어주는데, dp[i]에는 첫번째 돌에서 i번째 돌까지 건너가는 모든 경우 중, 힘이 가장 적게 드는 경우의 값이 들어간다.
- 가장 오른쪽에 있는, 마지막에 있는 돌로 건너가는 경우이기에 dp[n-1]을 출력해준다.
- j번째 돌에서 i번째 돌로 이동할 때 필요한 힘을 구하고, j번째 돌까지 갈때 필요한 최대 힘이 저장되어 있는 dp[j]와 비교해 더 큰값을 power에 넣어준다.
- dp[i]의 값과 힘을 비교하여 작은 값을 dp[i]에 저장해준다.
```python
import sys
input = sys.stdin.readline

N = int(input())
rocks = list(map(int, input().split()))

INF = 999999999
dp = [0] + [INF] * (N-1)

for i in range(1, N):
    for j in range(0, i):
        power = max((i-j) * (1 + abs(rocks[i]-rocks[j])), dp[j])
        dp[i] = min(dp[i], power)

print(dp[-1])
```