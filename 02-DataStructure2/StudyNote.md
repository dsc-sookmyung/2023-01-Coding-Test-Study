## 1620
풀이) 포켓몬의 이름과 번호를 저장하기 위해 두 개의 딕셔너리를 만들어준다. (key 값이 번호인 딕셔너리, key 값이 포켓몬 이름인 딕셔너리로 생성)
두 개의 딕셔너리에 저장하고, 번호가 들어온다면 포켓몬 이름을, 이름이 들어오면 알맞은 번호를 출력한다.
- 딕셔너리가 아닌 리스트에 저장했을때 시간초과가 발생했다. 
  - 리스트에서 탐색을 하는 경우 시간복잡도 O(n)
  - 딕셔너리는 hash table을 사용하여 시간복잡도 O(1)
  - 인덱스 탐색이나 특정 문자 탐색을 할 때, 딕셔너리를 사용하는 것이 유리할 수 있다는 걸 기억해두자!

- rstrip()의 중요성
``` python 
  import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    
    answer = []
    for i in range(N):
        answer.append([i, input()])  # 순서, 이름
    
    for _ in range(M):
        question = input()
        if question.isdigit():  # 숫자면
            # print(int(question)-1)
            question = int(question) - 1
            print(answer[question][1])
        else:
            for i in range(N):
                if question == answer[i][1]:
                    print(i+1)
```
⇒ 여기서 계속 question에 숫자를 넣어도 if문 안으로 들어가질 않았는데, input = sys.stdin.readline 을 작성해 받아주는데, 기본적으로 readline은 개행문자를 포함하고 있다. 
  그래서 문자열 맨 마지막에 개행문자가 포함되어 출력되기에, 개행문자때문에 isdigit()에서 false가 나왔다. 
<br>
⇒ rstrip()을 사용해 문자열 맨 마지막의 공백을 삭제해준다.

## 14425
풀이) M개의 문자열을 집합 set()에 넣어주고, 문자열이 그 집합에 포함되어었다면 result에 1씩 더해준다. (dict()을 사용한 풀이 또한 가능)

- 처음에 두 개의 리스트에 문자열을 담아 for문을 통해 비교하는 방법을 사용했지만 시간초과가 발생했다.
- set
  - 중복되지 않는 고유한 요소들을 갖고 있으며, 순서가 없다. 중복을 허용하지 않는다는 특징으로 set은 자료형의 중복을 제거하기 위한 필터로 사용된다.
  - 순서가 상관 없기에, 같은 요소가 들어있다면 같은 집합이다.
```python
    s1 = set([1, 2, 3])
    s1 = set({1, 2, 3})  # 위와 동일
    s2 = set("Hello")
    # s2 = {'e', 'H', 'l', 'o'}
    s3 = set()  # 비어있는 집합 자료형
    s1.add(4)  # 값을 1개 추가하기 : add
    s1.update([4, 5, 6])  # 값을 여러 개 추가하기 : update
    s1.remove(2)  # 특정 값 제거하기 : remove
    s1.discard("4")  # 특정 값을 안전하게 제거하기(해당 값이 있으면 삭제, 없으면 아무 일도 일어나지X) : discard
    s1.pop()  # 임의의 요소를 반환해 해당 요소 제거하기(set 비어있으면 오류발생) : pop
```

- dict
  - 키와 값 한쌍이 하나의 대응관계를 갖고 있는 자료형

  - 순서에 상관없이 키를 이용해서 바로 값에 접근이 가능하도록 만들어진 데이터
  - 딕셔너리 = {키1 : 값1, 키2 : 값2}
  - 중복되는 키는 저장하지 않으며, 값에는 숫자, 문자, 튜플, 리스트, 딕셔너리 등 섞어서 가능
