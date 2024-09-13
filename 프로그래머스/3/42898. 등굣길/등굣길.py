def solution(m, n, puddles):
    graph = [[1 for _ in range(m)] for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i, j in puddles:
        graph[j - 1][i - 1] = 0

    # print("graph:")
    # for row in graph:
    #     print(row)
    # print("-----------------------")

    row_idx = m
    col_idx = n

    for i, g in enumerate(graph[0]):
        if g == 0:
            row_idx = i
            break

    for i, g in enumerate([g[0] for g in graph]):
        if g == 0:
            col_idx = i
            break

    # print(f"row_idx: {row_idx}, col_idx: {col_idx}")
    for i in range(row_idx):
        dp[0][i] = 1
    for i in range(col_idx):
        dp[i][0] = 1



    # ###########################
    # for row in dp:
    #     print(row)
    # print()


    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == 1:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
            # else:
            #     dp[i+1][j] = dp[i+1][j-1]
            #     dp[i][j+1] = dp[i-1][j+1]
            #     # dp[i][j] = 0
            # dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

            # for row in dp:
            #     print(row)
            # print()

#     for row in dp:
#         print(row)

    
    
    return dp[n-1][m-1]