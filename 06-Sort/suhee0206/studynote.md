# Sort

## 목차

- **개념**

  - [정렬 알고리즘](#정렬-알고리즘)
    - [선택 정렬](#선택-정렬)
    - [삽입 정렬](#삽입-정렬)
    - [퀵 정렬](#퀵-정렬)
    - [계수 정렬](#계수-정렬)
    - [그 외 정렬 알고리즘](#그-외-정렬-알고리즘)
      - 병합 정렬
      - 버블 정렬
      - 힙 정렬
    - [정렬 알고리즘의 시간 복잡도 비교](#정렬-알고리즘의-시간-복잡도-비교)
  - [파이썬의 정렬 라이브러리](#파이썬의-정렬-라이브러리)

- **문제**

  - [10825 국영수](#10825-국영수)
  - [10814 나이순 정렬](#10814-나이순-정렬)
  - [11652 카드](#11652-카드)
  - [18870 좌표 압축](#18870-좌표-압축)
  - [2108 통계학](#2108-통계학)

  - [23881 알고리즘 수업 - 선택 정렬 1](#23881-알고리즘-수업---선택-정렬-1)



## 개념

> 다음은 [이것이 취업을 위한 코딩테스트다 with 파이썬](http://www.yes24.com/Product/Goods/91433923)에서 발췌한 내용입니다.

### 정렬 알고리즘

정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다. 

정렬 알고리즘으로 데이터를 정렬하면, 이진 탐색(Binary Search)이 가능해진다. 

#### 선택 정렬

<img src="https://codepumpkin.com/wp-content/uploads/2017/10/selectionSort.gif" width="300px" /> 



_출처: https://codepumpkin.com/selection-sort-algorithms/_

데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복한다. 이 방법은 가장 원시적인 방법으로 '매번 가장 작은 것을 선택'한다는 의미에서 선택 정렬(Selection Sort) 알고리즘이라고 한다.

선택 정렬은 가장 작은 데이터를 앞으로 보내는 과정은 N - 1번 반복하면 정렬이 완료된다.

```python
# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  max_index = i # 가장 작은 원소의 인덱스
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]	# 스와프
  
print(array)
```

**선택 정렬의 시간 복잡도는 `O(N^2)`**이므로, 매우 비효율적이다. 다만, 특정한 리스트에서 가장 작은 데이터를 찾는 일이 코딩 테스트에서 잦으므로 선택 정렬 소스코드 형태에 익숙해질 필요가 있다.  

#### 삽입 정렬

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif?20110309111239" width="300px" />  

*출처: https://commons.wikimedia.org/wiki/File:Insertion-sort-example.gif*

데이터를 하나씩 확인하며, 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 삽입 정렬(Insertion Sort)라고 부른다.  더불어 삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.

삽입 정렬은 선택 정렬에 비해 구현 난이도가 높은 편이지만 선택 정렬에 비해 실행 시간 측면에서 더 효율적인 알고리즘으로 잘 알려져 있다. 특히 삽입 정렬은 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적이다. 

```python
# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  for j in range(i, 0, -1):	# 인덱스 i부터 1까지 감소하며 반복하는 문법
    if array[j] < array[j-1]:	# 한 칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j]
    else:	# 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break
```

**삽입 정렬의 시간 복잡도는 `O(N^2)`**으로, 선택 정렬과 흡사한 시간이 소요된다. 여기서 꼭 기억할 내용은 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다는 점이다. 최선의 경우 `O(N)`의 시간 복잡도를 가진다. 따라서 거의 정렬되어 있는 상태로 입력이 주어지는 문제라면 퀵 정렬 등의 여타 알고리즘을 이용하는 것보다 삽입 정렬을 이용하는 거시 정답 확률을 높일 수 있다. 

#### 퀵 정렬

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif" width="300px" /> 

_출처: https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif_

퀵 정렬은 정렬 알고리즘 중에 가장 많이 사용되는 알고리즘이며, 퀵 정렬과 비교할 만큼 빠른 알고리즘으로 '병합 정렬' 알고리즘이 있다. 

퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다. 퀵 정렬에서는 피벗(Pivot)이 사용된다. 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'을 바로 피벗이라고 표현한다. 피벗을 설정하고 리스트를 분할하는 방법에 따라 여러 가지 방식으로 퀵 정렬이 구분되는데, 가장 대표적인 분할 방식으로는 호어 분할(Hoare Partition) 방식이 있다. 호어 분할은 리스트에서 첫 번째 데이터를 피벗으로 정한다. 

```python
# 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end:	# 원소가 1개인 경우 종료
    return
  pivot = start	# 피벗은 첫 번째 원소
  left = start + 1
  right = end
  while left <= right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:	# 엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else:	# 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)
  
quick_sort(array, 0, len(array) - 1)
print(array)
```

**퀵 정렬의 평균시간 복잡도는 `O(NlogN)`**이고, **최악의 경우 시간 복잡도가 `O(N^2)`**이다. 데이터가 무작위로 입력되는 경우 퀵 정렬은 빠르게 동작할 확률이 높다. 하지만 리스트의 가장 왼쪽 데이터를 피벗으로 삼을 때, '이미 데이터가 정렬되어 있는 경우'에는 매우 느리게 동작한다. 파이썬의 퀵 정렬을 기반으로 작성된 기본 정렬 라이브러리를 이용하면 추가적인 로직을 더해줘서 `O(NlogN)`을 보장해주기 때문에 걱정하지 않아도 된다. 

#### 계수 정렬

<img src="https://media.tenor.com/zswbYsLbYqEAAAAd/counting-sort.gif" width="300px" /> 

계수 정렬(Counting Sort) 알고리즘은 '데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때'만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다. 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있다. 계수 정렬이 이러한 특징을 가지는 이유는, 계수 정렬을 이용할 때는 '모든 범위를 담을 수 있는 크기의 리스트(배열)을 선언'해야 하기 때문이다. 

계수 정렬은 직접 데이터의 값을 비교한 뒤에 위치를 변경하며 정렬하는 방식(비교 기반의 정렬 알고리즘)이 아니다. 계수 정렬은 일반적으로 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다는 특징이 있다. 

```python
# 계수 정렬
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1	# 각 데이터에 해당하는 인덱스의 값 증가
  
for i in range(len(count)):	# 리스트에 기록된 정렬 정보 확인
  for j in range(count[i]):
    print(i, end=' ')	# 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```

모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최댓값의 크기를 K라고 할 때, **계수 정렬의 시간 복잡도는 `O(N+K)`**이다. 따라서 데이터의 범위만 한정되어 있다면 효과적으로 사용할 수 있으며 항상 빠르게 작동한다. 사실상 현존하는 정렬 알고리즘 중에서 기수 정렬(Radix Sort)과 더불어 가장 빠르다고 볼 수 있다. 

**계수 정렬의 공간 복잡도는 `O(N+K)`**이다. 

#### 그 외 정렬 알고리즘

- **병합 정렬**

  병합 정렬 또는 합병 정렬(Merge Sort)는 시간 복잡도가 `O(NlogN)`인 비교 기반 정렬 알고리즘이다. 

​	<img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif?20151222172210" width="300px" />  

​	_출처: https://commons.wikimedia.org/wiki/File:Merge-sort-example-300px.gif_

- **버블 정렬**

  버블 정렬 또는 거품 정렬(Bubble Sort)은 시간 복잡도가 `O(N^2)`로 상당히 느리지만, 코드가 단순하기 때문에 자주 사용된다.

​	<img src="https://upload.wikimedia.org/wikipedia/commons/0/06/Bubble-sort.gif?20110418154649" width="300px" /> 

​	_출처: https://commons.wikimedia.org/wiki/File:Bubble-sort.gif_

- **힙 정렬**

  힙 정렬(Heap Sort)이란 최대 힙 트리나 최소 힙 트리를 구성해 정렬을 하는 방법으로서, 내림차순 정렬을 위해서는 최소 힙을 구성하고 오름차순 정렬을 위해서는 최대 힙을 구성하면 된다. 일반적인 경우 `O(NlogN)`의 시간복잡도를 가진다. 

​	<img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif?20110419031008" width="300px" /> 

​	_출처: https://commons.wikimedia.org/wiki/File:Heapsort-example.gif_

#### 정렬 알고리즘의 시간 복잡도 비교

| Algorithm      | Time Complexity |              |              | Space Complexity |
| -------------- | --------------- | ------------ | ------------ | ---------------- |
|                | **Best**        | **Average**  | **Worst**    | **Worst**        |
| Quick Sort     | `O(Nlog(N))`    | `O(Nlog(N))` | `O(N^2)`     | `O(log(N))`      |
| Merge Sort     | `O(Nlog(N))`    | `O(Nlog(N))` | `O(Nlog(N))` | `O(N)`           |
| Heap Sort      | `O(Nlog(N))`    | `O(Nlog(N))` | `O(Nlog(N))` | `O(1)`           |
| Bubble Sort    | `O(N)`          | `O(N^2)`     | `O(N^2)`     | `O(1)`           |
| Insertion Sort | `O(N)`          | `O(N^2)`     | `O(N^2)`     | `O(1)`           |
| Selection Sort | `O(N^2)`        | `O(N^2)`     | `O(N^2)`     | `O(1)`           |
| Counting Sort  | `O(N+K)`        | `O(N+K)`     | `O(N+K)`     | `O(K)`           |

### 파이썬의 정렬 라이브러리

파이썬은 기본 정렬 라이브러리인 `sorted()` 함수를 제공한다. `sorted()`는 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌는데, 병합 정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 `O(NlogN)`을 보장한다는 특징이 있다. 

`sorted()` 함수는 리스트, 딕셔너리, 집합 자료형 등을 입력받아서 정렬된 결과를 리스트 자료형으로 리턴한다. 

`sort()` 함수를 이용하면, 리스트 내부 원소를 바로 정렬하고, 별도의 정렬된 리스트가 반환되지 않는다. 

`sorted()`와 `sort()`를 이용할 때는 key 매개변수를 입력으로 받을 수 있다. key값으로는 함수가 들어가며, 이는 정렬 기준이 된다. lambda를 이용해 우선 순위를 가진 여러 개의 정렬 기준을 입력할 수 있다. (Cf. [10825 국영수](#10825-국영수))

코딩 테스트에서 정렬 알고리즘이 사용되는 경우를 일반적으로 3가지 문제 유형으로 나타낼 수 있다.

1. **정렬 라이브러리로 풀 수 있는 문제:** 단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용 방법을 숙지하고 있으면 어렵지 않게 풀 수 있다.
2. **정렬 알고리즘의 원리에 대해서 물어보는 문제:** 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.
3. **더 빠른 정렬이 필요한 문제:** 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다. 



## 문제

### [10825 국영수](https://www.acmicpc.net/problem/10825)

문제) 학생 N명의 이름, 국어, 영어, 수학 점수가 주어졌을 때 다음과 같은 조건으로 학생의 성적을 정렬하라.

1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

분류) 정렬

해설) `sorted` 메서드를 사용한다. `key`에 조건에 있는 값들을 순서대로 넣어준다. 감소하는 순서라면 `-1`을 곱해줘야 한다.

메모) 이름을 사전순으로 정렬하려면 이름 전부를 비교해야 되는데, 이름의 첫 글자만 비교해서 첫 번째 시도 때 틀렸다. 

```python
import sys

read = sys.stdin.readline
N = int(read())

scores = []

for _ in range(N):
  score = read().split()
  # 성적은 string에서 int로 타입 변경
  for i in range(len(score)):
    if score[i].isdigit():
      score[i] = int(score[i])
  scores.append(score)

sorted_scores = sorted(scores, key = lambda x : (-x[1], x[2], -x[3], x[0])

for x in sorted_scores:
  print(x[0])
```



### [10814 나이순 정렬](https://www.acmicpc.net/problem/10814)

문제) 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하라.

분류) 정렬

해설)  `sorted` 메서드를 사용한다. 입력을 받으면서, 가입한 순서 정보를 배열에 함께 저장한다. `key`에 조건에 있는 값들을 순서대로 넣어준다. 

참고) [10825 국영수](https://www.acmicpc.net/problem/10825) 문제와 매우 유사하다. 대신 이번에는 가입한 순서 정보를 따로 배열에 저장해줘야 한다. 

```python
import sys

read = sys.stdin.readline
N = int(read())

members = []

for i in range(N):
  age, name = read().split()
  members.append([int(age), name, i])	# i는 가입한 순서 정보

sorted_members = sorted(members, key = lambda x: (x[0], x[2]))

for x in sorted_members:
  print(x[0], x[1])
```



### [11652 카드](https://www.acmicpc.net/problem/11652)

문제) 정수가 적힌 카드 N장 중, 가장 많이 가지고 있는 정수를 구하라. **만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.** 

분류) 정렬

해설) 카드를 정렬한 후, counter로 개수를 센 후에, 가장 많이 갖고 있는 정수를 `Counter`의 `most_common` 메서드를 이용해 구한다.

카드를 정렬하는 이유는, 가장 많이 가지고 있는 정수가 여러 가지인 경우 작은 것을 출력하기 위해 작은 값들부터 나열되어 있어야되기 때문이다. `most_common([n])`에서 `n`에 1을 입력하면 가장 많이 가지고 있는 정수 한 개를 `[(key, value)]` 형태로  리턴한다.

메모) 문제를 끝까지 잘 읽자!

```python
import sys
from collections import Counter

read = sys.stdin.readline
N = int(read())

cards = []
for _ in range(N):
  cards.append(int(read()))

cards.sort()
counter = Counter(cards)
print(counter.most_common(1)[0][0])
```



### [18870 좌표 압축](https://www.acmicpc.net/problem/18870)

문제) N개의 좌표에 좌표 압축을 적용한 결과를 출력하라. Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다. 

분류) 정렬

해설) 각 좌표보다 작은 값의 개수(중복 제거)를 구하는 문제다.

 `set`을 이용해 중복 값을 제거해주고, `sorted`를 이용해 값을 정렬한다. 이렇게 생성된 `sorted_x_list`에 있는 값들의 인덱스가 바로 각 값보다 작은 값의 개수가 된다. 이 인덱스를 각 좌표가 빠르게 참조하게 하기 위해 `dict`에 key에는 값을, value에는 인덱스를 저장한다. `dict`에 좌표 값을 입력하면, 각 값보다 작은 값의 개수가 리턴된다.

메모) 처음에 dictionary를 사용하지 않고, 마지막에 이중 for문을 이용해서 값을 구해줬더니 시간 초과가 발생했다. 항상 제한을 잘 확인하자! (1 <= N <= 1,000,000, -10^9 <= Xi <= 10^9)

```python
import sys

read = sys.stdin.readline
N = int(read())

x_list = list(map(int, read().split()))

sorted_x_list = sorted(set(x_list))
dict = dict()
for i in range(len(sorted_x_list)):
  dict[sorted_x_list[i]] = i

for x in x_list:
  print(dict[x], end=' ')
```



### [2108 통계학](https://www.acmicpc.net/problem/2108)

문제) N개의 수가 주어졌을 때, 네 가지 기본 통계값인 산술평균, 중앙값, 최빈값, 범위를 구하라.

분류) 정렬

