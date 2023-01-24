# Map, Set

## 목차

- **[개념](#개념)**
  - [List, Tuple, Set, Dictionary](#List,-Tuple,-Set,-Dictionary)
    - [비교](#비교)
    - [List의 사용](#List의-사용)
    - [Tuple의 사용](#Tuple의-사용)
    - [Set의 사용](#Set의-사용)
    - [Dictionary의 사용](#Dictionary의-사용)
    - [활용](#활용)
  - [Map](#Map)
    - [Python map()](#Python-map())
- **[문제](#문제)**
  - [1620 나는야 포켓몬 마스터 이다솜](#1620-나는야-포켓몬-마스터-이다솜)
  - [14425 문자열 집합](#14425-문자열-집합)
  - [11279 최대 힙](#11279-최대-힙)
  - [2075 N번째 큰 수](#2075-N번째-큰-수)
  - 
- **[참고 자료](#참고-자료)**



## 개념

### List, Tuple, Set, Dictionary

List, Tuple, Set, Dictionary는 모두 iterable(반복 가능한) 객체다. 

아래 내용은 [List, Tuple, Set, Dictionary의 차이점과 활용을 잘 설명한 글](https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/)과 [예제로 배우는 파이썬 프로그래밍](http://pythonstudy.xyz/python/article/12-%EC%BB%AC%EB%A0%89%EC%85%98--List)에서 갖고 왔다.

#### 비교

| **List**                                                     | **Tuple**                                                    | **Dictionary**                                               | **Set**                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| List is a non-homogeneous data structure that stores the elements in single row and multiple rows and columns | Tuple is also a non-homogeneous data structure that stores single row and multiple rows and columns | Dictionary is also a non-homogeneous data structure which stores key value pairs | Set data structure is also non-homogeneous data structure but stores in single row |
| Can be represented by [ ]                                    | Can be represented by ( )                                    | Can be represented by { }                                    | Can be represented by { }                                    |
| Allows duplicate elements                                    | Allows duplicate elements                                    | Doesn’t allow duplicate keys.                                | Will not allow duplicate elements                            |
| Example: [1, 2, 3, 4, 5]                                     | Example: (1, 2, 3, 4, 5)                                     | Example: {1: “a”, 2: “b”, 3: “c”, 4: “d”, 5: “e”}            | Example: {1, 2, 3, 4, 5}                                     |
| Can be created using **list()** function                     | Can be created using **tuple()** function.                   | Can be created using **dict()** function.                    | Can be created using **set()** function                      |
| mutable                                                      | immutable                                                    | mutable                                                      | mutable                                                      |
| ordered                                                      | ordered                                                      | ordered (Python 3.7 and above)                               | unordered                                                    |
| Creating an empty list l=[]                                  | Creating an empty Tuple t=()                                 | Creating an empty dictionary d={}                            | Creating a set a=set() b=set(a)                              |

#### List의 사용

```python
# Python3 program for explaining use of list

# Lists
l = []

# Adding Element into list
l.append(5)
l.append(10)
print(l)																	# Output: [5, 10]

# Indexing and Slicing
print(l[-1])															# Output: [10]
print(l[:])																# Output: [5, 10]

# Modifying Element in list
l[1] = 8
print(l)																	# Output: [5, 8]											

# Popping Elements from list
l.pop()																		# del l[1]
print(l)																	# Output: [5]

# Merging Lists
a = [1, 2]
b = [3, 4, 5]
c = a + b																	# c = [1, 2, 3, 4, 5]

# Iterating List
d = a * 3																	# d = [1, 2, 1, 2, 1, 2]

# Searching List
i = d.index(2)														# i = 1
n = d.count(1)														# n = 3

# List Comprehension: [표현식 for 요소 in 컬렉션 [if 조건식]]
lc = [n ** 2 for n in range(10) if n % 3 == 0]
print(lc)																	# Output: [0, 9, 36, 81]
```

#### Tuple의 사용

```python
# Python3 program for explaining use of tuple

# Tuple
t = tuple(l)															# l = [5]

# Tuples are immutable
print("Tuple", t)													# Output: Tuple (5,)
print()

# Merging & Iterating over tuples works the same ways as for lists.

# Tuple Assign Variable
name = ("Hee", "Suh")
print(name)																# Output: ('Hee', 'Suh')
firstname, lastname = name
print(lastname, ',', firstname)						# Output: Suh, Hee
```

#### Dictionary의 사용

```python
# Python3 program for explaining use of dictionary

# Dictionary
d = {}

# Creating dict
# 1. Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print(d)									# Output: {5: 'Five', 10: 'Ten'}

# 2. Creating dict from Tuple List
prices = [('banana', 3000), ('strawberry', 10000)]
mydict = dict(persons)		# {'banana': 3000, 'strawberry', 10000}

# 3. Creating dict from Key=Value parameter
scores = dict(a=80, b=90, c=85)
print(scores['b'])				# Output: 90

# Removing key-value pair
del d[10]
print(d)									# Output: {5: 'Five'}

# Removing all
prices.clear()						# {}

# Reading Values in dict
for key in scores:
  val = scores[key]
  print("%s : %d" % (key, val))
  
# dict.keys()
keys = scores.keys()
for k in keys:
  print(k)

# dict.values()
values = scores.values()
for v in values:
  print(v)
  
# dict.items()
items = scores.items()		# dict_items([('a': 80), ('b': 90), ('c': 85)])
itemsList = list(items)		# [('a': 80), ('b': 90), ('c': 85)]

# dict.get()
scores.get("a")						# 80
scores.get("d")						# None
scores["d"]								# Error
if "d" in scores:
  print(scores["d"])
  
# dict.update(): updating multiple elements in dict at once
scores.update({"a": 95, "c": 90})
print(scores)							# Output: {'a': 95, 'b': 90, 'c': 90}

# Dictionary Comprehension: {key표현식 : value표현식 for items in iterable}
country_capital = {'대한민국': '서울',
                  	'영국': '런던',
                  	'미국': '워싱턴',
                  	'일본': '도쿄'}
capital_country = {capital: country for country, capital in country_capital.items()}
print(capital_country) 		# Output: {'서울': '대한민국', '런던': '영국', '워싱턴': '미국', '도쿄': '일본'}
```

#### Set의 사용

```python
# Python3 program for explaining use of set

# Set
s = set()

# Adding element into set
s.add(5)
s.add(10)															# add()를 사용하면 정렬이 될 때도, 안 될 때도 있음
print(s)															# Output: {10, 5}

# Removing element from set
s.remove(5)
print(s)															# Output: {10}
print()

# Defining set
myset = {1, 1, 3, 5, 5}
print(myset) 													# Output: {1, 3, 5}

# Converting list to set
mylist = ["A", "A", "B", "B", "B"]
s = set(mylist)
print(s)															# Output: ["A", "B"]

# Updating multiple elements
myset.update({2, 3, 4})								# {1 ,2, 3, 4, 5}

# Removing all elements from set
myset.clear()													# set()

# Set Operations
a = {1, 3, 5}
b = {1, 2, 5}

i = a.intersection(b)
# i = a & b
print(i)															# Output: {1, 5}

u = a.union(b)
# u = a | b
print(u)															# Output: {1, 2, 3, 5}

d = a.difference(b)
# d = a - b
print(d)															# Output: {3}
```

#### 

#### 활용

**List**

- Used in JSON format
- Useful for Array operations
- Used in Databases

**Tuple**

- Used to insert records in the database through SQL query at a time
  E.g., (1.’sravan’, 34).(2.’geek’, 35)
- Used in parentheses checker

**Dictionary**

- Used to create a data frame with lists
- Used in JSON

**Set**

- Finding unique elements
- Join operations



### Map

#### Python Map()

**`map()`** 함수는 **iterable**(list, tuple, dict, set, str, range etc.)의 각 요소에 주어진 함수를 적용하고, **iterator**를 리턴한다. 

**문법**

```python
map(function, iterable, ...)
```

**예제**

```python
# Working of map()

def calculateSquare(n):
	return n*n

numbers = (1, 2, 3, 4)
# 1. def function
result = map(calculateSquare, numbers)
# 2. lambda function
restul = map(lambda x: x*x, numbers)
print(result)

# Converting map object to set
numbersSquare = set(result)
print(numbersSquare)		# {16, 1, 4, 9}
```

```python
# Passing Multiple iterators to map() using Lambda

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lamda n1, n2: n1+n2, num1, num2)
print(list(result))		# [9, 11, 13]
```



## 문제

### [1620 나는야 포켓몬 마스터 이다솜](https://www.acmicpc.net/problem/1620)

문제) 1에서 N번까지의 포켓몬의 이름이 주어졌을 때, 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력하라.

분류) 자료 구조 - Dictionary

해설) Dictionary Comprehension을 이용하여 key, value가 숫자, 이름으로 되어있는 dictionary와 이름, 숫자로 되어있는 dictionary를 각각 만든다. ascii code를 이용하여 입력이 숫자라면 전자의 dictionary를, 문자라면 후자의 dictionary를 사용하여 답을 구한다. 

```python
import sys

N, M = map(int, sys.stdin.readline().split())
read = sys.stdin.readline
pocketmon_by_number = {(i+1): read().rstrip() for i in range(N)}
pocketmon_by_name = {name: number for number, name in pocketmon_by_number.items()}
for _ in range(M):
  problem = sys.stdin.readline().rstrip()
  if ord(problem[0]) >= 48 and ord(problem[0]) <= 57:	# ascii code
    print(pocketmon_by_number[int(problem)])
  else:
    print(pocketmon_by_name[problem])
```



### [14425 문자열 집합](https://www.acmicpc.net/problem/14425)

문제) M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

분류) 자료 구조 - Dictionary

해설) M개의 문자열을 `dict()`에 문자열, 문자열의 개수 쌍으로 저장한다. 문자열이 S에 포함되어 있다면 정답에 문자열의 개수를 더해준다. 

참고) 문제를 잘 파악하자! 같은 문자열의 집합의 개수를 구하는 것이 아니기 때문에, M개의 문자열을 `set()`에 저장하면 안되고, 문자열의 개수를 세줘야 되는 점을 주의해야 한다. 

```python
import sys

read = sys.stdin.readline
N, M = map(int, read().split())
S = {read().rstrip() for _ in range(N)}
D = {}
for _ in range (M):
  word = read().rstrip()
  if word in D:
    D[word] += 1
  else:
    D[word] = 1

ans = 0
for key in D.keys():
  if key in S:
    ans += D[key]

print(ans)
```



### [11279 최대 힙](https://www.acmicpc.net/problem/11279)

문제) 배열에 자연수 x를 넣는다. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다. **만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.**

분류) 자료 구조 - Heap (최대 힙)

해설) 문제 그대로 최대 힙을 구하면 된다. `from queue import PriorityQueue`를 이용해도 되지만, [`heapq()`가 더 빠르므로](https://stackoverflow.com/questions/36991716/whats-the-difference-between-heapq-and-priorityqueue-in-python), `heapq()`를 사용하자. `heapq()`는 최소 힙이므로, 최대 힙으로 변경하고 싶다면, 값을 음수로 바꿔주면 된다.

참고) 문제를 끝까지 잘 읽자! 첫 시도에 문제에 볼드 처리한 곳을 제대로 안 읽어서 틀렸다.

```python
import sys
import heapq

read = sys.stdin.readline
N = int(read())

h = []
for _ in range(N):
  x = int(read())
  if x>0:
    heapq.heappush(h, (-1)*x)
  elif x==0:
    if len(h):
      print((-1)*heapq.heappop(h))
    else:
      print(0)
```



### [2075 N번째 큰 수](https://www.acmicpc.net/problem/2075)

문제) NxN 표에 수 N^2개가 채워져 있고, 모든 수는 자신의 한 칸 위에 있는 수보다 크다. 이때 N번째 큰 수를 찾아라. 단, 1 <= N <= 1,500이며 **메모리 제한은 12MB**다. 

분류) 자료 구조 - Heap (최소 힙)

해설) 메모리 제한이 있기 때문에 N^2개의 값을 모두 저장한 후 정렬하는 방법을 사용할 수 없다. 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 점과 최소 힙을 이용한다. 

첫 번째 행에서 가장 큰 수를 최소 힙에 삽입한다. 두 번째 행부터는 최소 힙(최댓값을 저장됨)에 저장된 최솟값보다 큰 값들을 모두 최소 힙에 삽입한다. 그리고 메모리 초과를 방지하기 위해 최소 힙의 길이를 최대 N으로 유지해준다. (최소 힙에서 `heappop()`을 하면 가장 작은 값을 삭제하므로 최댓값 N개를 유지한다) 마지막으로 최소 힙에서 `heappop()`을 해주면 최댓값 N개 중 가장 작은 값, 즉 N번째로 큰 수가 리턴된다. 

```python
import sys
import heapq

read = sys.stdin.readline
N = int(read())
h = []
heapq.heappush(h, max(list(map(int, read().split()))))
for i in range(1, N):
  line = list(map(int, read().split()))
  min_val = heapq.heappop(h)
  for j in range(N):
    if line[j] > min_val:
      heapq.heappush(h, line[j])
  heapq.heappush(h, min_val)
  while len(h) > N:
    heapq.heappop(h)

print(heapq.heappop(h))
```



## 참고 자료

- https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
- http://pythonstudy.xyz/python/article/12-%EC%BB%AC%EB%A0%89%EC%85%98--List
- https://www.programiz.com/python-programming/methods/built-in/map