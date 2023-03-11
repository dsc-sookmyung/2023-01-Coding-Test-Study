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