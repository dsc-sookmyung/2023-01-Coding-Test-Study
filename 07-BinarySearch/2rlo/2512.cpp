// BOJ 2512 예산

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int bs(vector<int> arr, int n, int m, int max)
{
    int low = 0, high = max;
    int sum, res;

    while (low <= high)
    {
        sum=0;
        int mid = (low + high) / 2;
        for (int i = 0; i < n; i++)
        {
            sum += min(arr[i], mid);
        }
        if (m >= sum)
        {
            res = mid;
            low = mid + 1;
        }
        else
            high = mid - 1;
    }

    return res;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    vector<int> request;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        request.push_back(temp);
    }
    cin >> M;

    sort(request.begin(), request.end());
    cout << bs(request, N, M, request[N-1]);
    return 0;
}