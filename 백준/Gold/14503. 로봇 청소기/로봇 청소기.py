import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = []

# 시작 위치, 바라보는 방향
start_x, start_y, d = map(int, input().split(" "))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)

# 0: 청소 안 됨
# 1: 벽
# 2: 청소함


def backtrack(x, y, d):
    global result


    if graph[x][y] == 0:
        graph[x][y] = 2
        # print(x, y)
        result += 1



    # 4방향을 기준으로 현재 가진 방향을 갖고 재귀
    for i in range(4):
        d = (d+3)%4

        nx = x + dx[d]
        ny = y + dy[d]

        if 0<=nx and nx<n and 0<= ny and ny <m and graph[nx][ny] == 0:
            backtrack(nx, ny, d)
            return # 한 방향에서 재귀가 시작했으므로 다음 방향에서 실행되지 않도록 막는 것


    bx = x - dx[d]
    by = y - dy[d]

    if 0 <= bx and bx < n and 0 <= by and by < m and graph[bx][by] != 1:
        backtrack(bx, by, d)
    else:
        # 후진이 불가한 경우
        return





backtrack(start_x, start_y, d)
print(result)
