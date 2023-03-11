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