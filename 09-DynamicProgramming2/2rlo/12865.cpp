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