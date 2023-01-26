# 9012번 : 괄호

문제 : 주어진 문자열이 괄호가 VPS인지 확인하기

## 풀이
stack을 이용하여 푼다!
'('가 들어왔을 때 stack에 집어넣고, ')'가 들어왔을 때 stack의 최상단의 것을 pop 하도록 한다. 
모든 for 문을 돌고나서 최종적으로 stack에 값이 남아있거나 for 문을 도는 동안 스택에 값이 존재하지 않는데 pop 해야하는 경우 VPS가 아니기 떄문에 NO를 출력한다

```
import sys

n = int(input())

for i in range(n):
    a = input()
    stack = []
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else :
                print("NO")
                break
    else:
        if not stack:
            print('YES')
        elif stack:
            print("NO")
```


# 1158번 : 요세푸스 순열

문제 : 원형으로 정렬되어있을 때 순서대로 K 번쨰 사람을 제거한다. 

## 풀이

원형으로 정렬되어있기 때문에, 사람n 보다 index 값이 커지면 다시 처음으로 돌아와서 세어야 한다. 따라서 index = index % N(사람 수)를 통해 몇바퀴를 돌던 돌아올 수 있도록 한다.

```
n, k = map(int,input().split())

a = []
for i in range(1,n+1):
     a.append(i)
res = []
num = k-1
for i in range(n):
    if len(a)> num:
        res.append(a.pop(num))
        num += k-1
    elif len(a) <= num:
        num = num % len(a)
        res.append(a.pop(num))
        num += k-1
print("<",', '.join(str(i) for i in res),">",sep ='')
```

# 1966번 : 프린터 큐

문제 : 프린터는 FIFO로 인쇄를 진행하되 인쇄물 마다 있는 우선순위를 따른다

## 해설 
Queue 사용!
가장 우선순위가 높은 인쇄할 수 있도록 맨 앞에 있는 큐의 값이 일순위인지 파악한다. 일순위라면 인쇄한다
일순위가 아닌 경우에는 큐의 값을 맨 뒤로 보내고 다음 큐의 값을 확인하도록 한다.


```
import sys
# queue
from collections import deque

T = int(input())

for _ in range(T):
    n,m = map(int, input().split())
    data = deque(list(map(int,sys.stdin.readline().split())))
    idx = 0

    while data:
        tmp = data.popleft()
        m -=1
        if tmp ==max(data):
            idx +=1
            if m < 0:
                print(idx)
                break
        else:
            data.append(tmp)
            if m<0:
                m = len(data) -1
```

# 10799 문제 : 쇠막대기

문제 : 쇠막대기와 레이저를 통해 몇개의 쇠막대기가 만들어지는지 구하라

## 해설

st라는 리스트는 막대기의 갯수
()는 레이저, (      )는 막대기이므로 (가 들어오면 일단 st에 넣는다.
그 후 레이저인지, 막대인지 판단하여 길이를 추가하도록 설계한다.

```
bar = list(input())
answer = 0
res = []

for i in range(len(bar)):
    if bar[i] == '(':
        res.append('(')

    else:
        if bar[i-1] == '(': 
            res.pop()
            answer += len(st)

        else:
            res.pop() 
            answer += 1 

print(answer)
```
