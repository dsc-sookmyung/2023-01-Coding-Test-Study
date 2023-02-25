// BOJ 11652 카드

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, max = 1, cnt = 1;
    long long res;
    long long arr[100001];

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr + N);

    res = arr[0];
    for (int i = 1; i < N; i++)
    {
        if (arr[i] == arr[i - 1])
            cnt++;
        else
            cnt = 1;

        if (max < cnt)
        {
            max = cnt;
            res = arr[i];
        }
    }

    cout << res << "\n";

    return 0;
}