# [1158 요세푸스 순열](https://www.acmicpc.net/problem/1158)
> 접근 방법 

리스트의 인덱스를 증가시키며 제거할 사람을 찾는다. 이때 제거 대상인 사람은 리스트에서 삭제한다. 인덱스를 증가시킬 때는 직전 반복문에서 제거되는 아이템 한개를 고려하여 k-1만큼 증가시키고, 리스트의 길이보다 커지면 나머지 연산으로 줄여준다.

> 통과한 코드

출력 형태가 <3, 4, 5, 6>이었다. 리스트 사이에 쉼표를 넣어 출력하는 부분은 ``', '.join(result)``을 사용했고, 꺽새 사이에 띄어쓰기 제거는 `sep=""`으로 제거했다.

```python
import sys

read = sys.stdin.readline

n, k = map(int, read().split())
people = [i for i in range(1, n + 1)]
result = []
remove_index = 0

for _ in range(n):
    remove_index += k - 1
    if remove_index >= len(people):
        remove_index %= len(people)
    result.append(str(people[remove_index]))
    people.pop(remove_index)

print("<", ', '.join(result), ">", sep="")
```

# [1966 프린터 큐](https://www.acmicpc.net/problem/1966)

> 접근 방법

큐의 맨 앞자리가 가장 큰 숫자일 때 해당 숫자를 pop하여 출력한다. 가장 큰 숫자가 아니라면 pop하고 다시 append한다. 타겟인 숫자가 맨 앞자리에서 뽑힐 때까지 맨앞에서 pop된 횟수를 센다. 앞뒤에 아이템을 넣는 연산이 많으므로, deque를 사용하여 시간 복잡도를 줄일 수 있다. deque의 앞뒤 추가 제거 연산 시간 복잡도는 O(1)이다.

> 통과한 코드
```python
import sys
from collections import deque

read = sys.stdin.readline

test_count = int(read())
for _ in range(test_count):
  n, m = map(int, read().split())
  arr = list(map(int, read().split()))
  queue = deque(arr)
  target_index = m

  answer = 0
  while target_index >= 0:
    max_value = max(queue)
    front = queue.popleft()
    target_index -= 1
    if front == max_value:
      answer += 1
      if target_index < 0:
        print(answer)
        break
    else:
      queue.append(front)
      if target_index < 0:
        target_index = len(queue) - 1
```

# [10799 쇠막대기](https://www.acmicpc.net/problem/10799)

> 접근 방법

막대기 하나를 레이저로 세번 자르면 네 조각이 된다. 막대기 하나를 여러 레이저로 잘랐을 때 생기는 조각의 개수는 레이저 개수 + 1이다. 문자열이 괄호로 나오기 때문에, 막대기의 시작 괄호로 판단되면 스택에 넣고 막대기의 끝 괄호로 판단되면 스택에서 pop한다. 레이저로 판단하면 조각의 개수를 센다. 조각의 개수를 세야하는 경우는 레이저로 판단될 때, 막대기의 끝이 나왔을 때이다.

> 통과한 코드

```python
import sys
from collections import deque

read = sys.stdin.readline
brackets = read()
stack = deque()
count = 0
i = 0

while i < len(brackets) - 1:
  if brackets[i] == '(':
    # 다음꺼가 )이면 레이저니까 막대기개수 누적합
    if brackets[i + 1] == ')':
      count += len(stack)
      i += 1
    # 다음꺼가 (이면 얜 맥대기니까 스택에 추가하기
    elif brackets[i + 1] == '(':
      stack.appendleft('-')
  elif brackets[i] == ')':
    # 막대기 끝나면 하나 추가
    count += 1
    stack.pop()
  i += 1

print(count)

```

# [9012 괄호](https://www.acmicpc.net/problem/9012)

> 접근 방법

시작 괄호가 나오면 스택에 넣었다가 끝 괄호가 나오면 가장 위에 쌓인 괄호부터 pop한다. 모든 괄호에 대해 연산을 수행했을 때 스택에 남은 괄호가 있다면 짝이 맞지 않는 괄호 문자열이다. 또는 끝괄호가 나왔는데 짝지어지는 시작괄호가 없다면 역시 맞지 않는 괄호 문자열이다.

> 통과한 코드

```python
# 스택
import sys
from collections import deque

def check_vps(ps):
  stack = deque()
  for bracket in ps:
    if bracket == '(':
      stack.appendleft(bracket)
    elif bracket == ')':
      if stack:
        stack.pop()
      else:
        print("NO")
        return
  if len(stack) == 0:
    print("YES")
  else:
    print("NO")

read = sys.stdin.readline

t = int(read())
pss = [read().rstrip() for _ in range(t)]

for ps in pss:
  check_vps(ps)
```
