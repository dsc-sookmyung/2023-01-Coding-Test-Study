## 문제
### 11726 2xn 타일링
1) n의 범위가 1000까지이기에, 길이가 1001인 리스트 d를 만들어 초기화 시켜준다.
2) 점화식을 for문에 넣고 돌려주기 위해, d[1]과 d[2]의 값을 구해 넣어준다.
3) 직사각형 가로의 길이가 n일때의 경우의 수는 (n-1)의 경우의 수 + (n-2)의 경우의 수를 더한 값이다. 즉, d[n-1] + d[n-2] 이다. 
4) n이 3부터 일때는 반복문을 통해 값을 구해주고, 10007로 나눈 나머지를 d[i]에 저장해 d[N]을 구해준다.
```python
import sys
input = sys.stdin.readline

N = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 2

for i in range(3, N+1):
    d[i] = (d[i-1] + d[i-2]) % 10007
print(d[N])
```
### 11055 가장 큰 증가하는 부분 수열
1) for문을 통해 각 인덱스 위치에서 가장 큰 증가 부분 수열의 합을 구한다. 
2) i가 인덱스 0부터 N-1까지, j는 0부터 i-1까지 순회하며, 각 dp 테이블에는 가장 큰 증가하는 부분 수열의 합이 들어가게 된다.
3) for문을 통해 현재 인덱스 값이 이전 인덱스 값보다 크다면, dp[i]와 dp[j]+nums[i] 중 큰 값으로 업데이트 시켜준다. (현재 인덱스 위치 i에서 가장 큰 부분 수열의 합과 이전 인덱스 위치에서 가장 큰 부분 수열의 합 + 현재 인덱스의 수를 비교)
4) dp에 저장된 값 중 가장 합이 큰 것을 출력해준다.
```python
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [i for i in nums]

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])
print(max(dp))
```
### 9465 스티커
* 참고 : https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-9465-%EC%8A%A4%ED%8B%B0%EC%BB%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
1) 위 사이트를 참고하며 가능한 경우의 수를 통해 점화식을 세워주었다. 지그재그로 이동하는 경우와 한칸 건너뛰는 걍우가 있다.
=> 이때까지의 최댓값을 더한 숫자를 저장하고 있는 왼쪽 대각선의 숫자 또는 그 왼쪽 숫자를 더할 수 있기에 둘 중에 큰 값을 더해주면 된다.
2) 2부터 n-1까지 돌면서 해당 숫자를 기준으로 대각선 값을 비교하는데, 왼쪽 대각선의 숫자(한칸 전, n-1)와 그 왼쪽 숫자(두칸 전, n-2)를 비교하며 큰 값을 더한다.
3) dp에서 가장 마지막 인덱스인 n-1에 있는 값중 큰 값을 출력해준다.
```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
```
### 9084 동전
1) 사용가능한 동전들의 값을 입력받고, 크기가 M+1인 배열을 만들어준다.
2) dp에 0원부터 차례대로 그 금액을 만들 수 있는 가짓수를 구하고, 최종적으로 M원을 만들 수 있는 가짓수를 구해준다. 
3) 0원을 만드는 가짓수는 동전을 0개 사용하는 방법으로 1가지 존재하므로, dp[0] = 1로 만들어준다.
4) M원을 만들 수 있는 방법이 X개 있다면, X가지 방법에 V짜리 동전을 더해 M+V의 금액을 만들 수 있다. 
5) 점화식은 dp[i] = d[i] + d[i-k]로 금액 i를 k금액의 동전으로 만드는 경우이다.
6) ex. 1원, 2원으로 17원을 만드는 방법은 16원을 만드는 경우에 1원을 사용하는 경우 + 15원을 만드는 경우에 2원 동전을 사용하는 경우 2가지이다.
7) 금액 M을 만드는 방법인 dp[M]을 출력해준다.
```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0 for i in range(M+1)]
    dp[0] = 1

    for i in range(N):
        for j in range(coins[i], M+1):
            dp[j] += dp[j-coins[i]]
    print(dp[M])
```