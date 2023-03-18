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