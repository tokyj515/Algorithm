import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

# 시작 위치, 바라보는 방향
start_x, start_y, d = map(int, input().split())

# 방향 설정: 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 0: 청소 안 됨
# 1: 벽
# 2: 청소함

def clean(x, y, d):
    global result

    # 현재 위치를 청소
    if graph[x][y] == 0:
        graph[x][y] = 2
        result += 1

    # 네 방향을 모두 확인
    for i in range(4):
        # 왼쪽 방향으로 회전
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        # 그 방향으로 이동할 수 있으면 이동하고 재귀적으로 청소
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            clean(nx, ny, d)
            return

    # 네 방향 모두 청소가 되어 있거나 벽인 경우 후진
    bx = x - dx[d]
    by = y - dy[d]

    # 후진할 수 있으면 후진
    if 0 <= bx < n and 0 <= by < m and graph[bx][by] != 1:
        clean(bx, by, d)
    else:
        # 후진도 불가능하면 멈춤
        return

# 청소 시작
clean(start_x, start_y, d)

# 결과 출력
print(result)