해설) 파이썬의 라이브러리로 간단하게 해결이 가능하다. 

- 산술평균:  `sum` 메서드를 이용해 수의 합을 구하고, 수의 개수로 나눠준 후에, `round` 메서드를 이용해 소수점 이하 첫째 자리에서 반올림한 값을 리턴한다.
- 중앙값: 수를 정렬한 후에, 가운데 인덱스에 해당하는 값을 리턴한다.
- 최빈값: 수를 정렬한 후에, `Counter` 를 이용해 수의 개수를 센다. 수를 정렬하는 이유는, 최빈값이 여러 개 있을 때 최빈값 중 두 번째로 작은 값을 출력하기 위함이다. 최빈값은 `Counter`의 `most_common` 메서드를 이용하여 구하고, 최빈값이 여러 개인 경우에는 두 번째로 작은 값을, 한 개인 경우에는 그 값을 출력한다. `most_common` 메서드 사용법은 [11652 카드](#11652-카드) 문제 해설을 참고하자.
- 범위: `max` 메서드를 이용해 가장 큰 수를 구하고, `min` 메서드를 이용해 가장 작은 수를 구해서 두 값을 빼준다. 

```python
import sys
import math
from collections import Counter

read = sys.stdin.readline
N = int(read())

numbers = []
for _ in range(N):
  numbers.append(int(read()))

def mean(array):
  return round(sum(array) / len(array))

def median(array):
  array.sort()
  return array[int(len(array) / 2)]

def mode(array):
  array.sort()
  counter = Counter(array)
  two_modes = counter.most_common(2)
  if len(two_modes) == 2 and two_modes[0][1] == two_modes[1][1]:
    return two_modes[1][0]
  else:
    return two_modes[0][0]

def sub_max_min(array):
  return max(array) - min(array)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(sub_max_min(numbers))
```



### [23881 알고리즘 수업 - 선택 정렬 1](https://www.acmicpc.net/problem/23881)

문제) 주어진 선택 정렬 의사 코드의 방식으로 배열 A를 오름차순 정렬할 경우, K번째 교환되는 수를 구하라.

