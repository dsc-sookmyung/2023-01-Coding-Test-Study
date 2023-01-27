// BOJ 10799 쇠막대기

#include <iostream>
#include <stack>
using namespace std;

int main()
{
    int res = 0;
    stack<char> st;

    string iron;
    cin >> iron;

    for (int i = 0; i < iron.size(); i++)
    {
        if (iron[i] == '(')
            st.push(iron[i]);
        else
        {
            if (iron[i - 1] == ')')
            {
                st.pop();
                res += 1;
            }
            else
            {
                st.pop();
                res += st.size();
            }
        }
    }

    cout << res << "\n";
    return 0;
}