from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    depth = [0] * (n + 1)
    queue = deque()
    cnt = 0

    # 그래프 세팅
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # bfs
    queue.append(1)
    visited[1] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                depth[i] = depth[v] + 1

    max_depth = max(depth)
    for i in depth:
        if i == max_depth:
            cnt += 1

    return cnt