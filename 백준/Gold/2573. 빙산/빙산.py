

import sys
input = sys.stdin.readline

from collections import deque


n, m = map(int, input().split(" "))
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

time = 0


for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)


def bfs(start_x, start_y):
    queue = deque()

    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx and nx <n and 0<= ny and ny <m and not visited[nx][ny] and graph[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1



while True:
    time += 1

    # 녹기
    new_graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            water = 0

            if graph[i][j]:
                for nx, ny in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
                    if 0<= nx and nx <n and 0<= ny and ny <m and graph[nx][ny] == 0:
                        water += 1

            new_graph[i][j] = max(0, graph[i][j] - water)
    graph = new_graph


    # 영역 개수 세기
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    if cnt >= 2:
        print(time)
        exit()


    if cnt == 0:
        print(0)
        exit()