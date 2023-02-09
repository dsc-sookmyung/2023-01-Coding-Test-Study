// BOJ 20436 ZOAC 3

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v;

void init()
{
    v.push_back('q' - 'a');
    v.push_back('w' - 'a');
    v.push_back('e' - 'a');
    v.push_back('r' - 'a');
    v.push_back('t' - 'a');
    v.push_back('a' - 'a');
    v.push_back('s' - 'a');
    v.push_back('d' - 'a');
    v.push_back('f' - 'a');
    v.push_back('g' - 'a');
    v.push_back('z' - 'a');
    v.push_back('x' - 'a');
    v.push_back('c' - 'a');
    v.push_back('v' - 'a');
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    init();
    
    int arr[26][2] = {
        {1, 2},
        {5, 3},
        {3, 3},
        {3, 2},
        {3, 1},
        {4, 2},
        {5, 2},
        {6, 2},
        {8, 1},
        {7, 2},
        {8, 2},
        {9, 2},
        {7, 3},
        {6, 3},
        {9, 1},
        {10, 1},
        {1, 1},
        {4, 1},
        {2, 2},
        {5, 1},
        {7, 1},
        {4, 3},
        {2, 1},
        {2, 3},
        {6, 1},
        {1, 3}};

    char l, r;
    string s;

    cin >> l >> r;
    cin >> s;

    int res = 0;

    for (int i = 0; i < s.size(); i++)
    {
        if(find(v.begin(), v.end(), s[i]-'a') != v.end()){
            res += (abs(arr[l-'a'][0]-arr[s[i]-'a'][0]) + abs(arr[l-'a'][1]-arr[s[i]-'a'][1]));
            res++;
            l=s[i];
        }
        else
        {
            res+=(abs(arr[r-'a'][0]-arr[s[i]-'a'][0]) + abs(arr[r-'a'][1]-arr[s[i]-'a'][1]));
            res++;
            r=s[i];
        }
    }

    cout << res << "\n";

    return 0;
}