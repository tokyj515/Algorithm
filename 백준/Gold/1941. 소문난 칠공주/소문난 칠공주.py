import sys
from collections import deque

input = sys.stdin.read

# 방향 벡터 (상, 하, 좌, 우)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 입력을 5x5 그리드로 변환
input_data = input().strip().split()
graph = [list(row) for row in input_data]

# 선택된 위치를 기록하는 2차원 배열
selected = [['.' for _ in range(5)] for _ in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
answer = 0

def is_connected():
    # 선택된 위치들이 연결되어 있는지 확인
    queue = deque()
    found = False

    for i in range(5):
        for j in range(5):
            if selected[i][j] != '.':
                queue.append((i, j))
                visited[i][j] = 1
                found = True
                break
        if found:
            break

    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and selected[nx][ny] != '.':
                visited[nx][ny] = 1
                queue.append((nx, ny))

    # 방문 배열 초기화
    for i in range(5):
        for j in range(5):
            visited[i][j] = 0

    return cnt == 7

def backtrack(depth, index):
    global answer
    
    if depth == 7:
        s_count = sum(1 for i in range(5) for j in range(5) if selected[i][j] == 'S')
        if s_count >= 4 and is_connected():
            answer += 1
        return
    
    for i in range(index, 25):
        x, y = divmod(i, 5)
        if selected[x][y] == '.':
            selected[x][y] = graph[x][y]
            backtrack(depth + 1, i + 1)
            selected[x][y] = '.'

# 백트래킹 시작
backtrack(0, 0)
print(answer)
