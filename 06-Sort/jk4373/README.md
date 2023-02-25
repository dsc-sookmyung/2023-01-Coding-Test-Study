# 풀이

## 10825 국영수

### 문제
학생의 성적을 정렬해야한다. 
국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 정렬하자

### 풀이
key : 학생 이름
value : list(국어, 영어 , 수학)
정렬 기준에 맞게 하기 위해 람다를 사용한다. 
Score.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

```
import sys
N = int(sys.stdin.readline())
Score = [list(sys.stdin.readline().split())for _ in range(N)]

Score.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for idx in Score:
    print(idx[0])
```

## 10814 나이순 정렬

### 문제
정렬을 해야한다.
나이 오름차순, 나이가 같으면 먼저 가입한 사람부터 정렬하자

### 풀이
가입한 순서대로 입력이 들어오기 때문에 순서를 key로 하도록 하고 value를 이름과 나이를 받는다.
나이를 먼저 기준으로 하고, 따로 저장한다! 따로 저장한 걸 딕셔너리로 만들어 출력
주의 ! 나이는 int, 이름은 str이기 때문에 따로따로 입력을 받았다

```
import sys

N = int(sys.stdin.readline())
Table = []
for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    Table.append((age, name))
Table.sort(key = lambda x: x[0])

for i in Table:
    print(i[0], i[1])
```

## 11652 카드

### 문제
가장 많이 가지고 있는 카드를 출력해야한다

### 풀이
딕셔너리를 이용해 풀이. 들어온 카드의 숫자를 key로 하여, value의 값을 들어올 때마다 1씩 추가하여 입력한다. 
정렬 : count인 value를 기준으로 (내림차순) 정렬한 후, 숫자를 기준으로 다시 정렬하여 반환

```
import sys

N = int(sys.stdin.readline())
cards ={}
for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp in cards:
        cards[tmp] += 1
    else:
        cards[tmp] = 1

result = sorted(cards.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])
```

## 18870 좌표 압축

### 문제
좌표 압축을 해야한다!
좌표 압축이란 들어온 좌표를 순서대로 인덱스화 하자! 작은게 0부터 시작

### 풀이
값을 받아와서 for문을 돌며 인덱스순서대로 dict를 만든다. 이 만든 dict를 불러와서 처음에 받았던 좌표를 인덱스로 하여 값을 출력한다!

```
import sys
N = int(sys.stdin.readline())
map = list(map(int,sys.stdin.readline().split()))

map_sorted = []
map_sorted = list(sorted(set(map)))

map_dic = {map_sorted[i]:i for i in range(len(map_sorted))}

for i in map:
    print(map_dic[i], end=' ')
```