# 06-Sort

 - 정리한 문제
 1. 10825 국영수
 2. 10814 나이순 정렬
 3. 11652 카드
 4. 18870 좌표 압축
 5. 2108 통계학
 <br>

 ## 10825 국영수

 ### 설명
 - 배열이 주어졌을 때, 기준인 key값을 정의해서 정렬할 수 있는지 물어보는 문제이다.
 - sort함수의 key값으로 람다함수를 사용하여 해당 과목(국어, 영어, 수학, 이름)의 조건별로 정렬해준다.
 - sort 기본이 오름차순이므로 내림차순 정렬은 앞에 - 부호를 붙여 정렬한다.
 - 앞에 올수록 우선순위가 높게 적용된다.

```python
import sys
input = sys.stdin.readline

n = int(input())
gradeCard = [input().split() for i in range(n)]

gradeCard.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in gradeCard:
  print(student[0])
```

 ## 10814 나이순 정렬

 ### 설명
 -  마찬가지로, 배열이 주어졌을 때, 기준인 key값을 정의해서 정렬할 수 있는지 물어보는 문제이다.
 -  나이와, 나이가 같다면 입력된 순서대로 출력하면 되는 문제이다.
 - 이미 입력된 순서대로 배열을 만들었기 때문에 나이만 신경써서 정렬하면 된다.

```python
import sys
input = sys.stdin.readline

n = int(input())
memberCard = [input().split() for i in range(n)]

memberCard.sort(key = lambda x: int(x[0]))

for member in memberCard:
  print(*member)             
```

## 11652 카드

 ### 설명
 -  숫자가 여러개 주어졌을 때, 가장 많이 입력된 숫자를 출력하는 문제이다.  (만약 가장 많이 입력된 숫자가 여러개라면 그 중 작은것을 출력)
 - 해당 숫자와 그 숫자가 입력된 개수, 이 두 개 정보를 가지고 있어야 한다고 생각이 들어서 바로 dictionary가 생각났다.
 - 숫자가 key값이고 그 숫자의 개수가 value인 defaultdict를 이용하였다.
 - 숫자를 받아 해당 key값(숫자)에 대한 value값(개수)을 +1 해준다.
 - 만약 이번에 갱신된 숫자의 개수가 현재 가장 많이 가지고 있는 정수의 개수보다 크다면 현재 가장 많이 가지고 있는 정수(maxNum)를 갱신해준다.
 - 만약 이번에 갱신된 숫자의 개수가 현재 가장 많이 가지고 있는 정수의 개수와 같다면 가장 많이 가지고 있는 정수가 여러가지인 것이다, 그 중 작은것을 골라야 하므로 min함수를 써서 작은것을 골라준다.

### defaultdict❓

- defaultdict는 특정 키 값으로 접근했을 때 그 값이 없을 경우 value값을 default로 설정하여 dict에 넣어준다.
 - dictionary에 해당 key값이 없다면 오류를 내지 않고 default값을 설정해주기 때문에 이를 이용하면 해당 key값이 존재하는지 아닌지 같은 코드를 생략할 수 있어서 좋다.
- ex) 만약 defaultdict(int) 값으로 설정할 경우 해당 key값이 존재하지 않는다면 value값이 0으로 설정

```python
import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
numberCard = defaultdict(int)
#현재 가장 많이 가지고 있는 정수
maxNum = 0

for _ in range(n):
  num = int(input())
  numberCard[num] += 1
  if(numberCard[num] > numberCard[maxNum]):
    maxNum = num
  elif(numberCard[num] == numberCard[maxNum]):
    maxNum = min(num, maxNum)

print(maxNum)              
```

## 18870 좌표 압축

 ### 설명
 - 좌표 x1를 압축한 결과는 해당 배열에서 x1보다 작은, 서로 다른 것의 개수이다.
 - 배열을 오름차순으로 정렬하면 **자신의 인덱스 값 = 자신보다 작은 것의 개수**이다. 이때 "***서로 다른 것***"이라는 조건을 만족해야 하므로 set으로 바꿔 중복을 없애준 후 정렬해준다.
 - 이 문제는 최대 1,000,000개의 입력이 주어져서  O(N)안에 풀어야 한다.
 - 즉, 해당 좌표가 있을 때 그 좌표보다 작고, 서로 다른 것의 개수를 O(1)의 시간 만에 찾아야 한다.
 - 따라서 x좌표를 key값으로 가지고, 그 x좌표보다 작은좌표의 개수를 value로 가지는 dict를 만들어 준다.

```python
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

#자신의 인덱스가 자기보다 작은것의 개수이다.
sorted_x = sorted(set(x))

#x좌표를 key값으로 가지고, 그 x좌표보다 작은좌표의 개수를 value로 가지는 dict
dict_x = {sorted_x[i] : i for i in range(len(sorted_x))}

for i in x:
  print(dict_x[i], end = " ")               
```

## 2108 통계학

 ### 설명
 - 여러 숫자가 주어졌을 때, 평균, 중앙값, 최빈값, 범위를 구해 출력하는 문제이다.
 - 최빈값을 구하는 부분이 <11652 카드문제>와 비슷했지만 이 문제는 최빈값이 여러 개일 경우 제일 작은 값이 아니라 **2번째로 작은값**을 구해야 한다.
 - defaultdict에 (숫자 : 개수)를 넣어주고 개수는 오름차순으로, 숫자는 내림차순으로 정렬해주었다.
 - 위처럼 정렬하면 배열의 1번째 마지막에 있는 수가 최빈값이면서 제일 작은 숫자일 것이다.
 - 이 문제에서 최빈값이 여러 개일 경우 2번째로 작은 수를 구해야 하므로 배열의 2번째 마지막에 있는 것 또한 최빈값이라면 해당 값을 출력해준다.
 - 이 때 배열 안에 1개의 튜플만 있을 수도 있어서 무작정  배열의 2번째 마지막에 접근할 경우 인덱스 오류가 날 수 있기 때문에 주의해줘야 한다.

```python
import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
num = [int(input().rstrip()) for i in range(n)]
num.sort()

def printMean():
  mean = round(sum(num)/n, 0)
  print(int(mean))

def printMedian():
  print(num[n//2])

def printMode():
  dict = defaultdict(int)
  for i in num:
    dict[i] += 1
  sorted_dict = sorted(dict.items(), key = lambda x: (x[1], -x[0]))
  if(len(sorted_dict) > 1 and sorted_dict[-1][1] == sorted_dict[-2][1]):
    print(sorted_dict[-2][0])
  else:
    print(sorted_dict[-1][0])

def printRange():
  print(num[-1] - num[0])

printMean()
printMedian()
printMode()
printRange()
```
