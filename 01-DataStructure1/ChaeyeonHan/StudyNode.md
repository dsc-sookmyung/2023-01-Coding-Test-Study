### 스택

- 박스 쌓기에 비유하여 아래에 있는 박스를 치우기 위해서는 위에 있는 박스를 먼저 치워야 한다.
- 선입후출, 후입선출 구조
- 스택 구현 → 별도의 라이브러리 필요X, `append()와 pop()` 메서드를 통해

```python
stack = []  # 빈 스택 초기화
stack = [1, 2, 3]
stack.append(4)  # 원소 넣기
x = stack.pop()  # 가장 마지막 원소 제거하기, 제거한 원소 리턴받을 수 있음
y = stack[-1]  # 원소 제거하지 않고 가져오기만 할 때

print(stack)  # 최하단 원소부터 출력 -> [1, 2, 3]
print(stack[::-1])  # 최상단 원소부터 출력 -> [3, 2, 1]
```

파이썬의 기본 클래스인 list를 통해 스택을 흉내낼 수 있다.

### 큐

- 대기 줄에 비유하여 먼저 온 사람이 먼저 들어간다.
- 선입선출 구조
- 큐 구현 → deque는 스택과 큐의 기능을 모두 가진 객체로, 양쪽에 출입구 갖고 있음

```python

from collections import deque

queue = deque()  # 큐는 구현을 위해 deque 라이브러리를 사용함
queue.append(5)
queue.append(3)
queue.append(2)  # deque([5, 3, 2])

# 왼쪽에서 값을 빼고 싶으면 popleft(), 넣고 싶으면 appendleft()
# 오른쪽에서 값을 빼고 싶으면 pop(), 넣고 싶으면 append()

```