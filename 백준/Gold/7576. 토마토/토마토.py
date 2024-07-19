import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())

graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]

# 그래프 입력받기
for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)

# print(graph)


# 토마토가 익은 좌표 큐에 넣기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1

# 익은 토마토 주변에 존재하는 토마토들의 상태 체크
while queue:
    x, y = queue.popleft()
    #   print(x, y)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            graph[nx][ny] = 1
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

            # print(nx, ny)
            # for row in visited:
            #     print(row)
            # print()

#   print(queue)


# print(graph)
# print(visited)


# # 총 며칠이 소요되는지
# day = 0
# for row in visited:
#     for e in row:
#         if e == 0:
#             print(-1)
#             exit()
#     day = max(day, max(row))
#
# print(day - 1)
#

max_days = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:  # If there's still an unripe tomato
            print(-1)
            exit()
        if visited[i][j] > max_days:
            max_days = visited[i][j]

print(max_days-1)






