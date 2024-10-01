import sys
input = sys.stdin.readline

n, m  = map(int, input().split(" "))

graph = []

for _ in range(n):
    temp = list(map(int, input().split(" ")))
    graph.append(temp)


for i in range(1, n):
    graph[i][0] += graph[i-1][0]

for i in range(1, m):
    graph[0][i] += graph[0][i-1]



for i in range(1, n):
    for j in range(1, m):
        graph[i][j] += max(graph[i-1][j], graph[i][j-1], graph[i-1][j-1])





# for row in graph:
#     print(row)

print(graph[n-1][m-1])