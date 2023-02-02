// BOJ 1541 잃어버린 괄호

#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int res = 0;

    string input, num;
    cin >> input;

    bool isMinus = false;

    for (int i=0; i<=input.size(); i++){
        if(input[i] == '-' || input[i] == '+' || i == input.size()) {
            if (isMinus) {
                res -= stoi(num);
                num = "";
            }
            else {
                res += stoi(num);
                num = "";
            }
        }
        else {
            num += input[i];
        }

        if(input[i] == '-') {
            isMinus = true;
        }
    }

    cout << res << "\n";

    return 0;
}