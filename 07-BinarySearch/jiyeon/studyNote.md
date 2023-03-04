# 07-이분탐색

 - 정리한 문제
 1. 1789 수들의 합
 2. 2512 예산
 3. 1654 랜선 자르기
 4. 22871 징검다리 건너기
 <br>

 ## 1789 수들의 합
분명 이분탐색 추천문제에서 가져왔는데 아마 잘못 써져있던거 같네요🙇‍♀️ 그리디 문제인거 같습니다.

 ### 설명
 - 서로 다른 N개의 합이 S이다. 이때, N의 최대값을 구하는 문제이다. (N, S는 자연수)
 - 합을 이루는 자연수의 개수가 최대가 되어야 함으로 1, 2, 3, ... 작은 수부터 더해준다.
 - S에서 1,2,3 ... 을 차례로 빼준다.
-  1️⃣현재 빼줘야 하는 숫자(i)보다 S가 큰 경우 => S에서 빼고, i+1 하고 다음 턴
- 2️⃣현재 빼줘야 하는 숫자(i)와 S가 같은 경우 => S에서 해당 숫자를 빼주면 0, 즉 합이 다 구해진 것이다. i가 마지막 숫자이자 서로 다른 N개 자연수의 개수가 된다.
- 3️⃣현재 빼줘야 하는 숫자(i)보다 S가 작은 경우 => S가 더 작기 때문에 더 이상 빼줄 수 없다. 이 경우에는 그냥 현재 합을 이루는 자연수 중 제일 큰 수에다가 i값을 더해주면 되기 때문에 i-1이 답이 된다.

