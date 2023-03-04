// BOJ 22871 징검다리 건너기 (large)

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int N;
long long arr[5001], dp[5001];

long long solve(int x)
{
    if (x == N - 1)
        return 0;
    long long &ans = dp[x];
    if (ans != -1)
        return ans;

    ans = 1e10;
    for (int i = x + 1; i < N; i++)
    {
        ans = min(ans, max(solve(i), (i - x) * (1 + abs(arr[x] - arr[i]))));
    }
    return ans;
}
int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    memset(dp, -1, sizeof(dp));

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    cout << solve(0) << endl;

    return 0;
}