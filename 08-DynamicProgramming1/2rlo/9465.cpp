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