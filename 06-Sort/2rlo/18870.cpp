// BOJ 18870 좌표 압축

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    vector<int> v(N);

    for (int i = 0; i < N; i++)
    {
        cin >> v[i];
    }

    vector<int> vc(v);
    sort(vc.begin(), vc.end());
    vc.erase(unique(vc.begin(), vc.end()), vc.end());

    for (int i = 0; i < N; i++)
    {
        auto it = lower_bound(vc.begin(), vc.end(), v[i]);
        cout << it - vc.begin() << " ";
    }

    return 0;
}