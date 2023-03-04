// BOJ 10814 나이순 정렬

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct user
{
    int age, order;
    string name;
};

bool cmp(user a, user b)
{
    if (a.age == b.age)
        return a.order < b.order;
    return a.age < b.age;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;

    cin >> N;
    vector<user> v(N);

    for (int i = 0; i < N; i++)
    {
        cin >> v[i].age >> v[i].name;
        v[i].order = i;
    }

    sort(v.begin(), v.end(), cmp);

    for (int i = 0; i < N; i++)
    {
        cout << v[i].age << " " << v[i].name << "\n";
    }

    return 0;
}