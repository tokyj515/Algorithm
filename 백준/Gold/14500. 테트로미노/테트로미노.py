import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)


max_val = 0



dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(dep, x, y, sum):
    global max_val

    if dep == 4:
        max_val = max(max_val, sum)
        # print(f"x: {x}, y: {y} => sum: {sum}")
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx and nx < n and 0<= ny and ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(dep+1, nx, ny, sum+graph[nx][ny])
            visited[nx][ny] = 0


def check_t(x, y):
    global max_val

    shape = [
        [(0, 0), (-1, 0), (1, 0), (0, -1)], #ㅏ
        [(0, 0), (-1, 0), (1, 0), (0, 1)], #ㅓ
        [(0, 0), (0, -1), (0, 1), (1, 0)], #ㅗ
        [(0, 0), (0, -1), (0, 1), (-1, 0)], #ㅜ
    ]

    for s in shape:
        sum = 0
        possible = True # 현 위치에서 해당 모양이 가능한지

        for dx, dy in s:
            nx = x + dx
            ny = y + dy

            if 0<= nx and nx <n and 0<= ny and ny < m :
                sum += graph[nx][ny]
            else:
                possible = False
                break

        if possible:
            max_val = max(max_val, sum)





for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(1, i, j, graph[i][j])
        visited[i][j] = 0
        # print()

        check_t(i, j)


print(max_val)


