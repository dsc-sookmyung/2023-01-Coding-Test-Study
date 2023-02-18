// BOJ 2667 단지번호붙이기

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, cnt;
int map[25][25];
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };
vector<int> ans;

void dfs(int x, int y) {
	map[x][y] = 0;
	cnt++;
	for (int i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || nx >= n || ny<0 || ny>=n)continue;
		if (!map[nx][ny])continue;
		dfs(nx, ny);
	}
}
int main() {

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			scanf("%1d", &map[i][j]);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (map[i][j] == 1)
			{
				cnt = 0;
				dfs(i, j);
				ans.push_back(cnt);
			}
	sort(ans.begin(), ans.end());
	int size = ans.size();
	printf("%d\n", size);
	for (int i = 0; i < size; i++)
		printf("%d\n", ans[i]);

	return 0;
}