// BOJ 2578 빙고

#include <iostream>
using namespace std;

int num[6][6];

bool check()
{
    int bingo = 0, crossR = 0, crossL = 0;
    for (int i = 1; i <= 5; i++)
    {
        int col = 0, row = 0;
        for (int j = 1; j <= 5; j++)
        {
            if (num[i][j] == 0)
                row++;
            if (num[j][i] == 0)
                col++;
        }
        if (row == 5)
            bingo++;
        if (col == 5)
            bingo++;
        if (num[i][i] == 0)
            crossR++;
        if (num[i][6 - i] == 0)
            crossL++;
    }

    if (crossR == 5)
        bingo++;
    if (crossL == 5)
        bingo++;
    if (bingo >= 3)
        return true;
    return false;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int call, res = 0;

    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            cin >> num[i][j];
        }
    }

    for (int i = 1; i <= 25; i++)
    {
        res++;
        cin >> call;
        for (int j = 1; j <= 5; j++)
        {
            for (int k = 1; k <= 5; k++)
            {
                if (num[j][k] == call)
                {
                    num[j][k] = 0;
                    if (check())
                    {
                        cout << res << "\n";
                        return 0;
                    }
                }
            }
        }
    }

    return 0;
}