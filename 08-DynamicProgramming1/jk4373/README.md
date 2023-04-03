## 동적계획법 (Dynamic Programming)

하나의 큰 문제를 여러 개의 작은 문제로 나누어 푸는 방법.
이 때 기존의 결과를 저장하여 재활용한다!
주로 반복되는 문제를 파악해 점화식을 설립해 문제를 쉽게 해결하고자 한다.

동적 계획법 조건

1. 겹치는 부분이 있다.
2. 최적 부분 구조

# 11055 2\*n 타일링

## 문제

2*n 크기의 직사각형이 주어졌을 때 1*2, 2\*1 타일로 채우는 방법의 수를 구하자

## 해설

현재 위치와 그 전까지의 사각형 위치의 결과를 이용해 한 칸씩 앞으로 나아가며 경우의 수를 구한다.

## 코드

```
import sys

N = int(sys.stdin.readline())
D =[0,1,2] #사각형 0번째는 0개, 1번째 2*1은 1개, 2번째 2*2는 2개 ...
for i in range(3,N+1):
     D.append(D[i - 2] + D[i - 1])
     D[i] = D[i] %10007

print(D[N])


```

# 11055 가장 큰 증가하는 부분 수열

## 문제

증가하는 부분 수열을 구할 때, 합이 가장 큰 수열을 구하시오.

## 풀이

그 위치에서 가장 합이 큰 부분 수열을 담는 배열 D
모든 부분 수열을 구하기 위해 반복문 2개를 돌며, for i in range(1,N) ...
for j in range(i)로 증가하는 부분 수열이 된다면, 합이 더 큰지, 그 위치의 값이 더 큰지 비교해 배열 D에 최댓값을 담아낸다. 증가하는 부분 수열이 아니라면 두 위치중 더 큰 값을 담아 그 위치까지의 부분수열의 최대값을 유지하도록 한다.
이렇게 배열 D를 규칙대로 채워나가면 배열 중 최대값이 가장 큰 증가하는 부분수열이 된다.

## 코드

```
import sys


N = int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))

D=[1]*N
D[0]=arr[0]
for i in range(1,N):
  for j in range(i):
    if arr[j]<arr[i]:
      D[i]=max(D[i], D[j]+arr[i])
    else:
      D[i]=max(D[i], arr[i])

print(max(D))
```

# 9465 스티커

## 문제

2\*n 배열의 스티커가 있다. 이 스티커는 하나 선택시 상하좌우의 스티커는 사용하지 못한다.
상냥이가 매긴 각각의 스티커 점수가 있을 때 스티커 점수가 최대가 되도록 스티커를 선택해보자.

## 해설

현재의 위치에서 최대 점수를 기록한다. 스티커는 지그재그 방향으로 움직이거나 한 줄 건너뛰고 다음 줄을 선택하는 방식, 두가지가 있다. 따라서 지그재그와 건너뛰기 중 더 점수가 최대가 되는 방향으로 각각 선택하며 최대 점수를 기록해 나간다.
(건너뛰는 방법이 생각이 안나서 검색해봤습니다...)

## 풀이

```
import sys

T = int(input())

for i in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    if N> 1:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
    for j in range(2,N):
        arr[0][j] += max(arr[1][j-1],arr[1][j-2])
        arr[1][j] += max(arr[0][j-1],arr[0][j-2])
    print(max(arr[0][N-1],arr[1][N-1]))

```

# 9084 동전

## 문제

동전의 종류와 금액이 주어질 때 금액을 만드는 모든 경우의 수를 구하시오

## 풀이

어떤 동전을 몇개 사용했는지가 아니라, 방법 경우의 수 그 자체를 구하는 문제이다.
따라서 현재 위치는 현재까지 동전을 만들 수 있는 경우의 수를 나타낸다.
배열 중 0 index는 항상 1가지 방법이라고 간주한다.(그래야 점화식을 세울 수 있다!!)
예시 -> 1원 2원으로 0원을 만드는 방법 1가지
1원을 만드는 방법 :1가지
2원을 만드는 방법 :2가지 [1,1],[2]
3원을 만드는 방법 :2가지 [2원을 만드는 방법,1]
4원을 만드는 방법 : [2원을 만드는 방법] + [3원을 만드는 방법] 4가지
5원을 만드는 방법 : [4원을 만드는 방법] + [3원을 만드는 방법]

## 코드

```
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    M = list(map(int,sys.stdin.readline().split()))
    money = int(sys.stdin.readline())

    dp = [0] * (money+1) # 0원 만드는 방법은 항상 1
    dp[0] =1
    for mm in M:
        for i in range(1,money+1):
            if i >= mm:
                dp[i] += dp[i -mm]
    print(dp[money])
```