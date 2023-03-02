# 정렬

## 정렬 종류와 비교

- 계수 : O(N+K) 최댓값이 백만 이하이고, 데이터 중복이 많으면 유리하다
- 정렬 라이브러리 : O(NlogN) 무난하게 사용 가능
- 퀵 : O(NlogN) 데이터 특성을 파악하기 어렵다면 사용. 이미 데이터가 정렬되어있다면 느리다
- 삽입 : O(N^2) 이미 데이터가 거의 정렬되어있다면 매우 빠름. 정렬 범위를 넓히는 알고리즘
- 선택 : O(N^2) 가장 작은 데이터를 앞으로 보내는 알고리즘

## 계수 정렬

데이터가 정수이고, 가장 큰 데이터와 작은 데이터의 차이가 백만 이하이면 사용할 수 있다. 데이터 중복이 많다면 유리하다. 데이터 개수가 N, 데이터 중 최댓값이 K라면 최악의 경우 시간 복잡도 O(N+K)이다.

숫자 리스트에서 숫자가 나타난 횟수를 세서, 출력할 때 해당 횟수만큼 숫자를 출력하는 방식이다.

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2] # 최솟값 0, 최댓값 9
count = [0] * max(array) + 1

for i in range(len(array)):
	count[array[i]] += 1

for i in range(len(count)):
	for j in range(array[i]):
		print(i, end = ' ')
```

## 정렬 라이브러리

파이썬은 기본 정렬 라이브러리인 sorted() 함수를 제공한다. 리스트, 딕셔너리, 집합 자료형을 입력받아 정렬된 결과를 리스트로 반환한다. 시간 복잡도는 O(NlogN)이다.

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array) # 정렬된 배열을 복사
array.sort() # 원본을 정렬
```

```python
# 키 기준으로 정렬하기
array = [('바나나', 2), ('사과', 5), ('당근', 3)]
result = sorted(array, key=lambda x:x[1])

dict = {
	'바나나': 2,
  '사과': 5,
	'당근': 3
}
result = sorted(dict.items(), key = lambda item: item[1])
```

## 퀵 정렬

평균 시간 복잡도는 O(NlogN)이다. 기준이 되는 피벗 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다. 피벗을 가장 왼쪽 값으로 설정하면, 큰 데이터는 피벗의 오른쪽부터 작은 데이터는 끝부터 탐색한다. 두 값이 선택되면 위치를 바꾼다. 만약 엇갈린다면 작은 데이터와 피벗을 바꾸고 종료한다. 이러한 작업은 피벗을 기준으로 작은 데이터와 큰 데이터로 분할한다. 더이상 정렬할 수 있는 데이터가 없을 때까지 분할을 반복한다.

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
	if len(array) <= 1:
		return array
	
	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail if x <= pivot]
	right_side = [x for x in tail if x > pivot]

	return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

## 삽입 정렬

시간 복잡도 O(N^2)이다. 느린 정렬에 속하지만, 이미 정렬된 데이터가 많은 경우 최대 O(N)의 시간 복잡도를 보인다. 삽입 정렬은 특정한 데이터를 적절한 위치에 삽입한다. 특정 데이터가 적절한 위치에 들어가기 전에 그 앞까지의 데이터는 이미 정렬되어 있는 것을 보장한다. 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에 그 위치에 삽입된다는 점이 특징이다.

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1): # 앞의 범위에 대해 위치 찾기
		if array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j] # swap
		else:
			break
```

## 선택 정렬

시간 복잡도 O(N^2). 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 과정을 반복하여 오름차순 정렬한다. 매번 가장 작은 것을 선택하는 알고리즘이다.

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	min_index = i
	for j in range(i+1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
	array[i], array[min_index] = array[min_index], array[i]
```


