// BOJ 1620 나는야 포켓몬 마스터 이다솜

#include <iostream>
#include <string>
#include <map>
#include <cctype>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    map<string, int> pokemon;
    string name[100001];

    cin >> n >> m;

    for (int i = 1; i <= n; i++)
    {
        string temp;
        cin >> temp;
        pokemon.insert({temp, i});
        name[i] = temp;
    }

    for (int i = 1; i <= m; i++)
    {
        string temp;
        cin >> temp;
        if (isdigit(temp[0]))
        {
            cout << name[stoi(temp)] << "\n";
        }
        else
        {
            auto it = pokemon.find(temp);
            cout << it->second << "\n";
        }
    }

    return 0;
}