# 동적계획법(DP)
> 하나의 큰 문제를 여러 개의 작은 문제로 나누어서 그 결과를 저장하여 다시 큰 문제를 해결할 때 사용하는 것   
> 알고리즘이 아닌 문제해결 패러다임으로 볼 수 있음음

</br>

## 사용 이유
- 일반적인 재귀 방식 또한 DP와 유사하나, 일반적인 재귀를 단순히 사용할 시 동일한 작은 문제들이 여러 번 반복되어 비효율적인 계산이 될 수 있음
- 즉, DP를 사용하면 효율적으로 문제 해결 가능

</br>

## 사용 조건
1. Overlapping Subproblems (겹치는 부분 문제)
   - 동일한 작은 문제들이 반복하여 나타나는 경우에 사용 가능
2. Optimal Substructure (최적 부분 구조)
   - 부분 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있는 경우

</br>

## DP 사용 절차
1. DP 사용 가능 문제인지 확인
   - 위의 사용 조건이 충족되는 문제인지 체크
   - 보통 특정 데이터 내 최대화/최소화 계산, 특정 조건 내 데이터 세기, 확률 등의 계산
2. 문제의 변수 파악
   - 문제 내 변수의 개수를 알아내야 함
3. 변수 간 관계식 만들기 (점화식)
   - 점화식을 통해 짧은 코드 내에서 반복/재귀를 통해 문제가 자동으로 해결되도록 구축
4. 메모 (memoization or tabulation)
   - 변수의 값에 따른 결과 저장
5. 기저 상태 파악
   - 가장 작은 문제의 상태를 알아야 함
6. 구현
   - Bottom-Up (Tabulation 방식): 반복문 사용
   - Top-Down (Memoization 방식): 재귀 사용

</br>

## 구현 방식
1. Bottom-Up 방식
   - 아래에서부터 계산을 수행하고 누적시켜서 전체 큰 문제를 해결
   - dp[0]부터 시작하여 반복문을 통해 점화식으로 결과를 내 dp[n]까지 그 값을 전이시켜 재활용하는 방식
2. Top-Down 방식
   - dp[0]의 기저 상태에서 출발하는 대신 dp[n]의 값을 찾기 위해 위에서부터 바로 호출을 시작하여 dp[0]의 상태까지 내려간 다음 해당 결과 값을 재귀를 통해 전이시켜 재활용하는 방식
---

</br>

# BOJ 11726 2xn 타일링
## 문제 요약
1. 입력: n
2. 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하기
3. 출력: 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지

</br>

## 풀이과정
1. 점화식: dp[n] = dp[n-1] + dp[n-2]
2. dp[1] = 1, dp[2] = 2

</br>

## 코드
```cpp
// BOJ 11726 2xn 타일링

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    vector<int> dp;

    cin >> n;
    dp.push_back(1);
    dp.push_back(2);

    for(int i=2; i<n; i++){
        dp.push_back((dp[i-1]+dp[i-2]) % 10007);
    }

    cout << dp[n-1];
    
    return 0;
}
```

</br>

---

</br>

# BOJ 11055 가장 큰 증가하는 부분 수열
## 문제 요약
1. 입력: 수열 A의 크기 N, 수열 A를 이루고 있는 $A_j$
2. 출력: 수열 A의 합이 가장 큰 증가하는 부분 수열의 합
</br>

## 풀이과정
1. dp[i] = A[i]를 증가하는 부분 수열의 마지막 요소라고 할 때의 부분 수열의 합
2. 현재 A[i]보다 작은 값 중에서 dp가 dp[i]보다 큰 값을 dp[i]로
3. dp[i]에 현재 위치 값(A[i])를 더해줌
4. res는 기존 res와 dp[i] 중 최댓값

</br>

## 코드
```cpp
// BOJ 11055 가장 큰 증가하는 부분 수열

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, A[1001], dp[1001] = {0,}, res = 0;

    cin >> N;

    for (int i = 1; i <= N; i++)
    {
        cin >> A[i];
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j < i; j++)
        {
            if (A[j] < A[i])
                dp[i] = max(dp[i], dp[j]);
        }
        dp[i] += A[i];
        res = max(dp[i], res);
    }

    cout << res;

    return 0;
}
```

</br>

# BOJ 9465 스티커
## 문제 요약
1. 입력: 테스트 케이스의 개수 T, n, n개의 정수
2. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용 할 수 없게 됨
3. 출력: 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값
</br>

## 풀이과정
1. dp[0][i] = 윗줄 i번째 스티커를 택했을 때의 최댓값, dp[1][i] = 아랫줄 i번째 스티커를 택했을 때의 최댓값 
2. 점화식
   - dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + dp[0][i]
   - dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + dp[1][i]

</br>

## 코드
```cpp
// BOJ 9465 스티커

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    while (T--)
    {
        int n;
        cin >> n;
        int dp[2][100001] = {0, };
        dp[0][0] = dp[1][0] = 0;
        for (int i = 1; i <= n; i++)
        {
            cin >> dp[0][i];
        }
        for (int i = 1; i <= n; i++)
        {
            cin >> dp[1][i];
        }

        for (int i = 2; i <= n; i++)
        {
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + dp[0][i];
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + dp[1][i];
        }

        int res = max(dp[1][n], dp[0][n]);

        cout << res << "\n";
    }

    return 0;
}
```
---

</br>

# BOJ 9084 동전
## 문제 요약
1. 입력: 테스트 케이스의 개수 T, 동전의 가지 수 N, N가지 동전의 각 금액이 오름차순으로, 주어진 N가지 동전으로 만들어야 할 금액 M
2. 출력: N가지 동전으로 금액 M을 만드는 모든 방법의 수를 한 줄에 하나씩

</br>

## 풀이과정
1. dp[i] = i원을 만들 수 있는 방법의 수
2. 점화식: dp[i] = dp[j] + dp[j-coin[i]]

</br>

## 코드 
```cpp
// BOJ 9084 동전

#include <iostream>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    while (T--)
    {
        int N, M, dp[10001] = {
                      0,
                  },
                  coin[21];
        cin >> N;

        for (int i = 1; i <= N; i++)
        {
            cin >> coin[i];
        }
        cin >> M;

        dp[0] = 1;
        for (int i = 1; i <= N; i++)
        {
            for (int j = coin[i]; j <= M; j++)
            {
                dp[j] = dp[j] + dp[j - coin[i]];
            }
        }

        cout << dp[M] << "\n";
    }

    return 0;
}
```
---

</br>

