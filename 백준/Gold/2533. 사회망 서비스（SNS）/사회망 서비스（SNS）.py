import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

dp = [[0, 0] for _ in range(n+1)]
# for i in range(n+1):
#     dp.append([0, 0])
# 얼리어댑터가 아닐 때0, 맞을 때1

dp[1][0] = 0
dp[1][1] = 1



for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


# for row in graph:
#     print(row)
#

def dfs(v):
    visited[v] = 1
    # print(v, end=" ")

    dp[v][0] = 0
    dp[v][1] = 1

    # for row in dp:
    #     print(row)
    # print()

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

            # v: 부모, i: 자식
            dp[v][0] += dp[i][1]
            dp[v][1] += min(dp[i][0], dp[i][1])





#
# for i in range(2, n+1):
#     if not visited[i]:
#         dfs(i)

dfs(1)

# for row in dp:
#     print(row)
# print()

# print(min(dp[n][0], dp[n][1]))
print(min(dp[1][0], dp[1][1]))