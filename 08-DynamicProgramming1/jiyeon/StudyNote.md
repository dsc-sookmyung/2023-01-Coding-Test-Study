# 08-동적계획법 1

 - 정리한 문제
 1. 11726 2×n 타일링
 2. 11055 가장 큰 증가하는 부분 수열
 3. 9465 스티커
 4. 9084 동전
 <br>

 ## 11726 2×n 타일링

 ### 설명
 - dp[n]에 2*n의 직사각형을 채우는 방법의 개수를 갱신하며 저장한다.
 -  dp[n]은 dp[n-1]에 길쭉한 세로 모양의 블럭 하나를 붙이는 경우 + d[n-2]에 가로모양의 블럭 두개를(=정사각형)을 붙이는 경우, 즉 dp[n] = dp[n-1] + d[n-2]이다.

❓ 왜 양쪽에 붙이는 경우가 있을 수 있는데 x2를 안해주는지?
양쪽에 붙일 경우 이전에 나왔던 방법과 중복된다. 따라서 블록을 붙일 경우 오른쪽에만 붙여준다 생각하고 진행해준다.
```python
import sys
input = sys.stdin.readline

dp = [0] * 1001
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)
```

 ## 11055 가장 큰 증가하는 부분 수열

 gdsc 코딩테스트 행사에서 이 문제와 엄청 비슷하게 나왔던 문제가 있어서 기억에 남았다!

 ### 설명
 -  maxsum 배열에 해당 인덱스까지 증가부분수열의 최대합을 저장하며 갱신한다.
 -  maxsum[n]을 구하려면 n이전에 있는 수들을 싹 다 검사해주면서 **maxsum[n]보다 작은 값이 있다면 증가부분수열에 해당**하므로 최대값을 비교해 값을 갱신해준다.
 - n번째자리의 수도 합에 포함시켜야 하므로 값을 더해준다.
```python
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
#해당 인덱스까지 증가부분수열의 최대합 저장해놓을 배열
maxsum = [0]*n

for i,num in enumerate(arr):
  for j in range(i-1,-1,-1):
    if(num>arr[j]):
      maxsum[i] = max(maxsum[i], maxsum[j])
  maxsum[i] += num

print(max(maxsum))   
```

## 9465 스티커

규칙을 발견하면 어렵지 않은 문제 였는데, 이상한 부분에서 엄청 고생한 문제였다😅


 ### 설명
 - dp에 뗄 수 있는 스티커의 최대값을 갱신하며 저장한다.
⏺️⏺️⏺️☑️⏺️
⏺️⏺️⏺️⏺️⏺️
- 만약 위와 같은 스티거에서 검정색 부분을 뗄 때 의 최대값은
⏺️⏺️⏺️☑️⏺️      	
⏺️2️⃣1️⃣⏺️⏺️  
- 1을 뗄 때 최대값과(= dp[1️⃣]) 2를 뗄 때 최대값(= dp2️⃣[]) 중에 최대값이다.
	- 검정색을 뗀 다면 바로 왼쪽에 있는 것은 뗄 수 없으므로 고려하지 않아도 된다.
	- 왼쪽 아래 있는1️⃣을 뗄 수 있으므로 비교해줘야 한다.
	-  또한 1️⃣을 뗄 경우에 2️⃣를 떼지 못하기 때문에 2️⃣를 떼는 경우도 비교해줘야 한다.
- n의 개수가 1일 경우는 입력값 2개중 큰값을 출력
- dp초기값 세팅을 위에 2개 아래 2개 총 4개를 해주어서 인덱스오류를 방지했다.

```python
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  sticker = [list(map(int, input().split())) for _ in range(2)]
  if(n != 1):
	#dp초기값 세팅
    dp = [0] * 2
    dp[0] = [sticker[0][0]]  + [sticker[0][1]+sticker[1][0]] +[0]*(n-2)
    dp[1] = [sticker[1][0]]  + [sticker[0][0]+sticker[1][1]] +[0]*(n-2)
    for i in range(2, n):
      dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
      dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]
    print(max(dp[0][n-1], dp[1][n-1]))
  else:
    print(max(sticker[0][0], sticker[1][0]))
```           


## 9084 동전

### 설명
- dp배열에 금액을 만드는 방법의 수를 갱신하며 저장한다.
- 5와 7로 22를 만드는 예를 생각해보자
	- 17을 만들려면 17 - 5 = 12에 5를 더하면 만들 수 있으므로 dp[17]에 dp[12]의 값을 더해주면 된다.
- dp의 0번째 인덱스는 1, 나머지는 0으로 초기화
- 코인별로(5, 7) 돌아가며  금액을 만드는 방법의 수를 갱신해준다.

```python
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
  n = int(input())
  coins = list(map(int, input().split()))
  money = int(input())
  dp = [1] + [0 for i in range(money)]
  for coin in coins:
    for i in range(coin, money+1):
      dp[i] += dp[i-coin]
  print(dp[money])
```
