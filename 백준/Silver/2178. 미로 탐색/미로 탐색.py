import sys
from collections import deque



# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, sys.stdin.readline().split())

graph =[]
# visitd = [[] for _ in range(n)]

# 그래프 세팅
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(temp)


# print(graph)


# 최소 칸 -> BFS
def bfs():
    #큐 설정, 시작 위치 인덱스
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위 내인지
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 갈 수 있는 곳인지 아닌지
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


    return graph[n-1][m-1]


print(bfs())