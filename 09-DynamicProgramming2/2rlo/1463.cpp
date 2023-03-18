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