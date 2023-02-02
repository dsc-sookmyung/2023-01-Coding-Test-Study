// BOJ 14916 거스름돈

#include <iostream>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, res = 0;

    cin >> n; 

    if (n==1 || n ==3)
    {
        cout << -1 <<"\n";
        return 0;
    }

    if(n % 5 % 2)
    {
        cout << n/5-1 + (n%5+5) / 2;
    }
    else
    {
        cout << n/5+n%5/2;
    }
    
    return 0;
}