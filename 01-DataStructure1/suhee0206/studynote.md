# Stack, Queue, Deque

#### [9012 괄호](https://www.acmicpc.net/problem/9012)

문제) 올바른 괄호 문자열(VPS)인지 아닌지 판단하라.

분류)  자료 구조 `stack`, python의 `list` 이용

해설) 문자열의 뒤에서부터 괄호의 개수를 셌을 때, 오른쪽 괄호의 개수보다 왼쪽 괄호의 개수가 많거나, 괄호들이 쌍을 다 이루고 오른쪽 괄호가 남는다면 VPS가 아니다. 

stack에서 pop을 했을 때, 

- `)`이 나오면 왼쪽 괄호를 기다리고 있는 오른쪽 괄호의 개수를 뜻하는 변수 `right`에 1을 더한다.

- `(`이 나오면, 짝을 맞출 오른쪽 괄호가 있는지 확인하고, 있다면 왼쪽 괄호를 기다리고 있는 오른쪽 괄호를 하나 감소시키고, 없다면 짝을 맞출 수 없어서 VPS가 아니다. (왼쪽 괄호의 개수가 더 많은 상황)

stack이 empty가 될 때까지 pop을 반복해준 후에, 대기하고 있던 오른쪽 괄호가 다 사라졌다면 VPS가 맞고, 남아있다면 VPS가 아니다. 

```python
import sys

def vps(str):
  stack = list(str.strip())
  right = 0
  
  while stack: 
    char = stack.pop()
    if char == '(':
      if right > 0:
        right = right - 1
      else:
        return False
    else:
      right = right + 1

  if right == 0:
    return True
  else:
    return False
    
count= int(sys.stdin.readline())
for _ in range(count):
  str = sys.stdin.readline()
  if vps(str):
    print("YES")
  else:
    print("NO")
```



#### [1158 요세푸스 문제](https://www.acmicpc.net/problem/1158)

문제) N명의 사람이 원을 이루면서 앉아있고 K번째 사람을 제거할 때, 원에서 사람들이 제거되는 순서인 (N, K)-요세푸스 순열을 구하라.

분류) 자료 구조 - 원형  `queue`, python의 `list` 이용 

해설) K만큼 더한 후 원형 리스트의 길이로 나눈 나머지 값(`(num+K-1) % len(circular_list)`)으로 제거해야 하는 인덱스를 구한다.

```python
import sys

read = sys.stdin.readline
N, K = map(int, read().split())

circular_list = []
josephus = []

for i in range(1, N+1):
  circular_list.append(i)

num = 0
while len(circular_list):
  num = (num+K-1) % len(circular_list)
  val = circular_list.pop(num)
  josephus.append(val)
  
print('<', end='')
print(', '.join(str(item) for item in josephus), end='')
print('>')
```

참고) `deque`을 이용하여 문제를 풀 수도 있다. deque의 앞에서 K-1개의 요소를 빼서 deque의 뒤에 넣고, K번째 요소는 josephus 리스트에 넣어주는 것을 반복하면 된다. 



#### [1966 프린터 큐](https://www.acmicpc.net/problem/1966)

문제) Queue의 가장 앞에 있는 문서의 '중요도'를 확인했을 때, 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다고 했을 때, 궁금한 문서가 몇 번째로 인쇄되는지 출력하라. 

분류) 자료 구조 - `deque` 

해설) deque을 이중 배열로 구성해서 0번째 인덱스에는 중요도를, 1번째 인덱스에는 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 저장한다. 현재 Queue의 최댓값이 가장 앞에 있는 문서의 값보다 크다면, 가장 앞에 있는 문서를 빼서 뒤에 넣고, 그렇지 않다면 인쇄한다. 

```python
import sys
from collections import deque

T = int(sys.stdin.readline())
while T:
  order = []	# 인쇄 순서 저장
  
  N, M = map(int, sys.stdin.readline().split())
  
  deq = deque(list(map(int, sys.stdin.readline().split())))
  for i in range(len(deq)):
    deq[i] = [deq[i], i]

  while len(deq):
    if max(deq)[0] > deq[0][0]:
      deq.append(deq.popleft())
    else:
      order.append(deq.popleft())

  for i in range(N):
    if order[i][1] == M:
      print(i+1)
      break
  
  T = T-1
```



#### [10799 쇠막대기](https://www.acmicpc.net/problem/10799)

문제) 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 조각의 총 개수를 구하라. 

분류) 자료 구조 - `stack`

해설) 문자열을 순회했을 때 

- `(`가 나오면 `stack`에 push하고, 

- `)`가 나오면 `stack`에서 pop한 후에, 경우를 나눠서

  - 바로 앞에 위치한 문자가 `(`라면 `()`레이저이므로 stack의 크기만큼 조각이 생기고,

  - 바로 앞에 위치한 문자가 `)`라면 쇠막대기의 끝이므로 조각이 한 개만 생긴다.

```python
import sys

str = sys.stdin.readline().rstrip()

ans = 0
stack = []
for i in range(len(str)):
  if str[i]=='(':
    stack.append(str[i])
  else:
    stack.pop()
    if str[i-1]=='(':
      ans += len(stack)
    else:
      ans += 1
      
print(ans)
```

