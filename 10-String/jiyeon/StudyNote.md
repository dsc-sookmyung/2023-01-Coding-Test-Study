# 10-문자열

 - 정리한 문제
 1. 10789 세로읽기
 2. 6550 부분 문자열
 3. 20291 파일정리
 4. 17609 회문
 <br>

 ## 10789 세로읽기

 ### 설명
 - 입력 받은 문자열을 세로로 출력하면 되는 문제이다.
 - 입력 받은 문자열 중 가장 길이가 긴 문자열만큼 for문을 돌아주면서 현재 인덱스가 문자열의 길이를 넘지 않으면 해당 문자열[인덱스] 값을 출력해준다.

```python
import sys
input = sys.stdin.readline

arr = []
maxLength = 0

for _ in range(5):
  arr.append(list(input().rstrip()))

maxLength = max(map(len, arr))

for j in range(maxLength):
  for i in range(5):
    if(len(arr[i]) > j):
      print(arr[i][j], end = "")
```

 ## 6550 부분 문자열

 ### 설명
 -  s와 t가 주어졌을 때, s가 t안에 포함된 부분 문자열인지 판별하는 문제이다.
 - s와 t 각각 인덱스 0부터 시작해서 비교해준다.
 - 각 인덱스에 접근한 값이 같을 경우 s의 인덱스와 t의 인덱스 둘 다 1 더해준다.
 - 같지 않을 경우 t의 다음 문자에서 s와 같은 문자가 있는지 확인해줘야 하므로 t의 인덱스만 1 더해준다.
 - s의 인덱스가 len(s)와 같아질 경우 s가 t의 부분 문자열이므로 while문을 빠져나온다. 또는 t의 인덱스가 len(t)와 같아져 더 이상 비교할 문자가 없을 경우도 while문을 빠져나온다.
 -  while문을 나왔을 때, s의 인덱스가 len(s)이면 부분 문자열이므로  "Yes" 출력, 아니면 "No" 출력
```python
import sys
input = sys.stdin.readline

def checkSinT(s, t):
  s_idx = 0
  t_idx = 0
  while(s_idx<len(s) and t_idx<len(t)):
    if(s[s_idx] == t[t_idx]):
      s_idx+=1
    t_idx+=1
  if(s_idx == len(s)):
    print("Yes")
  else:
    print("No")

while(True):
  inputText = input().split()
  if(len(inputText) == 0):
    break
  checkSinT(list(inputText[0]), list(inputText[1]))
```

## 20291 파일정리

 ### 설명
 - "." 을 기준으로 문자열을 분리할 수 있는지 물어보는 문제인 것 같다.
 - split(".")로 파일이름과 확장자를 분리해서 받는다.
 - 확장자의 개수를 세는건 defaultdict를 이용했다.
 - [확장자(key) : 개수(value)]를 담은 defaultdict를 정렬한 후 출력해주었다.

```python
import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
  filename, extension = input().rstrip().split(".")
  dic[extension] += 1

sortedDict = sorted(dic.items())

for i in sortedDict:
  print(*i)
```           


## 17609 회문

### 설명
- 문자열이 주어졌을 때, 그 자체로 회문인지(0 출력), 한 문자만 삭제하면 되는 유사회문인지(1 출력), 그 외인지(2 출력)를 구하는 문제이다.
- 회문인지 구하는 것은 쉽다. 양 끝부터 시작해 중간까지 확인해주면서 다 같으면 회문이다.
- 만약에 양 끝에서부터 같은지 확인해주다가 **다른 것**이 나왔다! ➡️ 유사회문인지 확인해줘야한다.
- 이미 같은 것이 확인된 애들은 빼고 **다른 것이 나온 지점**에서 양 끝 한 문자씩 삭제한 문자가 회문인지 확인해준다. 만약 회문이면 이 문자열은 유사회문인 것이다.
	- 나는 위 과정을 재귀로 해줬는데, 문자를 하나 삭제하는 것이기 때문에 재귀를 1번만 돌아야 하므로 cnt라는 변수로 재귀 브레이크를 걸어주었다.
- 만약  a**m**m**u**a 이면 m과 u가 다른 것이 나온 지점이고 양 끝 a는 같은 것을 이미 확인해줬으니 빼고 mmu중 양 끝 한 문자씩 삭제한 **mm과 mu**를 검사해주면 되는 것이다. 이 때, mm은 회문이어서 1이 나오는데, mu는 회문이 아니어서 2가 나온다. 어쨌든 한 문자만 삭제해서 회문이 되기만 하면 되므로 둘 중에 min값이 답이 된다.

<br/>
🤔뭔가 cnt로 브레이크를 넣은 부분이 맘에 들지 않아서 생각을 다시 좀 해봐야 할 것 같다.

```python
import sys
input = sys.stdin.readline

n = int(input())

def isPalindrome(s):
  global cnt
  for i in range(len(s)//2):
    if(s[i] != s[len(s)-i-1]):
      if(cnt == 0):
        cnt += 1
        a = isPalindrome(s[i:len(s)-i-1])
        b = isPalindrome(s[i+1:len(s)-i])
        return(min(a, b))
      return(2)
  if(cnt == 0): return(0)
  return(1)

for i in range(n):
  cnt = 0
  s = list(input().rstrip())
  print(isPalindrome(s))

```
