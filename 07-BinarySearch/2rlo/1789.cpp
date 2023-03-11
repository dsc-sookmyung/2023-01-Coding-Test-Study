// 1789 수들의 합

#include <iostream>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long S, sum;
    int num = 1, res = 0;

    cin >> S;

    while (true) {
        sum += num;
        res++;
        if ( sum > S ){
            res--;
            break;
        }
        num++;
    }

    cout << res ;

    return 0;
}