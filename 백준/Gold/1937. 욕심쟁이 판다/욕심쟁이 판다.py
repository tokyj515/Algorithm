import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)



n = int(input())

graph = []
visited = [[0 for _ in range(n)] for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


answer = []
result = []

max_val = 0
cnt = 0



def dfs(x, y):
    # global cur_cnt, cur_sum
    # visited[x][y] = 1
    # cur_sum += graph[x][y]
    # cur_cnt += 1
    # # answer.append((x, y))

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx and nx < n and 0<= ny and ny < n and graph[x][y] < graph[nx][ny] and not visited[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)

    return dp[x][y]



for i in range(n):
    for j in range(n):
        max_val = max(max_val, dfs(i,j))
        # if not visited[i][j]:
        #     cur_sum = 0
        #     cur_cnt = 0
        #     dfs(i, j)
        #
        #     if cur_sum > max_val:
        #         max_val = cur_sum
        #         cnt = cur_cnt



print(max_val)







# # visited[i][j] = 1
# dfs(i, j)
# result.append(answer)
# answer = []
# # visited[i][j] = 0



# max_val = 0
# cnt = 0
#
# for res in result:
#     temp = 0
#     for x,y in res:
#         temp += graph[x][y]
#
#     if max_val <= temp:
#         max_val = max(max_val, temp)
#         cnt = len(res)

