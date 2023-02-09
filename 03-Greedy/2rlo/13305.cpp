// BOJ 13305 주유소

#include <iostream>
#include <climits>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    long long res = 0;
    int cost = INT_MAX;
    int len[100001], oil[100001];

    cin >> n;

    for (int i = 0; i < n - 1; i++)
    {
        cin >> len[i];
    }

    for (int i = 0; i < n; i++)
    {
        cin >> oil[i];
    }

    for(int i=0; i<n; i++){
        if(oil[i] < cost)
            cost = oil[i];
        res += (long long)cost * (long long)len[i];
    }

    cout << res << "\n";

    return 0;
}