### 10825 국영수
#### 풀이) 
- sort()를 사용하여 정렬할 때, 람다를 사용하여 정렬 기준을 설정할 수 있다.
- 오름차순 정렬시 key=lambda x:x[0]으로, 내림차순 정렬시 key=lambda x: -x[0]으로 작성한다.
- 문제 조건에 맞게 국어는 내림차순, 영어는 오름차순, 수학은 내림차순 정렬을 해준다.

```python
import sys
n = int(sys.stdin.readline())
scores=[]

for _ in range(n):
    a, b, c, d = map(str, sys.stdin.readline().split())
    scores.append([a, int(b), int(c), int(d)])

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
# 국어점수 감소 순서/영어점수 증가 순서/수학점수 감소 순서

for i in range(n):
    print(scores[i][0])
```

### 10814 나이순 정렬
#### 풀이) 
- 앞의 문제와 마찬가지로, 람다를 사용하여 정렬 기준을 설정해준다.
- 나이순으로 정렬하고, 나이가 같다면 가입순으로 정렬해주는데 아래 코드처럼 x[0]의 조건만 넣어줘도 나이가 같으면 먼저 가입한 순으로 들어간다.
```python
import sys
n = int(sys.stdin.readline())

members=[]
for _ in range(n):
    a, b = sys.stdin.readline().split()
    a = int(a)  # 숫자로 바꿔주기
    members.append([a, b])

sorted_members = sorted(members, key=lambda x: x[0])
# 나이순으로 먼저 정렬, 나이 같다면 가입한 순으로(정렬하면 가입순으로 나온다!)

for i in range(n):
    print(sorted_members[i][0], sorted_members[i][1])

```

### 11652 카드
#### 풀이) 
- 카드의 숫자와 갯수를 딕셔너리에 함께 저장해준다.
- 카드를 매번 입력받을 때마다 해당 숫자가 딕셔너리에 있는지 확인하고, 없다면 새로 추가해주고 있다면 해당 value를 1 증가시킨다.
- 가장 많이 갖고 있는 정수, 여러개라면 숫자가 작은 것을 출력하는 조건을 주기위해 lambda를 사용해준다.
```python
import sys
input = sys.stdin.readline

N = int(input())
cards_dict = {}

for _ in range(N):
    a = int(input())
    if a not in cards_dict:
        cards_dict[a] = 1
    else:
        cards_dict[a] += 1

max_key = sorted(cards_dict.items(), key=lambda x: (-x[1], x[0]))
print(max_key[0][0])
```


### 18870 좌표압축
#### 풀이)
- 처음에 이중 for문을 사용해서 특정 숫자보다 작은 숫자의 갯수를 구하는 방식으로 풀었는데 시간초과가 나왔다.
- 이중 for문을 없애기 위해 set()을 사용하여 입력받은 숫자들의 중복을 제거하고 오름차순 정렬시킨 리스트인 sorted_nums를 새로 만든다.
- sorted_nums를 사용하여 딕셔너리에 해당 좌표와 그 좌표보다 작은 숫자의 갯수(=정렬시켰으므로 인덱스 번호가 된다)를 저장한다.
- 출력해야할 nums를 보며 딕셔너리에서 해당하는 값을 꺼내 출력해준다. 

```python
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(list(set(nums)))

dict = {sorted_nums[i]: i for i in range(len(sorted_nums))}
# print(dict)

for i in nums:
    print(dict[i], end=' ')
```



### 2108 통계학
#### 풀이) 
- 최빈값은 딕셔너리를 사용해 숫자가 나온 횟수를 카운트해서 구해준다.
- 딕셔너리에 저장된 숫자가 1개이거나 첫번째 숫자와 두번째 숫자가 다른 경우에는(최빈값이 한개인 경우) 최빈값을 출력한다.
- 첫번째와 두번째의 값이 같은 경우, 즉 최빈값이 여러 개 있는 경우 두번째로 작은 값을 출력한다.
- 파이썬 collections 모듈의 Counter를 사용해서 최빈값을 구하는 방법도 있다.
```python
import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()

def average(nums):
    total = sum(nums)
    return round(total/len(nums))

def middle(nums):
    return nums[int(N/2)]

def freq(nums):
    dic = dict()
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    dic = list(dic)
    if len(dic) == 1 or dic[0][1] != dic[1][1]:
        print(dic[0][0])
    else:
        print(dic[1][0])

def range(nums):
    return nums[len(nums)-1] - nums[0]

print(average(nums))
print(middle(nums))
freq(nums)
print(range(nums))

# 최빈값 구하기
from collections import Counter

def freq(nums):
    # Counter를 이용해 빈도수를 구해주고, most_common(2)를 사용하여 빈도수가 높은 숫자 2개를 가져온다
    cnt = Counter(nums).most_common(2)
    if len(nums) > 1 and cnt[0][1] == cnt[1][1]:  # 최빈값이 여러개인 경우(두개가 같음)
        return (cnt[1][0])
    else:
        return (cnt[0][0])

```

