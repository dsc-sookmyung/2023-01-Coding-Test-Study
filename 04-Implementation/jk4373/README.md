# 구현
구현 같은 경우 완전탐색, 시뮬레이션으로 종류가 나뉜다.

## 전구 21918
### 문제 
전구는 불이 꺼짐과 켜짐의 상태를 유지할 수 있고, 전구는  4가지의 명령을 받을 때 상태가 바뀐다. 이 때 n개의 명령어가 들어온 이후 전구의 상태를 나타내시오

### 풀이
4가지의 명령어를 함수로 만들어 명령어가 들어오면 해당하는 함수를 실행하도록 설계했다.

### 코드
```
#21918 전구
import sys

n, m = map(int,sys.stdin.readline().split())
lights = list(map(int,sys.stdin.readline().split()))
command = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]


def comm_one(lights,i,x):
    lights[i-1] = x
def comm_two(lights,l,r):
    for i in range(l-1,r):
        if lights[i] ==1:
            lights[i] = 0
        else:
            lights[i] = 1
def comm_three(lights,l,r):
    for i in range(l-1,r):
        lights[i] =0
def comm_four(lights,l,r):
    for i in range(l-1,r):
        lights[i] =1
        
        
for i in range(m):
    case = command[i][0]
    one = command[i][1]
    two = command[i][2]
    if case == 1:
        comm_one(lights,one,two)
    elif case ==2:
        comm_two(lights,one,two)
    elif case ==3:
        comm_three(lights,one,two)
    else:
        comm_four(lights,one,two)

for idx in range(len(lights)):
    print(lights[idx], end =' ')
```

## 블랙잭 2798
### 문제
기존의 블랙잭 룰은 21을 넘지 않고 가장 가까운 카드를 얻었을 때 승리한다. 
새로운 블랙잭은 딜러가 N장의 카드를 펼쳐서 보여주고 숫자 M을 외칠 때 3장을 더해서 숫자 M보다 작거나 같으면서 가장 M에 가까운 카드를 정하는 사람이 이기게 된다.
따라서 3장을 골랐을 때 M에 가장 가까운 합을 구해야 한다.

### 풀이
모든 경우의 수를 구하였다... for 문을 3번 돌려서 3가지를 더하는 경우를 조합으로 구해 sort 한 후 M과의 차가 가장 작은 수를 답으로 출력한다.

### 코드
```
# 2798 블랙잭
import sys

n,m = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))

cards.sort(reverse=True)

sum_tmp = 0
sum = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum_tmp = cards[i]+ cards[j] + cards[k]
            # print(cards[i], cards[j] , cards[k], "합은 = ",sum_tmp)
            sum.append(sum_tmp)
# print("sum is",sum)
min_gap = sys.maxsize
min_sum = 0
for i in range(len(sum)):
    gap = m - sum[i]
    if gap >=0 and min_gap> gap:
        min_gap = gap
        min_sum = sum[i]
print(min_sum)
```

## 소가 길을 건나긴 이유1 14467

### 문제 
소가 10마리 있을 때 소의 움직임을 기록한 n줄의 관찰 횟수가 나온다. 이 관찰횟수를 토대로 소가 움직인 횟수를 구하시오

### 풀이
소의 위치를 dict로 만들어서 dict상의 위치의 변화가 있을 때 움직인 횟수를 1 증가시키도록 하였다.

### 코드
```
#14467 소가 길을 건너간 이유
import sys
n = int(input())
cows = [-1]*10
cows_cnt = {}
cnt = 0
for i in range(n):
    c,go = map(int,sys.stdin.readline().split())
    if c in cows_cnt:
        if cows_cnt[c] != go:
            cnt +=1
    cows_cnt[c] = go
print(cnt)
```

## 빙고 2578
### 문제
5*5 빙고판이 주어졌을 때 3빙고가 나오는 순간을 출력하시오

### 풀이
원래는 dict로 풀다가.. 시간관계상 배열을 통해 전부 검색하는 방식을 사용했다.
사용자의 빙고판과 사회자의 빙고판을 받아 사회자의 빙고판을 전부 탐색하면서 3빙고가 나올 때까지 반복문을 돌아간다.

### 코드
```
# 2578 빙고
import sys

#불린 숫자 기록
check = [[0]*5 for i in range(5)]
# 불린 답
bingo = [list(map(int,sys.stdin.readline().split()))  for _ in range(5)]
answer = [list(map(int,sys.stdin.readline().split()))  for _ in range(5)]

#빙고 찾는 함수
def find_bingo(check):
    bingo =0
    for j in range(5):
        if sum(check[j]) ==5: # 가로
            bingo +=1
        if sum([t[j] for t in check]) == 5:
            bingo+=1
    if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5:
        bingo +=1
    if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5:
        bingo +=1
    return bingo

idx = 0


for i in range(5):
    for j in range(5):
        for k in range(5):
            for h in range(5):
                if answer[i][j] == bingo[k][h]:  
                    bingo[k][h] = 0  
                    idx += 1  
                    if find_bingo(bingo) >= 3:  
                        print(idx)  
                        exit() 
```