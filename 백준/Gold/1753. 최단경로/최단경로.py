import sys
input = sys.stdin.readline

from collections import defaultdict
from heapq import heappush, heappop

V, E = map(int, input().split(" "))
K = int(input())

graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split(" "))
    graph[u].append((v, w))

INF = float('inf')


def dijkstra(start):
    dist = [INF for _ in range(V+1)]

    pq = []
    pq.append((0, start))
    dist[start] = 0

    while pq:
        now_dist, v = heappop(pq)

        if dist[v] < now_dist:
            continue


        for next, cost in graph[v]:
            new_dist = now_dist + cost

            if new_dist < dist[next]:
                dist[next] = new_dist
                heappush(pq, (new_dist, next))


    return dist

answer = dijkstra(K)

for a in answer[1:]:
    if a == INF:
        print('INF')
    else:
        print(a)

