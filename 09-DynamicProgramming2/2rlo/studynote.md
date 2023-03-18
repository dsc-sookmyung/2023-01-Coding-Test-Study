# BOJ 1149 RGB거리
## 문제 요약
1. 입력: 집의 수 N, 각 집을 빨강, 초록, 파랑으로 칠하는 비용
2. 규칙
   - 1번 집의 색은 2번 집의 색과 같지 않아야 한다   
   - N번 집의 색은 N-1번 집의 색과 같지 않아야 한다   
   - i(2 <= i <= N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다   
3. 출력: 모든 집을 칠하는 비용의 최솟값

</br>

## 풀이과정
1. dp[i][0]은 i번째 집을 빨강색으로 칠할 때의 최소 비용, dp[i][1]은 i번째 집을 초록색으로 칠할 때의 최소비용, dp[i][2]는 i번째 집을 파란색으로 칠할 때의 최소비용
2. dp[i]가 빨강색으로 칠해지려면?   
   - i-1번이 초록색이거나 파란색이여야 함
3. 다른 색깔도 동일
4. dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
   
</br>

## 코드
```cpp
// BOJ 1147 RGB거리

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, dp[1001][3], cost[3];

    cin >> N;
    dp[0][0] = dp[0][1] = dp[0][2] = 0;

    for(int i=1; i<=N; i++){
        cin >> cost[0] >> cost[1] >> cost[2];
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[0];
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[1];
        dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + cost[2];
    }

    cout << min(dp[N][2],min(dp[N][0], dp[N][1]));
    
    return 0;
}
```

</br>

---

</br>

# BOJ 2156 포도주 시식
## 문제 요약
1. 입력: 포도주 잔의 개수 n, 포도주 잔에 들어있는 포도주의 양
2. 포도주 시식 규칙
   - 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야하고, 마신 후에는 원래 위치에 다시 놓아야한다   
   - 연속으로 놓여있는 3잔을 모두 마실 수는 없다   
3. 출력: 최대로 마실 수 있는 포도주의 양
   
</br>

## 풀이과정
1. dp[i]를 i번째 잔까지 포도주의 최대 양으로 정의
2. dp[1] = 1번째 잔    
   dp[2] = 1번째 잔 + 2번째 잔   
   dp[3] = 1, 2번째 잔 or 1,3번째 잔 or 2,3번쩨 잔   
3. dp[i] = dp[i-3] + i-1번째 잔 + i번째 잔 or   
   dp[i-2] + i번째 잔 or dp[i-1]

</br>

## 코드
```cpp
// BOJ 2156 포도주 시식

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, dp[10001], wine[10001];

    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> wine[i];

    dp[0] = wine[0] = 0;
    dp[1] = wine[1];
    dp[2] = wine[1] + wine[2];

    for (int i = 3; i <= N; i++)
    {
        dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], max(dp[i - 2] + wine[i], dp[i - 1]));
    }

    cout << dp[N] << endl;

    return 0;
}
```

</br>

# BOJ 1463 1로 만들기
## 문제 요약
1. 입력: 1보다 크거나 같고, $10^6$보다 작거나 같은 정수 N
2. 연산
   - 정수 X가 3으로 나누어 떨어지면, 3으로 나눈다   
   - 정수 X가 2로 나누어 떨어지면, 2로 나눈다   
   - 1을 뺀다
3. 출력: 연산 횟수의 최솟값
</br>

## 풀이과정
1. dp[N] = 숫자 N을 1로 만드는 최솟값
2. dp[1] = 0   
   dp[2] = 1   
   dp[3] = 1
3. dp[i] = 3으로 나눠지면 min(dp[i-1]+1, dp[i/3]+1)   
   2로 나눠지면 min(dp[i-1]+1, dp[i/2]+1)      

</br>

## 코드
```cpp
// BOJ 1463 1로 만들기

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, dp[1000001]={0,};
    cin >> N;

    dp[2] = dp[3] = 1;

    for (int i = 4; i <= N; i++)
    {
        dp[i] = dp[i - 1] + 1;
        if (i % 2 == 0)
            dp[i] = min(dp[i], dp[i / 2] + 1);
        if (i % 3 == 0)
            dp[i] = min(dp[i], dp[i / 3] + 1);
    }

    cout << dp[N] << endl;

    return 0;
}
```
---

</br>

# BOJ 12865 평범한 배낭
## 문제 요약
1. 입력: 물품의 수 N, 버틸 수 있는 무게 K, 각 물건의 무게 W, 해당 물건의 가치 V
2. 출력: 배낭에 넣을 수 있는 물건들의 가치합의 최댓값

</br>

## 풀이과정
1. dp[i][j] = 무게 j까지 담을 수 있는 배낭에 i번째까지 물품을 사용하여 배낭에 담을 수 있는 최대 가치
2. knapsack 알고리즘 사용
3. dp[i][j] = max(v[i] + dp[i-1][j-w[i]], dp[i][j])

</br>

## 코드 
```cpp
// BOJ 12865 평범한 배낭

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K, W[101], V[101], dp[101][100001];
    cin >> N >> K;

    for (int i = 1; i <= N; i++)
    {
        cin >> W[i] >> V[i];
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= K; j++)
        {
            dp[i][j] = dp[i - 1][j];
            if (W[i] <= j)
                dp[i][j] = max(V[i] + dp[i - 1][j - W[i]], dp[i][j]);
        }
    }

    cout << dp[N][K] << endl;

    return 0;
}
```
---

</br>

