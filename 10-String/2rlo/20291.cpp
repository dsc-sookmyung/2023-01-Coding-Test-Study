// BOJ 20291 파일 정리

#include <iostream>
#include <string>
#include <map>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    string s;
    map<string, int> ex;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> s;
        s = s.substr(s.find('.') + 1);
        ex[s]++;
    }

    for (auto it = ex.begin(); it != ex.end(); it++)
    {
        cout << (*it).first << " " << (*it).second << "\n";
    }

    return 0;
}