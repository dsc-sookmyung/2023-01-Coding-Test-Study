# Sort
## 10825 국영수 
문제가 요구한 순서대로 정렬하여 출력한다

```python
import sys  
  
read = sys.stdin.readline  
  
n = int(read().strip())  
answer = {}  
  
for _ in range(n):  
    s = list(read().strip().split())  
    answer[s[0]] = list(map(int, s[1:]))  
  
answer1 = sorted(answer.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))  
  
for i in range(n):  
    print(answer1[i][0])
```

**[풀이]**
1) 학생 총 인원 수를 n에 저장 
2) 학생 이름을 key로 하고 국어, 영어 수학 점수 list를 value로 갖는 딕셔너리 answer생성
3) answer 딕셔너리의 key-value쌍을 국어는 내림차순으로 영어는 오름차순으로 수학은 내림차순으로 이름은 사전 순으로 정렬하도록하고 그 반환 리스트를 answer1에 저장
4) answer1에서 이름만 차례로 출력 

<br/>

## 10814 나이 순 정렬  
회원들의 나이와 가입한 순서를 모두 저장한 후 정렬

```python
import sys  
  
read = sys.stdin.readline  
n = int(read().strip())  
answer = {}  
for i in range(n):  
    s = list(read().strip().split())  
    s[0] = int(s[0])  
    answer[i] = s  
  
answer1 = sorted(answer.items(), key=lambda x: (x[1][0], x[0]))  
answer1 = dict(answer1)  
for i in answer1.values():  
    print(*i)
```

**[풀이]**
1) 회원의 수를 n에 저장
2) 입력한 순서대로 그 인덱스를 key로 하고 회원의 나이와 이름 list를 value로 갖는 딕셔너리 answer를 만듦
3) answer의 key-value 쌍을 먼저 회원의 나이를 기준으로 오름차순으로 그리고 key를 기준으로 오름차순으로 정렬한 후 반환 리스트를 answer1에 저장 
4) answer1을 다시 딕셔너리로 만든 후 answer1의 value 리스트에서 값을 하나씩 출력 

<br/>

## 11652 카드 
적혀있는 수가 같은 카드의 개수를 구한 후 정렬 

```python
import sys  
  
read = sys.stdin.readline  
n = int(read())  
card = {}  
  
for i in range(n):  
    c = int(read())  
    if c in card.keys():  
        card[c] += 1  
  else:  
        card[c] = 0  
  
answer = sorted(card.items(), key=lambda x: (-x[1], x[0]))  
print(answer[0][0])
```

**[풀이]**
1) 카드의 총 개수를 n에 저장
2) 카드에 적혀있는 수를 하나씩 입력받으면서 그 값이 card라는 딕셔너리의 key가 되도록 하고 그 카드의 총 개수를 value로 저장
3) card딕셔너리의 key-value쌍을 value를 기준으로 내림차순으로 정렬한 후 key를 기준으로 오름차순으로 정렬하고 그 반환 리스트를 answer에 저장
4) answer에서 인덱스가 0인 원소의 key값을 출력 

<br/>

## 18870 좌표 압축 
문제에서 원하는 답이 중복된 값을 제거한 후 정렬한 리스트의 인덱스 번호라는 것을 알아야 하 시간복잡도를 고려해야 한다.

```python
import sys

read = sys.stdin.readline
n = int(read())
xlist = list(map(int, read().strip().split()))
xSetList = sorted(set(xlist))
xDict = {}
for i in range(len(xSetList)):
    xDict[xSetList[i]] = i

for j in xlist:
    print(xDict[j], end=" ")
```

**[풀이]**
1) n에 좌표의 개수를 저장
2) 좌표값들을 xlist라는 리스트에 저장
3) 중복된 값을 빼고 오름차순으로 정렬한 리스트의 인덱스 값이 정답이므로 xlist의 중복된 값을 제거하기 위해 set()을 사용하고 정렬을 한 후의 반환 리스트를 xSetList에 저장
4) 시간복잡도를 고려하여 xDict라는 딕셔너리 생성 후 xSetList의 값을 key로 하고 인덱스를 value로 저장
5) xlist를 돌면서 각 값에 해당하는 인덱스를 xDict에서 출력

<br/>

> 처음에는 아래의 코드처럼 문제의 답이 중복된 값을 제거한 후 정렬한 리스트의 인덱스라는 것과 리스트를 사용하여 반복문을 돌릴 경우 시간복잡도를 고려하지 못하여 시간초과가 발생했다. 그래서 위의 코드와 같이 딕셔너리를 이용하여 key값으로 바로 찾을 수 있게 하였다. 

```python
import sys  
  
read = sys.stdin.readline  
n = int(read())  
xlist = list(map(int, read().strip().split()))  
xSetList = list(set(xlist))  
answer = [0] * n  
  
for i in range(n):  
 cnt = 0 
 result = 0 
 while cnt < len(xSetList): 
	 if xlist[i] > xSetList[cnt]: 
		 result += 1 
	 answer[i] = result 
	 cnt += 1  
	 
print(*answer)
```
