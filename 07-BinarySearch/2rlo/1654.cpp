// BOJ 1654 랜선 자르기

#include <iostream>
#include <algorithm>
using namespace std;

int K, N, res;
int len[10001];
int maxL = 0;
long long mid, high, low;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> K >> N;
    for (int i = 0; i < K; i++)
    {
        cin >> len[i];
        if (maxL < len[i])
            maxL = len[i];
    }

    low = 1;
    high = maxL;
    res = 0;

    while (low <= high)
    {
        mid = (low + high) / 2;
        int cnt = 0;
        for (int i = 0; i < K; i++)
            cnt += len[i] / mid;

        if (cnt >= N)
        {
            low = mid + 1;
            if (res < mid)
                res = mid;
        }
        else
            high = mid - 1;
    }

    cout << res;
    return 0;
}