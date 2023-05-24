# 10798 세로 읽기

## 문제

문자열을 세로로 읽어보자

## 해설

가장 긴 줄의 문자열 수만큼 반복문을 돌려 세로로 한 줄 씩 인덱스를 반환해 세로로 읽도록 하였다

```python
import sys


arr = []
lines = []
ans = ''
for _ in range(5):
    tmp = sys.stdin.readline().rstrip()
    tmp_line = len(tmp)
    lines.append(tmp_line)
    arr.append(tmp)

line_max = max(lines)

for i in range(line_max):
    for j in range(5):
        if i < lines[j]:
            ans = ans + arr[j][i]
print(ans)
```

# 6550 부분 문자열

## 문제

s가 t의 부분문자열인지 구하시오

## 해설

처음에 함수로 풀이했는데 왜인지 답이 계속 틀렸다 해서 하나씩 비교하여 갯수를 세어 부분문자열이 되는지 확인했다.

```python
import sys

def find_st(s,t):
    s_last = len(s) -1
    b_idx = -1
    for i in range(len(t)):
        for j in range(len(s)):
            t_str = s[j]
            idx = t.find(t_str,i)
            if idx == -1:
                return('NO')
            else:
                if idx > b_idx:
                    b_idx = idx
                    if j == s_last:
                        return('YES')
                else:
                    break
    return('NO')

while True:
    try :
        s,t = sys.stdin.readline().rstrip().split()
        flag = 0
        idx = 0

        for i in range(len(t)):
            if t[i] == s[idx]:
                idx+=1
                if idx == len(s):
                    flag = 1
                    break

        if flag == 1:
            print('Yes')
        else:
            print('No')
    except:
        break
```

# 20291 파일 정리

## 문제

파일에 있는 확장자의 종류를 모아 알파벳순으로 출력하시오.

## 해설

확장자 부분을 구해서 딕셔너리에 존재하면 +1 하고, 존재하지 않으면 1을 생성한다.
그 후 정렬함수 lamda로 key 값을 오름차순 기준으로 정렬하여 출력한다

```python
import sys

N = int(sys.stdin.readline())
expand_dict ={}
for i in range(N):
    file = sys.stdin.readline().rstrip().split('.')
    expand = file[1]
    if expand in expand_dict:
        expand_dict[expand] +=1
    else :
        expand_dict[expand] =1

expand_dict = sorted(expand_dict.items(),key = lambda x:x[0], reverse=False)

for j in expand_dict:
    print(j[0], j[1])
```

# 17609 회문

## 문제

회문이면 0
유사회문이면 1
둘 다 아니면 2를 출력하시오

## 해설

회문임을 확인하는 함수를 작성해 left, right index를 통해 하나씩 비교해가면 가운데로 이동한다.
left, rigth가 같지 않은 경우 두가지를 비교하여 유사회문인지 확인해야한다.(왼쪽을 제거한 경우, 오른쪽을 제거한 경우) 그 때 확인하는 함수로 secondrun 함수를 사용했다.
이 두 경우가 모두 아닐 때 2를 출력하도록 함수를 작성하였다.

```python
import sys

def secondrun(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            return False
    return True


def findcheck(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            check1 = secondrun(word,left+1,right)
            check2 = secondrun(word,left,right-1)
            if(check1 or check2):
                return 1
            else:
                return 2
    return 0

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    left=0
    right=len(word)-1
    print(findcheck(word,left,right))
```
