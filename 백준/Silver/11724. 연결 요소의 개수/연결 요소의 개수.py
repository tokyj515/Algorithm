import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0


def dfs(graph, visited, v):

    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)
    #
    # return True




for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


# print(graph)

for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, visited, i)
        cnt+=1

print(cnt)