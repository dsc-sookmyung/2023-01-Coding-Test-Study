## 그리디
그리디 알고리즘은(탐욕법) 현재 상황에서 지금 당장 좋은 것만 선택하는 알고리즘이다. 이 알고리즘은 매 순간 가장 좋아 보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에
대해서는 생각하지 않는다.
<br>
Ex) 거스름돈 : 손님에게 거슬러줘야 할 돈이 N원일 때, 500원, 100원, 50원, 10원짜리 동전을 사용하여 거스름돈 동전의 최소 갯수 구하기 
```python
n = 1260
count = 0
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin
print(count)
```

### 1541 잃어버린 괄호
#### 풀이) 
- 숫자와 +, - 로 구성된 식을 입력받아 괄호를 넣어 결과가 최소가 되게 해줘야 한다.
- 기호를 기준으로 split해서 식을 받고, 그 다음 - 기호가 나오기 전까지의 합을 모두 더해 빼준다.

#### 예시) <br>
입력 : 3 + 4 - 3 - 10 + 24    # 식을 -를 기준으로 나눈다. 

'3 + 4'  '3'  '10 + 24'     # +를 기준으로 나눠 값을 더해준다. 

7  3  34     # 그 다음, 각 숫자들 사이에 빼기 연산을 해준다.

7 - 3 - 34 = -30

출력 :  -30

```python
import sys
input = sys.stdin.readline

cal = input().rstrip().split('-')  # input을 받을 때 -를 기준으로 split()해준다
num = []

for i in cal:
    tmp = i.split('+')
    sum = 0
    for j in tmp:
        sum += int(j)
    num.append(sum)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)

```

### 2217 - 로프
#### 풀이) 
- 로프를 N개 사용한다고 하면, 들어올릴 수 있는 물체의 최대 중량은 N * (N개 로프들 중 중량의 최솟값) 이다.
- 모든 로프를 사용하는게 아니므로, 각 로프가 들 수 있는 중량을 오름차순 정렬을 하고, 해당 로프가 포함되었을 때의 최대 중량을 계산하여 nums리스트에 넣어주어 최댓값을 찾는다.


```python
import sys
input = sys.stdin.readline

N = int(input())
weight = []
for _ in range(N):
    weight.append(int(input()))
weight.sort()

nums = []
for i in weight:
    nums.append(i*N)
    N -= 1
print(max(nums))
```

### 14916 - 거스름돈
#### 풀이)
- 2원과 5원을 사용해서 거스름돈을 줄 때, 최대한 5원 동전의 갯수가 많게 해주면 동전의 갯수가 최소가 된다.
- 거슬러줘야하는 금액이 5로 나누어 떨어지는지 확인하고, 5의 배수가 아니라면 2씩 빼주면서 5의 배수인지 확인한다.
- 최종적으로 나누어 떨어지지 않아서, 거슬러줘야하는 금액이 0보다 작아진다면 -1을 출력한다.

```python
import sys
input = sys.stdin.readline

n = int(input())
count = 0  # 동전의 갯수

while True:
    if n % 5 == 0:  # 5의 배수라면
        count += n // 5
        break
    else:
        n -= 2
        count += 1
    if n < 0:
        break
if n < 0:
    print(-1)
else:
    print(count)
```

### 11508 - 2+1 세일
#### 풀이)
- 최소비용이 되려면 3개씩 묶어서 구매할 때 무료로 지불하는 금액이 최대한 커져야 한다.
- 가격을 입력받아 sort()함수로 내림차순 정렬을 하고, 순서대로 3개씩 묶어서 구매하면 된다.
- 인덱스 번호가 2, 5, 8 .. 인 물건을 무료로 구매하기에, 3으로 나눴을 때 나머지가 2가 아니면 지불비용 result에 추가해준다.

```python
import sys
input = sys.stdin.readline

N = int(input())
costs = []
for _ in range(N):
    costs.append(int(input()))
costs.sort(reverse=True)

result = 0
for i in range(N):
    if i % 3 != 2:  # 나머지가 2가 아니면 -> result에 더해준다
        result += costs[i]
print(result)
```

### 13305 - 주유소
#### 풀이)
- 현재 지나가는 도시의 주유소 가격이 앞으로 지나가야 하는 도시들 중에 최솟값이라면(맨 마지막 도시를 제외하고) 남은 거리만큼 모두 구매하고, 최소가 아니라면 다음 도시로 이동하는데 필요한만큼만 구해하는 방법으로 풀었다.
- 서브태스크에서 입력받는 수가 커지는 경우를 고려하면, 첫 주유소 가격을 최솟값 변수에 넣어주고 각 도시를 이동할 때마다 주유소 값을 비교하여 넣어주는 방법이 더 효율적이다. 

```python
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# routes = list(map(int, input().split()))  # 도로 길이
# costs = list(map(int, input().split()))  # 리터당 가격
#
# result = 0
# for i in range(N-1):
#     min_costs = min(costs[i:N-1])
#     # print(min_costs)
#     if costs[i] == min_costs:
#         result += costs[i] * sum(routes[i:])
#         break
#     else:
#         result += costs[i] * routes[i]
# print(result)

import sys
input = sys.stdin.readline

N = int(input())
routes = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = 0
min_costs = costs[0]
for i in range(N-1):
    if costs[i] < min_costs:
        min_costs = costs[i]
    result += min_costs * routes[i]
print(result)
```

### 20365 - 블로그2
#### 풀이)
- 풀이 방법에 대해서는 빨리 와닿았는데, 딕셔너리를 활용한 구현이 쉽지 않았다.
- 딕셔너리 count를 만들어서 빨강과 파랑을 색칠할 횟수를 저장한다.
- 맨 처음에 무슨 색이던 일단 색칠해주고, for문을 돌면서 현재 색상과 이전 색상이 다르다면 딕셔너리에 카운트 해준다.
- 결과로는 딕셔너리에 저장한 B와 R 중 최솟값(해당 색상이 더 적은 것) + 1(전체를 색칠하는 횟수) 를 출력해준다. 

```python
import sys
input = sys.stdin.readline

N = int(input())
colors = list(input().rstrip())
count = {'B': 0, 'R': 0}  # 칠할 횟수 저장

count[colors[0]] += 1  # 맨 처음 색칠하기
for i in range(1, N):
    if colors[i] != colors[i-1]:  # 이전색과 다르다면
        count[colors[i]] += 1
# print(count)
print(min(count['B'], count['R']) + 1)

```
