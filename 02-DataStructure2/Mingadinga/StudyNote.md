[#14225 문자열 집합](https://www.acmicpc.net/problem/14425)

> 접근 방법

문제에서 문자열 보기가 `집합`이라고 했으므로, 파이썬의 집합 자료형으로 보기 문자열을 입력 받았다. 그리고 입력으로 들어오는 대상 문자열을 집합의 in 연산자를 사용했다.

> 파이썬 set의 시간 복잡도

**파이썬 set은 내부적으로 해시테이블을 사용**하므로, 순서를 보장하는 리스트에 비해 검색과 삭제 속도가 빠르다. 
리스트의 in, remove() 시간 복잡도는 O(N)인데 비해 집합의 in, remove()의 시간 복잡도는 O(1)이다.
집합은 순서를 보장하지 않는 데이터 집합에 대해서 리스트에 비해 빠른 연산을 제공하므로, 집합을 사용할 수 있는 조건이라면 집합을 사용하는 것이 좋다.

set의 주요 연산 시간 복잡도는 다음과 같다.
- `len(s)`: O(1)
- `s.add(item)`: O(1)
- `item in s`, `item not in s`: O(1)
- `s.remove(item)`: O(1)
- `s.discard(item)`: O(1)
- `s.pop()`: O(1)
- `s.clear()`: O(1)
- `set(...)`: O(len(...))
- `s == t`, `s != t`: O(len(s))
- `s <= t`, `s >= t`: O(len(t))
- `s | t`, `s & t`, `s - t`, `s ^ t`: O(len(s) + len(t))
- `for v in s:`: O(N)
- `s.copy()`: O(N)


> 통과한 코드

```python
import sys

read = sys.stdin.readline
n, m = map(int, read().split())
set = set()
count = 0
for _ in range(n):
  set.add(read().rstrip()) # O(1)

for _ in range(m):
  if read().strip() in set: # O(1)
    count += 1

print(count)
```


[#14225 문자열 집합](https://www.acmicpc.net/problem/14425)

> 접근 방법

파이썬은 힙을 사용할 수 있는 라이브러리로 heapq를 제공하는데, 최소힙이다. 최대힙으로 사용하고 싶다면 push, pop할 때 부호를 반대로 바꿔야 한다.

> heapq의 시간 복잡도

- `heapq.heappush(heap, 3)`: O(logN)
- `heapq.heappop(heap)`: O(logN)
- `heapq.heapify(heap)`: O(N)

> 통과한 코드

```python
import sys
import heapq

read = sys.stdin.readline
n = int(read())
heap = []

for _ in range(n):
  target = int(read().rstrip())
  if isinstance(target, int) and target > 0:
    heapq.heappush(heap, -target)
  elif target == 0:
    if heap:
      print(-heapq.heappop(heap))
    else:
      print(0)
```

[#2075 n번째 큰 수](https://www.acmicpc.net/problem/2075)

> 접근 방법

n*n 개의 숫자를 전부 탐색하여 가장 큰 n개의 숫자를 구하고 n번째 큰 숫자를 출력한다.
이때 메모리 제한으로 인해 모든 숫자를 배열에 저장한 후 탐색할 수 없다. 그래서 숫자를 하나씩 받을 때마다 보관할지 버릴지 정해야 한다.
모든 숫자를 탐색했을 때 가장 큰 n개의 숫자를 남기려면, 리스트에 우선 n개의 숫자를 저장하고 그 다음부터는 리스트의 최솟값보다 더 큰 숫자로만 대체해야 한다.
들어온 순서와 상관없이 우선순위가 가장 높은 것부터 pop하는 우선순위 큐를 활용할 수 있고, 우선순위 큐는 주로 힙으로 구성한다.
우선순위는 가장 작은 숫자가 높으므로 최소힙을 사용한다.
n 크기의 최소힙을 구성하고, 최소힙의 root보다 더 큰 숫자가 들어오면 pop하고 새로운 숫자를 push한다.
모두 탐색하면 pop과 push를 반복했으므로 최소힙이 정렬된 상태이다. 가장 앞자리에 있는 힙이 n번째 큰 숫자이다.

> 우선순위 큐와 힙

우선순위 큐는 우선순위가 높은 것부터 꺼내는 자료구조이다.
그리고 힙은 루트 노드에 우선순위가 높은 데이터를 위치시키는 자료구조이다.
힙을 활용하면 시간복잡도 O(logN)으로 우선순위가 가장 높은 아이템을 꺼낼 수 있다.


> 통과한 코드
```python
import sys
import heapq

read = sys.stdin.readline
n = int(read())
max_heap = []

for _ in range(n):
  targets = list(map(int, read().split()))
  for target in targets:
    if len(max_heap) < n:
      heapq.heappush(max_heap, target)
    if target > max_heap[0]:
      heapq.heappop(max_heap)
      heapq.heappush(max_heap, target)
print(max_heap[0])
```

[#1620 나는야 포켓몬 마스터 이다솜](https://www.acmicpc.net/problem/1620)

> 접근 방법

딕셔너리를 쓸까 리스트를 쓸까 고민하다가 리스트를 선택했다. 
주요 연산은 번호로 포켓몬 이름을 알아오는 것과 포켓몬 이름으로 번호를 알아내는 연산이다.
딕셔너리는 번호를 key로, 이름을 value로 저장할 수 있고 리스트는 인덱스에 value를 바로 저장한다.
딕셔너리는 key로 value를 검색하는 것은 O(1)로 빠르지만, value로 key를 찾는 작업은 리스트로 변환 후에 순차 탐색해야하므로 O(n)이다.
리스트의 인덱스 검색은 마찬가지로 O(1)이고 순차탐색은 O(n)이다.
시간복잡도가 동일하므로 메모리를 절반으로 사용하는 리스트를 선택했다.

> 통과한 코드

```python
import sys

read = sys.stdin.readline
n, m = map(int, read().split())
pokedex  = [read().rstrip() for _ in range(n)]
questions = [read().rstrip() for _ in range(m)]

for question in questions:
  if question.isdigit():
    print(pokedex[int(question) - 1])
  else:
    print(pokedex.index(question) + 1)
```

[#21939 문제 추천 시스템 Version 1](https://www.acmicpc.net/problem/21939)

> 문제 접근 방법

추가, 삭제, 최소값, 최대값 연산이 주로 발생한다.
최소힙과 최대힙을 두면 각 힙의 루트가 최소값, 최대값을 가진다.
이때 추가와 삭제 때문에 힙에도 동기화가 이루어져야하는데, 힙은 노드를 삽입할 수는 있지만 중간 노드를 삭제하는 기능은 없기 때문에
삭제 요청이 들어왔다면 해당 문제번호는 추천에서 제외해야한다. 삭제 요청이 들어온 후 다음 턴에서 추천이나 추가 요청이 들어왔을 때
삭제되지 않은 문제번호가 남아있다면 문제가 발생하므로, 영향을 받는 큐에 대해서 삭제된 문제 번호는 pop해야 한다.

어디서 막혔냐면 삭제 요청이 들어온 문항 번호에 대해서 다음 턴에 바로 힙에서 삭제를 시도한 것이다.
만약 중간에 있는 문제를 삭제하려면 아직 유효한 문제까지 모두 pop해야하는데 이걸 어쩌지 고민하다가 결국 구글링을 했다.
힙에서 데이터는 무조건 루트를 통해 pop되니까, 루트를 대상으로 문제를 삭제하면 충분했다.
아직 힙 연산이 익숙하지 않은 것 같다. 문제 좀 더 풀어봐야지.


> 통과한 코드

```python
import sys
import heapq

read = sys.stdin.readline
n = int(read())
min_heap = []
max_heap = []
problems = {}

for _ in range(n):
  prob_number, diff = map(int, read().split())
  heapq.heappush(min_heap, (diff, prob_number))
  heapq.heappush(max_heap, (-diff, prob_number))
  problems[prob_number] = True

m = int(read())
for _ in range(m):
  commands = list(read().split())
  print(commands)
  if commands[0][0] == "a":
    prob_number, diff = int(commands[1]), int(commands[2])
    while not problems[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while not problems[min_heap[0][1]]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, (diff, prob_number))
    heapq.heappush(max_heap, (-diff, prob_number))
    problems[prob_number] = True

  elif commands[0][0] == "s":
    prob_number = int(commands[1])
    problems[prob_number] = False

  elif commands[0][0] == "r":
    if commands[1] == "1":
      while not problems[max_heap[0][1]]:
        heapq.heappop(max_heap)
      print(max_heap[0][1])
    elif commands[1] == "-1":
      while not problems[min_heap[0][1]]:
        heapq.heappop(min_heap)
      print(min_heap[0][1])
```


