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