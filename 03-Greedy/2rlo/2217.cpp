// BOJ 2217 로프

#include <iostream>
#include <queue>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, res = 0;
    priority_queue<int> rope;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        rope.push(temp);
    }

    for (int i = 0; i < n; i++)
    {
        int sum = rope.top() * (i + 1);
        rope.pop();
        if (sum > res)
            res = sum;
    }

    cout << res << "\n";

    return 0;
}