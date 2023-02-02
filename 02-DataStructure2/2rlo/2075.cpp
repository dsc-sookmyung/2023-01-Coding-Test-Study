// BOJ 2075 N번째 큰수

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    priority_queue<int, vector<int>, greater<int>> q;

    cin >> n;

    for (int i = 0; i < n * n; i++)
    {
        int temp;
        cin >> temp;
        q.push(temp);
        if (q.size() > n)
            q.pop();
    }

    cout << q.top() << "\n";

    return 0;
}