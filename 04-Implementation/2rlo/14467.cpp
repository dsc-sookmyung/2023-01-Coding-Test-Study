// BOJ 14467 소가 길을 건너간 이유 1

#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, num, loc, res = 0;
    int cow[11];

    memset(cow, -1, 11*sizeof(int));

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> num >> loc;
        if (cow[num] != -1){
            if(cow[num] ^ loc) res++;
        }
        cow[num] = loc;
    }

    cout << res << "\n";

    return 0;
}