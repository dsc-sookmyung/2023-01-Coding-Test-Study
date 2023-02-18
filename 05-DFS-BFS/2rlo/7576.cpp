// BOJ 7576 토마토

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct tomato {
	int x, y;
};

int n, m, ans;
int map[1000][1000];
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };
queue<tomato> q;

void bfs() {
	while (!q.empty()) {
		int x = q.front().x;
		int y = q.front().y;
		q.pop();
		for (int i = 0; i < 4; i++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if (map[nx][ny])continue;
			map[nx][ny] = map[x][y] + 1;
			q.push({ nx, ny });
		}
	}
}

int main() {
	scanf("%d %d", &m, &n);
	
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			scanf("%d", &map[i][j]);
			if (map[i][j] == 1)
				q.push({ i,j });
		}
	bfs();
	for(int i=0; i<n; i++)
		for (int j = 0; j < m; j++)
		{
			if (map[i][j] == 0)
			{
				printf("-1\n");
				return 0;
			}
			if (ans < map[i][j])
				ans = map[i][j];
		}
	printf("%d\n", ans - 1);
	return 0;
}