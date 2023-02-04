## 14916 거스름돈

### 문제 
쓰는 동전은 2원과 5원이며 동전의 개수가 최소가 되도록!

### 풀이
동전이 1원이 아닌 이상 금액만큼의 동전의 개수가 나오지 않으므로 반복문을 금액만큼 돌린다.
5원을 최대한 많이 사용해야 개수가 최소가 되기 떄문에 5원의 개수를 한개씩 늘려가면서 사용한 동전의 개수가 최소인지 확인한다.

(+2와 5의 배수인 경우에만 가능하므로 항상 배수인지 확인하고 틀리면 -1 입력)

### 코드
```
# 14916 거스름돈

n = int(input())
count = 0

for i in range(n):
    rest = n - 5*i
    if rest % 2 ==0 and rest >=0:
        temp = i + rest //2
        if temp < count or count ==0:
            count = temp 
if count ==0:
    print(-1)
else:
    print(count)
```

## 2217 로프
### 문제
줄을 이용해서 물건을 끌어올려야한다! 최대 하중은? 이 때 줄마다의 굵기가 달라 들 수 있는 중량은 서로 다를 수있다.

### 풀이
처음에 이 문제를 틀렸던 이유가, 어떠한 상황에서도 가진 줄을 모두 사용해야한다고 생각해서였다!! 하지만.. 엄청난 무게도 견디는 줄
(예를 들어 줄 3개가 있으면 1000키로, 5키로, 2키로그람)이 있다면 그 줄만 사용해서 최대 하중을 만들 수 있다!!

따라서 큰 순서대로 최대 중량 * 개수(1씩 늘어남)을 통해 저장한 다음에, 가장 큰 값을 찾도록 한다.

### 코드
```
#2217 로프
import sys
n = int(input())
w = []
for _ in range(n):
    tmp = int(sys.stdin.readline())
    w.append(tmp)
w.sort(reverse=True)
for i in range(len(w)):
    w[i] = w[i]*(i+1)
# print(min(w)*n ) # 왜 아니지?? 생각해보니 압도적으로 높은 하중을 견디는게 있으면 그거 하나만 연결하면 된다!!
print(max(w))

```

## 11508 2+1 세일

### 문제
3개씩 묶인다면 가장 싼 건 무료?!
이 때 가장 저렴하게 구입하는 방법은?

### 풀이
3개씩 묶이지 않을 때... 에 너무 집착해서 풀다보니까 예외상황에 대응하지 못하는 경우가 오히려 생기게 되었다.
최소 금액으로 구입하려면 높은 금액대로 정렬 한 뒤에 3개씩 묶일 때마다 그 가격은 제외하도록하면 자연스럽게 가장 저렴하게 구입하게 된다!

### 코드
```
#11508 2+1 세일
import sys
n = int(input())
lst = []

for _ in range(n):
    m = int(sys.stdin.readline())
    lst.append(m)
# lst.sort()
# etc = len(lst) % 3
# sum=0
# for i in range(etc):
#     sum = sum + lst[i]
#     del lst[i]
lst.sort(reverse= True)
sum =0
for i in range(len(lst)):
    if (i+1) %3:
        sum = sum + lst[i]
print(sum)
```

## 13305 주유소
### 문제
여러 도시를 지나야할 때, 주유 가격을 최소로 하는 방법은?

### 풀이
처음 풀이 방법은, 최소.. 일 수 는 있겠으나 논리적으로 이미 지나온 주유소를 다시 들를 수 없으므로 부분점수를 받은 풀이이다.

최종 풀이는 이전 도시의 가격과 계속 비교하며 주유를 하도록 풀었다.

### 코드
1) 부분점수 코드
```
# 13305 주유소
import sys

N =int(input())
road =list(map(int,input().split()))
price =list(map(int,input().split()))
lst =[]
ans = 0
for i in range(N-1): # price
    tmp=[]
    for j in range(N-1): # road
        if j > i:
            continue
        else:
            cost = road[i]*price[j]
            tmp.append(cost)
    lst.append(tmp)

for idx in range(len(lst)):
    tmp = min(lst[idx])
    ans = ans + tmp
print(ans)
    
```

2)최종 제출 코드
```
# 13305 주유소
import sys

N =int(input())
road =list(map(int,input().split()))
price =list(map(int,input().split()))
    
take = price[0]
ans = 0
for i in range(N-1):
    if price[i]< take:
        take = price[i]
    ans = ans + take*road[i]
print(ans)
```