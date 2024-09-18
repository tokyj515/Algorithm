import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
visited = [[-1 for _ in range(m)] for _ in range(n)]  # 방문하지 않은 곳을 -1로 초기화

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

start_x, start_y = 0, 0

# 입력 받기
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

    if 2 in temp:  # 시작점 찾기 (2인 좌표)
        start_x = i
        start_y = temp.index(2)

# BFS 함수
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0  # 시작점은 거리 0

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위 체크 및 방문하지 않은 곳 체크
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1  # 거리 갱신

# BFS 실행
bfs(start_x, start_y)

# 1인 지점 중 방문하지 못한 곳은 -1로 설정
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == -1:
            visited[i][j] = -1
        elif graph[i][j] == 0:  # 벽(0)은 그대로 0으로 유지
            visited[i][j] = 0

# 결과 출력
for row in visited:
    print(*row)
