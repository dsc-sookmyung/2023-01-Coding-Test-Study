// BOJ 6550 부분 문자열

#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s, t;

    while (cin >> s >> t)
    {
        bool res = false;
        int idx = 0;

        for (int i = 0; i < t.size(); i++)
        {
            if (s[idx] == t[i])
                idx++;
            if (idx == s.length())
            {
                res = true;
                break;
            }
        }

        if (res)
            cout << "Yes\n";
        else
            cout << "No\n";
    }

    return 0;
}