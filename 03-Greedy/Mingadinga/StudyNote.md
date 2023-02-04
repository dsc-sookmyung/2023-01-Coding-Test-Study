# Greedy
탐욕 알고리즘은 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법이다. 각 단계에서 최선의 선택을 한 것이 전체적으로도 최선인 상황에서 사용할 수 있는 알고리즘이다.

그리디 알고리즘은 동적 프로그래밍 사용 시 지나치게 많은 일을 한다는 것에서 착안하여 고안된 알고리즘이다. 동적 프로그래밍을 사용하여 풀 수 있는 문제 중 부분 최선이 전체 최선인 경우, 시간 복잡도를 줄이기 위해 사용한다. 예를 들어 최소 비용을 구하는 문제에서 언제나 비용이 작은 것을 골랐을 때 그 답이 곧 전체의 최소 비용이 되는 경우이다. 

출처 : [제로초님 블로그](https://www.zerocho.com/category/Algorithm/post/584ba5c9580277001862f188)


# [14916 거스름돈](https://www.acmicpc.net/problem/14916)
> 접근 방법 

거스름돈 동전 개수가 최소가 되려면 더 비싼 동전인 5원을 많이 줘야 한다. 우선 5원으로 거스름돈을 줄 수 있는지 확인하고, 가능하다면 5원만 사용해서 거슬러준다. 5원만으로 거슬러줄 수 없다면, 2원을 하나 사용하고 거스름돈을 차감해 5원짜리로 거슬러줄 수 있는지 확인한다. 이렇게 하면 5원을 최대한 많이 사용해 거슬러줄 수 있으므로 동전 개수가 최소가 된다.

> 통과한 코드
```python
import sys

balance = int(input())
coin_count = 0

while True:
    if balance % 5 == 0: # 5원짜리 사용 가능
        coin_count += balance // 5
        break
    else: # 2원짜리 사용할 수 있도록 차감
        balance -= 2
        coin_count += 1

    if balance < 0: # 더이상 거슬러줄 수 없음
        break

if balance < 0:
    print(-1)
else:
    print(coin_count)
```


# [2217 로프](https://www.acmicpc.net/problem/2217)
> 접근 방법
로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구한다. 이때 로프는 임의의 개수를 사용해도 상관 없다. 

로프들을 사용해 들어올릴 수 있는 최대 중량은 로프 중 들어올릴 수 있는 중량이 가장 작은 로프가 결정한다. 로프를 세 개를 모두 사용할 때 최대 중량은 가장 약한 로프의 최대 중량 * 3(로프 개수)이다. 로프의 개수와 어떤 로프를 선택했는지에 따라 최대 중량이 달라지는데, 어차피 최대 중량을 구하는 것이므로 모든 조합을 따지기 보다는, 개수에 맞춰 튼튼한 로프들의 조합으로 비교하는 것이 더 효율적이다. 따라서 개수가 1개, 2개, ... , n개 선택했을 때 버틸 수 있는 최대 중량을 구해서 가장 큰 값을 구하면 된다.
> 통과한 코드
```python
import sys

rope_count = int(input())
ropes_weight = []

for i in range(rope_count):
    ropes_weight.append(int(input()))
ropes_weight.sort(reverse=True)

max_weight_per_rope = []
for j in range(rope_count):
    max_weight_per_rope.append(ropes_weight[j] * (j+1))

print(max(max_weight_per_rope))
```


# [11508 2+1 세일](https://www.acmicpc.net/problem/11508)
> 접근 방법

최소비용으로 유제품을 구입해야 한다. 세개씩 샀을 때 가장 가격이 싼 제품은 무료로 받을 수 있다. 최소비용이려면 각 묶음에서 무료로 받을 수 있는 제품이 가장 비싸야 한다. 그러려면 제일 비싼 제품 순으로 세개씩 묶어서 사면 된다. 총 금액은 전체 금액의 합계 - 내림차순 정렬한 금액 기준 2, 5, .. , 3n - 1번째 금액을 더하면 된다.


> 통과한 코드
```python
import sys

yogurt_count = int(input())
yogurt_price = []

for i in range(yogurt_count):
    yogurt_price.append(int(input()))
yogurt_price.sort(reverse=True)

free_price = 0
for i in range(2, len(yogurt_price), 3):
  free_price += yogurt_price[i]

print(sum(yogurt_price) - free_price)
```


# [13305 주유소](https://www.acmicpc.net/problem/13305)
> 접근 방법

도시로 이동하는 최소의 비용을 계산한다. 이동 비용이 최소이려면 기름 값이 싼 곳에서 충전하면 된다. 문제를 풀때 자꾸 머릿속에서 턱턱 걸리는 것이 있었는데, 그건 바로 기름의 구입 순서였다. 문제를 풀 때는 지금 방문한 도시의 기름값이 다음 도시의 기름값보다 쌀지 알 수 없고, 이 도시를 지나면 다음 도시에선 이 가격으로 못 살텐데 얼마나 기름을 구입하는 것이 최적일지 어떻게 확신하지?!라는 고민을 했다. 하지만 이건 현실이 아니고 알고리즘 문제기 때문에 어느 도시의 기름값이 가장 싼지 알 수 있다. (현실에서도 인터넷만 있다면 알 수 있다 바보야) 그래서 최소 비용으로 도시를 이동하려면, 더 싼 기름으로 이동하면 된다. 현재 방문한 도시의 기름값이 이전의 방문했던 도시들의 기름값보다 싸다면 다음 도시로 이동할 때는 이 도시에서 기름을 구입한다. 만약 다음 도시의 기름이 현재 가장 싼 기름값보다 싸지 않다면, 현재 가장 작다고 저장된 기름 가격으로 이동하면 된다.  


> 오류 : 런타임 에러

아무 생각없이 파이썬 input()으로 입력을 받았는데, 채점 8% 쯤에서 런타임 에러가 발생하며 실패했다. 알고보니 파이썬은 한 줄로 입력되는 숫자들은 input()으로는 입력 받을 수 없고, 스트림으로 입력 받아 공백으로 분리하고 리스트로 변환해야한다더라. 그래서 `list(map(int, read().split()))`를 사용해 입력받았다.
참고한 자료 : [백준 QA!](https://www.acmicpc.net/board/view/10856)

```python
import sys

read = sys.stdin.readline

city_count = int(input())
city_length = []
oil_price = []

for i in range(city_count - 1):
    city_length.append(int(input()))

for i in range(city_count):
    oil_price.append(int(input()))

min_oil_price = oil_price[0]
min_total_price = min_oil_price * city_length[0]
for i in range(1, city_count - 1):
    if min_oil_price > oil_price[i]:
        min_oil_price = oil_price[i]
    min_total_price += min_oil_price * city_length[i]

print(min_total_price)
```

> 통과한 코드
```python
import sys

read = sys.stdin.readline

city_count = int(input())
city_length = list(map(int, read().split()))
oil_price = list(map(int, read().split()))

min_oil_price = oil_price[0]
min_total_price = min_oil_price * city_length[0]
for i in range(1, city_count - 1):
    if min_oil_price > oil_price[i]:
        min_oil_price = oil_price[i]
    min_total_price += min_oil_price * city_length[i]

print(min_total_price)
```