# 문자열

## 목차

- 문제
  - [10798 세로읽기](https://www.acmicpc.net/problem/10798)
  - [6550 부분 문자열](https://www.acmicpc.net/problem/6550)
  - [20291 파일 정리](https://www.acmicpc.net/problem/20291)
  - [17609 회문](https://www.acmicpc.net/problem/17609)



## 문제

### [10798 세로읽기](https://www.acmicpc.net/problem/10798)

문제) 다섯줄의 입력이 주어졌을 때, 왼쪽에서 오른쪽으로, 위에서 아래로 세로로 글자를 읽는다. 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다. 이때 세로로 읽은 순서대로 글자들을 공백 없이 출력하라.

분류) 문자열

해설) 다섯줄의 입력을 2차원 배열로 만들어준다. 각 줄의 길이는 최소 1개에서 15개로 다양하므로 가장 긴 줄의 길이를 구한 후 그 길이만큼 for문을 돌린다. 각 열의 행의 개수는 5개로 동일하므로, 다섯 개의 행에 대해 각 행의 해당 열에 글자가 있는지 확인하고, 있다면 리스트(`answer`)에 글자를 추가한다. 읽은 순서를 `answer`라는 리스트에 저장한 후에 마지막에 문자열로 변환하여 출력한다. 

```python
import sys

read = sys.stdin.readline
board = []
max_row_len = 0
for _ in range(5):
  row = list(read().rstrip())
  max_row_len = max(len(row), max_row_len)
  board.append(row)
answer = []
for i in range(max_row_len):
  for j in range(5):
    if len(board[j]) > i:
      answer.append(board[j][i])
print(''.join(answer))
```



### [6550 부분 문자열](https://www.acmicpc.net/problem/6550)

문제) 2개의 문자열 s와 t가 주어졌을 때 s가 t의 부분 문자열인지 판단하는 프로그램을 작성하라. 부분 문자열을 가지고 있는지 판단하는 방법은 t에서 몇 개의 문자를 제거하고 이를 순서를 바꾸지 않고 합쳤을 경우 s가 되는 경우를 이야기 한다.

분류) 문자열

해설) 입력이 들어오지 않을 때까지 루프를 돌면서 여러 개의 테스트 케이스를 입력 받는다. 인덱스 `i`를 이용하여 문자열 `s`에 있는 문자에 접근한다. 문자열 `t`에 있는 문자를 확인하면서, `s[i]`와 같다면 `i`를 하나 증가시켜서 문자열 `s`에 있는 다음 문자가 문자열 `t`에 있는지 확인한다. `i`가 문자열 `s`의 길이와 같아졌다면, 문자열 `t`의 부분 문자열이라는 뜻이므로 "Yes"를 출력하고, for문을 다 돌렸는데, `i`와 문자열 `s`의 길이가 같지 않다면 "No"를 출력한다.

참고) 새로 알게 된 python 지식

1. python 3.8부터 도입된 [Assignment Expressions](https://peps.python.org/pep-0572/)를 이용하면 while문에서 변수에 값을 할당할 수 있다. **`NAME := expr`**
2. if-else문의 indentation이 동일하지 않아도 앞의 if문에 따라 else문이 동작한다! 그래서 if문은 for문 안에, else문은 for문 밖에 있는데 정삭 작동한다. ?!?!

메모) 무한 루프를 돌리면 런타임 에러(ValueError)가 발생한다. 입력 개수가 정해지지 않았을 때 무한 루프를 돌려도 괜찮았던 문제가 있어서 똑같이 했는데 이번에는 에러가 발생해버렸다. 아쉽게도 그 문제가 몇 번이었는지 기억이 나지 않는다 :(

```python
import sys

read = sys.stdin.readline
while line := read():
  s, t = line.split()
  i = 0
  for x in t:
    if x == s[i]:
      i += 1
    if i == len(s):
      print("Yes")
      break
  else:
    print("No")
```



### [20291 파일 정리](https://www.acmicpc.net/problem/20291)

문제) 파일 이름이 주어졌을 때, 확장자의 이름과 그 확장자 파일의 개수를 하나씩 출력하라. 확장자가 여러 개 있는 경우 확장자 이름의 사전순으로 출력한다.

분류) 문자열, 딕셔너리

해설) `split()`을 이용하여 문자열을 `.`을 기준으로 자르고, `.` 뒤에 있는 확장자를 가져온다. 딕셔너리에 확장자의 이름(key)과 확장자 파일의 개수(value)를 저장하고, `sorted`를 이용하여 딕셔너리를 오름차순으로 정렬한다. `sorted`는 Tuple 쌍으로 이루어진 리스트를 리턴하므로, 리스트 요소의 0번째 값이 key(확장자의 이름)고, 1번째 값이 value(확장자 파일의 개수)다.

```python
import sys

read = sys.stdin.readline
N = int(read())
extension_dict = dict()
for _ in range(N):
  extension = read().rstrip().split('.')[1]
  if extension in extension_dict:
    extension_dict[extension] += 1
  else:
    extension_dict[extension] = 1
sorted_extension_dict = sorted(extension_dict.items())
for item in sorted_extension_dict:
  print(item[0], item[1])
```



### [17609 회문](https://www.acmicpc.net/problem/17609)

문제) 문자열이 회문(palindrome)이라면 0을, 유사회문(pseudo palindrome)이면 1을, 일반 문자열이면 2를 출력하라. 회문은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열이며, 유사회문은 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이다.  

분류) 문자열

해설) 회문인지 아닌지 판단하는 함수(`isPalindrome`)를 만든다. 입력 받은 문자열이 회문인지 확인해서 회문이라면 0을 리턴하고, 회문이 아니라면 유사회문인지 여부를 확인하는 함수(`answer`)를 만든다. 앞 뒤 방향으로 볼 때 문자가 다르다면, 앞 방향의 문자를 하나 삭제했을 때 문자열이 회문인지 확인한다. 이때 리스트 슬라이싱을 사용하여 문자를 삭제한다. 만약 이 문자열이 회문이라면 유사 회문이여서 1을 리턴하고, 회문이 아니라면 뒤 방향의 문자를 하나 삭제해서 회문인지 확인한다. 만약 이 문자열이 회문이라면 1을 리턴하고, 이 문자열마저 회문이 아니라면 일반 문자열이므로 2를 리턴한다.   

메모) 처음에 `슬라이싱`을 이용하지 않고, `copy`를 import 해와서 `copy.deepcopy`와 `pop()`을 사용해서 풀었더니 시간 초과가 발생했다. 

```python
import sys

read = sys.stdin.readline
T = int(read())

def isPalindrome(string):
  for i in range(len(string)//2):
    last_index = len(string) - 1
    if string[i] != string[last_index - i]:
      return False
  return True

def answer(string):
  if isPalindrome(string):
    return 0
  for i in range(len(string)//2):
    last_index = len(string) - 1
    if string[i] != string[last_index - i]:
      string_one = string[:i] + string[i+1:last_index+1]
      if isPalindrome(string_one):
        return 1
      string_two = string[:last_index-i] + string[last_index-i+1:]
      if isPalindrome(string_two):
        return 1
      else:
        return 2

for _ in range(T):
  string = list(read().rstrip())
  print(answer(string))
```

