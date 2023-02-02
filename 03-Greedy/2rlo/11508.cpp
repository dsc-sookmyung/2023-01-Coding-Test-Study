// BOJ 11508 2+1 세일

#include <iostream>
#include <queue>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, res = 0;
    priority_queue<int> product;

    cin >> n;

    for(int i=0; i<n; i++)
    {
        int temp;
        cin >> temp;
        product.push(temp);
    }

    for (int i=1; i<=n; i++)
    {
        if (i%3)
            res += product.top();
        product.pop();
    }

    cout << res << "\n";
    
    return 0;
}