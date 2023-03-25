## 문제
### 10798 세로읽기
1) 다섯줄의 문자열을 입력받고, result 리스트에 저장해준다.
2) 문자열을 읽을 때, 해당 인덱스에 문자열이 없다면 출력하지 않고 넘어가줘야 한다.
3) 각 줄은 최대 15글자까지 가능하고, 총 5줄이므로 이중 for문을 이용해서 각 줄의 글자수보다 i가 작으면 출력해주고 없다면 그냥 넘어간다.

```python
import sys
input = sys.stdin.readline

words_list = [input().rstrip() for _ in range(5)]
result = []
for i in range(15):
    for j in range(5):
        if len(words_list[j]) > i:
            result.append(words_list[j][i])

print(''.join(result))
# 인덱스 순서는
# [0][0], [1][0], [2][0], [3][0], [4][0], [0][1],,
```

### 6550 부분 문자열
1) t의 길이만큼 탐색하며 s의 문자열을 이루는 문자가 있는지 찾아준다.
2) 이때, 순서를 바꾸지 않고 합쳤을 때 s가 되야 한다는 조건이 있으므로 탐색에 인덱스를 체크하며 같은 문자열이 있다면, 앞으로만 이동하게 idx를 증가시킨다.
3) idx의 값이 s의 길이와 같아진다면, 부분 문자열을 만들 수 있기에 flag값을 1로 설정하고, Yes를 출력한다. 
```python
import sys
input = sys.stdin.readline

while True:
    st = input().rstrip()
    if not st:  # 입력받은게 없다면
        break
    s, t = st.split()
    flag = 0
    idx = 0

    for i in range(len(t)):
        if t[i] == s[idx]:
            idx += 1  # 인덱스 값 증가시켜줌
            if idx == len(s):
                flag = 1
                break
    if flag == 1:
        print("Yes")
    else:
        print("No")
```
### 20291 파일정리
1) N개의 파일을 입력받고, .을 기준으로 split해준다.
2) result 딕셔너리에 입력받은 파일을 저장하는데, 이미 해당 확장자가 있다면 value를 1 증가시키고, 없다면 딕셔너리에 추가해준다.
3) 입력받은 N개의 파일 딕셔너리를 result.items()로 리스트로 변환하고, 사전순 정렬을 해주고 출력한다. 

```python
import sys
input = sys.stdin.readline

N = int(input())
files = [input().rstrip() for _ in range(N)]

result = {}
for i in range(N):
    a, b = files[i].split(".")  # sbrus txt
    if b in result:
        result[b] += 1  # 해당 확장자 파일 1 증가
    else:
        result[b] = 1

result = list(result.items())  # 딕셔너리 -> 리스트 변환
result.sort(key=lambda x: x[0])

for i in range(len(result)):
    print(result[i][0], result[i][1])
```

### 17609 회문
1) 문자열을 입력받아 회문인지, 유사회문인지, 일반 문자열인지 판별해야 한다.
2) 회문인지는 is_palindrome 함수를 통해 비교한다. left와 right의 문자가 같은지 비교하며 left는 1씩 증가시키고, right은 1씩 감소시켜 정가운데로 이동하며 비교한다.
3) 중간에 다른 문자가 있는 경우, 유사회문인지를 판단해줘야 한다. 유사회문은 한 문자를 건너뛰고 같은 경우이기에, left를 한칸 건너뛰고 비교하거나 right을 한칸 건너뛰고 비교한다.
4) check_left이나 check_right의 값이 True라면, 유사회문이므로 1을 출력한다.
5) False가 나온다면 일반 문자열이기에 2를 출력해준다.

```python
import sys
input = sys.stdin.readline

def is_pseudo(words, left, right):  # 유사회문인지
    while left < right:
        if words[left] == words[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def is_palindrome(words, left, right):  # 회문인지
    while left < right:
        if words[left] == words[right]:
            left += 1
            right -= 1
        else:
            check_left = is_pseudo(words, left + 1, right)
            check_right = is_pseudo(words, left, right - 1)
            if check_right or check_left:
                return 1
            else:
                return 2
    return 0



N = int(input())
for _ in range(N):
    words = input().rstrip()
    left , right = 0, len(words)-1
    ans = is_palindrome(words, left, right)
    print(ans)
```