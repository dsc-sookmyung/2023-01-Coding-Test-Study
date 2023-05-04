# [10798 세로읽기](https://www.acmicpc.net/problem/10798)

> 접근 방법

원본 데이터가 이렇게 들어오면

```
00 01 02 03 
10 11 
20 21 22 23 
30 31 32 
40 41 42 43 44
```
 <br>

이렇게 출력하면 된다
```
00 10 20 30 40
01 11 21 31 41
02    22 32 42 
03    23    43
            44
```
리스트를 인덱스로 접근할건데, 존재하지 않는 인덱스에 바로 접근하면 런타임 터지니까
접근 가능한 인덱스인지 체크해야한다. 길이 배열을 두어서 현재 탐색중인 열의 인덱스로 접근 가능한지 검사했다.


> 통과한 코드


```python
import sys
read = sys.stdin.readline

words = [read().rstrip() for _ in range(5)]
words_length = [len(word) for word in words]
result = []

for i in range(max(words_length)):
  for j in range(5):
    if words_length[j] <= i: continue
    result.append(words[j][i])

print(''.join(result))
```


# [6550 부분 문자열](https://www.acmicpc.net/problem/6550)

> 접근 방법

s의 문자를 하나씩 t에서 찾았다.
이때 탐색 중인 인덱스의 s와 t의 같으면 현재 s의 글자는 존재하는 것이고, s와 t의 인덱스를 다음으로 조정한다.<br>
만약 탐색 중인 인덱스의 s와 t가 일치하지 않으면 t만 다음 인덱스로 넘어간다.<br>
만약 s가 t의 부분 문자열이면 s와 t가 일치하는 경우에서 s의 마지막 인덱스를 정상적으로 찾았을 것이다.<br>
반면 순서가 꼬이거나 부분 문자열이라면 s의 마지막 인덱스를 정상적으로 찾지 못하고 끝냈을 것이다.<br>
플래그 변수를 두어서 반복문을 탈출하고 결과를 출력하게 했다.<br>


> 통과한 코드

```python
import sys
read = sys.stdin.readline

def is_s_done(s_index, s): # s 탐색 끝났는지
  if s_index == len(s): 
    return True

while True:
  ss = read().rstrip()
  if not ss: break
  s, t = ss.split()
  t_index, s_index = 0, 0
  is_sub_string = False # 플래그

  while s_index < len(s) and t_index < len(t):
    if t[t_index] == s[s_index]:
      s_index += 1
      is_sub_string = is_s_done(s_index, s)
      if is_sub_string: break
    t_index += 1

  if is_sub_string: print("Yes")
  else: print("No")

```

# [20291 파일 정리](https://www.acmicpc.net/problem/20291)

> 접근 방법

파일이름과 확장자로 나누고, 딕셔너리를 두어서 확장자를 키로 파일 개수를 저장한다.


> 통과한 코드

```python
import sys
read = sys.stdin.readline

n = int(read())
files = [read().rstrip() for _ in range(n)]
d = {}

for file in files:
  file_name, file_extension = file.split('.')
  if file_extension not in d.keys():
    d[file_extension] = 1
  else:
    d[file_extension] += 1

result = sorted(d.items(), key=lambda d:d[0])
for extension, count in result:
  print(extension, count)
```



# [17609 회문](https://www.acmicpc.net/problem/17609)

> 접근 방법

기러기 이효리 찾는거는 파이썬 리스트 뒤집어서 간단하게 확인 가능하다.
근데 유사 회문은 왼쪽과 오른쪽 포인터 두고, 글자가 다를 때 해당 글자를 삭제해서 회문이 되는지 비교하면 된다.
범위 조건문에 = 를 넣어서 자꾸 틀렸다.


> 통과한 코드

```python
import sys

read = sys.stdin.readline


def check_palindrome(word):
    if word[:] == word[::-1]: return 0

    l_index, r_index = 0, len(word) - 1
    while l_index < r_index:
        if word[l_index] == word[r_index]:
            l_index += 1
            r_index -= 1
        else:
            # 유효한 범위이면
            if l_index < r_index:
                # 왼쪽 제거  
                temp = word[:l_index] + word[l_index + 1:]
                if temp[:] == temp[::-1]: return 1
                # 오른쪽 제거
                temp = word[:r_index] + word[r_index + 1:]
                if temp[:] == temp[::-1]: return 1
            return 2


n = int(read())
words = [read().rstrip() for _ in range(n)]

for word in words:
    print(check_palindrome(word))
```