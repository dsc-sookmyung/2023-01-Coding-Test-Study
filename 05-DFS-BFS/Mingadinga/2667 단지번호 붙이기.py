import sys

read = sys.stdin.readline

n = int(read())

graph = []
village_count = 0
temp_count = 0
house_count = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    # 인덱스 벗어나면 False
    if (x < 0 or x >= n) or (y < 0 or y >= n):
        return False
    # 현재 노드가 미방문이라면
    if graph[x][y] == 1:
        graph[x][y] = 0
        # house_count[village_count] += 1
        global temp_count
        temp_count += 1
        # 상하좌우 탐색
        for i in range(len(dx)):
            dfs(x + dx[i], y + dy[i])
        return True
    # 방문 노드라면 더이상 탐색하지 않는다
    return False


for i in range(n):
    graph.append(list(map(int, read().rstrip())))

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            village_count += 1
            house_count.append(temp_count)
            temp_count = 0

house_count.sort()
print(village_count)
for count in house_count:
    print(count)