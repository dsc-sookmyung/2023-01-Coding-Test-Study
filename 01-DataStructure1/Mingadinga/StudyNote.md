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


# [18258 큐2](https://www.acmicpc.net/problem/18258)

> 접근 방법

입력받은 명령어에 따라 큐 연산을 실행해야 한다.
간단하게 큐를 구현할 수 있는 deque 라이브러리를 사용했다.
큐는 popleft(), append() 명령어를 사용한다. 개수는 len(deque)를 사용하고, deque에 요소가 들어있는지 여부는 null 판별로 구분할 수 있다.

> 통과한 코드

```python
import sys
from collections import deque

read = sys.stdin.readline

queue = deque()
n = int(read())

for _ in range(n):
  command = read().rstrip()
  if command == "pop":
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif command[0] == "p":
    push, item = map(str, command.split())
    queue.append(item)
  elif command[0] == "f":
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif command[0] == "b":
    if queue:
      print(queue[len(queue)-1])
    else:
      print(-1)
  elif command[0] == "s":
    print(len(queue))
  elif command[0] == "e":
    print(1 if len(queue) == 0 else 0)
  
```


# [2164 카드2](https://www.acmicpc.net/problem/2164)

> 접근 방법

제일 위에 있는 것부터 꺼낸다고 하길래 스택인 줄 알고 신나게 코드를 짰는데
위에 있는걸 아래에 다시 넣는 연산에서 appendleft()를 쓰고 있는 것이었다.. 뭔가 이상해서 연산 순서를 써봤더니
큐로 푸는게 맞았다. ㅎㅋㅎㅋ
역시 손으로 풀어봐야 제맛

> 통과한 코드

```python
import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
stack = deque([i for i in range(n, 0, -1)])

while stack:
  stack.pop()
  if len(stack) == 1:
    print(stack.pop())
    break
  stack.appendleft(stack.pop())
```

# [1936 후위 표기식2](https://www.acmicpc.net/problem/1936)

> 접근 방법

후위 표기식은 뒤에서부터 탐색을 시작해 먼저 나온 연산자와 두개의 피연산자를 계산하는 방식이다.
선입선출이 되어야하므로 스택을 사용했다. 변수와 숫자를 관리해야했는데, 변수는 A부터 Z까지 순서대로 나온다고 했으므로
값을 리스트에 저장해두고 아스키코드 값의 차이를 이용해 인덱스에 접근했다.
eval() 함수를 이용할까 하다가 시간복잡도가 O(N)이라는거 보고 그냥 조건문 돌렸다.

> 통과한 코드

```python
import sys
from collections import deque

read = sys.stdin.readline
stack = deque()

n = int(read())
expression = read().rstrip()
number = [int(read().rstrip()) for _ in range(n)]

for token in expression:
  if token >= 'A' and token <= 'Z':
    stack.append(number[ord(token)-ord('A')])
  else:
    second = stack.pop()
    first = stack.pop()
    if token == '+':
      stack.append(first + second)
    elif token == '-':
      stack.append(first - second)
    elif token == '*':
      stack.append(first * second)
    elif token == '/':
      stack.append(first / second)

print("{:.2f}".format(stack.pop()))
```


# [2346 풍선 터뜨리기](https://www.acmicpc.net/problem/2346)

> 접근 방법

인덱스 순환이 있길래 보자마자 순환 큐가 떠올랐으나
저번에 비슷한 문제에서 리스트 제거로 쉽게 푼 문제가 생각나서 리스트로 열심히 뽑아보았다.
그러나 원래 인덱스를 복원할 방법이 없어서 풀다가 포기.. 구글링해서 순환 큐로 다시 풀었다.
순환 큐로 푸니 복잡한 인덱스 계산 과정이 필요하지 않아서 아주 간단했다.


> 통과한 코드

```python
import sys
from collections import deque

read = sys.stdin.readline
n = int(read())
balloons = list(map(int, read().split()))
spin_queue = deque()
result = []

for i in range(len(balloons)):
  spin_queue.append((i, balloons[i]))

while spin_queue:
  index, move_value = spin_queue.popleft()
  result.append(index + 1)
  if move_value > 0:
    spin_queue.rotate(-(move_value - 1))
  else:
    spin_queue.rotate(-move_value)

print(' '.join(map(str, result)))
```


# [2504 괄호의 값](https://www.acmicpc.net/problem/2504)

> 배운 것

코드에 예외 케이스와 조건문이 많아지면 뭔가 잘못됐다는 메시지를 수신할 수 있게 됐다.
예제에 과적합되고 이해하기도 어렵고 연산 속도도 느려진다. 이럴 떈 내 코드의 문제를 찾아 개선하자.

> 접근 방법

이 문제.. 결국 못 풀었다. 구글링으로 정답 코드를 보고나서도 이해하는데 한참 걸렸다.
처음에는 예제에 있는 문자열을 가지고 스택에서 괄호와 숫자를 함께 푸시하고 팝하는 방식으로 시나리오를 짜보았다.


`예제 : (()[[]])([])`

