// BOJ 14502 연구소

#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

#define MAX 10

int MAP[MAX][MAX];
int WMAP[MAX][MAX];
bool visited[MAX][MAX] = {
    0,
};
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int N, M, cnt = 3, res = 0;

void bfs()
{
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            WMAP[i][j] = MAP[i][j];
        }
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            if (WMAP[i][j] == 2)
            {
                queue<pair<int, int>> q;

                q.push({i, j});
                visited[i][j] = true;

                while (!q.empty())
                {
                    int curY = q.front().first;
                    int curX = q.front().second;
                    q.pop();

                    for (int next = 0; next < 4; next++)
                    {
                        int NextY = curY + dx[next];
                        int NextX = curX + dy[next];

                        if (!visited[NextY][NextX] && WMAP[NextY][NextX] == 0)
                        {
                            q.push({NextY, NextX});
                            visited[NextY][NextX] = true;
                            WMAP[NextY][NextX] = 2;
                        }
                    }
                }
            }
        }
    }

    memset(visited, false, sizeof(visited));
    int temp = 0;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            if (WMAP[i][j] == 0)
                temp++;
        }
    }

    if (temp > res)
        res = temp;
}

void search()
{
    if (cnt == 0)
        return bfs();
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            if (MAP[i][j] == 0)
            {
                cnt--;
                MAP[i][j] = 1;
                search();
                cnt++;
                MAP[i][j] = 0;
            }
        }
    }
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    memset(MAP, -1, sizeof(MAP));
    memset(WMAP, -1, sizeof(WMAP));

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            cin >> MAP[i][j];
        }
    }

    search();
    cout << res << "\n";

    return 0;
}