분류) 정렬, 구현

해설) 선택 정렬 의사 코드를 내가 선택한 언어로 구현하면 된다.

1. 배열 A의 마지막 인덱스부터 1번째 인덱스(두 번째 수)까지 for문을 반복하면서, `A[:i+1]` 중 가장 큰 수를 찾는다. 

   Python은 1초에 2*10^7의 연산을 하고, (5 <= N <= 10^4)이므로, for문으로 가장 큰 수를 찾으면 `O(N^2)`이기에 시간 초과가 발생한다. 따라서 리스트의 내장함수인 `index`를 사용해서 가장 큰 값(`max`)의 인덱스를 구한다. 

2. 현재 인덱스와 가장 큰 값의 인덱스가 다른 경우, K를 하나 감소시키고, 두 값을 swap한다.

3. K가 0인 경우, K 번째 교환되는 경우이므로, 작은 수부터 출력하고 for문을 마쳤는데 K가 양수라면 -1을 출력한다.

메모) 선택 정렬을 내 멋대로 구현하는 것이 아니라, 문제에서 준 선택 정렬 의사 코드에 따라 구현해야 한다! [선택 정렬](#선택-정렬)과 다르게 구현해야 한다.

```python
import sys

read = sys.stdin.readline
N, K = map(int, read().split())
A = list(map(int, read().split()))

# A의 마지막 인덱스부터 1번째 인덱스(두 번째 수)까지 반복
for i in range(len(A)-1, 0, -1):
  max_index = i
  max_index = A.index(max(A[:i+1]))
  if i != max_index:
    K = K-1
    A[i], A[max_index] = A[max_index], A[i]
  if K==0:
    print(A[max_index], A[i])
    break
if K:
  print(-1)
```
