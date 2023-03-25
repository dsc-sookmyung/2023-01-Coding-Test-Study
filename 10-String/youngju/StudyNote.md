# String 
## 10798 세로읽기 

```python
import sys

read = sys.stdin.readline

words = [read().strip() for _ in range(5)]
cnt = 0
for i in range(5):
    cnt = max(len(words[i]), cnt)

answer = ""
tmp = 0
while cnt > 0:
    for i in range(5):
        if tmp + 1 > len(words[i]):
            continue
        else:
            answer += words[i][tmp]
    tmp += 1
    cnt -= 1

print(answer)
```

**[풀이]**
1) 문자 다섯 줄을 모두 입력 받아 words리스트에 저장 
2) words리스트의 문자들 중에서 길이가 가장 긴 문자의 길이를 구해 cnt에 저장
3) words리스트를 순서대로 돌면서 각 문자의 첫 번째 문자부터 answer에 더한다
4) 이때 각 문자의 길이가 cnt보다 작을 경우에는 continue를 통해 건너뛰고 진행
5) answer출력 

<br/>

## 6550 부분 문자열 
문제를 꼼꼼히 읽어야겠다고 생각한 문제이다,,ㅎ 문제를 정확히 읽지 않아 Yes가 아니라 YES,  No가 아니라 NO로 작성하여 어디가 틀렸는지 찾느라 엄청 고생했다😭

```python
from collections import deque

while True:
    try:
        s, t = input().split()

        sq = deque(s)

        for i in t:
            if sq and sq[0] == i:
                sq.popleft()

        if sq:
            print("No")
        else:
            print("Yes")
    except:
        break
```

**[풀이]**
1) s와 t를 입력 받고 s를 deque로(sq) 만든다 
2) t문자열 한 글자씩을 sq의 첫 번째 글자와 비교하고 이때 두 글자가 같은 글자이면 sq에서 해당 글자를 pop한다 
3) 만약 sq에 글자가 남아있다면 No를 남아있지 않다면 Yes를 출력 

<br/>

##  20291 파일 정리 

```python
import sys

read = sys.stdin.readline

N = int(input())
files = [read().strip().split('.') for _ in range(N)]

dic = {}
for i in range(N):
    if files[i][1] in dic.keys():
        dic[files[i][1]] += 1
    else:
        dic[files[i][1]] = 1

dic = dict(sorted(dic.items()))

for k,v in dic.items():
    print(k, v)
```

**[풀이]**
1) 파일 목록들을 files리스트에 입력 받을 때 '.'을 기준으로 split하여 파일 이름과 확장자를 따로 저장한다
2) 파일 확장자를 key로 하고 확장자에 따른 파일 개수를 value로 하는 딕셔너리 dic을 만든다 
3) dic을 오름차순으로 정렬
4) 정렬한 dic의 key와 value를 출력 

<br/>

## 17609 회문 

```python
import sys

read = sys.stdin.readline

def check(str, left, right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

T = int(input())
strings = [list(read().strip()) for _ in range(T)]

for string in strings:
    if string == string[::-1]:
        print(0)
    else:
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                if check(string, left+1, right) or check(string, left, right-1):
                    print(1)
                    break
                else:
                    print(2)
                    break
```

**[풀이]**
1) 문자들을 리스트로 바꾼 후 strings리스트에 저장 
2) strings에서 하나씩 꺼내서 회문인지 아닌지 계산한다
3) 먼저 string리스트와 string리스트를 뒤집은 리스트가 같으면 0을 출력
4) (3)번의 경우가 아니라면 문자를 왼쪽과 오른쪽에서 출발해서 한 글자씩 비교
5) 비교할 때 같은 글자면 계속 비교하지만 같은 글자가 아니라면 왼쪽을 한 칸 건너뛴 경우 그리고 오른쪽을 한 칸 건너뛴 경우를 둘다 해본다
6) 각 경우에서 만약 다른 글자 없이 비교가 끝까지 마쳐지면 true를 또 다른 글자가 발견되면 false를 반환하도록 한다
7) 각 경우의 반환값을 비교해서 한 경우라도 true인 경우에는 유사회문이므로 1을 출력하고 둘다 false인 경우에는 2를 출력

