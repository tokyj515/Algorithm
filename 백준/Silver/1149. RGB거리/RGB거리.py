import sys
input = sys.stdin.readline

graph = []

n = int(input())

for _ in range(n):
    # 빨강 초록 파랑 -> 각 집을 칠하는 비용
    temp = list(map(int, input().rstrip().split(" ")))
    graph.append(temp)

dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0] = graph[0]

# for d in dp:
#     print(d)
# print()


for i in range(1, n):
    now = graph[i]


    # i번째에서 R를 칠하려면 이전에는 G, B 중에 작은 것을 칠할 것
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + graph[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + graph[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][2]
    #
    # for d in dp:
    #     print(d)
    # print()


print(min(dp[n-1]))