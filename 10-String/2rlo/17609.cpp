// BOJ 17609 회문

#include <iostream>
#include <string>
using namespace std;

int palindrome(string s, int check)
{
    int left, right;
    left = 0;
    right = s.size() - 1;

    while (left < right)
    {
        if (s[left] != s[right])
        {
            if (check == 0)
            {
                int len = right - left;
                if (palindrome(s.substr(left + 1, len), 1) == 0 || palindrome(s.substr(left, len), 1) == 0)
                    return 1;
                else
                    return 2;
            }
            else 
                return 2;
        }
        left++;
        right--;
    }
    return 0;
}
int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;
    
    for(int i=0; i<T; i++){
        string s;
        cin >> s;
        cout << palindrome(s, 0) << "\n";
    }
    return 0;
}