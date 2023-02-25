# DFS & BFS
> **DFS**: Depth First Search (깊이 우선 탐색)   
> **BFS**: Breadth First Search (너비 우선 탐색)

</br>

## DFS
- `재귀함수`나 `스택`으로 구현
- 노드 방문 시 방문(visited) 여부를 반드시 검사해야 함
- 장점
  - 저장 공간의 수요가 비교적 적음
  - 목표 노드가 깊은 단계에 있을 경우 해를 빠르게 구할 수 있음
- 단점
  - 해가 없는 경로에 깊이 빠질 가능성이 있음   
    → 따라서 미리 지정한 임의 깊이까지만 탐색하고 목표 노드를 발견하지 못하면 다음 경로를 따라 탐색하는 방법이 유용할 수 있음
  - 얻어진 해가 최단 경로가 된다는 보장이 없음

</br>

## BFS
- `큐` 자료구조를 이용
- 특정 조건의 최단 경로 알고리즘을 계산할 때 사용
- 장점
  - 출발 노드에서 목표 노드까지의 최단 길이 경로 보장
- 단점
  - 경로가 매우 길 경우에는 많은 기억 공간 필요
  - 해가 존재하지 않다면 모든 그래프를 탐색 후에 실패로 끝남
  - 무한 그래프의 경우에는 해를 찾지도, 끝내지도 못함
  

</br>

---

</br>

# BOJ 2606 바이러스
## 문제 요약
1. 입력: `컴퓨터의 수`, 네트워크 상에서 직접 `연결되어 있는 컴퓨터 쌍의 수`, 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 `직접 연결되어 있는 컴퓨터의 번호 쌍`
2. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸림
3. 출력: 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 `웜 바이러스에 걸리게 되는 컴퓨터의 수`

</br>

## 풀이과정
1. DFS 사용
2. 연결쌍 입력은 map으로 받음
3. 다른 노드가 방문되지 않았고 현재 노드와 이어져 있다면 dfs 호출

</br>

## 코드
```cpp
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
```

</br>

---

</br>

# BOJ 2667 단지번호붙이기
## 문제 요약
1. 입력: 지도의 크기 `N`(NxN), N개의 자료(`0 or 1`)
2. 1은 집이 있는 곳, 0은 없는 곳
3. 좌우, 아래위로 다른 집이 있어 연결 된 경우 단지로 처리
4. 출력: 첫 줄에 `총 단지 수`, `각 단지내 집의 수`를 `오름차순`으로 정렬하여 한 줄에 하나씩 출력

</br>

## 풀이과정
1. 연결되는 것은 상하좌우에 인접한 다른 집이 있는 경우
2. 숫자가 붙어서 입력되므로 `%1d`로 입력 받음
3. 방문한 집인 경우 map[x][y]를 `0`으로
4. x, y축의 편한 이동을 위해 `dx, dy` 배열 사용

</br>

## 코드
```cpp
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
```

</br>

# BOJ 7576 토마토
## 문제 요약
1. 입력: 상자의 크기 `M(가로), N(세로)`, 둘째 줄부터는 하나의 상자에 저장된 `토마토들의 정보`(1 = 익은 토마토, 0 = 안 익은 토마토, -1 = 토마토가 들어있지 않음)
2. 보관 후 하루가 지나면 익지 않은 토마토들은 인접한 익은 토마토의 영향을 받아 익게 됨
3. 인접함의 기준은 상하좌우
4. 출력: 토마토가 모두 익을 때까지의 최소 날짜
</br>

## 풀이과정
1. BFS 사용
2. 출력 전 안 익은 토마토(0)이 있는지 확인 (-1이 가로막아 익지 못하는 경우)

</br>

## 코드
```cpp
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
```
---

</br>

# BOJ 14502 연구소
## 문제 요약
1. 입력: 세로 크기 `N`, 가로 크기 `M`, N개의 줄에 `지도의 모양`이 주어짐(0: 빈 칸, 1: 벽, 2: 바이러스의 위치)
2. 바이러스는 상하좌우 인접한 빈 칸으로 모두 퍼져나갈 수 있음
3. 새로 세울 수 있는 벽의 수는 3개이며 꼭 3개를 세워야 함
4. 안전 영역의 크기는 벽을 세운 후 바이러스가 퍼질 수 없는 곳의 크기
5. 출력: 얻을 수 있는 `안전 영역의 최대 크기`
</br>

## 풀이과정
1. BFS 사용
2. search 함수로 만들 수 있는 모든 벽을 따져봄
3. search 함수에서 cnt가 0이 되는 순간 bfs 실행
4. bfs에서 입력받은 map을 wmap에 복사하고 2 발견 시 시작
5. 결과로 받은 배열에서 0의 개수를 세서 최댓값 비교로 res 값 초기화

</br>

## 코드 
```cpp
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
```
---

</br>

