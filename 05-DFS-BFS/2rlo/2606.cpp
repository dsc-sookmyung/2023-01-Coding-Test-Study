// BOJ 2606 바이러스

#include <iostream>
using namespace std;

int N, M;
int map[101][101] = {
    0,
};
bool visited[101] = {
    0,
};
int res = 0;

void dfs(int v)
{
    visited[v] = true;
    res++;

    for (int i = 1; i <= N; i++)
    {
        if (visited[i] == 0 && map[v][i] == 1)
        {
            dfs(i);
        }
    }
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        map[a][b] = 1;
        map[b][a] = 1;
    }

    dfs(1);

    cout << res - 1;

    return 0;
}