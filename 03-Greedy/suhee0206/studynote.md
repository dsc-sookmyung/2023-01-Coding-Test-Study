# Greedy Algorithm

## 목차

- **[개념](#개념)**
  - [Greedy Algorithm](#greedy-algorithm)
- **[문제](#문제)**
  - [14916 거스름돈](#14916-거스름돈)
  - [2217 로프](#2217-로프)
  - [11508 2+1 세일](#11508-2+1-세일)
  - [13305 주유소](#13305-주유소)



## 개념

### Greedy Algorithm

현재 상황에서 지금 당장 좋은 것만 선택하는 알고리즘이다.

문제에서 '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 알게 모르게 제시해준다. 대체로 기준은 정렬 알고리즘을 사용했을 때 만족시킬 수 있으므로 그리디 알고리즘 문제는 자주 정렬 알고리즘과 짝을 이뤄 출제된다. 

어떤 코딩 테스트 문제를 만났을 때, 바로 문제 유형을 파악하기 어렵다면 그리디 알고리즘을 의심하고, 문제를 해결할 수 있는 탐욕적인 해결법이 존재하는지 고민해보자. 만약 오랜 시간을 고민해도 그리디 알고리즘으로 해결 방법을 찾을 수 없다면, 다이나믹 프로그래밍이나 그래프 알고리즘 등으로 문제를 해결할 수 있는지를 재차 고민해보는 것도 한 방법이다. 

*출처: [이것이 취업을 위한 코딩테스트다 with 파이썬](http://www.yes24.com/Product/Goods/91433923)*



## 문제

### [14916 거스름돈](https://www.acmicpc.net/problem/14916)

문제) 2원짜리와 5원짜리만으로 거슬러줄 때, 거스름돈이 n인 경우 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하라. 

분류) 그리디 알고리즘

해설) 동전을 최소로 사용해야하므로, 큰 단위인 5원을 먼저 사용하여 거스름돈을 구성한다. 5원의 개수를 최대로 해서 시작한 후에, 거스롬돈이 맞춰지지 않으면 5원을 한 개씩 줄인다. 

```python
import sys

n = int(sys.stdin.readline())

balance = 0
two = 0
five = n // 5

while True:
  balance = n - five*5
  two = balance // 2
  balance = balance - two*2
  if balance == 0:
    print(five + two)
    break
  if balance:
    if five:
      five = five - 1
    else:
      print(-1)
      break
```



### [2217 로프](https://www.acmicpc.net/problem/2217)

문제) 중량이 w인 물체에 k개의 로프를 병렬로 연결하면 로프에 모두 고르게 w/k만큼의 중량이 걸릴 때, 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구하라. N개의 로프를 모두 사용해야 할 필요는 없다. 

분류) 그리디 알고리즘

해설) N개의 로프가 버틸 수 있는 각각의 최대 중량을 큰 값 순으로 정렬한다. 물체에 중량은 균등하게 걸리므로, n번째로 큰 값을 가진 로프와 그보다 무거운 중량을 버틸 수 있는 로프들이 들어올릴 수 있는 중량이 같다. 따라서 n번째로 큰 값을 가진 로프를 기준으로 해서, 해당 로프와 그보다 무거운 중량을 버틸 수 있는 로프들만 사용해서 들어올릴 수 있는 물체의 최대 중량을 구한다.

```python
import sys

read = sys.stdin.readline

N = int(read())
data = [int(read()) for _ in range(N)]

data.sort(reverse=True)
max_weight = 0

for i in range(N):
  weight = (i+1) * data[i]
  if weight > max_weight:
    max_weight = weight

print(max_weight)
```



### [11508 2+1 세일](https://www.acmicpc.net/problem/11508)

문제) 유제품 3개를 한 번에 산다면 그중에서 가장 싼 것은 무료일 때, N팩의 유제품을 모두 살 때 필요한 최소비용을 구하라.  

분류) 그리디 알고리즘

해설) 가능한 가장 비싼 제품들로 꾸러미들을 만들자! 꾸러미에서 가장 싼 것이 비쌀 수록, 무료로 지불하는 제품의 가격이 높아져서 적은 비용을 사용해도 된다. 

우선 높은 가격 순으로 정렬한다. 가격순으로 세 개씩 묶는다고 생각하면, 묶음의 세 번째 제품은 무료다. 따라서 세 번째 제품을 제외한 제품들의 가격을 더한다. 

```python
import sys

read = sys.stdin.readline

N = int(read())
C = [int(read()) for _ in range(N)]
C.sort(reverse=True)

answer = 0
for i in range(N):
  if (i+1) % 3 == 0:
    pass
  else:
    answer = answer + C[i]

print(answer)  
```



### [13305 주유소](https://www.acmicpc.net/problem/13305)

문제) N개의 도시가 일직선 도로에 있고, 인접한 두 도시 사이의 도로들은 서로 길이가 다를 수 있다. 각 도시 마다 주유소가 있고, 주유소의 리터당 가격은 다를 수 있다. 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 출력하라. 

분류) 그리디 알고리즘

해설) 왼쪽에서 오른쪽으로 가면서 최소 기름값을 갱신하면 된다. 앞, 뒤 인덱스를 확인할 필요 없이 그때그때 기름값을 비교하면 된다. 

현재 도시의 기름값이 더 비싸면 최소 기름값을 그대로 사용하고, 
현재 도시의 기름값이 더 저렴하다면, 최소 기름값을 갱신하고 주유한다. 

메모) 처음에 무지 복잡하게 풀고 서브태스크 1번만 맞춰서 부분점수 17점만 받았다. 기름값을 갱신하기만 하면 된다는 컨셉을 혼자 떠올리지 못했다. 분발하자! 

```python
import sys

read = sys.stdin.readline

N = int(read())
L = list(map(int, read().split()))
C = list(map(int, read().split()))

answer = 0
min_cost = C[0]

for i in range(N-1):
  if C[i] < min_cost:
    min_cost = C[i]
  answer = answer + min_cost*L[i]

print(answer)  
```

