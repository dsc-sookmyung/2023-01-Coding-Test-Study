# 01-DataStructure1


 ## 9012 괄호

 ### 설명
 - 괄호 문자열이 주어졌을 때 올바른 괄호열인지 판단하는 문제이다.
 - 괄호 문자들을 차례로 돌면서 스택에 넣어주고 () 짝이 맞을 경우 pop해준다.
 - 차례로 다 돈 뒤 스택이 비어있으면 다 짝이 맞았다는 뜻이므로 True를 스택이 비어있지 않으면 짝이 맞지 않았다는 뜻이므로 False 리턴한다.

```python
import sys
from collections import deque
input = sys.stdin.readline

num = int(input().rstrip())
dq= deque()

def isVPS(testcase):
  dq.clear()
  for i in testcase:
    if(i == ')'):
      if(dq):
        dq.pop()
      else:
        return False
    else:
      dq.append(i)
  if(dq):
    return False
  else:
    return True

for i in range(num):
  testcase = list(input().rstrip())
  if(isVPS(testcase)):
    print("YES")
  else:
    print("NO")
```

 ## 1158 요세푸스 문제
 ### 설명
 - N, K가 주어졌을 때 1,2,3, ... ,N의 순열에서 K번째 수를 삭제하고, 그 다음 K번째 수를 삭제하는 것을 수가 없어질 때까지 반복하는 문제이다.
 - N개의 수를 deque에 차례로 담고 k-1번 만큼 왼쪽으로 회전 시켜준 후 제일 앞의 수를 popleft()해주면 K번째를 삭제하게 된다.
 - 위 과정을 deque가 빌 때까지 반복한다.

```python
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
deque = deque(i+1 for i in range(n))
result = []

while(deque):
  deque.rotate(-(k-1))
  result.append(deque.popleft())

print("<%s>"%", ".join(map(str, result)))
```

## 1966 프린터 큐

 ### 설명
 - 문서들을 First In First Out순으로 인쇄하되, 만약 이번에 출력 될 문서가 중요도가 제일 높은 문서가 아닐 경우 다시 순서를 맨 끝으로 보낸다. 이때 M번째 자리에 놓인 문서는 몇 번째로 인쇄되는지 찾는 문제이다.
 - 문서들의 초기 위치를 나타낸 수를 deque에 넣어주고 문서들의 중요도를 담은 배열인 importance를 만들어준다. 즉, 문서의 위치를 i라고 한다면 그 문서의 중요도는 importance[i]에 담긴것이다.
 - deque가 빌 때까지 돌면서 제일 앞에 있는 문서의 중요도가  max(importance)이면 출력해주고 중요도를 0으로 만들어준다. 문서의 중요도가 최대값이 아니라면 deque의 맨 뒤로 보내준다.


```python
import sys
input = sys.stdin.readline
from collections import deque

testcaseNum = int(input())

for _ in range(testcaseNum):
  n, m = map(int, input().split())
  dq = deque([i for i in range(n)])
  importance = list(map(int, input().split()))
  count = 0
  while(dq):
    index = dq.popleft()
    if(importance[index] == max(importance)):
      importance[index] = 0
      count += 1
      if(index == m):
        print(count)
        break
    else:
      dq.append(index)
```

## 10799 쇠막대기

 ### 설명
 - ")" 괄호가 나왔을 때 레이저인지, 쇠막대기인지 구분하는 것이 이 문제의 포인트다. 바로 이전 괄호가 뭐였는지에 따라 구분해줄 수 있다.
- "("가 나왔을 때는 deque에 넣어준다.
- ")"가 나왔을 경우 레이저인지 쇠막대기인지 구분해준다.
	 - 바로 앞 괄호가 "(" 였을 경우 ➡️ 레이저
	 - 바로 앞 괄호가 ")" 였을 경우 ➡️ 쇠막대기
- 레이저일 경우 deque에 들어있는 "("괄호의 수 만큼의 막대기가 다 잘리는 것이므로 len(deque)만큼 더해주고, 쇠막대기 일 경우 자신의 쇠막대기 조각만 +1 해주면 된다.

```python
import sys
input = sys.stdin.readline
from collections import deque

brackets = list(input().rstrip())
dq = deque()
count = 0

for i in range(len(brackets)):  
  if(brackets[i] == '('):
    dq.append(brackets[i])
  else:
    dq.pop()
    if(brackets[i-1] == '('):
      count += len(dq)
    else:
      count += 1

print(count)
```
