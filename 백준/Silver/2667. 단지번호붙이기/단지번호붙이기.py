import sys
sys.setrecursionlimit(10**6)


# 전역변수
N = int(sys.stdin.readline())
graph = []


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = []
cnt = 0

#함수
def dfs(x, y):
    global cnt

    # 범위 체크
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    # 집이 있는 경우
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0 #이제 다시 방문하지 않을 것이니 0으로 변경

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny) # 여기서 다음 것이 1인지 0인지 판단 안 해도 됨
        return True

    return False




# 구현부
for _ in range(N):
    temp = list(map(int, list(sys.stdin.readline().rstrip())))
    graph.append(temp)


for i in range(N):
    for j in range(N):
        if dfs(i, j):
            result.append(cnt)
            cnt = 0


result.sort()

# 출력
print(len(result))
for i in result:
    print(i)