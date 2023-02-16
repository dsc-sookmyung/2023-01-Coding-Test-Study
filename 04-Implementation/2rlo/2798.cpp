// BOJ 2798 블랙잭

#include <iostream>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, sum = 0, max = 0;
    int num[101];

    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        cin >> num[i];
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            for (int k = j + 1; k < N; k++)
            {
                sum = num[i] + num[j] + num[k];
                if (sum <= M)
                {
                    if (sum > max)
                        max = sum;
                }
            }
        }
    }

    cout << max << "\n";
    
    return 0;
}