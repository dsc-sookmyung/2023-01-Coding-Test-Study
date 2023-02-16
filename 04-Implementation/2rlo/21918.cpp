// BOJ 21918 전구

#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    int s[4001] = {
        0,
    };

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
    {
        cin >> s[i];
    }

    for (int i = 0; i < M; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;

        if (a == 1)
        {
            s[b] = c;
        }
        else if (a == 2)
        {
            for (int i = b; i <= c; i++)
            {
                s[i] = !s[i];
            }
        }
        else if (a == 3)
        {
            for (int i = b; i <= c; i++)
            {
                s[i] = 0;
            }
        }
        else
        {
            for (int i = b; i <= c; i++)
            {
                s[i] = 1;
            }
        }
    }

    for (int i = 1; i <= N; i++)
        cout << s[i] << ' ';

    return 0;
}