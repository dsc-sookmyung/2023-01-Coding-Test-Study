## 문제
### 1149 RGB거리
1) colors[i][0], colors[i][1], colors[i][2]는 i번째 집을 빨강, 초록, 파랑으로 칠했을 때의 최솟값이다.
2) i번째 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
3) 세 값 중 가장 작은 값을 출력
```python
import sys
input = sys.stdin.readline

N = int(input())
colors = []

for _ in range(N):
    colors.append(list(map(int, input().split())))

for i in range(1, N):
    colors[i][0] = min(colors[i-1][1], colors[i-1][2]) + colors[i][0]
    colors[i][1] = min(colors[i-1][0], colors[i-1][2]) + colors[i][1]
    colors[i][2] = min(colors[i-1][0], colors[i-1][1]) + colors[i][2]
print(min(colors[N-1][0], colors[N-1][1], colors[N-1][2]))
```
### 2156 포도주 시식
1) d[i]는 i번째 포도주까지 최대로 마신 포도주의 양이다.
2) 현재 i번째 포도주를 마시지 않는 경우, 현재 i번째 포도주를 마시고 i-2번째 포도주까지 마시는 경우, i,i-1번째를 포도주를 마시고 i-3번째까지 마시는 경우 세가지가 존재한다.
3) 1, 2까지는 최댓값이 연속으로 마신 경우이므로 따로 분류해 값을 넣어준다.
```python
import sys
input = sys.stdin.readline

n = int(input())
amount = []
for _ in range(n):
    amount.append(int(input()))

d = [0] * (n+1)
d[1] = amount[0]
if n >= 2:
    d[2] = amount[0] + amount[1]
    for i in range(3, n+1):
        d[i] = max(d[i-2] + amount[i-1], d[i-3] + amount[i-2] + amount[i-1], d[i-1])
print(d[n])
```
### 1463 1로 만들기
1) 숫자가 2와 3으로 나누어 떨어지는 경우는 1을 빼는 것보다 훨씬 횟수를 줄일 수 있다.
2) 나누어 떨어진다면, d[i]와 d[i//2] + 1(d[i // 3] + 1) 중 더 작은 값을 선택해준다.
```python
import sys
input = sys.stdin.readline

N = int(input())
d = [0] * (N + 1)

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
print(d[N])
```
### 12865 평범한 배낭
어떻게 풀지 모르겠어서 구글링했다..
1) 무게와 가치를 stuff 배열에 저장한다
2) 무게가 현재 인덱스의 무게보다 크다면 물건을 담을 수 없기에 이전 인덱스의 값을 가져온다.
3) 무게가 현재 인덱스의 무게보다 작다면 물건을 담을 수 있기에 value + knapsack[i - 1][j - weight]과  knapsack[i - 1][j]를 비교해 더 큰 값을 넣어준다.
4) knapsack[N][K]의 값을 출력해준다.
```python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])
```