[#10825 국영수](https://www.acmicpc.net/problem/10825)

> 접근 방법

파이썬의 sorted 라이브러리는 다중 조건에 대해 정렬이 가능하다. 람다를 사용해서 다중 조건식을 표현할 수 있다.
키를 지정할 때 내림차순에 대해서는 마이너스, 오름차순에 대해서는 그냥 변수를 사용한다.
다중 조건식에 넣는 순서대로 정렬을 수행하므로 우선순위가 높은 조건식부터 쓴다.
문제에서는 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순으로 정렬하라고 했으므로
순서에 맞게 음수 표현 구분해서 라이브러리를 사용하면 된다. (파이썬 짱 ^^)


> 통과한 코드

```python
import sys
read = sys.stdin.readline

n = int(read())
name_score_list = []
result = []

for _ in range(n):
  name, korean, english, math = map(str, read().split())
  name_score_list.append((name, int(korean), int(english), int(math)))

result = sorted(name_score_list, key = lambda x:(-x[1], x[2], -x[3], x[0]))

for name_score in result:
  print(name_score[0])
```

[#10814 나이순 정렬](https://www.acmicpc.net/problem/10814)

> 접근 방법

국영수 문제와 마찬가지로 파이썬 정렬 라이브러리의 다중 조건식을 사용하면 된다.
이렇게 날로 먹어도 되나 싶을 정도로 간단하게 풀었다.
시간 복잡도는 최악의 경우 O(NlogN)을 보장한다.


> 통과한 코드

```python
import sys
read = sys.stdin.readline

n = int(read())
age_name_list = []
result = []

for i in range(n):
  age, name = map(str, read().split())
  age_name_list.append((int(age), name, i))

result = sorted(age_name_list, key = lambda x:(x[0], x[2]))

for name_score in result:
  print(name_score[0], name_score[1])
```

[#10825 국영수](https://www.acmicpc.net/problem/10825)

> 접근 방법


> 통과한 코드

```python

```

[#18876 좌표 압축](https://www.acmicpc.net/problem/18876)

> 접근 방법

좌표를 중복 없이 정렬된 상태로 만들고, 보기 좌표들의 인덱스를 출력하면 된다.
중복 없이 정렬된 리스트로 만들기 위해 집합 변환, 리스트 변환, 정렬을 거쳤고 index 함수를 사용해 출력했다.
시간 복잡도가 각각 O(len(생성된 집합의 요소 개수)), O(len(리스트 요소 개수)), O(NlogN), N * O(N)이라 시간 초과 나지 않을지 걱정했는데
역시나 시간 초과로 틀렸다. 집합을 포기하고 싶지는 않아서, 중복 없는 좌표의 인덱스를 사전으로 저장하도록 바꿔서 O(N)으로 해결했다.

> 통과한 코드

```python
import sys
read = sys.stdin.readline

n = int(read())
points = list(map(int, read().split()))
result = []

unique_points = sorted(list(set(points)))

# 시간 초과
# for point in points:
#  result.append(unique_points.index(point))

unique_point_index = {}
for i in range(len(unique_points)):
  unique_point_index[unique_points[i]] = i

for point in points:
  print(unique_point_index[point], end = ' ')

```

[#11652 카드](https://www.acmicpc.net/problem/11652)

> 접근 방법

카드가 등장한 횟수를 우선 세고, 횟수를 기준으로 내림차순 정렬해서 첫번째 아이템의 카드 번호를 출력하면 된다. 
카드 등장 횟수는 딕셔너리로 저장했고, sorted 다중 조건으로 카드 횟수 내림차순, 카드 번호 오름차순 정렬했다.


> 통과한 코드

```python
import sys
read = sys.stdin.readline

n = int(read())
card_count_dict = {}

for _ in range(n):
  card = int(read())
  if card in card_count_dict:
    card_count_dict[card] += 1
  else:
    card_count_dict[card] = 1

result = sorted(card_count_dict.items(), key = lambda item : (-item[1], item[0]))
print(result[0][0])

```

[#23881 알고리즘수업1 - 선택정렬](https://www.acmicpc.net/problem/23881)

> 접근 방법

문제에 나와있는 의사코드를 구현하고, 교환 횟수를 카운트해서 조건에 맞을 때 숫자를 출력하면 된다.
의사코드는 맨 끝에서부터 정렬을 시작하여 가장 큰 수를 뒤로 보내는 선택 정렬이다.
교환 횟수를 만족할 때 교환되는 두 숫자를 작은 순서대로 출력해야 하는데,
교환 횟수를 만족하게 될 때는 직전 조건문에서 교환 횟수가 증가한 경우이고, 이떄 교환이 발생했다는 말이다.
맨 끝의 요소와 가장 큰 수를 출력하면 된다. 코드에서는 반복이 끝나기 전이므로 maxIndex와 last 인덱스에 있는 숫자를 출력한다.


> 통과한 코드

```python
import sys

read = sys.stdin.readline

n, k = map(int, read().split())
numbers = list(map(int, read().split()))
exchange_count = 0

for last in range(n - 1, 0, -1):
    maxIndex = numbers.index(max(numbers[0:last]))
    if numbers[maxIndex] > numbers[last]:
        numbers[maxIndex], numbers[last] = numbers[last], numbers[maxIndex]
        exchange_count += 1
    if exchange_count == k:
        print(numbers[maxIndex], numbers[last])
        break

if exchange_count < k:
    print(-1)
```

[#2108 통계학](https://www.acmicpc.net/problem/2108)

> 접근 방법

낮은 정답률을 보고 쫄았으나 파이썬 덕분에 무난하게 통과한 문제.
평균, 중간값, 범위는 파이썬 라이브러리를 사용하면 쉽게 풀 수 있다.
최빈값은 딕셔너리로 출현 빈도를 세고, 출현 빈도 내림차순 숫자 오름차순으로 정렬한다.
최빈값이 하나이면 딕셔너리의 첫번째 요소의 숫자를 바로 반환하고 최빈값이 여러개라면 두번째 요소의 숫자를 반환한다. 
최빈값의 판단은 숫자가 한개 주어진 경우, 숫자가 여러개지만 최빈값이 하나인 경우, 최빈값이 여러개인 경우로 나눌 수 있는데
사전의 길이가 1인 경우, 사전의 길이가 1보다 크지만 딕셔너리의 두번째 요소가 최빈값이 아닌 경우, 사전의 길이가 1보다 크고 딕셔너리의 두번째 요소도 최빈값인 경우로 구분한다.


> 통과한 코드

```python
import sys

read = sys.stdin.readline

n = int(read())
numbers = [int(read()) for _ in range(n)]
number_count = {}

# average
average = round((sum(numbers) / n), 0) + 1 - 1
print(f'{average:.0f}')

numbers.sort()

# mid
print(numbers[n // 2])

# max appearance
for number in numbers:
    if number in number_count:
        number_count[number] += 1
    else:
        number_count[number] = 1
sorted_number_count = sorted(number_count.items(), key=lambda x: (-x[1], x[0]))

max_count = sorted_number_count[0][1]
if len(sorted_number_count) > 1 and sorted_number_count[1][1] == max_count:
    print(sorted_number_count[1][0])
else:
    print(sorted_number_count[0][0])

# range
print(numbers[n - 1] - numbers[0])
```