```python
S = dict()
d = {'a': 123123}  # 딕셔너리 생성
d[999] = 10

# 해당 키가 딕셔너리에 있는지 확인
d = {'a': 123123, 'b': "blog", 'c': 3333}
if 'b' in d:
    print('b가 딕셔너리 안에 있습니다.')
else:
    print('b가 딕셔너리 안에 없습니다.')

# 딕셔너리에서 키 뽑기
d = {'a': 123123, 'kim': 'blockdmask', 'b': "blog", 'c': 3333, 123: 'name'}

print(d.keys())  # dict_keys(['a', 'kim', 'b', 'c', 123])
print(d.items()) # dict_items([('a', 123123), ('kim', 'blockdmask'), ('b', 'blog'), ('c', 3333), (123, 'name')])

# 값이 없을때 get 접근(딕셔너리의 키로 안전하게 값 얻기 : get → 값이 없으면 None을 반환)
r1 = d.get('ccc')  # -> d.get('ccc') = None
# 값이 있을때 get 접근
r3 = d.get('a')  # -> d.get('a') = 12

del d['a']  # del 딕셔너리[키] 를 통해 삭제 가능

```

## 11279
풀이) heapq 모듈을 이용하여 최대 힙을 만든다. 최대 힙 구현을 위해 값을 음수로 바꾸어 넣어주고 x가 0일때, 힙에서 가장 큰 값을 출력해준다. 

- 최소 힙, 최대 힙
  - 힙은 특정한 규칙을 갖는 트리로, 최댓값과 최솟값을 빠르게 찾을 수 있다.
  - 최소 힙 : 부모 노드의 키 값이 항상 자식 노드의 키 값보다 작다
  - 최대 힙 : 부모 노드의 키 값이 항상 자식 노드의 키 값보다 크다
  - 파이썬의 내장된 heapq 모듈을 사용해서 구현할 수 있음 → 기본적으로 최소 힙으로 구현되어 있다.
``` python
# 최소 힙 구현
import heapq
heap = []
for i in range(1, 6):
		heapq.heappush(heap, i)

for i in range(5):
		print(heapq.heappop(heap))

# 최대 힙 구현 => heapq에서는 최대 힙을 제공하지 않기에, 부호를 변경해서 최대힙을 구현한다!!!!
import heapq
heap = []
for i in range(1, 6):
		heapq.heappush(heap, -i)   # 부호를 바꿔서 최대힙에 넣어준다
# heap은 [-5, -4, -3, -2, -1] 가 된다.

for i in range(5):
		print(-heapq.heappop(heap))  # 출력할때에도 앞에 - 붙여준다
# 출력시 5, 4, 3, 2, 1이 출력된다. -> 큰 숫자부터 출력.

print(heapq.heappop(heap))
print(heap[0])  # -> 이렇게 리스트 값 꺼내오듯이 가져올 수 있음!!

```
## 2075
풀이) 메모리 제한의 문제로, 모든 값을 힙에 저장하지 말고 힙의 크기를 n으로 고정시켜준다. 처음에 힙이 비어있으면 입력받은 n개의 값을 모두 힙에 넣어준다. 그 이후부터는 입력받은 값과 힙을 비교한다. 
힙에 들어있는 값 중 가장 작은 수와 입력값을 비교해서 입력값이 크다면 힙에 있는 값을 heappop하고() 입력값을 힙에 넣어주는 과정을 반복해 N번째로 가장 큰 수는 최소 힙에서 heappop()을 해서 최댓값 N개 중 가장
작은 값인 heap[0]을 꺼내 출력해준다. 

- 메모리 초과
  - 처음에 기본 최대 힙으로 구현했을 때 메모리 초과 발생했다. 입력받는 N의 크기가 1 ~ 1500으로, 그냥 다 받으면 N^으로 배열의 최대크기가 2250,000 이 된다.
즉, 배열 크기가 너무 크다!! 
  <br>
  ⇒ N번째로 큰 수 출력시 배열의 크기를 줄이기 위해서 최소힙 크기를 n으로 고정시킨다.
새로운 value가 들어오면 힙의 첫번째 원소(가장 작은애)랑 value랑 비교해서, 힙에 들어있는 값보다 크다면 힙에 있는 값 빼고 value 넣어준다.
heap[0]을 출력하면 그게 곧 N번째로 큰수!!




