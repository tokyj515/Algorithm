import sys
from collections import deque


def dfs(graph, v, visited):
    visited[v] = 1
    graph[v].sort()
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1




# v: 방문 시작 노드
n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)