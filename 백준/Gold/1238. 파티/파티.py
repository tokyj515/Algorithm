import sys
input = sys.stdin.readline

from collections import defaultdict, deque
from heapq import heappop, heappush

N, M, X = map(int, input().split(" "))


graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split(" "))
    graph[u].append((v, w))




def dijkstra(start):
    pq = []
    dist = [float('inf') for _ in range(N + 1)]

    dist[start] = 0
    heappush(pq, (0, start))

    while pq:
        cur_dist, v = heappop(pq)

        if dist[v] < cur_dist:
            continue

        for next, w in graph[v]:
            new_dist = cur_dist + w

            if dist[next] > new_dist:
                dist[next] = new_dist
                heappush(pq, (new_dist, next))

    return dist


go = dijkstra(X)

for i in range(1, N+1):
    if i == X:
        continue
    come = dijkstra(i)
    go[i] += come[X]

print(max(go[1:]))