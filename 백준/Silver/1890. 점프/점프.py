import sys
input = sys.stdin.readline

n = int(input())


dp = [[0 for _ in range(n)] for _ in range(n)]
graph = []

for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)



# 적힌 수 + 오른쪽(0, 1)  or 아래(1,0)

dp[0][0] = 1

for i in range(n):
    for j in range(n):

        if dp[i][j] > 0 and graph[i][j] > 0:
            if j + graph[i][j] < n:
                # dp[i][j+graph[i][j]] = dp[i][j] + 1
                dp[i][j + graph[i][j]] += dp[i][j]

            if i + graph[i][j] < n:
                # dp[i+graph[i][j]][j] = dp[i][j] + 1
                dp[i + graph[i][j]][j] += dp[i][j]

        # for row in dp:
        #     print(row)
        # print()


print(dp[n-1][n-1])