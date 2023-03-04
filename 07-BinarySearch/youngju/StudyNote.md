# BinarySearch
## 1789 수들의 합 
n중 최댓값을 구하므로 반복문을 통해 1부터 더하면서 S를 기준으로 n을 구했다. 

```python
S = int(input())  
answer = 0  
result = 0  
for i in range(1, S+1):  
    result += i  
    if result == S:  
        answer = i  
    if result > S:  
        answer = i - 1  
  break  
print(answer)
```

**[풀이]**
1) 반복문을 통해 1부터 차례대로 더한 값을 result에 계속 저장 
2) result가 S와 같다면 N = i이므로 answer값을 i로 설정 
3) result가 S보다 커졌다면 N은 방금 더한 i 보다 1작아야 하므로 answer값을 i-1로 설정 
4) 반복문을 멈추고 answer를 출력 

<br/>

## 2512 예산 
상한액을 1부터 예산 요청들 중 최댓값 사이에서 이분탐색을 통해 구한다. 

```python
import sys

read = sys.stdin.readline
N = int(read().strip())
budgets = list(map(int, read().split()))
M = int(read().strip())


def sum_budgets(limit):
    result = 0
    for b in budgets:
        if b > limit:
            result += limit
        else:
            result += b

    return result


answer = 0
if sum(budgets) <= M:
    answer = max(budgets)
else:
    cnt = 0
    left = 1
    right = max(budgets)
    while left <= right:
        mid = (left + right) // 2
        if sum_budgets(mid) > M:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid

print(answer)
```


**[풀이]**
1) 여러 지방의 예산 요청들을 budgets 리스트에 저장 
2) 문제에서 말한 < ① 모든 요청이 배정될 수 있는 경우>는 sum(budgets)가 M보다 작거나 같을 때이므로 이때는 max(budgets)를 출력 
3) 문제에서 말한 < ② 모든 요청이 배정될 수 없는 경우 >일 때 이분 탐색을 시작 
4) 최솟값을 left에 1로 설정 하고 최댓값을 right에 max(budgets)로 설정 후 left가 right보다 작거나 같을 때까지 계속해서 값을 탐색 
5) mid를 설정하고 mid를 기준으로 필요한 총 금액을 sum_budgets()메서드를 통해 구한다 
6) sum_budgets()로 구한 값을 M과 비교하여 M보다 크면 right를 mid-1로 줄여주고 M보다 작거나 같으면 left를 mid+1로 설정 
7) 총 예산이 M을 넘으면 안되므로 left를 늘려줄 때 answer가 mid로 갱신되도록 하고 answer를 출력 

<br/>

##  1654 랜선 자르기 
랜선의 최대 길이를 1부터 랜선 길이들 중 최댓값 사이에서 이분탐색을 통해 구한다. 

```python
import sys

read = sys.stdin.readline
k, n = map(int, read().split())
length = [int(read().strip()) for _ in range(k)]
line = max(length)

left = 1
right = line
while left <= right:
    mid = (left + right) // 2

    result = 0
    for l in length:
        result += l // mid

    if result < n:
        right = mid - 1
    else:
        left = mid + 1

print(right)
```

**[풀이]**
1) k개의 랜선의 길이를 length리스트에 저장 
2) length리스트 중 최댓값을 line에 저장 
3) left를 1로 right를 line으로 설정한 뒤 left가 right를 넘지 않을 때까지 이분 탐색을 시도 
4) mid를 설정하고 length를 돌면서 총 몇 개의 랜선이 나오는지 구한다(result) 
5) result를 n과 비교하여 n보다 작으면 right를 mid-1로 줄여주고 n보다 크거나 같으면 left를 mid+1로 늘려준다
6) 이때 랜선의 최대 길이를 구해야 하므로 right를 출력 

<br/>

## 22871 징검다리 건너기(large) 
이분 탐색을 통해 풀려고 시도하다가 결국엔 구글링을 통해 dp로 푸는 방법으로 풀게 되었다😭 

```python
import sys

INF = 999999999
read = sys.stdin.readline

n = int(read())
nlist = list(map(int, read().strip().split()))
dp = [0] + [INF] * (n - 1)

for i in range(1, n):
    for j in range(0, i):
        power = max((i - j) * (1 + abs(nlist[i] - nlist[j])), dp[j])
        dp[i] = min(dp[i], power)

print(dp[-1])
```

**[풀이]**
1) 먼저 돌의 수를 nlist에 입력 받고 dp를 사용하기 위해 dp배열을 만든다 
> dp배열은 첫 번째 돌에서 인덱스 돌까지 가는 모든 경우의 수중 가장 힘이 작게 들 때의 힘을 저장해주기 위함 
2) 돌을 건너는 힘 중 최솟값을 구해야 하므로 dp배열 0번째를 제외하고 모두 INF를 통해 값을 채워준다 
3) i는 dp의 인덱스로 0번째 돌에서 1번째, 2번째...돌까지 가는 것을 의미 
4) j는 i까지 갈 때에 중간 과정에서 가장 마지막에 밟을 돌을 의미
> 즉, (0번째 돌 -> j번째 돌) -> (j번째 돌 -> i번째 돌) 로 i번째 돌까지 가는 모든 경우의 수를 구하는 것이다. 
이때 각 경우에서 드는 힘은 (0번째 돌 -> j번째 돌) 과 (j번째 돌 -> i번째 돌) 에서 드는 힘을 비교하여 둘 중 더 큰 값이 한 경우에서 드는 최종 힘의 값이다
5) 각 과정에서 드는 힘을 power라고 하면 power는 문제에서 주어진 식으로 (j번째 돌 -> i번째 돌)에서 드는 힘과 dp[j]에 저장된 (0번째 돌 -> j번째 돌)에서 드는 힘을 비교하여 더 큰 값을 저장
6) 이렇게 모든 경우에 대해 power를 계속 갱신하면서 dp[i]에 더 작은 값을 계속 저장
7) dp배열이 다 채워지면 문제에서 가장 오른쪽에 있는 돌로 건너갈 때 드는 힘 중 최솟값을 구하라고 했으므로 dp배열 중 가장 마지막 원소의 값을 출력 
