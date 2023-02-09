// BOJ 20365 블로그2

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, red = 1, blue = 1;
    string color;
    bool red_flag = true, blue_flag = true;

    cin >> n >> color;

    for (int i = 0; i < n; i++)
    {
        if (color[i] == 'B')
        {
            if (red_flag)
                red++;
            red_flag = false;
            blue_flag = true;
        }
        else if (color[i] == 'R')
        {
            if (blue_flag) blue++;
            blue_flag = false;
            red_flag = true;
        }
    }

    cout << min(red, blue);

    return 0;
}