```python
import sys
input = sys.stdin.readline

s = int(input())
i = 1

while(True):
  if(s > i):
    s -= i
    i += 1
  elif(s == i):
    print(i)
    break
  else:
    print(i-1)
    break
```

 ## 2512 예산

 이 문제는 이분 탐색 없이도 시간 제한 안에 풀 수 있어서 해당 풀이로 풀었다.

 ### 설명
 -  요청액의 총 합이 총 예산보다 적다면 모든 요청을 배정해 줄 수 있으므로 요청액의 최대값이 상한액이 된다.
 - 문제는 예산이 부족해 요청대로 배정해 줄 수 없는 경우이다.
 - 우선 각 지방마다 n빵한 예산을 준다고 치고, 만약 n빵한 예산보다 요청액이 적어서 차액이 남으면 remain에 저장해두고 뒤 쪽 지방에서 모자랄때 remain에서 가져오면 되지 않을까? 하는 생각으로 풀어보았다.
 - 상한액(budget)을 총 [예산//지방의 수]로 n빵해서 선언해주고, 임시로 나눠주고 남은 예산을 remain에 선언해주었다.
 - 요청액을 담을 배열은 오름차순 정렬해준다. 요청액 배열을 돌아주면서
 -  요청액이 상한액보다 **작거나 같다면**
	 - 요청액으로 배정해 줄 수 있는 경우이다. 차액(상한액 - 요청액)을 remain에 더해준다.
- **else** : 요청액이 상한액보다 **크다면**
	- 상한액으로 배정해 줄 수 없는 경우이다. 우리한테는 remain값이 있으므로 remain값을 공평히 나눈 값을 더한 임시 상한액을 만들어 준다.
	-  요청액이 해당 임시 상한액보다 **작거나 같다면**
		- 임시 상한액으로 요청액을 배정해 줄 수 있으므로 배정해준다.
		-  remain에서 배정해주기 위해 상한액보다 더 쓴 값(요청액 - 상한액)을 빼준다.
	- **else** : 요청액이 해당 임시 상한액보다 **크다면**
		- 요청액이 남은 remain을 다 털어서 만든 임시 상한액보다 크다는 것은 그냥 임시 상한액을 배상해줘야 한다는 뜻이다.
		- 요청액은 오름차순으로 들어옴으로 앞으로 들어오는 요청액도 모두 임시 상한액으로 배상해줘야 하는 것은 똑같으므로 break를 걸고 임시상한액을 출력해준다.
```python
import sys
input = sys.stdin.readline
n = int(input())
req = list(map(int,input().split()))
m = int(input())

req.sort()
budget = m//n
remain = m%n

if(sum(req) <= m):
  print(req[-1])
else:
  for idx, reqBudget in enumerate(req):
    if(reqBudget <= budget):
      remain += budget - reqBudget
    else:
      #기존 예산(budget) + 앞에서 쓰고 남은 예산(remain)을 공평히 나눈 값
      ebudget = budget + remain//(n-idx)
      if(reqBudget <= ebudget):
        remain -= reqBudget - budget
      else:
        break
  print(ebudget)     
```

## 1654 랜선 자르기

 ### 설명
-  랜선 여러개가 주어졌을 때 그 랜선들을 잘라 n개의 같은 길이의 랜선을 만들 경우 제일 최대 랜선의 길이는 무엇인지 구하는 문제이다.
-  문제에서 주어진 예로 설명해보자면 랜선길이는 각각 802, 743, 457, 539이다.
 - 11개의 랜선을 만들고 싶다고 할 때, 랜선을 만드는 **길이의 범위**를 생각해보았다.
 - 최소 1로 만들 수 있고 최대일 경우는 제일 큰 막대기로 하나의 랜선을 만드는 경우인 802이다.
 - 1에서 802까지 수를 하나하나 검사해서 랜선을 11개를 만들 수 있으면서 가장 최대인 수를 구해야 한다.
 - 제한 시간이 2초이므로 숫자 1부터 시작해서 랜선의 최대 길이 (2^31-1)= (2,147,483,647)까지를 다 볼 수는 없다. 따라서 이분탐색으로 O(logN)의 시간복잡도로 풀어야 한다.


### 코드 설명
countHowManyLanMadedBy(lanLine) : lanLine(=랜선 길이)로 만들 수 있는 랜선의 개수를 세는 함수이다.
<br>
```python
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
length = [int(input()) for _ in range(k)]
length.sort()

left = 1
right = length[-1]

def countHowManyLanMadedBy(lanLine):
  count = 0
  for i in length:
    count += i//lanLine
  return count

while(left <= right):
  mid = (left + right)//2
  if(countHowManyLanMadedBy(mid)>=n):
    left = mid + 1
  else:
    right = mid - 1

print(right)          
```           


## 22871 징검다리 건너기

이분탐색으로도 유형이 나와있지만 dp풀이밖에 안 떠올라서 dp로 풀었다.

### 어려웠던 점

 - 문제의 3번에 나와있는 ***돌을 한번 건너갈 때마다 쓸 수 있는 힘은 최대  K이다*** 라는 말이 이해가 안가서 한참 고민한 문제였다.
 - 만약에 2번 돌을 지나 3번 돌로 가는 최소힘을 구하려고 할 때, 2번 돌로 가는 최소힘이 **2**(dp에 미리 구해놓은 값)라고 하고, 2번 돌에서 3번 돌으로 가는 힘이 **5**라고 할 때, **2<5**이므로 쓰는 힘은 5이다. 라는 맥락으로 이해하고 풀긴 했는데 사실 아직 ***저 조건*** 이 무슨 의미인지는 잘 모르겠다😅 혹시 저 조건이 왜 나온지 추측하신 분은 리뷰남겨주세요🙌

### 설명
- dq[i]에는 i번째 돌까지 오는 모든 경우 중 최소힘을 저장한다.
- dp[i]를 구하는법
	- i번째 이전에 있는 돌들을 j라고 할 때,  j를 거쳐서 i에 오는 힘은 **0->j까지 최소힘**과  **j->i까지 가는 힘**, 둘 중 최대값이다.
	- 이 때 j = 0 ~ (i - 1) 만큼 for을 돌아주면서 j를 거쳐서 i에 오는 힘의 최소값이 dp[i]에 저장되면 된다.
- dp의 마지막 값이 마지막 돌까지가는 모든 경우 중 최소힘이므로 dp[-1]을 출력


```python
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

dp = [0] + [5000000000 for i in range(n-1)]
for j in range(n):
  for i in range(j):
    power = max(dp[i], (j-i)*(1+abs(A[i]-A[j])))
    dp[j] = min(dp[j], power)

print(dp[-1])
```