| input | stack |
|-------| ----- |
| (     | (                            |
| (     | ((                           |
| )     | (2                           |
| [     | (2[                          |
| [     | (2[[                         |
| ]     | (2[[] -> (2[3                | 
| ]     | (2[3] -> (2[3 -> (2 9 -> (11 |
| )     | (11) -> ( 11 -> 2 11 -> 22   |
| (     | 22(                          |
| [     | 22([                         |
| ]     | 22([] -> 22(3                |
| )     | 22(3) -> 22 ( 3 -> 22 6 -> 28 |

입력이 단독으로 (나 [이면 그냥 스택에 넣는다. 
입력이 ()나 []이면 2나 3을 스택에 넣는다.
입력이 )나 ]이면 짝인 괄호를 찾을 때까지 pop한다. 도중에 숫자가 나오면 킵해주고 숫자가 연속으로 나오면 현재 탐색 중인 괄호에 따라 곱하거나 더한다. 최종 연산 결과를 스택에 넣는다. 짝 괄호가 아닌 괄호가 나오면 0을 출력하고 끝낸다.

-> 위의 시나리오를 코드로 구현하다보니 너무 복잡해져서 이건 뭔가 아니다 싶었다. 그래서 숫자를 스택에 같이 넣지 말고 temp를 따로 두어서 최종값을 더하는 방법으로 수정했다.

| Input | stack | temp | result |
|-------|-------|-------|--------|
| ( | (     | 1 | 0      |
| ( | ((    | 2 | 0      |
|) | (     | 1 | 2      |
|[ | ([    | 3 | 2      |
|[ | ([[   | 9 | 2      |                   
|] | ([    | 1 | 11      |             
|] | (     | 1 | 11       |             
|) |       | 1 |22 <- 소괄호를 뽑았으니 2를 곱해보자 |

코드를 짜다보니 이건 뭔가 잘못됐다. 케이스가 너무 많이 쪼개졌다. 그리고 예제에 과적합한 풀이 방식이다. 그런데 … 여기서 뭘 어떻게 해야할지 모르겠어서 그냥 구글링을 했다. 머리가 너무 아팠기 때문. 구글링한 코드를 보고 컴파일 표를 다시 작성해봤다.

| Input | stack  | temp | result |
|-------|--------|-------|--------|
| ( | (      | 2 | 0 |
| ( | ((     | 4 | 0 |
| ) | (      | 2 | 4 |
| [ | ([     | 6 | 4 |
| [ | ([[    | 18 | 4 |
| ] | ([     | 6 | 22 |
| ] | (      | 2 | 22 |
| ) |        |  1 | 22 |
| ( | (      |  2 | 22 |
| [ | ([     |  6 | 22  |
| ] | ( | 2 | 28  |
| ) | | 1 | 28    |

정답 코드의 알고리즘 진행은 내 직관과는 너무 달랐다. 도대체 이걸 어떻게 푸는건지.. 다들 사고 방식이 컴퓨터랑 동기화된건지 싶었다. 

내가 놓쳤던 부분은 연속된 괄호가 아니더라도 시작 괄호가 나오면 곱해주고, 끝 괄호가 나왔을 때만 연속 괄호를 비교해서 최종결과에 반영하고 임시값을 복귀하는 것이다. 스택의 특성을 활용해서 임시값을 일관되게 바꿔주는 것이다. 이런 문제가 나오면 어떻게 풀어야할까?

일단 작은 예제로 쪼개서 컴파일 표를 여러번 그려보는게 좋을 것 같다.

| Input | stack | temp | result |
|------|-----|-------|--------|
| ( | ( | 1 | 0 |
| [ | ([ | 3 | 0 |
| ] | ( | 1 | 3 |
| ) | | 1 | 6 <- 소괄호를 뽑았으니 2를 곱해보자 |

위의 표는 내가 원래 풀었던 방식으로 컴파일 표를 작성했다. 계산이 일관적이지 않기 때문에 예외 케이스가 많아지고 예제에 과적합한 알고리즘이 만들어졌다. 정답 알고리즘으로 컴파일 표를 다시 그려보자.

| Input | stack | temp | result |
|-------|-------|-------|--------|
| ( | ( | 2 | 0 |
| [ | ([ | 6 | 0 |
| ] | ( | 2 | 6 |
| ) | | 1 | 6 |

연산이 일관적이어서 예외 케이스가 많아지지 않고 코드도 깔끔해졌다. 물론 컴파일표를 그리다보면 직관과 많이 벗어난 코드가 된다. 
나는 아직 알고리즘과 친숙하지 않은건지, 딱히 재능이 없어서 그런것인지 모르겠지만 처음부터 이런 계산 과정을 생각하긴 어려울 것 같다. 
그렇다면 기존에 내가 생각했던 알고리즘의 문제를 찾아서 개선하는 방향으로 사고해야겠다고 결심했다.

알고리즘 문제를 여러개 풀다보니, ***코드에 예외 케이스와 조건문이 많아지면 뭔가 잘못됐다는 메시지를 수신할 수 있게 됐다.
예제에 과적합되고 이해하기도 어렵고 연산 속도도 느려진다. 이럴 떈 내 코드의 문제를 찾아 개선하자.***
앞으로 문제 풀 때 활용할 수 있는 중요한 인사이트를 얻었다. 화이팅!


```python
import sys

read = sys.stdin.readline
brackets = read().rstrip()

stack = []
total = 0
tmp = 1

for i in range(len(brackets)):

    if brackets[i] == "(":
        stack.append(brackets[i])
        tmp *= 2

    elif brackets[i] == "[":
        stack.append(brackets[i])
        tmp *= 3

    elif brackets[i] == ")":
        if not stack or stack[-1] == "[":
            total = 0
            break
        if brackets[i-1] == "(":
            total += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            total = 0
            break
        if brackets[i-1] == "[":
            total += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(total)
```

