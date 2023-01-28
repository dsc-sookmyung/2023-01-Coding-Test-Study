// BOJ 14425 문자열 집합

#include <iostream>
#include <map>
using namespace std;

int main(){
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m, result=0;
    map<string, int> s;

    cin >> n >> m;

    for (int i = 1; i<=n; i++) {
        string temp;
        cin >> temp; 
        s.insert({temp, i});
    }

    for(int i=1; i<=m; i++){
        string temp;
        cin >> temp;
        if(s.find(temp) != s.end()){
            result++;
        }
    }

    cout << result << "\n";
    return 0;
}