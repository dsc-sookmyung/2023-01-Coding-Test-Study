# 9 - 동적계획법 2

 - 정리한 문제
 1. 1149 RGB거리
 2. 2156 포도주 시식
 3. 1463 1로 만들기
 4. 12865 평범한 배낭
 <br>

 ## 1149 RGB거리

 ### 설명
 - dp에 해당 **집을 칠하는 최소 비용**을 담는다.
 - i번째 행의 **0번째 집**을 칠하는 최소 비용은 **그 전 행의 1번째와 2번째 집의 비용 중 최소값**을 더한값
 - i번째 행의 **1번째 집**을 칠하는 최소 비용은 **그 전 행의 0번째와 2번째 집의 비용 중 최소값**을 더한값
 - i번째 행의 **2번째 집**을 칠하는 최소 비용은 **그 전 행의 0번째와 1번째 집의 비용 중 최소값**을 더한값


```python
import sys
input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1):
  dp[i+1][0] += min(dp[i][1], dp[i][2])
  dp[i+1][1] += min(dp[i][0], dp[i][2])
  dp[i+1][2] += min(dp[i][0], dp[i][1])

print(min(dp[n-1]))
```

## 2156 포도주 시식

 ### 설명
 - dp에 해당 잔까지 왔을 때의 최대로 마실 수 있는 포도주 양 저장
 - dp[i]를 구한다고 할 때
	 -  i번째 포도주를 마시는 경우(3번 연속으로 마실 수 없으므로 경우를 고려해줘야 한다.)
		 - i-1번째 포도주를 안마시는 경우 ➡️ dp[i-2]+wine[i]
		 - i-1번째 포도주를 마시는 경우 ➡️ dp[i-3]+wine[i-1]+wine[i]
	- i번째 포도주를 안마시는 경우  ➡️ dp[i-1]
- 다음과 같이 세가지 경우를 비교해서 최대값을 저장하면 된다.
- i-3까지 나오므로 인덱스 오류가 나지 않도록 3까지 초기화하기!


```python
import sys
input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = wine[:]

#dp초기화
if(n>=2):
  dp[2] += wine[1]
if(n>=3):
  dp[3] = max(wine[1]+wine[2], wine[1]+wine[3], wine[2]+wine[3])

for i in range(4, n+1):
  dp[i] = max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i],dp[i-1])

print(dp[n])
```           


## 1463 1로 만들기

### 설명
- dp에 해당 수를 만드는 최소 연산 횟수 저장
- dp[i]구하는 법
	- 1️⃣dp[i-1] + 1
	- 2️⃣(i가 2로 나눠 떨어질 경우) dp[i//2] + 1
	- 3️⃣(i가 3로 나눠 떨어질 경우) dp[i//3] + 1
- 위 1️⃣2️⃣3️⃣중 최소값이다.

```python
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] + [0 for i in range(n)]

for i in range(2, n+1):
  dp[i] = dp[i-1]+1
  if(i%2==0):
    dp[i] = min(dp[i], dp[i//2]+1)
  if(i%3==0):
    dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])
```


## 12865 평범한 배낭

어려워서 구글링으로 풀었다 💦

### 설명
- 행이 물건 n개, 열이 가방 무게 k개인 이차원 배열의 dp
- dp[n][k] => n번 물건까지 고려했을때 가방무게가 k라면 담을 수 있는 최대가치 저장
- 1️⃣ 물건의 무게가 커서 **가방에 넣을 수 없는** **경우** ➡️ dp[y][x] = dp[y-1][x]
- 2️⃣ **가방에 넣을 수 있는 경우**, 아래 두개를 비교해서 최대값 저장
	- 해당 물건을 넣지 않을 때 ➡️  dp[y][x] = dp[y-1][x]
	- 해당 물건을 넣을 때 ➡️  dp[y-1][x-w] + v

```python
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
bag = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().rstrip().split())
    bag.append((W, V))

#행이 물건 n개 배열, 열이 가방 무게 k개인 이차원배열
#해당 물건까지 고려했을때 가방무게가 _라면 담을 수 있는 최대가치 저장
dp = [[0]*(K+1) for _ in range(N+1)]  

for y in range(1, N+1): #y번째 물건일 경우
    w, v = bag[y]
    for x in range(1, K+1):
        if x-w <= 0:  #y번째 물건 무게 커서 가방에 넣을 수 x
            dp[y][x] = dp[y-1][x]
        else: #y번째 물건 가방에 넣을 수 o => y번째 물건을 넣는 경우와 안넣는 경우 중 최대값 구하기
            dp[y][x] = max(dp[y-1][x], dp[y-1][x-w] + v)

print(dp[N][K])
```
