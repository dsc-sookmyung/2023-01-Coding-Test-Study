# DynamicProgramming1 
## 11726 2xn타일링 
n이 1000까지이므로 총 1001개의 dp 리스트를 만들어서 구한다. 

```python
n = int(input())  
dp = [0] * 1001  
  
dp[1] = 1  
dp[2] = 2  
  
for i in range(3, 1001):  
    dp[i] = (dp[i-1] + dp[i-2]) % 10007  
  
print(dp[n])
```

**[풀이]**
1) n이 1000까지이므로 총 길이가 1001인 dp리스트를 만들고 0으로 초기화한다 
2) dp리스트에서 각 인덱스 번호가 n일 때라고 생각하여 n이 1일 때는 총 1가지이므로 dp[1]을 1로 n이 2일 때는 총 2가지이므로 dp[2]를 2로 초기화한다 
3) 그 다음 n이 3일 때부터 dp값은 해당 인덱스 바로 전 인덱스 두 개의 값을 더한 값이 총 가짓수이므로 dp[i-1] + dp[i-2] 이다 
4) 따라서 n이 3일 때부터는 반복문을 이용해서 값을 저장하고 문제에서 10007로 나눈 나머지를 요구했으므로 10007로 나눈 나머지로 값을 갱신해 나간다 
5) n일 때를 구해야하므로 dp[n]을 출력한다 

<br/>

## 11055 가장 큰 증가하는 부분 수열  
A리스트가 만들어지면 인덱스를 하나씩 증가시키면서 최댓값을 찾아야하므로 dp를 사용한다. 

```python
import sys

read = sys.stdin.readline

n = int(read())
alist = list(map(int, read().split()))
dp = [0] * n
dp[0] = alist[0]

for i in range(1, n):
    for j in range(i):
        if alist[j] < alist[i]:
            dp[i] = max(dp[j] + alist[i], dp[i])
        else:
            dp[i] = max(alist[i], dp[i])

print(max(dp))
```

**[풀이]**
1) 길이가 n인 dp리스트를 생성한 다음 0으로 초기화한다 
2) dp의 0번째 원소는 수열에서 0번째 값이랑 같으므로 수열의 0번째 값을 넣어준다 
3) dp리스트에서 1번째부터 n-1번째까지 돌면서 dp리스트를 채운다 
4) 이때 dp[i]를 구하기 위해서 i보다 작은 인덱스를 모두 돌면서 수열에서 본인보다 작은 값이라면 dp[j]와 본인의 값을 더한 값을 구해서 가장 큰 값을 dp[i]에 저장한다 
5) 수열에서 본인보다 작은 값이 아니라면 해당 값과 dp의 값을 비교해서 더 큰 값으로 저장한다 
6) 최댓값을 구해야 하므로 dp의 최댓값을 출력한다 

<br/>

##  9465 스티커 
스티커와 똑같은 이중 리스트를 만든 후 해당 인덱스에서 최댓값이 그 전 인덱스들 중 어떤 것과 본인을 더해야 하는지 찾는다. 그리고 n이 1일때를 고려해줘야 한다!! 런타임 에러가 많이 발생해서 구글링을 해보았는데 n이 1일 때를 고려하지 않아서 생긴 문제였다😭 

```python
import sys

read = sys.stdin.readline
t = int(read())

for _ in range(t):
    n = int(read())
    sticker1 = list(map(int, read().split()))
    sticker2 = list(map(int, read().split()))
    sticker = [sticker1, sticker2]

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
    else:
        dp = sticker
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    
        for i in range(2, n):
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    
        print(max(dp[0][n - 1], dp[1][n - 1]))
```

**[풀이]**
1) 2 * n개의 스티커 점수 리스트를 입력 받고 sticker이중 리스트에 저장한다 
2) n이 1이라면 (0,0)에 위치한 값과 (1,0)에 위치한 값을 비교해서 더 큰 값을 출력 
3) n이 1이 아니라면 dp리스트를 sticker와 똑같이 만들고 (0,1)에 위치한 값을 왼쪽 아래 (1,0)을 더한 값으로 (1,1)에 위치한 값을 왼쪽 위(0,0)을 더한 값으로 바꿔준다 
4) 그리고 2부터 n-1까지 돌면서 본인 기준으로 위쪽이나 아래쪽 대각선값을 비교하는데 이때 한 칸 전과 두 칸 전을 모두 비교해서 더 큰 값을 더해준다 
5) dp리스트에서 가장 마지막에 위치한 값들을 비교해서 더 큰 값을 출력한다 

<br/>

## 9084 동전 
점화식을 어떻게 세워야 할 지 생각이 떠오르지 않아 구글링을 통해 풀었다. 

```python
import sys  
  
read = sys.stdin.readline  
  
t = int(read())  
for _ in range(t):  
    n = int(read())  
    coin = list(map(int, read().split()))  
    m = int(read())  
  
    dp = [[0] * (m+1) for _ in range(n)]  
    for i in range(n):  
        dp[i][0] = 1  
  
  for i in range(n):  
        for j in range(1, m+1):  
            if i != 0:  
                dp[i][j] = dp[i-1][j]  
            if j - coin[i] >= 0:  
                dp[i][j] += dp[i][j - coin[i]]  
  
    print(dp[n-1][m])
```

**[풀이]**
1) dp리스트를 이중 리스트로 만든다. 이때 열은 동전을 사용해서 만든 총 금액을 의미하고 0원부터 m원까지로 설정한다. 그리고 행은 동전의 개수만큼 설정한다.
2) 모든 행의 0번째는 총 0원을 만드는 가짓수이므로 동전을 0개 사용하는 방법 1가지밖에 없으므로 모든 행의 0번째 값을 1로 만든다
3) dp리스트의 n번째 행은 coin리스트의 n번째 동전으로 j(1부터 m까지)원을 만들 수 있는 가짓수를 저장한다
4) 따라서 n만큼 반복문을 돌면서 동전이 작은 순서대로 j원을 만들 수 있는 가짓수를 채운다
5) 동전의 금액이 증가하면서 그 전 동전으로 j원을 만들 수 있는 가짓수를 불러와서 초기화를 한다
6) 그리고 j원에서 해당 동전의 금액만큼을 빼고 0보다 크거나 같을 경우에 해당 동전으로 그만큼의 금액을 만들 수 있는 가짓수를 불러와서 더한다 
7) dp리스트가 다 만들어지면 가장 마지막 줄의 m번째 값을 출력한다  
